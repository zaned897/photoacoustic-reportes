#!/usr/bin/env python3
"""Figura `bringup-etapas`: escalera de validación incremental del DAQ (etapas 0-8).
Cada etapa valida una sola capa y no se avanza hasta que la anterior pasa.

Salida: ../bringup-etapas.png
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(BASE, "bringup-etapas.png")

STAGES = [
    "Reloj + bitstream",
    "Trigger + detección de flanco",
    "Enlace UART",
    "Lectura ADC (voltímetro)",
    "Captura interna (5 kHz)",
    "Captura por trigger externo",
    "Ráfaga 270 @ 27 MSPS",
    "Ráfaga @ 54 MSPS (PLL ×2)",
    "+ 12 bits (LSB 2.44 mV)",
]


def main():
    fig, ax = plt.subplots(figsize=(9.2, 5.6))
    n = len(STAGES)
    for k, lbl in enumerate(STAGES):
        c = plt.cm.Blues(0.35 + 0.07 * k)
        ax.add_patch(Rectangle((k, k), 1, 1, facecolor=c, edgecolor="white", lw=1.5))
        ax.text(k + 0.5, k + 0.5, str(k), ha="center", va="center",
                color="white", fontsize=12, fontweight="bold")
        ax.text(k + 1.15, k + 0.5, f"{lbl}   ✓", ha="left", va="center",
                fontsize=9.5, color="#2f855a")
    # flecha de complejidad creciente
    ax.annotate("", xy=(8.7, 9.2), xytext=(0.3, 0.6),
                arrowprops=dict(arrowstyle="-|>", color="0.6", lw=1.5,
                                connectionstyle="arc3,rad=-0.12"))
    ax.text(2.0, 6.6, "complejidad / capacidad creciente", rotation=38,
            color="0.5", fontsize=9)
    ax.set_xlim(-0.3, 13.5)
    ax.set_ylim(-0.3, 9.5)
    ax.axis("off")
    ax.set_title("Bring-up por etapas: validación incremental del DAQ "
                 "(cada etapa valida una capa)", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT, dpi=150)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
