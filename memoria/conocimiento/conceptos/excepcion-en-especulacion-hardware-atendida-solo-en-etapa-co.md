---
tipo: "concepto"
titulo: "Excepción en especulación hardware: atendida solo en etapa commit"
temas: ["ac", "tomasulo"]
claves: ["especulación", "excepción", "commit", "Tomasulo", "ROB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

En ejecución especulativa (Tomasulo con ROB), las excepciones no se atienden inmediatamente. La instrucción marca la excepción en su entrada del ROB. Solo al llegar a commit (cabeza del ROB, sin especulación previa) se verifica y atiende la excepción, garantizando estado preciso.

> En la especulación basada en hardware (Tomasulo con especulación), una excepción causada por una instrucción especulativa: a) Es atendida sólo cuando la instrucción llega a la etapa commit
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf`

Relacionado: [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[bits-venenosos-en-especulacion-excepcion-no-recuperable-marc]] · [[tomasulo-especulativo-excepcion-en-instruccion-especulativa]] · [[paso-de-commit-en-tomasulo-especulativo-usa-rob-para-complet]] · [[como-rellenar-la-tabla-de-estado-en-tomasulo-con-especulacio]]
