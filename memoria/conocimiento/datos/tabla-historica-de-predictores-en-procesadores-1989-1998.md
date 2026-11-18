---
tipo: "dato"
titulo: "Tabla histórica de predictores en procesadores 1989-1998"
temas: ["ac", "historia", "prediccion-saltos", "procesadores"]
claves: ["80486", "Pentium", "Alpha 21264", "PowerPC", "UltraSparc", "R10000", "bimodal", "dos niveles"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[historia]] · [[prediccion-saltos]] · [[procesadores]]

Progresión histórica clave (página 47):
- 1989-1993: mayormente estáticos (siempre tomado, nunca tomado, por opcode).
- 1993-1994: primeros dinámicos de 1 bit (Gmicro, R8000) y bimodales de 2 bits en BTB/BHT (MC68060, Alpha 21064A, Pentium, PowerPC 604).
- 1995-1996: bimodales mayores (2K-512 entradas) en BHT o I-cache (Alpha 21164, UltraSparc, R10000, PowerPC 620, PA 8200).
- 1997: Pentium II — primer predictor adaptativo de dos niveles global (Gag).
- 1998: Alpha 21264 — predictor híbrido torneo (PAg + GAg) combinando local y global.

> Pentium II 1997 Dinámica Predictor 2 niveles adaptativo global (Gag) Alpha 21264 1998 Dinámica Híbrido (PAg + GAg)
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[predictores-de-un-nivel-de-historia-1-2-y-3-bits-con-procesa]] · [[ejemplos-reales-de-predictores-de-salto-en-procesadores-come]] · [[predictor-alpha-21264-tournament-branch-prediction-combina-l]]
