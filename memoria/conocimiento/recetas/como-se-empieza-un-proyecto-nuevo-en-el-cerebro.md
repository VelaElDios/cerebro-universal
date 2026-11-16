---
tipo: "receta"
titulo: "Cómo se empieza un proyecto nuevo en el cerebro"
temas: ["cerebro", "proyectos"]
claves: ["_plantilla", "proyecto.json", "spec.md", "verificar.py"]
proyectos: []
fuentes: ["README.md", "../../README.md"]
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

## Ampliación (2026-11-16, )
Pasos para crear un proyecto desde cero: (1) Copiar la carpeta `proyectos/_plantilla/` a `proyectos/<nombre>/` (sin espacios). (2) Escribir `spec.md` con las normas de qué producir y cómo, y adaptar `verificar.py` (test inmutable para las IAs). (3) Completar `proyecto.json` con al menos `nombre`, `temas` (lista de strings para filtrar lecciones), `necesita` (claves de `config/entornos.json` más paquetes `apt`/`pip` opcionales), `comando_prueba` (script que devuelve 0 si ok), y `"estado": "en-construccion"`. Opcionales: `repos`, `fuentes`, `copiar`, `protegidos`, `reintentar_si`, `archivo_principal`, `pasos`/`max_pasos`, `max_intentos`, `max_archivos_por_paso`, `roles`.
