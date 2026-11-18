---
tipo: "receta"
titulo: "Latencias VLIW examen AC para planificación bucle polinómico"
temas: ["ac", "latencias", "vliw"]
claves: ["ALU PF→ALU PF 3", "ALU PF→SF 2", "LF→ALU PF 1", "LF→SF 0", "ALU Ent→ALU Ent 0"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Diciembre2010.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[latencias]] · [[vliw]]

Tabla de latencias (ciclos de espera entre productor y consumidor) para el problema VLIW: 1) PF ALU → PF ALU: 3 ciclos (ej. MULTF → MULTF). 2) PF ALU → SF: 2 ciclos (ej. MULTF → SF). 3) Entera ALU → Entera ALU: 0 ciclos (ADDI → ADDI/BNE). 4) LF → PF ALU: 1 ciclo (LF → MULTF). 5) LF → SF: 0 ciclos (LF → SF). UF PF totalmente segmentadas (inician nueva op cada ciclo). Slots/ciclo: 2 memoria, 2 PF, 1 entera/salto.

> ALU PF                                     ALU PF                              3\n              ALU PF                                     SF                                  2\n              ALU Entera                                 ALU Entera                          0\n              LF                                         ALU PF                              1\n              LF                                         SF                                  0
> — `repo:datos/temarios/AC/examenes/Diciembre2010.pdf` (cita sin comprobar)

Relacionado: [[problema-examen-ac-planificacion-vliw-para-bucle-y-i-a-x-i-2]] · [[latencias-vliw-1-0-para-examen-enero-2026-problema-3]] · [[parametros-de-temporizacion-del-ejercicio-vliw-examen-enero]]
