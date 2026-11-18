---
tipo: "concepto"
titulo: "Compatibilidad binaria VLIW 2.0 con latencia fadd.d aumentada a 4 ciclos"
temas: ["ac", "compatibilidad", "examen", "vliw"]
claves: ["VLIW 2.0", "fadd.d latencia 3→4", "código binario sin recompilar", "hazard de datos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[compatibilidad]] · [[examen]] · [[vliw]]

VLIW expone latencias en ISA (compilador inserta nops/huecos). Si binario compilado para latencia 3 se ejecuta en HW con latencia 4: consumidores de fadd.d leerán registro antes de que productor escriba → hazard de datos (valor incorrecto). Como VLIW no tiene interlock hardware (compilador responsable), el procesador V2.0 o bien produce resultados erróneos, o bien requiere recompilar/reeschedule. Respuesta esperada: fallo silencioso (valor basura) o excepción si HW detecta hazard (poco probable en VLIW puro). Justificación: schedule original deja 3 huecos tras fadd.d; nuevo HW necesita 4; consumidor en ciclo 4 lee registro viejo.

> c) VLIW versión 2.0 (0,5 Puntos): Se lanza una revisión del procesador (VLIW Versión 2.0) diseñada para alcanzar mayores frecuencias de reloj. Como consecuencia, la unidad de suma en punto flotante se ha segmentado más profundamente, aumentando la latencia de la instrucción fadd.d de 3 ciclos a 4 ciclos. Si tomamos el código binario generado en la tabla del apartado 1 y lo ejecutamos tal cual en este nuevo procesador V2.0, ¿Qué ocurriría? Justifica detalladamente tu respuesta.
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf`

Relacionado: [[latencias-vliw-1-0-para-examen-enero-2026-problema-3]] · [[especificacion-vliw-1-0-para-examen-enero-2026-problema-3]]
