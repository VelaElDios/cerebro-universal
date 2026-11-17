---
titulo: "Evitar páginas casi vacías al final de anexos con longtable"
temas: ["latex", "maquetacion", "longtable"]
claves: ["Regla 9", "página casi vacía", "longtable", "párrafo suelto"]
estado: "propuesta"
veces: 1
fecha: "2026-11-17"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[maquetacion]] · [[longtable]]

## Problema
Un párrafo corto después de una `longtable` queda aislado en una página nueva, incumpliendo la Regla 9 (ninguna página casi vacía).

## Solución
Fusionar ese párrafo con el párrafo que introduce la tabla (antes de la `longtable`) y eliminar el párrafo posterior a la tabla. Así el texto fluye y no queda una página con solo una línea.

## Ejemplo
|
  % Antes (incorrecto)
  \end{longtable}
  }
  Párrafo suelto que queda solo en la siguiente página.

  % Después (correcto)
  Párrafo que introduce la tabla. Párrafo suelto integrado aquí.
  \end{longtable}
  }

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
