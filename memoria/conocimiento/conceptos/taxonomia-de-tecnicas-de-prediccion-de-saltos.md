---
tipo: "concepto"
titulo: "Taxonomía de técnicas de predicción de saltos"
temas: ["ac", "arquitectura", "clasificacion", "prediccion-saltos"]
claves: ["predicción fija", "predicción estática", "predicción dinámica", "basada dirección", "basada código operación", "dirigida compilador", "un nivel historia", "dos niveles historia", "híbridos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[clasificacion]] · [[prediccion-saltos]]

Clasificación jerárquica: Predicción fija (siempre tomado o siempre no tomado). Predicción verdadera: Estática (basada en código objeto: por dirección, por código de operación, dirigida por compilador) y Dinámica (basada en historia de ejecución: un nivel de historia, dos niveles de historia, híbridos). La predicción estática decide en tiempo de compilación; la dinámica usa hardware para adaptarse en tiempo de ejecución según el comportamiento histórico.

> Predicción fija – Siempre lo mismo, tomado o no tomado – Predicción verdadera – A veces tomado, a veces no tomado – Estática – Basada en el código objeto – Dinámica – Basada en la historia de la ejecución – Basada en dirección – Basada en el código operación – Dirigida por el compilador – Un nivel de historia – Dos niveles de historia – Híbridos
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)
