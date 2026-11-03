# Customer board bring-up checklist (FAE)
1. **Visual / pre-power:** BOM pop check vs BOM.csv, orientation of U1 pin 1, D1/D2 polarity, no solder bridges on LQFP64 (magnifier).
2. **Impedance:** VBUS, AVDD, DVDD, VREF to GND > 1 kΩ (no shorts).
3. **Current-limited power-up:** bench supply 5 V, 100 mA limit; expect idle < 30 mA.
4. **Rails:** DVDD 3.30 ±0.05 V, AVDD 3.30 ±0.05 V, VREF 3.000 ±0.003 V, VBIAS 0.33 V; AVDD ripple < 1 mVpp (scope, 20 MHz BW, spring ground).
5. **Debug:** MCU-Link on J1, MCUXpresso IDE/LinkServer detects LPC55S16; flash blinky, verify clock with CLKOUT.
6. **LED drive:** scope across RS1/RS2 → 200 mV pulses, 100 µs, correct slot order; LED current 20 mA ±5%.
7. **TIA dark:** LEDs off, cover PD: output = VBIAS ±5 mV, noise < 0.5 mVrms.
8. **Ambient test:** room light on/off — LED-off slot tracks ambient, subtracted signal unchanged.
9. **Finger test:** PI 0.5–5%, SNR ≥ 20 dB in 0.5–5 Hz band (run `src/bringup.py` analysis on captured CSV).
10. **Motion:** shake 1–3 Hz, record motion ratio; flag > 3× for accelerometer-based MA cancellation discussion.
11. **Sign-off:** log rails, currents, SNR, photos; file issues against schematic rev.
