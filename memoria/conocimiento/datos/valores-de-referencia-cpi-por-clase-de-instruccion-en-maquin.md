---
tipo: "dato"
titulo: "Valores de referencia: CPI por clase de instrucción en máquinas con/sin hardware FP (Ejercicio 3)"
temas: ["ac", "cpi", "emulacion", "evaluacion-rendimiento", "hardware-punto-flotante"]
claves: ["CPI multiplicación FP", "CPI suma FP", "CPI división FP", "CPI enteras", "MFP", "MNFP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[emulacion]] · [[evaluacion-rendimiento]] · [[hardware-punto-flotante]]

Máquina MFP (con hardware FP, 1000 MHz):
- Mult FP: 6 ciclos
- Add FP: 4 ciclos
- Div FP: 20 ciclos
- Enteras: 2 ciclos

Máquina MNFP (sin hardware FP, todo entero a 2 ciclos, 1000 MHz):
- Mult FP emulada: 30 instrucciones enteras × 2 ciclos = 60 ciclos equivalentes
- Add FP emulada: 20 × 2 = 40 ciclos
- Div FP emulada: 50 × 2 = 100 ciclos
- Enteras nativas: 2 ciclos

> Multiplicación en punto flotante: 6 • Suma en punto flotante: 4 • División en punto flotante: 20 • Instrucciones entera: 2
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]]
