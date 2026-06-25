# Evidencia y media — reporte Sem 4

Material visual del experimento. Los **datos numéricos crudos** (CSV del
osciloscopio) van en `../capturas/`; las **figuras finales** del reporte van en
`../figuras/`.

## Estructura
- `fotos/` — fotos de cámara (banco, PCBs, montaje).
- `screenshots/` — capturas de pantalla del osciloscopio (.bmp/.png exportadas).
- `video/` — videos crudos (p. ej. el del ruido EM). ⚠️ **Videos grandes NO se
  versionan** (ver `.gitignore`): déjalos aquí localmente y commitea solo los frames.
- `frames/` — frames extraídos de los videos (para figuras como `ruido-em`).

## Inventario
| Archivo | Qué es | → Figura candidata |
|---|---|---|
| `screenshots/firstwave.bmp` | Pantalla del osciloscopio (laser_wave) | (interpretación de `laser_wave`) |
| `fotos/placa_acr_completa.jpeg` | Placa de acrílico con las PCBs | **`placa-acrilico`** |
| `fotos/ring_osc_con_cursor.jpeg` | Ringing en osciloscopio con cursores | **`ringing-falso`** (opción) |
| `fotos/ring_osc_cursor_2.jpeg` | Ringing en osciloscopio con cursores | `ringing-falso` (opción) |
| `fotos/ring_cursor_zoom.jpeg` | Zoom del ringing con cursor | `ringing-falso` (opción) |
| `fotos/fpga_adc_pc.jpeg` | FPGA + ADC + PC (montaje) | **`montaje`** / `daq-fpga-etapas` |
| `fotos/adc_fpga.jpeg` | ADC + FPGA (detalle) | `daq-fpga-etapas` (opción) |
| `fotos/dirver_corriente_viejo.jpeg` | Driver de corriente (versión vieja) | contexto del Driver |
| `fotos/evidencia_ruido_trigger.mp4` | Video del ruido EM en el disparo | **`ruido-em`** (extraer frame) |
| `fotos/video_daq_completo.mp4` | Video del DAQ en operación | evidencia general |
| `fotos/experimento_completo.mp4` | Video del experimento completo | evidencia general |

> Relación con datos: `../capturas/laser_wave.csv` es el export numérico de esa
> misma adquisición (osciloscopio en el láser, tensión).

## Pendiente
- Extraer frame(s) de `fotos/evidencia_ruido_trigger.mp4` → figura `ruido-em`.
- Recortar/elegir la mejor foto de ringing para `ringing-falso`.
