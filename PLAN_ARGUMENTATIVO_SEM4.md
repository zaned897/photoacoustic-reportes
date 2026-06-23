# Plan argumentativo — Reporte de Avance, Semestre 4

> Documento de trabajo. Backbone para (a) el reporte extenso de Sem 4 y (b) sus
> láminas de presentación, dando continuidad al reporte de Sem 3.
> Autor: Eduardo Santos Mena · Asesores: Dr. Samuel Pérez Huerta, Dr. Augusto David Ariza Flores.
> Estado: borrador para revisión. Las decisiones abiertas están al final (§9).

---

## 0. Tesis del semestre (idea central en una frase)

> **El semestre consolidó y validó la cadena electrónica de adquisición completa
> (DAQ con ADC físico + Driver V2.0) conforme al diseño. Al llevar el sistema al
> banco, la barrera crítica resultó estar en el primer eslabón de la cadena de
> detección: el transductor piezoeléctrico no entregó una señal eléctrica
> observable ni ante una fuente acústica mecánica conocida (rotura de mina,
> Hsu–Nielsen) ni ante la excitación láser, medido directamente en el osciloscopio
> —es decir, con independencia del DAQ y del transitorio EMI de la avalancha. El
> transitorio que sí aparece en el DAQ proviene del acoplamiento eléctrico
> (pickup) de la descarga HV, no de una detección acústica. El semestre, por
> tanto, localiza el problema en el front-end de detección acústica (salud del
> sensor, acoplamiento acústico y piso de observabilidad/pre-amplificación) y
> define su bring-up por capas —con fuente conocida, en el osciloscopio, antes del
> láser— como el paso decisivo.**

Esta tesis convierte un "no se pudo excitar el sensor" en lo que realmente es: un
**resultado de ingeniería** (aislamiento de la variable bloqueante mediante
validación por capas), coherente con la metodología de *bring-up* por etapas que
ya distingue a este proyecto.

---

## 1. Hilo argumentativo (arco narrativo del documento)

1. **De dónde venimos (continuidad Sem 3).** En Sem 3 el núcleo digital se validó
   con un *Virtual ADC* (señales sintéticas): integridad (0 % pérdida),
   linealidad (R²=1.0000) y respuesta dinámica. Quedó pendiente la integración
   física del ADC y la primera adquisición acústica real.
2. **Qué se logró en Sem 4 (lo positivo, sólido).**
   - **Integración física ADC↔FPGA validada con señal real**: el AD9226 opera y
     se lee correctamente; la cadena digital captura, almacena y transmite sin
     pérdida (validación por etapas `bringup/stage0…8`).
   - **Resolución y velocidad reales**: 12 bits efectivos (LSB = 2.44 mV) a
     54 MSPS (PLL ×2). Es decir, el DAQ ya **supera** lo planeado para Sem 4
     (8→12 bits) y demuestra resolución suficiente para resolver el *ringing* del
     transductor de 2.5 MHz.
   - **Driver V2.0 validado**: control embebido RP2040, gestión térmica y
     retroalimentación óptica (fotodiodo + TIA) operativos.
3. **El muro (lo negativo, honesto).** No se logró detectar ninguna onda acústica.
   Verificado **en el osciloscopio** (sin pasar por el DAQ): ni con una fuente
   acústica mecánica conocida (**Hsu–Nielsen**, rotura de mina) ni con la
   **excitación láser** apareció una señal atribuible a ultrasonido. El transitorio
   que el DAQ sí registra es *pickup* eléctrico de la avalancha (EMI), **no**
   detección acústica.
4. **El diagnóstico (el corazón del semestre).** El problema está en el **primer
   eslabón: el front-end de detección acústica**. Como una fuente conocida tampoco
   produjo señal en el osciloscopio, la incógnita no es el láser ni el digital, sino
   la cadena sensor → acoplamiento → (pre)amplificación → observabilidad. Se aborda
   con un *bring-up* por capas de la detección (§4): salud eléctrica del piezo,
   acoplamiento acústico, piso de observabilidad y pre-amplificación.
