---
tipo: "receta"
titulo: "Cómo obtener parámetros de hardware para el modelo Roofline en Linux"
temas: ["ac", "benchmark", "hardware", "linux", "lscpu", "stream"]
claves: ["lscpu", "STREAM", "FRECUENCIA_GHZ", "BW_DRAM", "TODO1"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[benchmark]] · [[hardware]] · [[linux]] · [[lscpu]] · [[stream]]

Procedimiento para rellenar TODO1 con datos reales de la máquina:
1. **Frecuencia CPU (GHz)**: ejecutar `lscpu` y buscar "CPU max MHz" o "CPU MHz". Convertir a GHz (dividir por 1000).
   - Ejemplo: 4900 MHz → 4.9 GHz.
2. **Ancho de banda DRAM (GB/s)**: ejecutar benchmark **STREAM** (compilar `stream.c` con `-O3 -fopenmp` y correr `./stream`).
   - Usar el valor "Copy" o "Scale" (suelen ser los más altos) en MB/s, convertir a GB/s (dividir por 1000).
   - Ejemplo: 26680 MB/s → 26.68 GB/s.
3. Sustituir en el script:
   ```python
   FRECUENCIA_GHZ = 4.9   # tu valor
   BW_DRAM = 26.68        # tu valor
   ```
Nota: La frecuencia debe ser la **máxima turbo sostenida** del núcleo, no la base. STREAM debe correr con afinidad a un solo núcleo para coincidir con el modelo mononúcleo.

> FRECUENCIA_GHZ = 4.9 # Tu frecuencia en GHz (de lscpu) BW_DRAM = 26.68 # Tus GB/s de la RAM (de STREAM)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py`

Relacionado: [[como-obtener-los-parametros-reales-de-tu-maquina-para-el-roo]] · [[como-generar-el-modelo-roofline-del-procesador-con-lscpu-y-s]] · [[valores-de-ejemplo-para-cpu-del-laboratorio-frecuencia-bw-pu]]
