# Wearable 2-Channel PPG Eval Board (NXP LPC55S16) — FAE design package
Design package for a discrete-AFE optical PPG eval board (IR 850 nm + red 660 nm) on an **NXP LPC55S16JBD64** (Cortex-M33, 16-bit ADC, SCTimer for LED/ADC slot sync). **Not fabricated; signal results are simulated.**

## Contents
- `hardware/BOM.csv` — real MPNs (NXP, TI, OSRAM, Murata, Nexperia)
- `hardware/netlist.net` — explicit netlist; `hardware/STACKUP.md` — 4-layer stackup + layout rules
- `docs/DESIGN_NOTES.md` — AFE, LED drive, ambient rejection, decoupling/return paths
- `BRINGUP_CHECKLIST.md` — customer bring-up steps with pass criteria
- `src/bringup.py` — simulated acquisition + SNR / ambient / motion checks; `src/layout_plot.py` — floorplan
- Figures: `figures/fig1_board_floorplan.png`, `figures/fig2_ppg_signal_analysis.png`

## Run
`pip install -r requirements.txt && python3 src/layout_plot.py && python3 src/bringup.py`

## Results (simulated)
| Ch | SNR (0.5–5 Hz) | Perfusion index | Motion ratio (10–14 s) |
|---|---|---|---|
| IR 850 nm | 21.1 dB | 2.25% | 3.9× |
| Red 660 nm | 21.5 dB | 1.35% | 6.1× |
Both channels clear the ≥20 dB checklist target at rest; injected 1.8 Hz motion falls inside the cardiac band and is NOT removed by filtering → justifies adding an accelerometer (rev B).

## Why no KiCad files
KiCad was not installable on the build host (`apt: Unable to locate package kicad`). Substituted an explicit netlist, stackup and floorplan plot. Next step: capture in KiCad 8 and run ERC/DRC.

## Limitations
Simulated signals and assumed noise; ambient-subtraction metric (~4.7 dB) is limited by the uncorrelated noise added in both slots in the model, not by 120 Hz flicker (which the band-pass already removes). Floorplan is conceptual, not routed.

## License
MIT — see `LICENSE`.