5. **La salida (constructiva).** Establecer una **detección acústica verificable con
   fuente conocida en el osciloscopio, antes del láser**: confirmar que el piezo está
   vivo y acoplado, añadir el **preamplificador de bajo ruido** que suba señales
   débiles por encima del piso de observación, y solo entonces reintroducir el láser.
   La EMI de la avalancha se trata como **artefacto a controlar** (apantallamiento,
   sincronía por disparo óptico), **no** como el problema central (§5).
6. **El costo (evaluación del retraso) y el re-plan.** El retraso está
   **localizado en un solo hito** (primera adquisición acústica), no es difuso;
   por eso es acotado y recuperable: el camino de datos ya está listo, así que la
   mitad posterior (procesamiento, reconstrucción, IA) puede comprimirse (§6).

---

## 2. Mapa claim → evidencia → estado

| # | Afirmación (claim) | Evidencia que la sostiene | Estado |
|---|---|---|---|
| C1 | El núcleo digital captura/transmite sin pérdida | `bringup/stage2,6,8`; diente de sierra continuo; FSM store-and-forward | ✅ Demostrado |
| C2 | La conversión es lineal y precisa | Exp. B Sem 3 (R²=1.0000, err 0.37 LSB) + ADC físico AD9226 en rango | ✅ (falta repetir con ADC físico → §5) |
| C3 | La resolución del DAQ basta para el *ringing* del sensor 2.5 MHz | 12 bits @ 54 MSPS → 21.6 muestras/ciclo @ 2.5 MHz; LSB 2.44 mV | ✅ Argumentable |
| C4 | El Driver V2.0 es estable y monitorea energía pulso a pulso | Esquemático TIA + fotodiodo; pruebas térmicas | ✅ Validado |
| C5 | No hubo detección acústica: ni Hsu–Nielsen ni láser produjeron señal en el osciloscopio | Pruebas directas en osciloscopio (sin DAQ) con fuente mecánica conocida y con láser | ⚠️ Resultado negativo (clave) |
| C6 | La señal observada (~150 mV pp, ~2.6 MHz) es *pickup* EMI, no detección | Persiste con sensor desconectado; coincide en t=0 (sin TOF); no cambia con la distancia | ✅ Demostrado (3 controles) |
| C6b | La incógnita está en el front-end de detección (sensor/acoplamiento/observabilidad) | Una fuente conocida tampoco se detectó → no es láser ni digital | 🔬 A localizar por bring-up (§4) |
| C9 | El hueco principal es la ausencia de preamplificador (piezo en crudo al ADC) | Setup actual sin LNA; señal PA µV–mV ≪ pickup de 150 mV | 🔬 Acción definida (§4.3–4.4) |
| C7 | Un preamplificador de bajo ruido + acoplamiento de impedancia resuelve el cuello de botella | Análisis de impedancia de fuente piezo vs. Z_in del ADC; SNR objetivo | 🔬 Por validar (§4.4) |
| C8 | La impedancia de entrada del ADC carga la señal piezo | El piezo es fuente de alta-Z; Z_in baja del ADC atenúa y desadapta | 🔬 Por cuantificar |

> Regla de honestidad: C1–C4 se reportan como **resultados**; C5 como **resultado
> negativo** (válido y valioso); C6–C8 como **hipótesis con plan de verificación**.
> No afirmar adquisición fotoacústica hasta tener señal con TOF coherente.

---

## 3. Estructura del documento extenso (continuidad con Sem 3)

Mismo esqueleto del Sem 3 + dos secciones nuevas (Plan B y Re-planificación).

