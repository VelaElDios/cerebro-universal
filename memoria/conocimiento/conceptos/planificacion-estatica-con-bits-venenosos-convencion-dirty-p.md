---
tipo: "concepto"
titulo: "Planificación estática con bits venenosos: convención dirty/prohibited"
temas: ["ac", "prediccion-saltos", "tomasulo"]
claves: ["poison bits", "dirty", "prohibited", "speculative execution", "static scheduling"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[tomasulo]]

En la planificación estática con bits venenosos, los registros que reciben un valor especulativo se marcan como «dirty» (envenenados) y las direcciones de memoria inválidas se marcan como «prohibited». La excepción no se lanza en el momento de la operación especulativa, sino que se difiere hasta que se intenta usar el registro envenenado o acceder a la dirección prohibida en una instrucción no especulativa (commit). Esto permite ejecutar instrucciones de forma especulativa sin detener el pipeline por fallos de predicción.

> The processor uses the static scheduling technique with poison bits. It uses ‘dirty’ for poisoned registers and ‘prohibited’ for invalid addresses.
> — `repo:datos/temarios/AC/examenes/June2025.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]]
