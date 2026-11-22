---
tipo: "receta"
titulo: "Prosa de TFG sin listas de capturas: agrupar capturas relacionadas con `subfigure` en LaTeX"
temas: ["capturas", "figuras", "latex", "memoria", "redaccion", "subfigure", "tfg"]
claves: ["subfigure", "subcaption", "La figura X muestra", "prosa", "adjustbox", "prosa continua"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-21"
actualizado: "2026-11-22"
---

Temas: [[capturas]] · [[figuras]] · [[latex]] · [[memoria]] · [[redaccion]] · [[subfigure]] · [[tfg]]

Temas: [[latex]] · [[redaccion]] · [[tfg]] · [[capturas]] · [[subfigure]]

**Regla central**  
Escribir párrafos narrativos que expliquen la interacción del usuario con la aplicación, citando las figuras dentro del texto con `\ref` / `\subref`. **Nada de frases sueltas** tipo «La figura X muestra…» por cada imagen. Las capturas que ilustran un mismo flujo o pantalla en distintos estados se agrupan en una sola `figure` con entorno `subfigure` (dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un `\caption` general y un `\subcaption` por subfigura.

---

### Ejemplo comparativo

**Mal (lista de capturas):**
> La figura 1 muestra la página de inicio. La figura 2 muestra el formulario de registro. La figura 3 muestra el error de contraseña.

**Bien (prosa integrada con subfigure):**
> Al acceder a la aplicación sin sesión, el usuario encuentra la página de inicio (Figura~\ref{fig:app-inicio-registro}), que presenta dos accesos directos: «Crear cuenta para jugar» y «Ya tengo cuenta». Si elige registrarse, el formulario valida el email y la contraseña en cliente (mínimo 8 caracteres) y muestra los errores en línea asociados a cada campo mediante \texttt{aria-describedby} (subfigura~\ref{fig:app-registro}). Al enviar, el servidor comprueba unicidad del email; si ya existe, devuelve 409 y la interfaz muestra el error sin recargar. Si es correcto, la cuenta queda \texttt{pending} y se envía el correo de confirmación; la interfaz avisa y lleva a la pantalla de entrar.

---

### Reglas para agrupar capturas

1. **Capturas relacionadas** (mismo flujo, misma pantalla en distintos estados) → una sola `figure` con `subfigure` (dos por fila: `0.48\textwidth`).
2. **Caption general** en la `figure` + **caption específico** en cada `subfigure`.
3. **Referenciar en el texto** con `\ref{fig:general}` o `\subref{fig:sub}`.
4. **Tamaños de imagen**:
   - Verticales (móvil): `width=\linewidth,height=0.35\textheight,keepaspectratio`
   - Horizontales: `width=\linewidth,height=0.42\textheight,keepaspectratio`
5. Si la figura resultante queda muy alta, envolver en `adjustbox{max totalheight=0.42\textheight,width=\linewidth}`.

---

### Plantilla `subfigure`

```latex
\begin{figure}[htbp]
\centering
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}
\subcaption{Página de inicio sin sesión.}
\label{fig:app-inicio}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}
\subcaption{Validación en cliente: email y contraseña con errores.}
\label{fig:app-registro}
\end{subfigure}
\caption{Inicio y registro: página pública y validación del formulario.}
\label{fig:app-inicio-registro}
\end{figure}
```

---

### Patrón de redacción para «La aplicación» (Cap 4) y «Cómo se juega» (Cap 4b)

1. Escribir un párrafo que explique la acción del usuario y la respuesta del sistema.
2. Insertar una figura con `subfigure` (dos por fila, `\begin{subfigure}{0.48\textwidth}`) que agrupe capturas relacionadas.
3. Cada subfigura tiene su `\subcaption` descriptivo; la figura general tiene `\caption` y `\label`.
4. Citar la figura general en el texto con `\ref{fig:...}` y, si hace falta, referenciar subfiguras con `\subref{...}`.
5. No dejar ninguna frase que empiece por «La figura X muestra…».

---

### Ejemplos en el repositorio

- `04-descripcion.tex`: figuras `fig:app-inicio-registro`, `fig:app-errores-acceso`, `fig:app-perfil-baja`, `fig:app-admin-full`, `fig:app-responsive`, `fig:app-estados-especiales`, `fig:hito4-flujo`, `fig:hito4-estados-privacidad`.
- `04b-juego.tex`: figuras `fig:juego-menu-vestuario`, `fig:juego-partida-mejora`, `fig:juego-jefe-ambiente`, `fig:juego-fin-pausa`, `fig:juego-club-pantallas-a`, `fig:juego-club-pantallas-b`.

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
> — `memoria/reglas-tfg.md`

---

## Ampliación (2026-11-21, memoria-procesos)
En la memoria final, las capturas de la aplicación (`app/`, `hito4/`, `juego/`) y de DoneTonic se agrupan en figuras con `subfigure` (dos por fila, `\begin{subfigure}{0.48\textwidth}`) con caption general y subcaptions. El texto explica el flujo de uso citando las figuras dentro de la prosa, no como frases sueltas. **Cada imagen aparece una sola vez en el sitio donde más sentido tiene; en el resto se cita con `\ref`**.  
Relacionado: [[cada-entrega-solo-lleva-lo-de-su-sprint-alcance-coherente]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

---

## Ampliación (2026-11-19, memoria-procesos)
Patrón correcto para la sección «La aplicación» (Cap 4) y «Cómo se juega» (Cap 4b) — ver reglas 1-5 arriba.

**Incorrecto (lista de capturas):**
> La figura~\ref{fig:app-inicio} muestra la página de inicio. La figura~\ref{fig:app-registro} muestra la validación del formulario. La figura~\ref{fig:app-entrar} muestra el error de contraseña.

**Correcto (prosa integrada con subfigure):**
> Al acceder a la aplicación sin sesión, el usuario encuentra la página de inicio (Figura~\ref{fig:app-inicio-registro}), que presenta dos accesos directos: «Crear cuenta para jugar» y «Ya tengo cuenta». Si elige registrarse, el formulario valida el email y la contraseña en cliente (mínimo 8 caracteres) y muestra los errores en línea asociados a cada campo mediante \texttt{aria-describedby} (subfigura~\ref{fig:app-registro}). Al enviar, el servidor comprueba unicidad del email; si ya existe, devuelve 409 y la interfaz muestra el error sin recargar. Si es correcto, la cuenta queda \texttt{pending} y se envía el correo de confirmación; la interfaz avisa y lleva a la pantalla de entrar.

Las capturas relacionadas (inicio + registro, entrar + error, perfil + baja) van en **una sola figura** con `subfigure` (dos por fila, `0.48\textwidth`), caption general y subcaptions. En el texto se cita la figura general (`\ref{fig:app-inicio-registro}`) y, si hace falta, la subfigura (`\subref{fig:app-registro}`).

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

---

Relacionado:  
[[cada-entrega-solo-lleva-lo-de-su-sprint-alcance-coherente]] · [[prosa-de-tfg-nada-de-la-figura-x-muestra-suelto-agrupar-capt]] · [[prosa-de-tfg-sin-listas-de-capturas-agrupar-con-subfigure]] · [[prosa-de-tfg-sin-cadenas-la-figura-x-muestra-regla-13-javier]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[agrupar-capturas-relacionadas-en-subfiguras-con-prosa-integr]] · [[agrupar-capturas-con-subfigure]]

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
> — `memoria/reglas-tfg.md`
> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con subfigure.
> — `memoria/reglas-tfg.md`

Fusionada con: Prosa de TFG vs lista de capturas (regla 13 Javier)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
