olvidar nota: diagramas-de-secuencia-pgf-umlsd-sintaxis-valida-y-errores-c
olvidar nota: como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re
olvidar nota: diagramas-de-secuencia-con-pgf-umlsd
olvidar nota: diagramas-de-secuencia-con-pgf-umlsd-sequencediagram
olvidar nota: diagramas-de-secuencia-con-pgf-umlsd-sintaxis-valida-y-error
olvidar nota: como-corregir-un-diagrama-de-secuencia-pgf-umlsd-que-falla-e
olvidar nota: replanteo-de-diagrama-de-secuencia-pgf-umlsd-para-evitar-des
olvidar nota: como-escribir-un-diagrama-de-secuencia-pgf-umlsd-valido-y-le
olvidar nota: como-replantear-diagramas-tikz-pgf-umlsd-para-pasar-revisar
olvidar nota: como-replantear-diagramas-de-secuencia-pgf-umlsd-para-pasar
aprender:
tipo: decision
temas: latex, pgf-umlsd, diagramas, reglas-tfg
titulo: Los diagramas nunca se escalan para que quepan
Los diagramas (TikZ, pgf-umlsd y pgfplots) nunca se meten en \resizebox, adjustbox ni scale para que quepan: eso deja las letras por debajo de 7,5 pt y revisar_figuras.py lo rechaza (reglas 16 y 19 de memoria/reglas-tfg.md). Tienen que caber a tamaño real.
En un diagrama de secuencia (pgf-umlsd) se consigue con poca separación entre participantes (\newinst[1] o \newinst[2]; con [4] o [5] se sale del margen), nombres de participantes cortos (Servicio, Repositorio), mensajes de 2-3 palabras y como mucho 6 participantes. Si aun así no cabe, se parte en dos diagramas.
Ejemplo probado en memoria-procesos (24/11/2026): fig:sec-partida, con 5 participantes y \newinst[2] para el primero y [1] para el resto, cabe sin escalar y pasa la prueba completa.
