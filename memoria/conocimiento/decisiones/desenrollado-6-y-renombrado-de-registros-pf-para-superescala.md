---
tipo: "decision"
titulo: "Desenrollado 6× y renombrado de registros PF para superescalar MIPS64 (examen 2015)"
temas: ["ac", "desenrollado", "mips64", "renombrado", "superescalar"]
claves: ["desenrollado 6 veces", "renombrado F4_i F6_i", "dependencias WAR WAW", "puntero R1 compartido"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[desenrollado]] · [[mips64]] · [[renombrado]] · [[superescalar]]

**Decisión de diseño para el desenrollado:**
- **Renombrado de registros PF:** Cada iteración i (1..6) usa sus propios registros temporales F4_i, F6_i para evitar dependencias de nombre (WAR/WAW) entre iteraciones. El código original reusa F4 y F6; al desenrollar sin renombrar, la iteración i+1 sobrescribiría F4 antes de que la iteración i termine su MUL.D/ADD.D, creando dependencias falsas que impiden el solapamiento.
- **Puntero R1 compartido:** Las instrucciones DADDUI R1,R1,8 son enteras y se ejecutan en orden (una por iteración) actualizando R1 secuencialmente. Las cargas L.D F4_i,0(R1) y almacenas S.D F6_i,0(R1) de la iteración i usan el valor de R1 **tras** la DADDUI de la iteración i-1 (o valor inicial para i=1). Con adelantamiento, la dirección efectiva está lista 1 ciclo después de la DADDUI.
- **Saltos BNE:** Cada iteración tiene su BNE. Al desenrollar, los 5 primeros BNE saltan al siguiente BNE (o a la siguiente instrucción si se coloca código entre ellos). El 6º BNE sale del bucle. Al haber salto retardado, la instrucción inmediatamente posterior a cada BNE (en orden de programa) ocupa su slot de retardo y se ejecuta siempre. En el código desenrollado lineal, se puede colocar una instrucción útil (p.ej. la L.D de la siguiente iteración) en el slot de retardo de cada BNE.
- **Orden de instrucciones en el desenrollado:** Se mantiene el orden de programa por iteración (L.D → MUL.D → ADD.D → S.D → DADDUI → BNE) pero se entrelazan instrucciones de distintas iteraciones en la planificación para ocultar latencias.

> a) Desenrolla el código 6 veces y planifícalo lo más compactamente posible para el superescalar planteado.
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[planificacion-superescalar-mips64-4-vias-con-latencias-pf-pr]] · [[como-desenrollar-8x-y-planificar-en-superescalar-4-issue-2-i]] · [[desenrollado-de-bucle-8-veces-para-superscalar-con-latencias]]
