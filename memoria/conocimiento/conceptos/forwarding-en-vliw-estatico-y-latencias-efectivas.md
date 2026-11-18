---
tipo: "concepto"
titulo: "Forwarding en VLIW estático y latencias efectivas"
temas: ["ac", "forwarding", "planificacion-estatica", "vliw"]
claves: ["forwarding", "bypass", "RAW hazard", "static scheduling", "VLIW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[forwarding]] · [[planificacion-estatica]] · [[vliw]]

El forwarding (bypass) en VLIW permite que el resultado de una operación esté disponible para la siguiente instrucción en el ciclo inmediatamente posterior a que termine su etapa productora (EX para ALU, MEM para carga). Sin forwarding, habría que esperar a WB. Con las latencias dadas:
- L.D emite en ciclo C → dato listo al final de C+1 (MEM=2) → consumidor puede emitir en C+2.
- ADD.D/MUL.D/DIV.D emiten en C → resultado listo al final de C+1 (EX=2) → consumidor en C+2.
- DADDUI emite en C → resultado en C (1 ciclo) → consumidor en C+1.
El planificador estático debe respetar estas distancias mínimas al colocar operaciones en los paquetes VLIW de 4 slots.

> Consider also that this processor supports forwarding and delayed branch.
> — `repo:datos/temarios/AC/examenes/January2016.pdf`

Relacionado: [[problema-de-planificacion-vliw-con-desenrollado-de-bucle-exa]] · [[parametros-de-temporizacion-vliw-examen-enero-2016]] · [[delayed-branch-en-vliw-y-su-efecto-en-planificacion]]