| Sección | Argumento que debe cargar |
|---|---|
| **Resumen (abstract)** | Validación de la cadena DAQ con ADC físico + Driver V2.0; identificación de la barrera analógica/EM como hallazgo central; definición del AFE y re-plan. Tono: avance sólido con un bloqueo bien diagnosticado. |
| **1. Introducción** | Retomar Sem 3 (caja blanca FPGA vs. caja negra osciloscopio). Tesis: el reto migró del dominio digital (resuelto) al dominio de la **detección analógica de señales débiles en presencia de excitación HV**. |
| **2. Objetivos del periodo** | Planeados (del cronograma Sem 3) vs. alcanzados. Distinguir: cumplidos (integración ADC, 12 bits), parcial (FIFO/ventana), bloqueado (primera adquisición acústica) y emergente (diagnóstico del AFE). |
| **3. Metodología y desarrollo** | 3.1 Integración física ADC↔FPGA y validación por etapas (bring-up). 3.2 Caracterización del DAQ en rango (linealidad, ruido, ENOB). 3.3 Montaje de detección y protocolo de intento de adquisición PA. 3.4 Driver V2.0 en operación. |
| **4. Resultados** | 4.1 DAQ con ADC físico validado (positivo). 4.2 Driver V2.0 (positivo). 4.3 **Intento de adquisición PA: resultado negativo caracterizado** (el falso positivo por EMI, con su firma temporal). |
| **5. Discusión** | El núcleo: §4 de este plan. Diagnóstico de causa raíz (EMI + impedancia + sincronía), análisis cuantitativo, por qué el preamp es decisivo. |
| **6. Limitaciones** | Ventana de 5 µs (~3.75 mm) ≪ profundidad requerida (~5.8 cm); sin pre-trigger; trigger eléctrico contaminado; falta validación acústica. |
| **7. Conclusiones** | Cadena digital cerrada y validada; cuello de botella aislado y accionable; proyecto listo para atacar el AFE. |
| **8. Plan B** | Validación acústica por pulso-eco / transmisión, desacoplada del láser (§5). |
| **9. Re-planificación y evaluación del retraso** | Cronograma revisado + análisis del impacto y de la recuperación (§6). |
| **10. Trabajo futuro** | AFE → primera señal PA en fantoma → reconstrucción → IA (denoising). |

---

## 4. Diagnóstico técnico central — bring-up de la detección acústica

### 4.1 La evidencia: lo observado es *pickup*, no acústica

Medición en osciloscopio (CH1 = pulso láser; CH2 = transductor Yushi 2.5 MHz vía
cable BNC–SMA, conectado **en crudo** al módulo ADC AD9226 / osciloscopio, **sin
preamplificador**):

- CH2 muestra una onda de **~150 mV pp** que **coincide exactamente** con el pulso
  láser de CH1, con apariencia de *ringing* de **~2.6 MHz**.
- **Tres controles prueban que NO es acústica:**
  1. **Desconexión del sensor:** la misma onda **persiste** con el transductor
     desconectado → no proviene del sensor.
  2. **Coincidencia temporal (t=0):** llega exactamente con el láser, **sin retardo
     de tiempo de vuelo** → es electromagnética (velocidad de la luz), no acústica
     (que llegaría µs después).
  3. **Distancia:** mover el láser/eventos a varias distancias del sensor no cambia
     la onda → sin dependencia de TOF.

El *ringing* de ~2.6 MHz lo fija la **red de entrada** (cable + Z_in del ADC/osc.) o
el propio driver, no la resonancia del piezo (persiste desconectado). Que se parezca
a 2.5 MHz es coincidencia.

**Conclusión:** la señal observada es **acoplamiento eléctrico (EMI/pickup)
sincronizado con el disparo**, no detección acústica. Hsu–Nielsen (mecánica, sin
láser) no produjo señal observable — coherente con que (a) **no hay
preamplificador** y (b) Hsu–Nielsen es de banda baja (<1 MHz), mal acoplada a un
transductor de 2.5 MHz. **Aún no se ha demostrado ninguna detección acústica real.**

### 4.2 Bring-up de la detección (escalera diagnóstica)

Mismo principio que el bring-up del FPGA: **una variable por capa**, no se avanza
hasta que la anterior pasa.

