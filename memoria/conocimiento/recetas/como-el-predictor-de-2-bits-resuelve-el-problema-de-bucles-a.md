---
tipo: "receta"
titulo: "Cómo el predictor de 2 bits resuelve el problema de bucles anidados"
temas: ["ac", "arquitectura-computadores", "bucles-anidados", "prediccion-saltos"]
claves: ["bucles anidados", "predictor 2 bits", "fallo única vez por iteración externa", "inicialización NT débil"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[bucles-anidados]] · [[prediccion-saltos]]

En bucles anidados (externo e interno), el salto del bucle interno se toma repetidamente hasta la última iteración. Con predictor de 1 bit, cada cambio de dirección causa fallo. Con 2 bits: en la primera iteración externa, el salto interno empieza en estado NT débil (01), predice NT, falla en la primera toma (pasa a DT 10), luego acierta las siguientes tomas (pasa a FT 11). En la última iteración, predice T (FT) pero el salto no se toma (fallo, pasa a DT). En la siguiente iteración externa, predice T (DT) y acierta. Resultado: solo 1 fallo por iteración externa (el de la última iteración del interno), salvo la primera iteración externa donde hay 2 fallos si se inicializa en NT.

> Resuelve el problema de los dos bucles anidados • El interno se predice incorrectamente sólo una vez por cada iteración externa (excepto en la primera iteración si la predicción inicial es NT)
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[predictor-dinamico-de-un-bit-funcionamiento-y-limitacion-en]] · [[calculo-de-predicciones-correctas-en-bucles-anidados-con-pre]] · [[predictor-de-1-bit-en-bucle-de-3-iteraciones-t-t-nt-produce]]
