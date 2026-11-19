---
tipo: "concepto"
titulo: "Confianza del conocimiento (verificado o propuesto)"
temas: ["cerebro", "conocimiento"]
claves: ["confianza", "verificado", "propuesto", "cita"]
proyectos: []
fuentes: ["scripts/cerebro/conocimiento.py", "../../README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[cerebro]] · [[conocimiento]]

Cada nota de `memoria/conocimiento/` lleva `confianza`:

- **`verificado`:** el código ha encontrado la cita literal de la nota en su fuente (las fuentes del proyecto, los archivos del borrador o el trozo del documento aprendido). Se puede usar sin volver a deducirlo.
- **`propuesto`:** no hay cita comprobada. Probablemente esté bien, pero hay que comprobarlo antes de darlo por cierto. Javier puede revisarlo y cambiarlo a `verificado`.

> (la cita aparece literal en la fuente)
> — `scripts/cerebro/conocimiento.py`

## Ampliación (2026-11-16, )
Dos niveles de confianza: (1) En `memoria/conocimiento/`, cada nota lleva `confianza: "verificado"` cuando tiene una cita literal comprobada del origen. (2) En `memoria/lecciones/`, las entradas nuevas creadas por el revisor tras arreglar un fallo nacen con `estado: "propuesta"`. Un humano (o proceso de revisión) debe leerlas y cambiar a `estado: "confirmada"` si son válidas, o borrarlas si son ruido. Solo las confirmadas se usan como lecciones para las IAs.

Relacionado: [[estructura-de-la-memoria-compartida-cerebro-md-estado-md-con]] · [[como-trabaja-el-cerebro-constructor-prueba-revisor]] · [[campos-de-proyecto-json-y-su-proposito]] · [[como-dar-instrucciones-al-cerebro-sin-tocar-el-borrador]]