| Capa | Prueba | Qué confirma | Si falla, apunta a |
|---|---|---|---|
| **D0** | Salud eléctrica del piezo: capacitancia (LCR), continuidad | Elemento vivo e intacto; da Cs para el presupuesto de ruido | Sensor/cableado abierto o dañado |
| **D1** | Estímulo mecánico directo **con el láser apagado** (toque/golpe en la cara) → osciloscopio 1 MΩ | El piezo convierte mecánica→voltaje (sin confundir con pickup) | Carga del osciloscopio, cable, o elemento muerto |
| **D2** | Fuente acústica conocida **acoplada**: pulso-eco / 2º transductor (in-band), o láser sobre absorbente fuerte mirando la **ventana retardada** | Hay transmisión acústica real al sensor | Acoplamiento (aire), geometría, o banda de la fuente |
| **D3** | Añadir **preamplificador** de bajo ruido junto al sensor | Sube señales débiles sobre el piso de observación | Confirma que faltaba ganancia / Z de entrada |
| **D4** | Reintroducir **láser** (PA) ya con D0–D3 en verde | Primera señal PA con TOF coherente | Aísla generación PA / fluencia / absorción |

> **Discriminador clave:** la señal acústica real llega **retardada** por el tiempo
> de vuelo (p. ej. 1 cm ≈ 6.5 µs); el pickup llega en **t=0**. Por eso D1 va con el
> **láser apagado**, y en D4 hay que buscar la señal **en la ventana retardada** (no
> en t=0) y verificar que **se desplaza al variar la distancia** fuente↔sensor.

### 4.3 Causas (re-ordenadas con la evidencia de §4.1)

1. **Sin preamplificador: el piezo va en crudo al ADC/osciloscopio.** Señales
   PA/eco (µV–mV) en un piezo de alta-Z, cargado por el cable BNC–SMA y la Z_in del
   instrumento, sin amplificar → quedan bajo el piso de observación **y bajo el
   pickup de 150 mV**. **Es el hueco principal.** Lo resuelve un LNA junto al sensor
   (§4.4); además, su salida de baja impedancia es mucho menos susceptible al pickup
   que la línea cruda de alta-Z.
2. **Pickup EMI dominante (~150 mV pp).** El driver láser/avalancha irradia y la
   línea de alta-Z + cable lo captan. Hay que **apantallar, aterrizar y separar en
   tiempo** (la señal real está retardada por TOF respecto al pickup en t=0 →
   ventana retardada / *time-gating*).
3. **Salud del sensor sin verificar.** No se midió la capacitancia (LCR). Confirmar
   que el piezo está vivo (D0) y responde a estímulo mecánico sin láser (D1).
4. **Conexión directa a un módulo ADC no pensado para fuente piezo de alta-Z.** El
   AD9226 module espera una fuente acondicionada (rango/Z definidos); el preamp/AFE
   resuelve la adaptación end-to-end.

> Nota acoplamiento: se usó gel y eventos a varias distancias, así que el camino
> acústico se intentó; pero hasta que no haya preamp + rechazo de pickup, no se podrá
> evaluar de verdad. **Verificar que sea gel de ultrasonido (acústico)**, no gel
> conductor de electrodos, y que la fuente PA y el transductor compartan el mismo
> medio acústico (no aire de por medio).

### 4.4 Especificaciones propuestas del preamplificador

Objetivo: amplificar señales PA débiles **en el sensor**, sin cargar el piezo de
alta-Z y sin añadir ruido apreciable, sobre la banda del transductor.

