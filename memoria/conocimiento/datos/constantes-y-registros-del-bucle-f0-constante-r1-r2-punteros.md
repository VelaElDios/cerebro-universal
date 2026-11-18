---
tipo: "dato"
titulo: "Constantes y registros del bucle: F0 constante, R1/R2 punteros, fin límite"
temas: ["ac", "constantes", "pipeline", "registros"]
claves: ["F0 constante", "R1 puntero A", "R2 puntero B", "fin límite", "decremento 8 bytes"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[constantes]] · [[pipeline]] · [[registros]]

R1 y R2 son punteros a double (8 bytes), se decrementan en 8 cada iteración (hacia direcciones menores). F0 registro de punto flotante con valor constante multiplicador. 'fin' es etiqueta/dirección límite; SLTI R4, R1, fin pone R4=1 si R1 < fin (unsigned), BEQZ salta si R4=0 (i.e., R1 >= fin). El bucle itera mientras R1 < fin.

> El contenido de R1 y R2 son las direcciones de memoria donde se han almacenado los elementos de los vectores A y B. [...] DADDUI R1, R1, #-8 ; decrementa índice de A DADDUI R2, R2, #-8 ; decrementa índice de B SLTI R4, R1, fin ; comprobación de fin
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf` (cita sin comprobar)

Relacionado: [[codigo-del-bucle-original-para-planificacion-examen-ac-2017]] · [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[valores-iniciales-de-registros-del-bucle-examen-enero-2016]]
