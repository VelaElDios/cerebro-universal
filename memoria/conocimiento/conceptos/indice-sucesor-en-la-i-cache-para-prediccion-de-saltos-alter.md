---
tipo: "concepto"
titulo: "Índice sucesor en la I-caché para predicción de saltos (alternativa a BTAC)"
temas: ["ac", "arquitectura", "i-cache", "indice-sucesor", "prediccion-saltos"]
claves: ["índice sucesor", "I-caché", "UltraSPARC", "Alpha 21264", "línea de caché", "instrucción destino"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[i-cache]] · [[indice-sucesor]] · [[prediccion-saltos]]

En lugar de BTAC separada, se añade un campo "índice sucesor" a cada línea de la I-caché. En la lectura de la línea, se obtiene en paralelo el índice sucesor. Si la línea contiene un salto condicional: predicción "tomado" → el índice apunta a la línea de la instrucción destino; predicción "no tomado" → apunta a la siguiente línea secuencial. Usado en UltraSPARC y Alpha 21264.

> A cada línea de la cache de instrucciones se añade un campo (índice sucesor). El acceso al índice sucesor se realiza en paralelo con la lectura de la línea de cache. Si existe una instrucción de salto en la línea de cache: si se predice como tomado, el índice sucesor apunta a la instrucción destino del salto; si se predice como no tomado, el índice sucesor apunta a la siguiente línea de cache
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)
