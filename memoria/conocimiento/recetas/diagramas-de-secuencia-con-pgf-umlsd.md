---
tipo: "receta"
titulo: "Diagramas de secuencia con pgf-umlsd"
temas: ["latex", "pgf-umlsd", "secuencia", "tikz"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock"]
proyectos: ["memoria-procesos"]
fuentes: ["proyectos/memoria-procesos/spec.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[pgf-umlsd]] · [[secuencia]] · [[tikz]]

- Entorno `sequencediagram`, en minúsculas. No existen `sequenceDiagram` ni `alt`: para alternativas se usa `sdblock`.
- Participantes con `\newthread` y `\newinst`.
- Llamadas anidadas con `call`, con origen, mensaje, destino y respuesta.
- Mensajes sueltos con `\mess`.
- En los textos de `\mess`, `call` y `\newinst` no puede ir `\#`, `\_`, `\&`, `#`, `&`, `_`, ningún comando ni, en `\mess`, paréntesis.

```latex
\resizebox{\textwidth}{!}{%
\begin{sequencediagram}
  \newthread{nav}{Navegador}
  \newinst[2]{api}{API (Express)}
  \begin{call}{nav}{POST /api/auth/login}{api}{200 o 401}
  \end{call}
\end{sequencediagram}}
```

> El entorno es `sequencediagram` (en minúsculas
> — `proyectos/memoria-procesos/spec.md`

Relacionado: [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[numeros-en-diagramas-de-secuencia-deben-coincidir-con-la-esp]] · [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-que-no-c]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