| Parámetro | Especificación propuesta | Justificación |
|---|---|---|
| Topología | LNA de voltaje alta-Z **o** amplificador de carga (virtual ground) | No cargar el piezo (alta-Z) / inmunidad a la capacitancia del cable |
| Impedancia de entrada | ≥ 1 MΩ ∥ pocos pF (voltaje) | Evitar el divisor que atenúa la señal |
| Ganancia | 40–60 dB (×100–×1000), 1–2 etapas | Llevar µV–mV al rango ±5 V del ADC |
| Ancho de banda (−3 dB) | 0.1–5 MHz plano | Cubre 2.5 MHz central y banda −6 dB (1–4 MHz) |
| Ruido referido a entrada | ≤ 3–5 nV/√Hz (idealmente < 1 nV/√Hz) | La señal PA está cerca del piso de ruido |
| GBW del amplificador | ≥ 500 MHz–1 GHz | Para ×100 plano hasta 5 MHz |
| Alimentación | ± 5 V (o single 5 V) de bajo ruido | Compatibilidad con AFE actual |
| Apantallamiento | Caja metálica + coax corto + guarda del nodo de alta-Z | Rechazo de EMI HV |

**Candidatos concretos a evaluar:**
- **AD8331 / AD8332** (LNA + VGA *purpose-built* para ultrasonido, ruido ~0.74 nV/√Hz) — **opción primaria**: hecho exactamente para recepción de eco.
- **OPA657** (JFET, GBW 1.6 GHz, 4.8 nV/√Hz) — alta-Z + alto BW, opción discreta.
- **Amplificador de carga** con front JFET (BF862 / 2SK170) + op-amp (AD8067) — robusto a la capacitancia del cable.
- **MAX4805/4806** — LNA de ultrasonido alternativo.

> Dejar en el reporte una tabla de *trade-off* y elegir 1 para fabricar. Verificar
> **acoplamiento de impedancias** transductor↔preamp↔AFE↔ADC end-to-end.

### 4.5 La EMI de la avalancha: artefacto a controlar (secundario)

No es el problema central, pero hay que (a) no confundirla con señal y (b) evitar que
sature la entrada cuando **sí** haya detección:
- **Sincronía por disparo óptico**: usar el fotodiodo/TIA del Driver V2.0 como t=0
  limpio, eléctricamente aislado del lazo de avalancha.
- **Apantallamiento Faraday** del transductor + preamp; coax corto; tierra en
  estrella; separación física del lazo HV.
- **Blanking / ventana retardada / pre-trigger** (etapa 9) para excluir el transitorio.

### 4.6 Cuantificación útil (para cerrar el argumento, una vez haya detección)

- **TOF:** v ≈ 1540 m/s → 1 cm ≈ 6.5 µs; 5.8 cm ≈ 37.7 µs. La ventana actual de
  5 µs ≈ **7.7 mm** → habrá que ampliarla (FIFO) para profundidad útil.
- **Ringing:** 54 MSPS / 2.5 MHz ≈ **21.6 muestras/ciclo** → resolución temporal
  suficiente (sostiene C3).
- **Impedancia:** estimar |Z| del piezo a 2.5 MHz vs. Z_in → atenuación; justifica
  numéricamente el preamp de alta-Z.
- **Ruido:** amplitud esperada (µV–mV) vs. piso (ruido referido × √BW) → ganancia y
  SNR objetivo.

---

## 5. Plan B (propuesto) — contingencia y prueba definitiva in-band

> Nota: la idea original de "validar con fuente conocida" **ya no es Plan B**: pasó a
> ser la ruta principal (§4.2, D2) y de hecho **ya se intentó** (Hsu–Nielsen, sin
> éxito). Lo que queda como Plan B es (1) la prueba **in-band** definitiva y (2) la
> contingencia de alcance del semestre.

### Plan B-1 — Prueba in-band del sensor (orden por viabilidad con tu equipo actual)
A diferencia de Hsu–Nielsen (<1 MHz), estas excitan al transductor en su propia banda
(2.5 MHz). Hoy **no tienes pulser ni 2º transductor**, así que el orden realista es:

1. **Láser sobre absorbente fuerte (ya lo tienes).** Disparar sobre un absorbente
   bien definido (grafito, cinta negra, tinta china) acoplado por gel a distancia
   conocida y buscar la señal **en la ventana retardada por TOF** (no en t=0). Si
   aparece y **se desplaza con la distancia**, es PA real. Es la prueba más directa
   una vez haya preamp + apantallamiento.
