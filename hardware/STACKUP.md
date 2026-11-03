# 4-layer stackup (1.6 mm, JLC-class)
L1 signal + components (AFE island top-left, MCU center) | L2 solid GND | L3 power (AVDD pour under AFE, DVDD elsewhere) | L4 signal / LED drive
Rules: TIA input nodes <5 mm, guard ring tied to VBIAS; LED current loop (LED→Q→Rsense→GND via) kept on L1 over L2, loop area <20 mm²; one 100 nF per VDD pin within 1 mm, via straight to L2; no digital traces crossing under AFE island; optical: PD/LED 3–6 mm spacing with 0.8 mm black opaque barrier.
