---
tipo: "receta"
titulo: "Cómo estructurar el CSV de entrada para la plantilla SUS"
temas: ["datos", "latex", "sus", "usabilidad"]
claves: ["respuestas.csv", "Likert", "CSV", "participantes", "perfiles"]
proyectos: ["plantilla-sus"]
fuentes: ["../plantilla-sus/spec.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[datos]] · [[latex]] · [[sus]] · [[usabilidad]]

El archivo `datos/respuestas.csv` debe tener una fila por participante con estas columnas exactas:
- `id`: identificador único (ej. U1, U2)
- `perfil`: rol del participante (ej. Cliente, Encargado)
- `q1` a `q10`: respuestas en escala Likert 1-5 (enteros)
- `comentario`: texto libre entre comillas

Ejemplo válido:
```
id,perfil,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,comentario
U1,Cliente,5,1,5,1,4,2,5,1,5,1,"Visualización de métricas clave sin editar fórmulas"
U2,Encargado,4,2,5,1,5,1,4,2,4,1,"Interfaz limpia y ágil"
```
Requisitos: 3-5 participantes de ejemplo con datos realistas. Si falta una respuesta o está fuera de 1-5, el documento debe avisar claramente en vez de calcular mal.

> Una fila por participante: id,perfil,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,comentario
> — `../plantilla-sus/spec.md`

Relacionado: [[estructura-de-archivos-obligatoria-para-la-plantilla-sus]] · [[escalas-de-transformacion-sus-adoptadas-sauro-lewis-bangor-e]] · [[como-se-calcula-la-puntuacion-sus-formula-y-ejemplo]]

Origen: [[proyectos/plantilla-sus/estado|plantilla-sus]]
