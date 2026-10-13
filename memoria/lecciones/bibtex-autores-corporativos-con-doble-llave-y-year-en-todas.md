---
titulo: "BibTeX: autores corporativos con doble llave y year en todas las entradas"
temas: ["latex", "bibtex"]
claves: ["cita mal formada", "falta el año", "bibtex", "apalike"]
estado: "confirmada"
veces: 1
fecha: "2026-10-13"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[bibtex]]

## Problema
Con `author = {Universidad de Castilla-La Mancha}` BibTeX cree que «Universidad» es el nombre y «de Castilla-La Mancha» el apellido, y cita «[de Castilla-La Mancha, ]». Sin `year`, apalike deja la cita «[Neon, ]».

## Solución
Los autores que son organizaciones van con doble llave (`author = {{GitHub}}`). Todas las entradas llevan `year`; si la fuente no da fecha, `year = {s.f.}` (sin fecha).

## Ejemplo
```bibtex
@misc{neonlimits,
  author = {{Neon}},
  title = {What are the limits and quotas for Neon's Free plan?},
  year = {s.f.},
  howpublished = {\url{https://neon.com/faqs/free-plan-limits-and-quotas}}
}
```

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
