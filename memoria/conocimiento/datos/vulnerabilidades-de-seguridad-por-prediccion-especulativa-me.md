---
tipo: "dato"
titulo: "Vulnerabilidades de seguridad por predicción especulativa: Meltdown, Spectre, Branch Privilege Injection"
temas: ["ac", "meltdown", "prediccion-saltos", "seguridad", "spectre"]
claves: ["Meltdown", "Spectre", "Branch Privilege Injection", "INTEL-2025-05-13-001-BranchPrivilegeInjection", "INTEL-SA-01247", "2018", "datos privilegiados", "kernel", "especulativo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[meltdown]] · [[prediccion-saltos]] · [[seguridad]] · [[spectre]]

Tres vulnerabilidades principales derivadas de la ejecución especulativa guiada por predictores de salto:
1. **Meltdown (2018)**: Afecta principalmente a Intel. Permite a programas de usuario leer memoria del kernel rompiendo el aislamiento de privilegios.
2. **Spectre**: Afecta a Intel, AMD, ARM. Engaña al predictor para ejecutar especulativamente código elegido por el atacante, filtrando datos vía side-channels (caché).
3. **Branch Privilege Injection (INTEL-2025-05-13-001-BranchPrivilegeInjection, INTEL-SA-01247)**: Variante más reciente (2025) que inyecta predicciones maliciosas en el predictor de saltos para forzar ejecución especulativa de gadgets controlados.
Todas explotan que el estado microarquitectónico (caché) no se revierte tras un fallo de predicción, dejando huellas medibles.

> El resultado de una predicción de salto puede dejar rastros de datos sensibles en la caché del procesador Un atacante puede forzar al predictor a tomar un salto incorrecto para ejecutar de forma especulativa un código que maneja datos confidenciales Ataques: – Meltdown (2018) (derrite las barreras de protección): Permite leer datos privilegiados (kernel) desde programas de usuario  Intel – Spectre: engaña al predictor de saltos para que ejecute una secuencia de código controlada por el atacante de forma especulativa Intel, AMD, ARM – Branch Privilege Injection (INTEL-2025-05-13-001-BranchPrivilegeInjection) , INTEL-SA-01247
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[arquitectura-epic-ia64-y-procesadores-itanium]] · [[instruccion-especulativa-ejecutada-antes-de-saber-si-realmen]] · [[recuperacion-ante-fallo-de-prediccion-descartar-resultados-e]] · [[recuperacion-ante-fallo-de-prediccion-de-salto-misprediction]]
