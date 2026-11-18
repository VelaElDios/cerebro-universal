---
tipo: "fuente"
titulo: "Enero2026 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Enero2026.pdf`.

## Resumen
Este trozo es un examen de Arquitectura de Computadores (curso 2025/26) que incluye 30 preguntas tipo test y un problema de segmentación software. El test cubre: distinción ISA/ORG, ley de Amdahl, cálculo de MIPS, clasificación de dependencias (RAW/WAR/WAW), planificación estática vs dinámica, funcionamiento de Scoreboard y Tomasulo, riesgos en pipeline RISC-V, predictores de salto (1 bit, BTB, correlacionado), Tomasulo especulativo con bits venenosos, características de superescalar y VLIW, cuota de mercado RISC-V, disipación de potencia, arquitecturas load-store, comparación ARM/RISC-V, clas
Este trozo contiene dos problemas completos de un examen de Arquitectura de Computadores (Enero 2026). El Problema 2 pide simular la ejecución de 7 instrucciones FP en un Tomasulo con especulación (ROB 4 entradas, 2 RS/unidad FP, 2 load buffers, latencias: load/store 2c, fmul 5c, fadd 2c, fdiv 10c, CDB exclusivo, recursos liberados al ciclo siguiente) y mostrar el ROB en ciclo 6. El Problema 3 pide optimizar un bucle Y[i]=(X[i]+K)*X[i] en VLIW 1.0 (5 slots: Mem1, Mem2, PF1, PF2, Int/Salto, fully pipelined, latencias PF→PF 3, PF→fsd 3, fld→PF 1, delayed branch 1 ciclo), desenrollar 4×, planific

## Lo que se sacó de él (19)
- [[accion-ante-fallo-en-btb-con-salto-tomado-real-predecir-nt-p]]
- [[aplicacion-de-la-ley-de-amdahl-para-acelerar-una-fraccion-de]]
- [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]]
- [[bucle-escalar-original-para-optimizacion-vliw-enero-2026-pro]]
- [[calculo-de-mips-a-partir-de-mezcla-de-instrucciones-cpi-y-fr]]
- [[calculo-speedup-vliw-vs-escalar-para-examen-enero-2026-probl]]
- [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]]
- [[compatibilidad-binaria-vliw-2-0-con-latencia-fadd-d-aumentad]]
- [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]]
- [[definicion-de-dependencia-de-nombre-waw-y-war]]
- [[especificacion-vliw-1-0-para-examen-enero-2026-problema-3]]
- [[formulas-de-rendimiento-cpi-tiempo-mips-mflops-speedup-amdah]]
- [[latencias-vliw-1-0-para-examen-enero-2026-problema-3]]
- [[peticion-de-instantanea-rob-en-ciclo-6-para-examen-enero-202]]
- [[planificacion-estatica-el-compilador-reordena-para-reducir-d]]
- [[predictor-de-1-bit-en-bucle-de-3-iteraciones-t-t-nt-produce]]
- [[secuencia-de-instrucciones-para-simulacion-tomasulo-problema]]
- [[segmentacion-software-software-pipelining-para-bucle-conteo]]
- [[traza-de-predictor-correlacionado-1-1-con-historia-global-de]]
