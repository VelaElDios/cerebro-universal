---
tipo: "concepto"
titulo: "Bits de predicción en la I-caché: funcionamiento y ventajas"
temas: ["ac", "arquitectura", "bits-prediccion", "i-cache", "prediccion-saltos"]
claves: ["bits predicción I-caché", "Alpha 21064", "Alpha 21064A", "UltraSPARC", "índice sucesor", "BTB independiente"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[bits-prediccion]] · [[i-cache]] · [[prediccion-saltos]]

Los bits de predicción se almacenan directamente en cada línea de la I-caché (o por instrucción). Al leer la línea, se accede en paralelo a los bits. Si hay un salto y se predice tomado, se usa el índice sucesor para ir a la instrucción destino. Dos variantes de diseño: bits por instrucción o bits por línea de caché. Acceso puede ser con BTB independiente o añadiendo índice sucesor a la I-caché. Ventajas: predice saltos que no están en BTB; overhead hardware moderado. Ejemplos: Alpha 21064 (2K×1 bit), Alpha 21064A (4K×2 bits), UltraSPARC (2K×1 bit).

> Añade los bits de predicción a cada línea de la cache de instrucciones. Alpha 21064 (1992) 2K x 1 bit Alpha 21064A (96) 4K x 2 bits UltraSparc (1992) 2K x 1 bit. Ventajas: Puede predecir instrucciones que no están en la BTB. No añade una cantidad extra excesiva de hardware
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[indice-sucesor-en-la-i-cache-para-prediccion-de-saltos-alter]]
