---
tipo: "receta"
titulo: "Diagramas de secuencia con pgf-umlsd (sequencediagram)"
temas: ["diagramas", "diagramas-secuencia", "latex", "pgf-umlsd", "secuencia", "sequencediagram", "tikz", "uml"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex", "spec del proyecto (bloque «Cómo se escribe un diagrama de secuencia»)", "memoria/reglas-tfg.md (ejemplo en spec)", "memoria/reglas-tfg.md", "../../memoria/reglas-tfg.md (ejemplo en spec)", "spec del proyecto (ejemplo compilado y probado)", "lección guardada (propuesta, sin confirmar)"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-21"
---

Temas: [[diagramas]] · [[diagramas-secuencia]] · [[latex]] · [[pgf-umlsd]] · [[secuencia]] · [[sequencediagram]] · [[tikz]] · [[uml]]

# Diagramas de secuencia con pgf-umlsd (sequencediagram)

Temas: [[diagramas]] · [[diagramas-secuencia]] · [[latex]] · [[pgf-umlsd]] · [[secuencia]] · [[tikz]]

## Reglas obligatorias para que compile y pase `revisar_umlsd.py`

1. **Entorno**: `sequencediagram` (minúsculas; no existen `sequenceDiagram` ni un entorno `alt`; para alternativas usar `sdblock`).
2. **Participantes**:
   - `\newthread{id}{Nombre}` para hilos/actores.
   - `\newinst[desplazamiento]{id}{Nombre}` para instancias (desplazamiento opcional).
   - El `id` no debe estar vacío, ni contener espacios ni caracteres especiales.
   - **Máximo 6 participantes por diagrama** (si hay más, agrupar o partir en varios).
3. **Llamadas anidadas**:
   ```latex
   \begin{call}{origen}{mensaje}{destino}{respuesta}
     ...
   \end{call}
   ```
4. **Mensajes simples**: `\mess{origen}{mensaje}{destino}`.
5. **Bloques alternativos** (equivalente a `alt`):
   ```latex
   \begin{sdblock}{alt}{condición}
     ...
   \end{sdblock}
   ```
6. **Bucles**:
   ```latex
   \begin{sdblock}{loop}{condición}
     ...
   \end{sdblock}
   ```
7. **Caracteres y comandos prohibidos** en los textos de `\mess`, `call`, `callself` y `\newinst`:
   - Versiones con barra invertida: `\#`, `\_`, `\&`, `\%`, `\$`, `\{`, `\}`
   - Versiones sueltas: `#`, `&`, `_`, `$`, `%`, `{`, `}`
   - Comandos LaTeX (p.ej. `\texttt{...}`)
   - **En `\mess` además**: paréntesis `(` `)`
8. **Declaración de participantes**: todo participante usado debe estar declarado en ese diagrama.
9. **Diagramas anchos**: envolver en `\resizebox{\textwidth}{!}{% ... %}` (el `%` final evita espacios extra).
10. **Diagramas altos**: usar `\begin{adjustbox}{max width=\textwidth,max totalheight=0.6\textheight} ... \end{adjustbox}` si ocupan casi una página.
11. **Códigos de estado HTTP**: usar los exactos de la doc técnica (ej. `400`, no `422`).
12. **Validación previa**: antes de compilar, pasar `scripts/revisar_umlsd.py` que valida sintaxis completa y reporta todos los fallos a la vez.

## Ejemplo completo (compilado y validado en la plantilla)

```latex
\begin{figure}[htbp]
\centering
\resizebox{\textwidth}{!}{%
\begin{sequencediagram}
  \newthread{nav}{Navegador}
  \newinst[2]{api}{API (Express)}
  \newinst[2]{srv}{userService}
  \newinst[2]{bd}{PostgreSQL}
  \begin{call}{nav}{POST /api/auth/login}{api}{200 o 401}
    \begin{call}{api}{authenticate(email, contraseña)}{srv}{usuario}
      \begin{call}{srv}{SELECT por email}{bd}{fila}
      \end{call}
    \end{call}
  \end{call}
  \begin{sdblock}{alt}{cuenta pendiente}
    \mess{api}{403 + enlace de reenvío}{nav}
  \end{sdblock}
\end{sequencediagram}}
\caption{Inicio de sesión local.}
\label{fig:sec-login}
\end{figure}
```

## Ejemplo mínimo correcto

```latex
\begin{sequencediagram}
  \newthread{u}{Usuario}
  \newinst[2]{api}{API}
  \begin{call}{u}{petición}{api}{respuesta}
  \end{call}
  \begin{sdblock}{alt}{caso error}
    \mess{api}{400 error}{u}
  \end{sdblock}
\end{sequencediagram}
```

## Citas de referencia

- **Especificación del proyecto** (bloque «Cómo se escribe un diagrama de secuencia») — cita sin comprobar:
  > El entorno es sequencediagram (en minúsculas; no existen sequenceDiagram ni un entorno alt: para alternativas, sdblock). Participantes con \newthread/\newinst, llamadas anidadas con call (origen, mensaje, destino, respuesta), mensajes sueltos con \mess y bloques alternativos con sdblock.

- **memoria/reglas-tfg.md** — cita sin comprobar:
  > El entorno es `sequencediagram` (en minúsculas; **no** existen `sequenceDiagram` ni un entorno `alt`: para alternativas, `sdblock`): participantes con `\newthread`/`\newinst`, llamadas anidadas con `call` (origen, mensaje, destino, respuesta), mensajes sueltos con `\mess` y bloques alternativos con `sdblock`.

## Historial / Ampliaciones

- **2026-11-16 (memoria-procesos)**: Primera consolidación de reglas: entorno, participantes, call, mess, sdblock, caracteres prohibidos, declaración obligatoria, resizebox/adjustbox.
- **2026-11-19 (memoria-procesos)**: Añadido ejemplo completo con figure, reglas estrictas (incluyendo bucles con `sdblock{loop}`), lista de errores comunes, y recordatorio de `revisar_umlsd.py`.
- **2026-11-21 (memoria-procesos)**: Reglas obligatorias para que `revisar_umlsd.py` pase (versión resumida), límite de 6 participantes, y referencia a ejemplo en `memoria/reglas-tfg.md`.

## Errores comunes que rompen la compilación

- Participante vacío: `\newinst{}{Label}` → «el participante "" no está declarado».
- Mensaje vacío: `\mess{a}{}{b}` → error de sintaxis.
- Paréntesis en `\mess`: `\mess{a}{func(x)}{b}` → usar `func x` o `funcion x`.
- Comando LaTeX en mensaje: `\mess{a}{\texttt{POST}}{b}` → usar `POST`.
- Usar `alt` como entorno: `\begin{alt}...\end{alt}` → usar `sdblock`.
- Participante no declarado en el diagrama.
- Caracteres prohibidos (`#`, `_`, `&`, `%`, `$`, `{`, `}`, `\`, paréntesis en `\mess`).

## Relacionados

[[diagramas-de-secuencia-con-pgf-umlsd]] · [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[numeros-en-diagramas-de-secuencia-deben-coincidir-con-la-esp]] · [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re]]

## Origen

[[proyectos/memoria-procesos/estado|memoria-procesos]]

> \begin{sequencediagram} \newthread{u}{Usuario} \newinst[2]{v}{Vista registro} \begin{call}{u}{escribe email y contraseña}{v}{ok} \end{call} \begin{sdblock}{alt}{ya existe} \mess{s}{409 ConflictError}{a} \end{sdblock} \end{sequencediagram}
> — `chapters/04-descripcion.tex` (cita sin comprobar)
> El entorno es sequencediagram (en minúsculas; no existen sequenceDiagram ni un entorno alt: para alternativas, sdblock). Participantes con \newthread/\newinst, llamadas anidadas con call (origen, mensaje, destino, respuesta), mensajes sueltos con \mess y bloques alternativos con sdblock.
> — `spec del proyecto (bloque «Cómo se escribe un diagrama de secuencia»)` (cita sin comprobar)
> El entorno es `sequencediagram` (en minúsculas; **no** existen `sequenceDiagram` ni un entorno `alt`: para alternativas, `sdblock`): participantes con `\newthread`/`\newinst`, llamadas anidadas con `call` (origen, mensaje, destino, respuesta), mensajes sueltos con `\mess` y bloques alternativos con `sdblock`.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Fusionada con: Diagramas de secuencia pgf-umlsd sintaxis correcta

Relacionado: [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-que-no-c]] · [[diagramas-de-secuencia-con-pgf-umlsd-reglas-de-sintaxis]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
