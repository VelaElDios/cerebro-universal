---
tipo: "receta"
titulo: "Cómo configurar SMTP saliente con Gmail (contraseña de aplicación)"
temas: ["correo", "grada-colchonera", "oauth", "saas"]
claves: ["SMTP_URL", "MAIL_FROM", "verificación en dos pasos", "contraseña de aplicación", "smtps://", "puerto 465"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/hito4-configuracion.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[correo]] · [[grada-colchonera]] · [[oauth]] · [[saas]]

1. En la cuenta Gmail que enviará correos: activa **verificación en dos pasos** (https://myaccount.google.com/security).
2. Ve a https://myaccount.google.com/apppasswords, crea contraseña de aplicación llamada `La Grada`, copia las 16 letras (sin espacios).
3. Construye `SMTP_URL` con formato: `smtps://<usuario>%40gmail.com:<16_letras>@smtp.gmail.com:465` (la `@` se codifica como `%40`).
4. Define `MAIL_FROM`: `La Grada Colchonera <tucorreo@gmail.com>`.
5. Límite diario de Gmail ~500 envíos; alternativa gratuita: Brevo (mismo formato de URL).

> La `SMTP_URL` queda así (la `@` del usuario se escribe `%40`): `smtps://tucorreo%40gmail.com:abcdefghijklmnop@smtp.gmail.com:465` y `MAIL_FROM`: `La Grada Colchonera <tucorreo@gmail.com>`.
> — `repo:saas/docs/hito4-configuracion.md`

Relacionado: [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
