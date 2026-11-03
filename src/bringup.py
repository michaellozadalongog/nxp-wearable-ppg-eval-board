"""FAE bring-up sanity script on SIMULATED PPG data (no hardware measured yet)."""
import numpy as np,matplotlib;matplotlib.use("Agg");import matplotlib.pyplot as plt;from scipy import signal
rng=np.random.default_rng(55);fs=500;t=np.arange(0,20,1/fs);hr=72/60
def ppg(ac):  # pulse shape: fundamental + dicrotic harmonic
    return ac*(np.sin(2*np.pi*hr*t)+0.35*np.sin(4*np.pi*hr*t+1.2))
ambient=0.05*np.sin(2*np.pi*120*t)  # fluorescent ambient (V) at TIA out
motion=np.where((t>10)&(t<14),0.08*np.sin(2*np.pi*1.8*t),0)
noise=lambda s:rng.normal(0,s,t.size)
# LED on/off sampling: ambient subtraction (LED-off sample subtracted)
ch={"IR":0.020,"RED":0.012}; out={}
b,a=signal.butter(3,[0.5,5],btype="band",fs=fs)
for n,ac in ch.items():
    raw_on=1.2+ppg(ac)+ambient+motion+noise(0.002); raw_off=0.3+ambient+motion*0.0+noise(0.002)
    sub=raw_on-raw_off; filt=signal.filtfilt(b,a,sub); filt_raw=signal.filtfilt(b,a,raw_on)
    clean=slice(0,10*fs); f,P=signal.welch(filt[clean],fs,nperseg=4096)
    band=(f>hr-0.15)&(f<hr+0.15)|(f>2*hr-0.15)&(f<2*hr+0.15); sig=P[band].sum();nz=P[(f>0.5)&(f<5)&~band].sum()
    seg=filt[10*fs:14*fs]; ma_ratio=np.std(seg)/np.std(filt[clean])
    out[n]=dict(snr_db=10*np.log10(sig/nz),motion_ratio=ma_ratio,ambient_rej_db=20*np.log10(np.std(raw_on-ppg(ac))/np.std(sub-ppg(ac))),pi=100*ac*1.35/1.2,filt=filt,raw=raw_on)
    print(n,{k:round(v,2) for k,v in out[n].items() if np.ndim(v)==0})
fig,ax=plt.subplots(2,1,figsize=(9,5),dpi=200,sharex=True)
ax[0].plot(t,out["IR"]["raw"],lw=.5);ax[0].set_ylabel("TIA out (V)\nraw LED-on");ax[0].set_title("Simulated 2-ch PPG bring-up (fs=500 Hz) — not measured data")
for n in ch:ax[1].plot(t,out[n]["filt"]*1e3,lw=.8,label=f"{n}: SNR {out[n]['snr_db']:.1f} dB, PI {out[n]['pi']:.1f}%")
ax[1].axvspan(10,14,color="r",alpha=.1,label="injected motion 10–14 s");ax[1].set_ylabel("ambient-sub + BPF (mV)");ax[1].set_xlabel("s");ax[1].legend(fontsize=7)
fig.tight_layout();fig.savefig("figures/fig2_ppg_signal_analysis.png")
