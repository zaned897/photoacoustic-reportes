#!/usr/bin/env python3
"""Figuras pedagógicas del muestreo del DAQ: ventana, muestras discretas (stem) y
los puntos de adquisición sobre la señal. Usa la captura real del DAQ.

Salida: ../daq-muestreo.png
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SEM4 = os.path.dirname(BASE)
DAQ = os.path.join(SEM4, "figuras", "exports", "ventana_20260624_200320.csv")
OUT = os.path.join(BASE, "daq-muestreo.png")
ORANGE, BLUE = "#dd6b20", "#2b6cb0"


def load_daq(path):
    n, t, mv = [], [], []
    for ln in open(path, errors="replace").read().splitlines():
        if ln.startswith("#") or ln.lower().startswith("muestra"):
            continue
        p = ln.split(",")
        try:
            n.append(int(float(p[0]))); t.append(float(p[2])); mv.append(float(p[4]))
        except (ValueError, IndexError):
            pass
    return np.array(n), np.array(t), np.array(mv)


def main():
    n, t, mv = load_daq(DAQ)
    Ts = np.median(np.diff(t)) * 1e3  # ns
    fig, ax = plt.subplots(2, 1, figsize=(7.4, 5.6))

    # --- Panel superior: ventana completa, cada muestra es un punto ---
    ax[0].plot(t, mv, color="0.8", lw=0.8, zorder=1)
    ax[0].scatter(t, mv, s=10, color=ORANGE, zorder=2)
    ax[0].set_title(f"Ventana de muestreo del DAQ: N={len(n)} muestras, "
                    f"Ts={Ts:.1f} ns (54 MS/s), {t[-1]-t[0]:.1f} us",
                    fontsize=10, loc="left")
    ax[0].set_xlabel("tiempo desde el trigger (us)")
    ax[0].set_ylabel("señal del sense 0.1 Ω (mV)")
    ax[0].grid(alpha=0.3)
    ax[0].annotate("cada punto = 1 muestra (12 bit)", xy=(t[5], mv[5]),
                   xytext=(1.2, mv.min()*0.6), fontsize=8, color=ORANGE,
                   arrowprops=dict(arrowstyle="->", color=ORANGE))

    # --- Panel inferior: zoom al transitorio, STEM (muestras discretas) ---
    k = 34  # primeras muestras (cubre el transitorio)
    ml, sl, bl = ax[1].stem(t[:k], mv[:k], basefmt=" ")
    plt.setp(ml, color=BLUE, markersize=4)
    plt.setp(sl, color=BLUE, lw=1)
    ax[1].set_title(f"Zoom al transitorio — muestras discretas (stem): "
                    f"primeras {k} muestras", fontsize=10, loc="left")
    ax[1].set_xlabel("tiempo desde el trigger (us)")
    ax[1].set_ylabel("señal del sense 0.1 Ω (mV)")
    ax[1].grid(alpha=0.3)
    it = int(np.argmax(np.abs(mv[:k] - np.median(mv))))
    ax[1].annotate(f"transitorio: ~1 muestra\n(t={t[it]:.3f} us, {mv[it]:.0f} mV)",
                   xy=(t[it], mv[it]), xytext=(t[it]+0.12, mv[it]*0.7),
                   fontsize=8, color=BLUE,
                   arrowprops=dict(arrowstyle="->", color=BLUE))

    fig.suptitle("Cómo muestrea el DAQ: ventana, muestras y puntos de adquisición",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT, dpi=150)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
