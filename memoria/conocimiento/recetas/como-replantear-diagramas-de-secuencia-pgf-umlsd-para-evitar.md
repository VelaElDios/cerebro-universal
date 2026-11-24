---
tipo: "receta"
titulo: "Cómo replantear diagramas de secuencia pgf-umlsd para evitar fallos de maquetación"
temas: ["diagramas-secuencia", "latex", "maquetacion", "pgf-umlsd"]
claves: ["revisar_maquetacion.py", "solape", "letras pequeñas", "flechas cruzan texto", "adjustbox", "node distance"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[diagramas-secuencia]] · [[latex]] · [[maquetacion]] · [[pgf-umlsd]]

Pasos para replantear un diagrama de secuencia que falla en revisar_maquetacion.py (letras < 7.5 pt, solapes, flechas cruzando texto):

1. **Eliminar `adjustbox` con `max totalheight`**: ese escalado reduce el tamaño de fuente por debajo del mínimo. Dejar el diagrama a tamaño natural; los parámetros de flotantes relajados en `include/extra.tex` (`topfraction=0.85`, `floatpagefraction=0.8`, etc.) permiten que la figura comparta página con texto.

2. **Aumentar separación horizontal**: usar `\newinst[4]` (o más) en lugar de `\newinst[3]` para dar ≥ 2.5 cm entre líneas de vida. Esto evita que las flechas y etiquetas choquen con cajas adyacentes.

3. **Sustituir auto-llamadas (`call` de un participante a sí mismo) por participantes explícitos**: las auto-llamadas generan bucles que a menudo se cruzan con flechas posteriores. Ejemplo: en lugar de `\begin{call}{srv}{firma HMAC y envia}{srv}{enviado}\end{call}`, crear participantes `TokenSigner` y `Mailer` y hacer `\begin{call}{srv}{firma token}{tok}{token}\end{call}` y `\begin{call}{tok}{envia correo}{mail}{enviado}\end{call}`. Mantener máximo 6 participantes; si hay más, agrupar (ej. "Frontend" = Vista + api.js) o dividir en dos diagramas (cliente/servidor).

4. **Limpiar etiquetas**: en `\mess`, `call`, `callself`, `\newinst`:
   - Sin acentos, sin paréntesis en `\mess`, sin comandos LaTeX, sin `# & _ $ %` sueltos.
   - Usar `\n` para saltos de línea en etiquetas largas.
   - Textos cortos y descriptivos (ej. "verifica token" en vez de "verifica HMAC").

5. **Declarar todos los participantes** con `\newthread`/`\newinst` antes de usarlos.

6. **Comprobar con `revisar_umlsd.py`** antes de compilar: detecta caracteres prohibidos, participantes no declarados, etc.

7. **Revisión visual en PDF**: abrir el PDF compilado, medir tamaño de fuente (debe ser ≥ 7.5 pt), verificar que no hay flechas atravesando cajas ni texto, que no hay palabras partidas con guion, que los codos (|-, -|) separan bien las cajas. Si falla, repetir desde paso 2.

Ejemplo corregido (registro):
```latex
\begin{figure}[htbp]
\centering
\begin{sequencediagram}
  \newthread{u}{Usuario}
  \newinst[4]{fe}{Frontend}
  \newinst[4]{api}{API}
  \newinst[4]{srv}{Servicio}
  \newinst[4]{tok}{TokenSigner}
  \newinst[4]{mail}{Mailer}
  \begin{call}{u}{email y clave}{fe}{ok}
  \end{call}
  \begin{call}{fe}{POST register}{api}{201 o 409}
    \begin{call}{api}{register}{srv}{usuario}
      \begin{call}{srv}{busca email}{srv}{fila o null}
      \end{call}
      \begin{sdblock}{alt}{existe}
        \mess{srv}{ConflictError}{api}
        \mess{api}{409}{fe}
      \end{sdblock}
      \begin{sdblock}{else}{nuevo}
        \begin{call}{srv}{hash y crea}{srv}{usuario}
        \end{call}
        \begin{call}{srv}{firma token}{tok}{token}
        \end{call}
        \begin{call}{tok}{envia correo}{mail}{enviado}
        \end{call}
        \mess{api}{201}{fe}
      \end{sdblock}
    \end{call}
  \end{call}
  \mess{fe}{aviso}{u}
\end{sequencediagram}
\caption{Registro con email y contraseña.}
\label{fig:sec-registro}
\end{figure}
```

> Reglas 16-18: Figura 3.3 (fig:sec-registro), página 36 del PDF, chapters/04-descripcion.tex:335 (medido en el PDF): 2 solape(s) de cajas o textos: «usuario» con «HMAC», «usuario» con «firma».
> — `memoria/chapters/04-descripcion.tex` (cita sin comprobar)

Relacionado: [[inventario-de-diagramas-obligatorios-y-su-estado-actualizado]] · Cómo corregir diagramas de secuencia pgf-umlsd para pasar reglas 16-18 de Javier · Cómo replantear diagramas de secuencia pgf-umlsd para pasar revisar_maquetacion.py · Cómo corregir un diagrama de secuencia pgf-umlsd que falla en revisar_maquetacion.py (reglas 16-18) · [[diagramas-de-secuencia-pgf-umlsd-reglas-para-pasar-revisar-m]] · [[como-evitar-que-diagramas-de-secuencia-pgf-umlsd-desborden-l]] · [[diagramas-de-secuencia-con-pgf-umlsd-reglas-de-sintaxis]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
