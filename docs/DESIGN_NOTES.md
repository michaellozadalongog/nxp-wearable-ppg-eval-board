# Analog front-end design notes
- **Photodiode in photovoltaic (zero-bias) mode** → lowest dark current; TIA RF=100 kΩ (0.1%) gives 100 mV/µA; CF=10 pF sets ~160 kHz BW, stable with SFH2701 capacitance (~ few pF) and OPA2380 90 MHz GBW. VBIAS 0.33 V keeps output off the rail.
- **LED drive:** MCU SCTimer gates N-FET constant-current sinks; I = Vset/RS (10 Ω → ~20 mA). IR and red time-multiplexed: slot sequence IR-on / RED-on / both-off (ambient), each 100 µs at 500 Hz frame rate.
- **Ambient light rejection:** firmware subtracts LED-off slot from LED-on slot (correlated double sampling); 0.5–5 Hz band-pass removes 100/120 Hz mains flicker and DC. Optical barrier between LED and PD stops direct crosstalk.
- **ADC:** LPC55S16 16-bit ADC0, external REF3330 3.0 V reference, hardware-triggered by SCTimer so sampling is phase-locked to the LED slot (settling ≥ 5τ of TIA).
- **Layout:** analog island over unbroken L2 GND; single-point AGND/DGND join; ferrite-isolated AVDD; 100 nF per VDD pin; LED current loop minimized; no clocks under TIA; guard ring on TIA inverting node.