2. **Pulso-eco "de pobre" con generador de funciones.** Excitar el transductor con un
   *burst* de 2.5 MHz vía resistencia serie y observar ecos tras el *drive*.
3. **Inyección eléctrica calibrada** al preamp/AFE → caracteriza ganancia, BW y ruido
   de la cadena receptora (sin parte acústica).

### Plan C — Adquirir instrumentación de validación acústica
Si lo anterior no zanja: conseguir/armar un **pulser de ultrasonido** (spike MOSFET)
y/o un **2º transductor** de 2.5 MHz para **pulso-eco / pitch–catch** en tanque de
agua — la validación in-band definitiva, desacoplada del láser.

Si la cadena capta eco/PA con SNR sano ⇒ sensor + preamp + DAQ probados, y la
incógnita restante se aísla a la **generación PA** (fluencia/absorción del láser).

### Plan B de alcance (si la señal PA sigue esquiva al cierre del semestre)
Reencuadrar el entregable del semestre como **"plataforma de instrumentación PA de
bajo costo con cadena de recepción validada por ultrasonido"** + caracterización
del AFE, difiriendo la imagen PA en fantoma. Sigue siendo una contribución
publicable de instrumentación (alineado con Mes 6 del plan original: artículo).

---

## 6. Re-planificación y evaluación del retraso

### 6.1 Estado vs. cronograma original de Sem 4 (del reporte Sem 3)

| Mes (plan original) | Entregable | Estado real |
|---|---|---|
| M1 Integración ADC-FPGA | Soldar AD9226, validar reloj | ✅ Hecho (a 54 MHz, no 65) |
| M2 Firmware FIFO + 8→12 bits | Buffers, 12 bits | 🟡 12 bits ✅; **FIFO/ventana grande pendiente** |
| M3 Pruebas en fantomas (A-scans) | Señal PA en gelatina+grafito | ❌ Bloqueado (detección) |
| M4 Procesamiento (retroproyección) | Reconstrucción básica | ⏳ No iniciado |
| M5 IA preliminar (denoising) | NN 1D | ⏳ No iniciado |
| M6 Escritura/difusión | Artículo + reporte | ⏳ En curso (este reporte) |

### 6.2 Evaluación del retraso (cómo argumentarlo)

- **Naturaleza:** el retraso está **localizado en un único hito** (M3, primera
  adquisición acústica). No es difuso ni afecta el camino de datos, que ya está
  cerrado (M1–M2 cumplidos o superados).
- **Magnitud:** acotada al ciclo **diseño→fabricación→prueba del AFE** (estimar en
  semanas, no meses). El Plan B corre en paralelo y de-riesga el hito.
- **Recuperabilidad:** alta. Una vez haya señal acústica, **M4 (retroproyección) y
  M5 (denoising) son mayormente software** sobre datos ya capturables → se pueden
  **comprimir/solapar**, recuperando parte del tiempo perdido.
- **Riesgo residual:** si el AFE no basta (EMI severa), el Plan B de alcance
  protege el entregable del semestre.

### 6.3 Cronograma revisado (propuesta, ajustar fechas)

| Bloque | Actividad | Entregable |
|---|---|---|
| B1 (ahora) | Diseño AFE: preamp + acoplamiento Z + apantallamiento + sincronía óptica | Esquemático + simulación + presupuesto de ruido |
| B1' (paralelo) | **Plan B**: validación pulso-eco / inyección calibrada | Eco real capturado por el DAQ (de-riesgo) |
| B2 | Fabricación y prueba del AFE | Cadena de recepción medida (ganancia/BW/ruido) |
| B3 | Firmware: ventana grande (FIFO) + ventana retardada/pre-trigger | A-scan de profundidad útil (~5.8 cm) |
| B4 | Primera adquisición PA en fantoma (gelatina + grafito) | A-scan PA con TOF coherente |
| B5 | Procesamiento: retroproyección (comprimido) | Imagen/reconstrucción básica |
| B6 | IA preliminar (denoising 1D) + escritura | NN + artículo/reporte |

