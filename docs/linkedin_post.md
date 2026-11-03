A PPG board that hits 20 dB SNR at rest can still fail on a moving wrist. I designed a 2-channel wearable PPG eval board around the NXP LPC55S16 to show where it fails and why.

What I built: a design package for a discrete-AFE optical PPG board (IR 850 nm + red 660 nm) on the LPC55S16JBD64 (Cortex-M33, 16-bit ADC). The SCTimer syncs LED and ADC slots so ambient light can be subtracted. It includes a BOM with real MPNs (NXP, TI, OSRAM, Murata, Nexperia), an explicit netlist, a 4-layer stackup with layout rules, design notes on decoupling and return paths, and a customer-style bring-up checklist with pass criteria.

Key results (simulated):
• SNR in the 0.5–5 Hz band: 21.1 dB IR and 21.5 dB red, both above the ≥20 dB bring-up target
• Perfusion index: 2.25% IR, 1.35% red
• Injected 1.8 Hz motion falls inside the cardiac band. Filtering can't remove it (3.9× and 6.1× motion ratio), so rev B needs an accelerometer for motion reference.

Limitations: the board isn't fabricated, the signals and noise are simulated, and the floorplan is conceptual, not routed. KiCad wasn't available on my build machine, so the next steps are schematic capture in KiCad 8, ERC/DRC, and then a real board bring-up.

I'm a biomedical engineering student at Hawaiʻi Pacific University looking for Summer 2027 internships in field applications engineering or similar customer-facing embedded roles at NXP. I'd welcome feedback from FAEs on the bring-up checklist.

Design package: https://github.com/michaellozadalongog/nxp-wearable-ppg-eval-board

📎 Attached: fig1_board_floorplan.png (board floorplan), fig2_ppg_signal_analysis.png (signal + SNR/motion analysis)

#NXP #EmbeddedSystems #Wearables #PPG #HardwareDesign
