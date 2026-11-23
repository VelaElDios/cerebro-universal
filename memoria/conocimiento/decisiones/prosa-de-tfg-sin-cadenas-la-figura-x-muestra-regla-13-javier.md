---
tipo: "decision"
titulo: "Prosa de TFG: nada de «La figura X muestra…» suelto; agrupar capturas con subfigure (regla 13 Javier)"
temas: ["figuras", "latex", "maquetacion", "memoria", "redaccion", "reglas-javier", "subcaption", "subfigure", "tfg"]
claves: ["subfigure", "subcaption", "prosa", "capturas", "figura", "La figura X muestra", "caption general"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "../../memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 13)"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-23"
---

Temas: [[figuras]] · [[latex]] · [[maquetacion]] · [[memoria]] · [[redaccion]] · [[reglas-javier]] · [[subcaption]] · [[subfigure]] · [[tfg]]

Temas: [[latex]] · [[memoria]] · [[redaccion]] · [[figuras]] · [[reglas-javier]] · [[subfigure]] · [[tfg]]

**Regla central**  
> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.  
> — `memoria/reglas-tfg.md` (cita sin comprobar)

**Instrucción general**  
Reescribir las secciones de manual de usuario (cap. 4 y 4b) como prosa continua: explicar qué hace el usuario y por qué la app responde, citando las figuras con `\ref` dentro del texto. Agrupar capturas relacionadas en una sola `figure` con `subfigure` (dos por fila, `\begin{subfigure}{0.48\textwidth}`), un `\caption` general y `\subcaption` por subfigura. Eliminar cualquier frase que empiece por «La figura», «La captura», «En la imagen» seguida solo de descripción visual sin contexto de uso.

**Ejemplo correcto (capítulo 04-descripcion.tex, sección «Inicio y registro»)**  
- Párrafo explica qué ve el usuario al llegar sin sesión.  
- `Figura~\ref{fig:app-inicio-registro}` agrupa 2 subfiguras: inicio y registro con validación.  
- Párrafo siguiente explica el comportamiento al entrar (mismo mensaje error, cuenta pendiente).  
- `Figura~\ref{fig:app-errores-acceso}` agrupa 2 subfiguras: error credenciales y sin permiso admin.  
- Cada subfigura tiene su `\subcaption` descriptivo.  
- En el texto: «la subfigura~\ref{fig:app-registro} muestra…» / «el aviso de la subfigura~\ref{fig:hito4-pendiente}…».  
Esto elimina las frases sueltas y hace que las capturas sirvan a la explicación.

**Problema**  
El borrador tenía ~45 frases sueltas tipo «La figura X muestra…», una por captura, lo que delata un trabajo poco profesional.

**Solución**  
Reescribir cada sección como prosa continua que explica el flujo de uso. Agrupar capturas relacionadas en una figura con `subfigure` (dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura. Citar las figuras dentro de la explicación con `\ref`.

## Ampliación (2026-11-20, memoria-procesos)
Aplicado en capítulos **04-descripcion** (manual SaaS) y **04b-juego** (manual juego).

**Cap. 04-descripcion (manual SaaS)**  
- `Figura~\ref{fig:app-inicio-registro}` agrupa inicio y registro.  
- `Figura~\ref{fig:app-errores-acceso}` agrupa error credenciales y sin permiso admin.  
- `Figura~\ref{fig:app-perfil-baja}`, `fig:app-admin-full`, `fig:app-responsive`, `fig:app-estados-especiales`, `fig:hito4-flujo`, `fig:hito4-admin-estados-privacidad` — cada una agrupa 2–4 capturas relacionadas con prosa que las integra.

**Cap. 04b-juego (manual juego)**  
- `Figura~\ref{fig:juego-menu-vestuario}` agrupa menú y vestuario.  
- `Figura~\ref{fig:juego-partida-mejora}` agrupa partida y mejora.  
- `Figura~\ref{fig:juego-fin-pausa}` agrupa fin y pausa.  
- `Figura~\ref{fig:juego-club-pantallas-a/b}` agrupan 8 pantallas del club en 2 figuras de 4 subfiguras cada una.

Relacionado: [[como-se-agrupan-capturas-con-subfigure]] · [[prosa-de-tfg-sin-cadenas-la-figura-x-muestra-regla-13-javier]] · [[prosa-de-tfg-sin-cadenas-la-figura-x-muestra-regla-13-javier]] · [[prosa-de-tfg-sin-listas-de-capturas-agrupar-con-subfigure]] · [[prosa-de-tfg-sin-listas-de-capturas-regla-13-javier]] · [[prosa-de-tfg-vs-lista-de-capturas]] · [[reescribir-frases-la-figura-x-muestra-como-prosa-integrada]] · [[cadenas-la-figura-x-muestra-prohibidas-prosa-integrada-con-s]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con subfigure.
> — `memoria/reglas-tfg.md`

Fusionada con: Prosa de TFG: nada de «La figura X muestra…» suelto; agrupar capturas en subfigure

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
