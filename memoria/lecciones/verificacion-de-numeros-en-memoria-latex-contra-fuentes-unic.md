---
titulo: "Cada cifra de un documento sale de las fuentes, también las pequeñas"
temas: ["general", "memoria"]
claves: ["no aparece en las fuentes", "inventado o mal copiado"]
estado: "confirmada"
veces: 1
fecha: "2026-10-13"
proyectos: ["memoria-procesos"]
---

Temas: [[general]] · [[memoria]]

## Problema
En un documento hecho a partir de fuentes (guía, documentación), las IAs cambian o «redondean» cifras.
El test solo comprueba los números mayores que 20, pero los pequeños también fallan: en la memoria de
procesos se escribió «16 PBIs iniciales, 17 con P19» cuando las fuentes dicen 15 y 16, y el revisor lo dio por bueno.

## Solución
Antes de escribir cualquier cifra (también las pequeñas, y las que salen de sumar), buscarla en las
fuentes y copiarla tal cual. Si hay que contar elementos de una lista (P1–P14 y P18), contarlos uno a uno
y comprobarlo con la tabla de la fuente. Lo que no está en las fuentes no se escribe.

## Ejemplo
«80 pruebas» → guia.md §7 «Total 80 pruebas automatizadas»; «15 PBIs al inicio» → gestion.md, tabla
«Evolución del sprint», fila «Inicio del Sprint 1».

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
