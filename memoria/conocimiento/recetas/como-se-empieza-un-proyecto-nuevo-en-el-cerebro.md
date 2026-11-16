---
tipo: "receta"
titulo: "Cómo se empieza un proyecto nuevo en el cerebro"
temas: ["cerebro", "proyectos"]
claves: ["_plantilla", "proyecto.json", "spec.md", "verificar.py"]
proyectos: []
fuentes: ["README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[cerebro]] · [[proyectos]]

1. Copiar `proyectos/_plantilla/` a `proyectos/<nombre>/`, con el nombre sin espacios.
2. Rellenar `spec.md` y adaptar `verificar.py`: es el test, va fuera de `borrador/` y las IAs no pueden tocarlo.
3. En `proyecto.json`, rellenar `temas`, `necesita` y `comando_prueba`. Si hace falta, también `repos` y `fuentes` (la única verdad), `protegidos`, `reglas` y `reintentar_si`.
4. Poner `"estado": "en-construccion"`.

> Copiar `proyectos/_plantilla/` a `proyectos/<nombre>/`
> — `README.md`