---

## 7. Reflexiones (sección de cierre del reporte)

- La metodología de **validación por capas** funcionó: permitió afirmar con certeza
  que el digital no es el problema y señalar el analógico — eso *es* el avance.
- El proyecto pasó de "¿podemos digitalizar?" (resuelto) a "¿podemos detectar
  señales débiles junto a una excitación HV?" — la pregunta correcta y más difícil.
- Lección: en sistemas PA de bajo costo, el **front-end analógico y la integridad
  electromagnética** dominan el éxito tanto como el cómputo. (Buen mensaje para el
  artículo de instrumentación de bajo costo.)

---

## 8. Esquema de láminas (presentación Sem 4)

Continuidad visual con las láminas de Sem 3. ~14 diapositivas:

1. Portada (título, autor, asesores, "Avance Semestre 4").
2. Recapitulación Sem 3 (caja blanca FPGA, validación virtual).
3. Objetivo del semestre y mapa de avances (cumplido/parcial/bloqueado).
4. Integración física ADC↔FPGA (foto + bring-up por etapas).
5. DAQ validado en rango: 12 bits @ 54 MSPS, linealidad, *ringing* resoluble.
6. Driver V2.0 validado (control RP2040 + retroalimentación óptica TIA).
7. El intento de detección: **Hsu–Nielsen y láser → nada en el osciloscopio**.
8. La distinción clave: el transitorio del DAQ es **EMI de la avalancha**, no detección.
9. **Diagnóstico**: el cuello de botella está en el front-end de detección + escalera D0–D4.
10. La solución: salud del piezo → acoplamiento → **preamplificador** (specs) → láser.
11. **Plan B**: prueba in-band por **pulso-eco** + contingencia de alcance.
12. Evaluación del retraso (localizado, acotado, recuperable).
13. Cronograma revisado (Gantt B1–B6).
14. Conclusiones y reflexiones.

---

## 9. Decisiones abiertas (lo que necesito de ti antes del documento extenso)

1. **Documento base (protocolo) y avances Sem 2**: aún no los tengo. ¿Los subes?
   Sirven para alinear introducción, objetivos generales y bibliografía.
2. **Transductor: ¿2 MHz o 2.5 MHz?** Tu AFE está calculado para 2.5 MHz; el repo
   dice 2 MHz. Unificar antes de escribir.
3. **Preamplificador**: ¿quieres comprometerte con la opción primaria (AD8331/8332
   de ultrasonido) o exploramos el amplificador de carga discreto? ¿Tienes datos
   reales del piezo (capacitancia/Z, frecuencia exacta) para el presupuesto de ruido?
4. **Plan B**: ¿tienes acceso a un *pulser* de ultrasonido / segundo transductor /
   tanque de agua para la validación pulso-eco? Eso define cuál variante de Plan B
   es realista.
5. **Datos/figuras reales del Sem 4**: capturas del "falso positivo", fotos del
   montaje, mediciones del ADC en rango → para poblar §4 de Resultados.
6. **Fechas**: rango de meses real del Sem 4 para fijar el cronograma revisado.
7. **Formato/destino**: ¿el reporte extenso lo hago como proyecto LaTeX (clonando
   la plantilla del Sem 3) y las láminas en Beamer/PowerPoint?

---

### Anexo: referencias reutilizables del `references.bib` (Sem 3)
Ya disponibles para citar: `lin_emerging_2022` (PAT/artritis), `wu_advanced_2021`,
`li_photoacoustic_2020` (LED 445 nm bajo costo), `xia_photoacoustic_2014`,
`wang_photoacoustic_2012`, `beard`/revisiones PA, `hauptmann_deep_2020`,
`grohl_deep_2021` (IA/denoising). Faltaría añadir refs de **LNA/AFE de ultrasonido**
y **EMI/integridad de señal** para sostener §4.
