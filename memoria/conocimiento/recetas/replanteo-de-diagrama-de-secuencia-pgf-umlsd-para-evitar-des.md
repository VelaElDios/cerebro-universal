---
tipo: "receta"
titulo: "Replanteo de diagrama de secuencia pgf-umlsd para evitar desbordamiento y cruces"
temas: ["diagramas", "latex", "pgf-umlsd"]
claves: ["sequencediagram", "newinst", "call", "mess", "sdblock", "adjustbox", "textwidth"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[diagramas]] · [[latex]] · [[pgf-umlsd]]

|
  Pasos para replantear un diagrama de secuencia que desborda o tiene cruces:
  1. **Reducir participantes a 4 máximo**: agrupar llamadas internas (TokenSigner, Mailer, BD) dentro del participante "Servicio" o "API" usando `call` anidados, no participantes separados.
  2. **Separación horizontal mínima**: `\newinst[2]` o `[3]` como mucho. Si hace falta más, el diagrama está mal planteado.
  3. **Etiquetas ultra-cortas**: solo ASCII, sin acentos, sin paréntesis en `\mess`, sin comandos LaTeX. Usar `\n` para saltos de línea dentro de `\mess`/`call`.
  4. **Llamadas anidadas para lógica interna**: en lugar de `\newinst` para cada módulo, usar `\begin{call}{srv}{accion interna}{srv}{resultado} \end{call}` dentro del participante Servicio.
  5. **Bloques alt/sdblock separados verticalmente**: `below=1.2cm` mínimo entre participantes; si una flecha de redirección cruza una caja, separar más o usar codos TikZ (requiere salir de sequencediagram a TikZ puro).
  6. **Envolver en adjustbox**: `\begin{adjustbox}{max width=\textwidth, max totalheight=0.6\textheight} ... \end{adjustbox}` para diagramas grandes. Nunca `resizebox` para encoger.
  7. **Ejecutar revisar_umlsd.py** antes de compilar: detecta participantes no declarados, etiquetas con caracteres prohibidos, flechas mal formadas.
  8. **Verificar en PDF**: letras ≥ 7.5 pt, sin cruces, sin palabras partidas, flechas de caja en caja.

> \begin{sequencediagram} ... \newinst[2]{fe}{Frontend} \newinst[2]{api}{API} \newinst[2]{srv}{Servicio} ... \end{sequencediagram}
> — `chapters/04-descripcion.tex` (cita sin comprobar)

Relacionado: [[diagramas-de-secuencia-pgf-umlsd-sintaxis-valida-y-errores-c]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
