---
tipo: "concepto"
titulo: "Modelo de programación SIMT en GPGPU"
temas: ["ac", "gpgpu", "simt"]
claves: ["SIMT", "Single Instruction Multiple Thread", "GPGPU", "modelo ejecución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[gpgpu]] · [[simt]]

Las GPGPUs usan el modelo SIMT (Single Instruction Multiple Thread): una misma instrucción se ejecuta sobre múltiples hilos (threads) en paralelo, cada uno con sus propios datos y contador de programa. Los hilos son gestionados por hardware (warp scheduler), no por el SO. La opción correcta es b.

> En las GPGPUs: a) Se usa un modelo de ejecución homogéneo b) Se usa un modelo de programación SIMT (Single Instruction Multiple Thread) c) Los thread son manejados por el Sistema Operativo d) Todas son falsas
> — `repo:datos/temarios/AC/examenes/Enero2018.pdf`

Relacionado: [[caracteristicas-de-arquitectura-simd-frente-a-mimd]] · [[slowdown-en-procesadores-con-multithreading-frente-a-monocor]] · [[en-la-taxonomia-de-flynn-los-multicomputadores-son-maquinas]]
