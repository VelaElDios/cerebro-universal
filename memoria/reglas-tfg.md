# Reglas para la memoria (TFG con la plantilla ESIIAB-UCLM)

Reglas fijas de Javier para cualquier memoria con formato de TFG (Sprint 3 en adelante). Las IAs las reciben en cada paso, tanto el constructor como el revisor. `scripts/revisar_maquetacion.py` comprueba automáticamente las que se pueden medir. **Una memoria no está terminada si incumple alguna.**

## Portada y plantilla

1. **Una sola portada: la oficial del TFG**, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de `elements/preambulo.tex`.
2. **No se quita nada de la plantilla:** portada, declaración de autoría, Resumen, Abstract, índices (general, de figuras y de tablas), capítulos, anexos y bibliografía. Solo se cambia lo que Javier pida expresamente.
3. **Títulos en negro y en negrita, sin azul:** `\definecolor{tema}{RGB}{0,0,0}`, con `\bfseries` en section y subsection. Los enlaces van sin recuadros de color (`\hypersetup{hidelinks}`).
4. **Sin páginas en blanco** entre capítulos: la memoria se entrega en PDF.

## Tablas

5. **Ninguna fila se pisa con otra:** columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01).
6. Texto de las tablas en `\small`. El código y las rutas van con `\path{}` o con `\texttt{}` más `\allowbreak`, para que no se salgan del margen.
7. Las tablas largas van en `longtable` y su última fila (por ejemplo, el Total) no se queda sola en otra página: usa `\\*` en las últimas filas.

## Figuras y páginas

8. **Ninguna página con una sola imagen:**
   - capturas como mucho a `height=0.42\textheight`;
   - diagramas grandes con `max totalheight`;
   - figuras `[htbp]` con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
9. **Ninguna página casi vacía** ni con una sección o una línea suelta: una sección de una o dos líneas se funde con otra o se convierte en un punto de una lista.
10. **Sin figuras repetidas:** cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone `\ref` a la figura que ya existe.
11. Las flechas de los captions y del texto son flechas de verdad (`$\rightarrow$`), nunca `->`.

## Diagramas

16. **Todo diagrama se lee bien a su tamaño en el PDF:** las letras del dibujo, una vez escalado, nunca son más pequeñas que las del pie de figura (unos 8-9 pt). Si para que quepa hay que encogerlo tanto que las letras quedan diminutas, el diagrama está mal planteado:
   - Diagramas de secuencia: **como mucho 6 participantes**. Si hay más, se agrupan (por ejemplo, «Vista + api.js» → «Frontend») o se parte en dos diagramas (lo que pasa en el navegador / lo que pasa en el servidor). `\resizebox` solo para encoger un poco, no para meter 9 columnas en el ancho de la página.
   - Si hace falta mucho ancho, la página puede ir en horizontal (`pdflscape`) como último recurso.
17. **Ninguna línea ni flecha atraviesa una caja o un texto, y ninguna caja pisa a otra.** Las flechas van de una caja a la siguiente (A → B, B → C), nunca de A a C pasando por encima de B; si hay que rodear, con codos (`|-`, `-|`) y separando bien las cajas (`node distance` suficiente). Las etiquetas de las flechas no se montan sobre las cajas.
18. **Dentro de las cajas no se parten palabras ni rutas** («sr-c/services»): o la caja es más ancha (`text width`), o el texto se pone en dos líneas a mano (`\\`), o se acorta.

## Contenido

12. **Cada entrega lleva solo lo de su sprint.** Por ejemplo, la del Sprint 1 va sin el juego. El título, el Resumen, el Abstract, la Introducción, las Conclusiones y los anexos tienen que coincidir con ese alcance.
13. **Prosa de TFG, no listas de capturas:** nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
14. **Todo tiene sentido:** cada figura y tabla se cita en el texto y se explica, no hay texto de relleno y el orden de las secciones sigue el de la plantilla.

## Cómo se comprueba

15. Antes de marcar TERMINADO, el PDF se revisa página a página, y `revisar_maquetacion.py` debe salir en verde. Lo que no mide el script (que las tablas se lean bien y que el orden tenga sentido) lo comprueba el revisor.
