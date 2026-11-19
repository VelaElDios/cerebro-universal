---
tipo: "receta"
titulo: "Cómo configurar lstopo para obtener tamaños de caché reales antes de la práctica"
temas: ["ac", "herramientas", "memoria"]
claves: ["lstopo", "hwloc", "caché L1 L2 L3", "KiB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_pintarLatvsMem.py"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[herramientas]] · [[memoria]]

Antes de rellenar TODO1, ejecutar `lstopo` (paquete hwloc) para leer los tamaños reales de caché del equipo:
- `lstopo --no-io --no-legend` muestra árbol de topología con tamaños en KiB/MiB.
- Buscar "L1d", "L2", "L3" en la salida; anotar valores en KiB (el script usa KiB).
- Ejemplo del script: L1=48 KiB, L2=1280 KiB, L3=25000 KiB.
- Si `lstopo` no está instalado: `sudo apt-get install hwloc` (Debian/Ubuntu) o equivalente.
- Verificar que los tamaños coinciden con `/sys/devices/system/cpu/cpu0/cache/index*/size`.

> Tamaños de las cachés observadas en lstopo (Cambia esto)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_pintarLatvsMem.py`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
