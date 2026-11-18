---
tipo: "receta"
titulo: "Dependencias en bucle MIPS64 de encriptación ASCIIZ (Problema 1)"
temas: ["ac", "dependencias", "mips", "pipeline"]
claves: ["LB", "DADD", "DADDUI", "SB", "BNEZ", "dependencia datos", "salida", "anti"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[mips]] · [[pipeline]]

Análisis de dependencias dentro de una iteración: 
- Dependencias de datos (RAW): I1→I2 (R2), I1→I3 (R2), I2→I6 (R3), I3→I4 (R2), I5→I1 (R1, siguiente iteración), I5→I4 (R1, misma iteración? I4 usa R1 antes de I5? I4: SB R2,0(R1) usa R1; I5: DADDUI R1,R1,#1 escribe R1 → antidependencia WAR). 
- Dependencias de salida (WAW): I1 e I3 escriben R2 → WAW en R2. I5 escribe R1, pero no hay otra escritura a R1 en la iteración. 
- Antidependencias (WAR): I4 lee R1, I5 escribe R1 → WAR en R1. I3 escribe R2, I4 lee R2 → WAR en R2 (pero I3 escribe antes que I4 lee? Orden: I3 escribe R2, I4 lee R2 → RAW, no WAR). 
Tabla resumen para el examen:
Dependencias de Datos: I1→I2 (R2), I1→I3 (R2), I2→I6 (R3), I3→I4 (R2), I5→I1 (R1, inter-iteración).
Dependencias de Salida: I1 e I3 sobre R2.
Antidependencias: I4→I5 (R1).

> loop: LB R2, 0(R1) # I1; carga en R2 el carácter actual de la cadena DADD R3, R2, R0 # I2; copia R2 en R3 DADDUI R2, R2, #5 # I3; codifica el carácter (también el character NUL) SB R2, 0(R1) # I4; almacena el carácter codificado en memoria DADDUI R1, R1, #1 # I5; R1 apunta al siguiente caráceter de la cadena BNEZ R3, loop # I6; comprueba si el carácter es NULL(0x00)
> — `repo:datos/temarios/AC/examenes/Enero2018.pdf`

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[dependencias-en-bucle-mips-de-carga-modificacion-almacenamie]] · [[dependencias-raw-war-y-waw-en-el-bucle-de-producto-escalar-v]] · [[analisis-de-dependencias-raw-war-waw-en-una-iteracion-del-bu]]
