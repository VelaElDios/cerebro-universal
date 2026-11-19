---
tipo: "concepto"
titulo: "Fusión de bucles (loop fusion) para localidad temporal"
temas: ["ac", "cache", "loop-transformation", "optimizacion"]
claves: ["loop fusion", "loop jamming", "temporal locality", "L1 cache", "single pass"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[cache]] · [[loop-transformation]] · [[optimizacion]]

**Loop fusion** (o *loop jamming*): combinar dos o más bucles que recorren el mismo rango de datos en un único bucle.

**Por qué mejora rendimiento:**
- **Localidad temporal**: en el código original, el primer bucle toca todos los elementos (lleva a L1/L2), pero al terminar, la caché se llena con los últimos elementos; cuando empieza el segundo bucle, los primeros ya han sido desalojados (*capacity miss*). Fusionando, cada elemento se lee, transforma y consume mientras sigue *caliente* en L1.
- **Reducción de ancho de banda**: se lee la memoria una sola vez (N lecturas) en lugar de dos (2N lecturas + N escrituras en el primer bucle).
- **Menos instrucciones de control**: un solo contador de bucle, una sola comprobación de límite por iteración.

**Condiciones de legalidad:**
- No hay dependencias de datos cruzadas que impidan reordenar (aquí: la normalización escribe `*it`, la suma lee `*it`; fusionando se hace `norm = *it - media; suma += norm*norm;` → legal).
- El cuerpo fusionado no excede registros disponibles (presión de registros).

**Ejemplo del trozo:**
```cpp
// Dos bucles → 2N accesos a memoria
for (auto it = v.begin(); it != v.end(); ++it) *it -= media;      // N lecturas + N escrituras
double suma = 0;
for (auto it = v.begin(); it != v.end(); ++it) suma += (*it)*(*it); // N lecturas

// Fusionado → N lecturas + N escrituras (si se guarda) o solo N lecturas
double suma = 0;
for (size_t i = 0; i < N; ++i) {
    float norm = v[i] - media;
    v[i] = norm;                 // opcional
    suma += double(norm)*norm;   // usa valor en registro
}
```

> Recorrer los datos en dos bucles rompe la localidad temporal: al iniciar la segunda pasada, los primeros elementos ya han sido expulsados de la caché.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp` (cita sin comprobar)

Relacionado: [[optimizar-std-list-a-std-vector-con-reserva-y-fusion-de-bucl]]
