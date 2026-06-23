# Reporte de Avance — Semestre 4 (LaTeX)

Proyecto LaTeX del reporte de avance del 4.º semestre. Da continuidad al Sem 3
(archivado en `../sem3/Avances_de_Semestre_3.zip`).

## Compilar

- **Overleaf** (recomendado): subir esta carpeta `sem4/` completa. Documento
  principal: `avances_sem4.tex`. Motor: **pdfLaTeX + Biber** (biblatex, estilo IEEE).
- Compila **con o sin las imágenes**: las figuras usan el macro `\figph`, que dibuja
  un recuadro *PLACEHOLDER* si el archivo aún no existe. Por eso puedes compilar el
  texto ahora y solo recompilar una vez cuando dejes los PNG.

## Figuras pendientes (dejar en `figuras/` con EXACTAMENTE estos nombres)

| Archivo | Contenido | Sección |
|---|---|---|
| `placa-acrilico.png` | Placa de acrílico con las PCBs de todas las etapas atornilladas | Metodología (integración) |
| `montaje.png`        | Foto del montaje de banco del intento de detección | Metodología (montaje) |
| `bringup-etapas.png` | Resultados de la validación por etapas del FPGA (ver `bringup/`) | Resultados (DAQ físico) |
| `pulsos-corriente.png` | Capturas del osciloscopio de los pulsos de corriente del Driver V2.0 | Resultados (Driver V2.0) |
| `ringing-falso.png`  | Osciloscopio: CH1 láser + CH2 onda de ~150 mV pp (pickup); idealmente la versión con sensor desconectado | Resultados (resultado negativo) |

> Nombres con guion (`-`), no guion bajo (`_`), para evitar problemas en LaTeX.
> Formato preferido PNG; si usas otro, ajustar la extensión en `avances_sem4.tex`.

## Pendientes de contenido (marcas `% TODO` en el `.tex`)

- Confirmar **periodo/fechas** del semestre (título y cronograma `tab:cronograma_rev`).
- Tabla de *trade-off* de candidatos a **preamplificador** y selección final.
- Asignar **meses/fechas reales** al cronograma revisado.
- Mediciones de banco (D0 capacitancia LCR, D1 toque sin láser) si se corren a tiempo.
