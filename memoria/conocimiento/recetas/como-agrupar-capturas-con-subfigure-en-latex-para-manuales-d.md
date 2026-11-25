---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure en LaTeX para manuales de usuario"
temas: ["capturas", "figuras", "latex", "manual-usuario", "maquetacion", "memoria", "subcaption", "subfigure"]
claves: ["subfigure", "height=0.42\\textheight", "caption general", "subcaption", "agrupación capturas", "agrupación", "capturas", "0.48\\textwidth", "\\subcaption", "\\caption", "\\label", "fig:app-inicio-registro", "fig:juego-menu-vestuario"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex (cambios aplicados en este paso)", "chapters/04-descripcion.tex", "memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 13) y chapters/04-descripcion.tex (ejemplos actuales)", "chapters/04-descripcion.tex, chapters/04b-juego.tex", "chapters/04-descripcion.tex (sección 6) y chapters/04b-juego.tex (sección 2)", "memoria/proyectos/memoria-procesos/chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-25"
---

Temas: [[capturas]] · [[figuras]] · [[latex]] · [[manual-usuario]] · [[maquetacion]] · [[memoria]] · [[subcaption]] · [[subfigure]]

Temas: [[capturas]] · [[figuras]] · [[latex]] · [[maquetacion]] · [[manual-usuario]] · [[subcaption]] · [[subfigure]]

**Propósito**  
Evitar páginas con una sola imagen (Regla 8) y cadenas de «La figura X muestra…» (Regla 12/13), agrupando capturas relacionadas en una figura flotante con subfiguras mediante el paquete `subcaption`.

**Procedimiento unificado**  
1. **Entorno contenedor**: `\begin{figure}[htbp]` (añadir `\centering` opcional tras `\begin{figure}`).  
2. **Subfiguras** (dos por fila):  
   ```latex
   \begin{subfigure}{0.48\textwidth}
     \centering
     \includegraphics[width=\linewidth,height=ALTURA,keepaspectratio]{ruta/archivo.png}
     \subcaption{Texto descriptivo individual.}
     \label{fig:subfigura-propria}
   \end{subfigure}
   \hfill
   ```  
   Repetir para la segunda subfigura.  
3. **Separación horizontal**: `\hfill` entre subfiguras.  
4. **Figura contenedora**:  
   ```latex
   \caption{Texto general que explica el conjunto.}
   \label{fig:contenedora}
   \end{figure}
   ```  
5. **Prosa integrada**: Redactar texto explicativo que cite la figura general y/o las subfiguras (ver *Estilos de referencia*). Eliminar frases sueltas tipo «La figura X muestra…».

**Especificación de alturas (ver CONTRADICCION)**  
- **Capturas móviles / verticales** (en subfigure): `height=0.35\textheight` (Nota B) o `0.42\textheight` (ejemplo Nota A).  
- **Capturas desktop / horizontales** (en subfigure): `height=0.35\textheight` (Nota B) o `0.42\textheight` (ejemplo Nota A).  
- **Figura simple (sin subfiguras)**: `height=0.42\textheight`.  
- **Si el grupo subfigure queda muy alto**: envolver toda la `figure` en  
  `\adjustbox{max totalheight=0.42\textheight,width=\textwidth}{...}`.

**Leyenda de subfigura**  
- Orden canónica: `\subcaption{Texto...}` (usada en Nota B y en el ejemplo de Nota A).  
- Nota A menciona que `\caption{...}` *también funciona* dentro de `subfigure` pero no es la orden estándar.

**Estilos de referencia**  
- **Opción A (Nota A)**: referenciar la figura general con sufijo de letra → `Figura~\ref{fig:contenedora}a`.  
- **Opción B (Nota A)**: referenciar subfiguras individuales con `\ref{fig:subfigura}` o `\subref{fig:subfigura}` (requiere cargar `subcaption` con opción `subrefformat=parens`).  
- **Estilo Nota B**: referencia al conjunto `Figura~\ref{fig:etiqueta-general}` y a subfigura concreta `subfigura~\subref{fig:etiqueta1} de la Figura~\ref{fig:etiqueta-general}`.

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

