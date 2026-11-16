---
tipo: "decision"
titulo: "Los datos de entrenamiento van a un repo privado"
temas: ["cerebro", "datos", "ia-local"]
claves: ["DATOS_TOKEN", "DATOS_REPO", "cerebro-datos", "jsonl"]
proyectos: []
fuentes: ["scripts/cerebro/dataset.py"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[cerebro]] · [[datos]] · [[ia-local]]

Cada llamada a una IA (sistema, mensaje, respuesta y qué pasó después: prueba, si se deshizo y el veredicto del revisor) se guarda como una línea JSON. Va comprimida por meses en el repo privado `cerebro-datos` (`datos/AAAA-MM/<proyecto>.jsonl.gz`), junto a `export/conocimiento.jsonl`, que tiene todas las notas del vault listas para RAG.

Va aparte por dos motivos:
- **Tamaño:** los mensajes llevan las fuentes y el borrador enteros.
- **Privacidad:** el vault es público.

Con estos datos, una IA local se puede afinar con los pasos aceptados y enseñar a preferirlos frente a los deshechos.

> los datos NO van al repo público
> — `scripts/cerebro/dataset.py`
