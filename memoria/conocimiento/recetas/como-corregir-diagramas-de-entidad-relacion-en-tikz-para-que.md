---
tipo: "receta"
titulo: "Cómo corregir diagramas de entidad-relación en TikZ para que no crucen cajas"
temas: ["latex", "memoria", "pgf-umlsd", "tikz"]
claves: ["fig:modelo-datos", "flecha atraviesa caja", "node distance", "coordenadas explícitas"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[memoria]] · [[pgf-umlsd]] · [[tikz]]

|
  1. Definir coordenadas explícitas para cada entidad (no usar positioning relativo que apile cajas).
  2. Colocar las cajas en una rejilla: session (-7,0), users (0,0), perfiles (9,0), records (9,-6).
  3. Dibujar flechas solo entre cajas vecinas o con codos que rodeen otras cajas:
     - users→perfiles: horizontal directo (east→west).
     - users→records: (users.east) -- ++(2,0) |- (records.south) → sale a la derecha, baja por la derecha de perfiles.
     - session→users: dashed horizontal (opcional).
  4. Etiquetas con `node[pos=0.75, right, font=\footnotesize]` en el tramo vertical, fuera de cajas.
  5. Verificar en PDF: ninguna flecha atraviesa una caja, letras ≥ 8 pt, node distance suficiente.
ejemplo: |
  \begin{tikzpicture}[
    entity/.style={rectangle, draw=tema, fill=gris95, rounded corners, minimum height=2.5cm, align=left, font=\small, text width=5.5cm},
    arrow/.style={-{Stealth[length=2.5mm]}, thick, color=tema}
  ]
    \node[entity] (session) at (-7,0) { ... };
    \node[entity] (users) at (0,0) { ... };
    \node[entity] (perfiles) at (9,0) { ... };
    \node[entity] (records) at (9,-6) { ... };
    \draw[arrow] (users.east) -- node[above, font=\footnotesize] {tiene su club} (perfiles.west);
    \draw[arrow] (users.east) -- ++(2,0) |- node[pos=0.75, right, font=\footnotesize] {tiene su mejor partida} (records.south);
  \end{tikzpicture}

> La línea inferior que conecta 'users' con 'juego_records' atraviesa por completo el espacio interior del diagrama pasando verticalmente por debajo de 'users'.
problema: La flecha users→juego_records bajaba 7.5 cm por la izquierda y pasaba por debajo de la caja users, cruzando el espacio interior del diagrama.
solucion: Reubicar las entidades con coordenadas explícitas: session (izquierda), users (centro), perfiles (derecha), records (debajo de perfiles). La relación users→records sale por el este de users, va horizontal a la derecha de perfiles, baja y entra por el sur de records. Usar flechas con codos (|-) y etiquetas fuera de líneas verticales. Aumentar separación horizontal entre cajas (≥ 2.5 cm).
> — `chapters/04-descripcion.tex` (cita sin comprobar)

Relacionado: [[como-escribir-un-diagrama-de-entidad-relacion-en-tikz-legibl]] · [[como-evitar-cruces-en-diagramas-tikz-pgf-umlsd]] · [[diagramas-ninguna-linea-flecha-atraviesa-cajas-codos-y-dista]] · [[como-corregir-solapes-de-etiquetas-en-diagramas-tikz-de-enti]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
