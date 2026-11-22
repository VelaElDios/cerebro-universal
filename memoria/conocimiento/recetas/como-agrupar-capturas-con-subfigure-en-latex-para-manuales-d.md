---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure en LaTeX para manuales de usuario"
temas: ["capturas", "figuras", "latex", "maquetacion", "subcaption", "subfigure"]
claves: ["subfigure", "height=0.42\\textheight", "caption general", "subcaption", "agrupación capturas", "agrupación", "capturas"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex (cambios aplicados en este paso)", "chapters/04-descripcion.tex", "memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 13) y chapters/04-descripcion.tex (ejemplos actuales)"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-20"
---

Temas: [[capturas]] · [[figuras]] · [[latex]] · [[maquetacion]] · [[subcaption]] · [[subfigure]]

Temas: [[figuras]] · [[latex]] · [[maquetacion]] · [[subcaption]] · [[subfigure]]

**Propósito**  
Evitar páginas con una sola imagen (Regla 8) y cadenas de «La figura X muestra…» (Regla 12), agrupando capturas relacionadas en una figura flotante con subfiguras (paquete `subcaption`, ya cargado en `include/extra.tex` según Nota A / `include/configuracion.tex` según Nota B).

**Procedimiento**  
1. Usar el entorno `figure` con especificador de posición `[htbp]`.  
2. Dentro, crear cada subfigura con `\begin{subfigure}{0.48\textwidth}` (dos por fila).  
3. Separar las subfiguras horizontalmente con `\hfill`.  
4. En cada subfigura:  
   - `\centering`  
   - `\includegraphics[width=\linewidth,height=ALTURA,keepaspectratio]{ruta/archivo.png}`  
     - Capturas móviles (verticales): `height=0.35\textheight` en subfigure, `0.42\textheight` en figure simple.  
     - Capturas desktop (horizontales): `height=0.35\textheight` en subfigure, `0.42\textheight` en figure simple.  
     - Si el grupo subfigure queda muy alto: envolver toda la `figure` en `\adjustbox{max totalheight=0.42\textheight,width=\textwidth}{...}`.  
   - **Leyenda individual**: `\subcaption{Texto...}` (orden canónica con `subcaption`; `\caption{...}` también funciona dentro de `subfigure` pero no es la orden estándar).  
   - `\label{fig:subfigura-propria}` propio.  
5. En la figura contenedora:  
   - `\caption{Texto general descriptivo.}`  
   - `\label{fig:contenedora}` distinto al de las subfiguras.  
6. En el texto: redactar prosa explicativa que integre las referencias.  
   - Opción A (Nota A): referenciar la figura general y usar sufijo de letra (`Figura~\ref{fig:contenedora}a`).  
   - Opción B (Nota A): referenciar subfiguras individuales con `\ref{fig:subfigura}` o `\subref{fig:subfigura}` (requiere opción `subrefformat=parens` al cargar `subcaption`).  
   - Estilo Nota B: referencia al conjunto `Figura~\ref{fig:etiqueta-general}` y a subfigura concreta `subfigura~\subref{fig:etiqueta1} de la Figura~\ref{fig:etiqueta-general}`.  
7. Eliminar todas las figuras sueltas y sus frases introductorias («La figura X muestra…»); integrar la explicación en la prosa.

**Ejemplo completo (dos subfiguras, verticales/móvil)**
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
  \subcaption{Registro con validación de campos.}
  \label{fig:app-registro}
