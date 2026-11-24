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


## Hecho por el cerebro (2026-11-24 17:17)

**Olvidar nota «diagramas-de-secuencia-pgf-umlsd-sintaxis-valida-y-errores-c»:** 1 notas borradas
  - Diagramas de secuencia pgf-umlsd — sintaxis válida y errores comunes

**Olvidar nota «como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re»:** 1 notas borradas
  - Cómo corregir diagramas de secuencia pgf-umlsd para pasar reglas 16-18 de Javier

**Olvidar nota «diagramas-de-secuencia-con-pgf-umlsd»:** 1 notas borradas
  - Diagramas de secuencia con pgf-umlsd

**Olvidar nota «diagramas-de-secuencia-con-pgf-umlsd-sequencediagram»:** 1 notas borradas
  - Diagramas de secuencia con pgf-umlsd (sequencediagram)

**Olvidar nota «diagramas-de-secuencia-con-pgf-umlsd-sintaxis-valida-y-error»:** 1 notas borradas
  - Diagramas de secuencia con pgf-umlsd: sintaxis válida y errores comunes

**Olvidar nota «como-corregir-un-diagrama-de-secuencia-pgf-umlsd-que-falla-e»:** 1 notas borradas
  - Cómo corregir un diagrama de secuencia pgf-umlsd que falla en revisar_maquetacion.py (reglas 16-18)

**Olvidar nota «replanteo-de-diagrama-de-secuencia-pgf-umlsd-para-evitar-des»:** 1 notas borradas
  - Replanteo de diagrama de secuencia pgf-umlsd para evitar desbordamiento y cruces

**Olvidar nota «como-escribir-un-diagrama-de-secuencia-pgf-umlsd-valido-y-le»:** 1 notas borradas
  - Cómo escribir un diagrama de secuencia pgf-umlsd válido y legible

**Olvidar nota «como-replantear-diagramas-tikz-pgf-umlsd-para-pasar-revisar»:** 1 notas borradas
  - Cómo replantear diagramas TikZ/pgf-umlsd para pasar revisar_maquetacion.py (reglas 16-18)

**Olvidar nota «como-replantear-diagramas-de-secuencia-pgf-umlsd-para-pasar»:** 1 notas borradas
  - Cómo replantear diagramas de secuencia pgf-umlsd para pasar revisar_maquetacion.py

**Aprender:** guardada [[los-diagramas-nunca-se-escalan-para-que-quepan]] como decision verificado
