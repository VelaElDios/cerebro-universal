---
tipo: "receta"
titulo: "Implementación predictor correlacionado (m,n) con BHR y BHT"
temas: ["ac", "arquitectura-computadores", "bhr", "bht", "prediccion-saltos"]
claves: ["Branch History Register", "BHR", "Branch History Table", "BHT", "m bits historia", "n bits predictor", "2^m tablas BHT"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[bhr]] · [[bht]] · [[prediccion-saltos]]

El BHR es un registro de desplazamiento de m bits que guarda el resultado (T/NT) de los últimos m saltos ejecutados. Su valor selecciona una de 2^m tablas BHT. Cada BHT tiene entradas de n bits (predictor n-bit) indexadas por bits del PC del salto actual. Total de bits = 2^m × n × (número de entradas por BHT seleccionadas por PC). Ejemplo: predictor (2,2) tiene BHR de 2 bits → 4 tablas BHT, cada entrada 2 bits.

> Implementación: predictor (m,n)  BHR: Branch History Register Registro de desplazamiento de m bits (estado T/NT de los últimos m saltos) Seleccionan una de entre 2m tablas de BHT  BHT: Branch History Table Cada entrada tiene n bits (es un predictor de n bits) El nº de entrada de predicción se selecciona con la dirección del salto • Nº bits predictor (m,n) =2m x n x Nº de entradas de predicción seleccionadas por la dirección del salto
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)
