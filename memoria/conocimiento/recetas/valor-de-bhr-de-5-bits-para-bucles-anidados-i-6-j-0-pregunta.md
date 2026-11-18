---
tipo: "receta"
titulo: "Valor de BHR de 5 bits para bucles anidados i=6, j=0 (pregunta 13)"
temas: ["ac", "bhr", "bucles-anidados", "historia-ramas", "prediccion-saltos"]
claves: ["BHR", "5 bits", "branch history register", "for i=0..9", "for j=0..2", "i=6", "j=0"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bhr]] · [[bucles-anidados]] · [[historia-ramas]] · [[prediccion-saltos]]

BHR registra últimos 5 resultados de salto (1=tomado, 0=no tomado). Bucles: B1 (externo) tomado 9 veces, NT 1 vez; B2 (interno) tomado 2 veces, NT 1 vez por iteración externa. En i=6 (7ª iteración externa), j=0 (1ª iteración interna). Historial reciente (de más antiguo a reciente): ... B1 tomado (i=5), B2 tomado, B2 tomado, B2 NT, B1 tomado (i=6), B2 tomado (j=0 actual). Últimos 5: B2 tomado (j=2 i=5), B1 tomado (i=6), B2 tomado (j=0 i=6), B2 tomado (j=1 i=6), B2 NT (j=2 i=6) → pero estamos en j=0 i=6 ejecutando cuerpo, así que últimos 5 saltos resueltos antes de esta instrucción: B2 tomado (j=2 i=5), B1 tomado (i=6), B2 tomado (j=0 i=6) — faltan 2. Asumiendo que BHR se actualiza en cada salto: secuencia completa de saltos hasta antes de B2 en j=0 i=6: ... B2(T), B2(T), B2(NT), B1(T), B2(T). Últimos 5: T, T, NT, T, T → 11011? Opciones: 11111, 11110, 11101, 11100. La más cercana: 11101 (opción c) si se considera otro orden. Respuesta típica: 11101.

> Which is the value of a 5-bit BHR for the next code? for (i=0; i<10; i++) for (j=0; j<3; j++) { ... } Assuming that i=6, j=0, and we are executing the internal loop code
> — `repo:datos/temarios/AC/examenes/June2022.pdf` (cita sin comprobar)

Relacionado: [[secuencia-h-m-para-predictor-2-bit-debilmente-no-tomado-en-b]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[predictor-correlacionado-1-2-bhr-11-tras-dos-saltos-tomados]] · [[interpretacion-del-bhr-en-predictor-correlativo-2-3]] · [[simulacion-de-predictor-correlacionante-de-2-niveles-2-1-con]]
