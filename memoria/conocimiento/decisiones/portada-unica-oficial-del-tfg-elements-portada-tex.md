---
tipo: "decision"
titulo: "Portada única oficial del TFG (elements/portada.tex)"
temas: ["latex", "memoria", "tfg"]
claves: ["portada", "elements/portada.tex", "Memoria.tex", "input", "escudo UCLM ESII"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-21"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[memoria]] · [[tfg]]

La memoria debe usar exclusivamente la portada oficial definida en `elements/portada.tex`, que incluye escudo, universidad, escuela, tipo de trabajo, título, autor y fecha centrados. El archivo principal `Memoria.tex` la incluye con `\input{elements/portada}`. Está prohibido añadir cualquier otra portada, incluida la «segunda portada» con logos UCLM/ESII que está en `elements/preambulo.tex`.

> **Una sola portada: la oficial del TFG**, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[estructura-de-la-memoria-tfg-esiiab-uclm-plantilla-oficial]] · [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]] · [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]] · [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]]

## Ampliación (2026-11-23, )
- Usar exclusivamente `elements/portada.tex` como portada (contiene escudo UCLM/ESIIAB, tipo de trabajo, título, autor, fecha, todo centrado).
- En `Memoria.tex` incluir `\input{elements/portada}`.
- NO añadir la «segunda portada» con logos UCLM/ESII que trae `elements/preambulo.tex`.
- No crear portadas adicionales ni personalizadas.