\end{subfigure}
\caption{Pantallas de acceso: inicio y registro.}
\label{fig:app-acceso}
\end{figure}
```

**Ejemplo de integración en prosa**  
> Al acceder a la aplicación sin sesión, el usuario encuentra la página de inicio (Figura~\ref{fig:app-acceso}a) y, tras pulsar «Registrarse», el formulario con validación (Figura~\ref{fig:app-acceso}b).  
> —o bien—  
> La figura~\ref{fig:app-acceso} muestra el flujo de registro (subfigura~\subref{fig:app-inicio}) y el error de validación (subfigura~\subref{fig:app-registro}).

**Ejemplos ya correctos en el borrador (Nota B)**  
- Figura~\ref{fig:app-inicio-registro} (Cap 4, inicio+registro)  
- Figura~\ref{fig:app-errores-acceso} (Cap 4, error entrar + sin permiso)  
- Figura~\ref{fig:app-perfil-baja} (Cap 4, perfil + baja)  
- Figura~\ref{fig:app-admin-full} (Cap 4, admin tabla + búsqueda)  
- Figura~\ref{fig:app-responsive} (Cap 4, admin móvil + perfil móvil)  
- Figura~\ref{fig:app-estados-especiales} (Cap 4, búsqueda vacía + 404)  
- Figura~\ref{fig:hito4-flujo} (Cap 4, 6 subfiguras en 3 filas)  
- Figura~\ref{fig:hito4-admin-estados-privacidad} (Cap 4, admin estados + privacidad)  
- Figura~\ref{fig:juego-menu-vestuario} (Cap 4b, menú + vestuario)  
- Figura~\ref{fig:juego-partida-mejora} (Cap 4b, partida + mejora)  
- Figura~\ref{fig:juego-jefe-ambiente} (Cap 4b, jefe + ambiente)  
- Figura~\ref{fig:juego-fin-pausa} (Cap 4b, fin + pausa)  
- Figura~\ref{fig:juego-club-pantallas-a} (Cap 4b, 4 pantallas club)  
- Figura~\ref{fig:juego-club-pantallas-b} (Cap 4b, 4 pantallas club)  
- Figura~\ref{fig:prueba-tecnica} (Cap 5, permitido + rechazado)  
- Figura~\ref{fig:produccion-verificacion} (Cap 5, correo + Google)  
- Figura~\ref{fig:donetonic-s2-capturas} (Anexo A1, gráficas + tablero S2)  
- Figura~\ref{fig:donetonic-s2-detalle} (Anexo A1, PBI detalle + tareas)

**Pendientes de agrupar/reescribir (Nota B)**  
- Cap 4 §6: varias figuras sueltas que deberían ir en subfigure (ya hecho en gran parte, revisar).  
- Cap 4b §2: ya agrupado en subfigures pero la prosa sigue siendo «La figura X muestra…».

**Fuentes y trazabilidad**  
- Aplicado en `chapters/04-descripcion.tex` (verificado).  
- Citado en `memoria/reglas-tfg.md` (propuesto, sin comprobar).  
- Ampliaciones 2026-11-16 y 2026-11-19 desde [[proyectos/memoria-procesos/estado|memoria-procesos]].

**Relacionado**  
[[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[limitar-altura-de-capturas-para-evitar-paginas-con-una-sola]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[agrupar-capturas-con-subfigure]] · [[como-se-agrupan-capturas-con-subfigure]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[arreglar-pagina-con-una-sola-imagen-regla-8-agrupando-en-sub]]

**Fragmentos de código referenciados**  
> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png} \subcaption{Página de inicio sin sesión.}  
> — `chapters/04-descripcion.tex (cambios aplicados en este paso)`  
> Las capturas relacionadas van juntas en una figura con `subfigure` (de `subcaption`, ya cargado; dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura.  
> — `memoria/reglas-tfg.md`
<<<CONTRADICCION>>
1. Ubicación de carga del paquete `subcaption`: Nota A dice `include/extra.tex`, Nota B dice `include/configuracion.tex`. 2. Altura por defecto en subfiguras: Nota A usa `0.42\textheight` en su ejemplo; Nota B recomienda `0.35\textheight` para subfiguras (móvil/desktop) y `0.42\textheight` solo para figure simple. 3. Leyenda de subfigura: Nota A menciona `\subcaption{...}` *o* `\caption{...}` (marcando contradicción); Nota B usa siempre `\subcaption{...}`. 4. Estilo de referencia: Nota A ofrece dos opciones (sufijo de letra sobre label contenedor, o `\ref`/`\subref` a labels propias con `subrefformat=parens`); Nota B usa `Figura~\ref{general}` para el conjunto y `subfigura~\subref{sub} de la Figura~\ref{general}` para individuales. 5. Estado de verificación: Nota A = «verificado»; Nota B = «verificado» pero sus ampliaciones vienen de «memoria-procesos» sin distinguir verificación propia.

> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png} \subcaption{Página de inicio sin sesión.}
> — `chapters/04-descripcion.tex (cambios aplicados en este paso)`
> Las capturas relacionadas van juntas en una figura con `subfigure` (de `subcaption`, ya cargado; dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura.
> — `memoria/reglas-tfg.md`
> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png} \subcaption{Página de inicio sin sesión.}
> — `chapters/04-descripcion.tex`

Fusionada con: Cómo agrupar capturas relacionadas con subfigure en LaTeX

Relacionado: [[agrupar-capturas-relacionadas-en-subfiguras-con-prosa-integr]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