**Ejemplos de integración en prosa**  
> Al acceder a la aplicación sin sesión, el usuario encuentra la página de inicio (Figura~\ref{fig:app-acceso}a) y, tras pulsar «Registrarse», el formulario con validación (Figura~\ref{fig:app-acceso}b).  
> —o bien—  
> La figura~\ref{fig:app-acceso} muestra el flujo de registro (subfigura~\subref{fig:app-inicio}) y el error de validación (subfigura~\subref{fig:app-registro}).  
> —estilo Nota B—  
> La figura~\ref{fig:app-inicio-registro} presenta el inicio y el registro; la subfigura~\subref{fig:app-inicio} de la figura~\ref{fig:app-inicio-registro} muestra la página pública.

**Ejemplos ya correctos en el borrador**  
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

**Pendientes de agrupar/reescribir**  
- Cap 4 §6: varias figuras sueltas que deberían ir en subfigure (ya hecho en gran parte, revisar).  
- Cap 4b §2: ya agrupado en subfigures pero la prosa sigue siendo «La figura X muestra…».

**Fuentes y trazabilidad**  
- Aplicado en `chapters/04-descripcion.tex` (verificado).  
- Citado en `memoria/reglas-tfg.md` (propuesto, sin comprobar).  
- Ampliaciones 2026-11-16, 2026-11-19 y 2026-11-25 desde [[proyectos/memoria-procesos/estado|memoria-procesos]].

**Relacionado**  
[[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[limitar-altura-de-capturas-para-evitar-paginas-con-una-sola]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[agrupar-capturas-con-subfigure]] · [[como-agrupar-capturas-con-subfigure-dos-por-fila]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[arreglar-pagina-con-una-sola-imagen-regla-8-agrupando-en-sub]] · [[prosa-de-tfg-sin-cadenas-la-figura-x-muestra-regla-13-javier]] · [[prosa-de-tfg-obligatoria-nada-de-listas-de-capturas-agrupar]]

**Fragmentos de código referenciados**  
> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png} \subcaption{Página de inicio sin sesión.}  
> — `chapters/04-descripcion.tex (cambios aplicados en este paso)`  
> Las capturas relacionadas van juntas en una figura con `subfigure` (de `subcaption`, ya cargado; dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura.  
> — `memoria/reglas-tfg.md`
<<<CONTRADICCION>>
1. Ubicación de carga del paquete `subcaption`: Nota A dice `include/extra.tex`, Nota B dice `include/configuracion.tex`. 2. Altura por defecto en subfiguras: Nota A usa `0.42\textheight` en su ejemplo; Nota B recomienda `0.35\textheight` para subfiguras (móvil/desktop) y `0.42\textheight` solo para figure simple. 3. Leyenda de subfigura: Nota A menciona `\subcaption{...}` *o* `\caption{...}` (marcando contradicción); Nota B usa siempre `\subcaption{...}`. 4. Estilo de referencia: Nota A ofrece dos opciones (sufijo de letra sobre label contenedor, o `\ref`/`\subref` a labels propias con `subrefformat=parens`); Nota B usa `Figura~\ref{general}` para el conjunto y `subfigura~\subref{sub} de la Figura~\ref{general}` para individuales. 5. Estado de verificación: Nota A = «verificado»; Nota B = «propuesto» pero sus ampliaciones vienen de «memoria-procesos» sin distinguir verificación propia.

> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png} \subcaption{Página de inicio sin sesión.}  
> — `chapters/04-descripcion.tex (cambios aplicados en este paso)`  
> Las capturas relacionadas van juntas en una figura con `subfigure` (de `subcaption`, ya cargado; dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura.  
> — `memoria/reglas-tfg.md`
> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png} \subcaption{Página de inicio sin sesión.}
> — `chapters/04-descripcion.tex (cambios aplicados en este paso)`
> Las capturas relacionadas van juntas en una figura con `subfigure` (de `subcaption`, ya cargado; dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura.
> — `memoria/reglas-tfg.md`
> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png} \subcaption{Página de inicio sin sesión.}
> — `chapters/04-descripcion.tex`
> \begin{figure}[htbp]\centering\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}\subcaption{Página de inicio sin sesión.}\label{fig:app-inicio}\end{subfigure}\hfill\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}\subcaption{Validación en cliente: email y contraseña con errores.}\label{fig:app-registro}\end{subfigure}\caption{Inicio y registro: página pública y validación del formulario.}\label{fig:app-inicio-registro}\end{figure}
> — `chapters/04-descripcion.tex, chapters/04b-juego.tex` (cita sin comprobar)

Fusionada con: Cómo agrupar capturas relacionadas con subfigure en LaTeX

Relacionado: [[como-escribir-prosa-de-tfg-integrando-capturas-sin-la-figura]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
