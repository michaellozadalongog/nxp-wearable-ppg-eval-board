import matplotlib;matplotlib.use("Agg");import matplotlib.pyplot as plt;from matplotlib.patches import Rectangle,Circle
f,a=plt.subplots(figsize=(8,5),dpi=200);a.add_patch(Rectangle((0,0),40,25,fc="#1b5e20",ec="k"))
parts={"U1 LPC55S16\nLQFP64":(18,8,10,10,"#222"),"U2\nOPA2380\nTIA":(12,13,3.5,4.5,"#333"),"U3 LDO\nAVDD":(5,3,4,3,"#333"),
"U4 LDO\nDVDD":(30,3,4,3,"#333"),"J1 SWD":(31,18,7,4,"#555"),"J2 USB-C":(34,9,6,5,"#777"),"U5 VREF":(12,3,3,3,"#333")}
for n,(x,y,w,h,c) in parts.items():a.add_patch(Rectangle((x,y),w,h,fc=c,ec="w"));a.text(x+w/2,y+h/2,n,color="w",ha="center",va="center",fontsize=6)
a.add_patch(Rectangle((1,12),15.5,12,fill=False,ec="yellow",ls="--",lw=1.5));a.text(1.5,23,"AFE analog island (AVDD/guard)",color="yellow",fontsize=6)
for (x,y,l) in [(3,20,"D1 IR"),(9,20,"D2 RED"),(3,13.5,"PD1"),(9,13.5,"PD2")]:a.add_patch(Circle((x,y),1,fc="orange" if "D" in l[:2] and "PD" not in l else "cyan"));a.text(x,y-1.8,l,fontsize=5,ha="center",color="w")
a.plot([1.5,11],[17,17],color="k",lw=3);a.text(1.5,17.4,"opaque LED/PD barrier",fontsize=5,color="w")
a.annotate("FB1 single-point\nAGND/DGND join",(14,12),(20,21),color="w",fontsize=6,arrowprops=dict(color="w"))
a.set_xlim(-1,41);a.set_ylim(-1,26);a.set_aspect("equal");a.set_title("PPG eval board floorplan (L1, 40×25 mm, 4-layer) — concept layout");a.set_xlabel("mm")
f.tight_layout();f.savefig("figures/fig1_board_floorplan.png")
