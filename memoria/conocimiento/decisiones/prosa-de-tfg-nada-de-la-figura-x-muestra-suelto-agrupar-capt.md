---
tipo: "decision"
titulo: "Prosa de TFG: nada de «La figura X muestra…» suelto; agrupar capturas en subfigure"
temas: ["latex", "memoria", "redaccion", "subcaption", "subfigure"]
claves: ["subfigure", "subcaption", "prosa", "capturas", "figura"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "../../memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[memoria]] · [[redaccion]]

|
  Ejemplo correcto (capítulo 04-descripcion.tex, sección «Inicio y registro»):
  - Párrafo explica qué ve el usuario al llegar sin sesión.
  - Figura~\ref{fig:app-inicio-registro} agrupa 2 subfiguras: inicio y registro con validación.
  - Párrafo siguiente explica el comportamiento al entrar (mismo mensaje error, cuenta pendiente).
  - Figura~\ref{fig:app-errores-acceso} agrupa 2 subfiguras: error credenciales y sin permiso admin.
  - Cada subfigura tiene su `\subcaption` descriptivo.
  - En el texto: «la subfigura~\ref{fig:app-registro} muestra...» / «el aviso de la subfigura~\ref{fig:hito4-pendiente}...».
  Esto elimina las frases sueltas y hace que las capturas sirvan a la explicación.

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con subfigure.
problema: El borrador tenía ~45 frases sueltas tipo «La figura X muestra…», una por captura, lo que delata un trabajo poco profesional.
solucion: Reescribir cada sección como prosa continua que explica el flujo de uso. Agrupar capturas relacionadas en una figura con `subfigure` (dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura. Citar las figuras dentro de la explicación con `\ref`.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

## Ampliación (2026-11-20, memoria-procesos)
Aplicado en capítulos 04-descripcion (manual SaaS) y 04b-juego (manual juego). Ejemplo: Figura~\ref{fig:app-inicio-registro} agrupa inicio y registro; Figura~\ref{fig:juego-menu-vestuario} agrupa menú y vestuario; Figura~\ref{fig:juego-partida-mejora} agrupa partida y mejora; Figura~\ref{fig:juego-fin-pausa} agrupa fin y pausa; Figura~\ref{fig:juego-club-pantallas-a/b} agrupan 8 pantallas del club en 2 figuras de 4 subfiguras cada una.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
