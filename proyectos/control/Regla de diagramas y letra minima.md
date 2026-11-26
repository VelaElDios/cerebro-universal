olvidar nota: diagramas-de-secuencia-max-6-participantes-agrupar-o-partir
aprender:
tipo: decision
temas: latex, diagramas, pgf-umlsd, reglas-tfg
titulo: Diagramas a tamaño real, letra mínima 7,5 pt y como mucho 6 participantes
Regla única (memoria/reglas-tfg.md, reglas 16 y 19, decidida por Javier el 26/11/2026): los diagramas (TikZ, pgf-umlsd, pgfplots) nunca se escalan; están prohibidos \resizebox, adjustbox y scale, ni siquiera para encoger un poco. La letra del diagrama tiene que medir al menos 7,5 pt en el PDF (es el umbral que mide scripts/revisar_figuras.py; lo ideal es acercarse al tamaño del pie de figura). Los diagramas de secuencia tienen como mucho 6 participantes; si no caben, se agrupan participantes o se parte el diagrama en dos. Para que quepan: \newinst[1] o [2], nombres de participantes cortos y mensajes de 2-3 palabras. Cualquier nota que diga otra cosa (8-9 pt, resizebox para ajustes menores) queda sustituida por esta.
