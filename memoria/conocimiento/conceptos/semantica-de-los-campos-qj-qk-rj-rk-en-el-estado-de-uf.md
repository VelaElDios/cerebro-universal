---
tipo: "concepto"
titulo: "Semántica de los campos Qj, Qk, Rj, Rk en el estado de UF"
temas: ["ac", "dependencias", "qj", "qk", "rj", "rk", "scoreboard", "tomasulo"]
claves: ["Qj", "Qk", "Rj", "Rk", "NO", "SI", "unidad funcional productora"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencias]] · [[qj]] · [[qk]] · [[rj]] · [[rk]] · [[scoreboard]] · [[tomasulo]]

En la fila Divide (UF5) del ciclo 16: Qj=2 (el operando Fj=f0 lo produce UF2=Mult1), Qk vacío (Fk=f6 ya disponible), Rj=NO (f0 no listo), Rk=SI (f6 listo). Cuando la UF productora termina, pone Rj/Rk=SI y la UF consumidora puede iniciar lectura de operandos. En ciclo 20, Divide muestra Qj/Qk vacíos y Rj=SI, Rk=SI, indicando que ambos operandos ya están listos y la división puede proceder.

> Divide SI Div f10 f0 f6 2 NO SI
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`
