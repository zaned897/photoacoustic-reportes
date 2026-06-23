# Reportes de tesis — Tomografía Fotoacústica e IA (LUMAT–UAZ)

Documentos de avance por semestre del doctorado de Eduardo Santos Mena
(asesores: Dr. Samuel Pérez Huerta, Dr. Augusto David Ariza Flores).

> **Aislamiento:** esto vive en la rama **`docs`** (huérfana, sin código) del repo
> `photoacoustic_daq`, materializada como un **git worktree** en esta carpeta
> hermana. Misma repo y mismo remoto que el firmware, pero **no interactúa** con las
> ramas de código (`main` / `feature/...`). Editar aquí no toca los archivos
> `.py`/`.v` y viceversa.

## Contenido
- `reportes/sem3/` — reporte del 3.º semestre (zip fuente LaTeX, archivado).
- `reportes/sem4/` — reporte del 4.º semestre (proyecto LaTeX en curso).
- `PLAN_ARGUMENTATIVO_SEM4.md` — plan argumentativo (backbone del reporte Sem 4).

## Compilar el reporte Sem 4
Detalle en `reportes/sem4/README.md`. Resumen (MiKTeX + Biber locales):

```powershell
cd reportes/sem4
pwsh -File build.ps1     # pdflatex -> biber -> pdflatex x2
```

En VS Code: abrir esta carpeta, abrir `reportes/sem4/avances_sem4.tex` y Ctrl+S
(compila al guardar; receta de Biber en `.vscode/settings.json`).

## Relación con el repo de código
El firmware/DAQ está en `../photoacoustic_daq` (ramas `main` / `feature/...`).
Para volver al código: trabaja en esa carpeta. Para los reportes: trabaja aquí.
