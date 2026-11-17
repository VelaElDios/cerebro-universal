---
tipo: "receta"
titulo: "Transformación AoS a SoA para optimización de caché (esquema de código)"
temas: ["ac", "aos", "cache", "optimización", "soa"]
claves: ["Array of Structs", "Structure of Arrays", "Particula", "id", "active", "data", "score", "vector contiguo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[aos]] · [[cache]] · [[optimización]] · [[soa]]

**AoS original**: `std::vector<Particula>` donde `Particula{int id; char active; int data; float score;}`. Si solo se usa `id`, se traen 16+ bytes por elemento (padding incluido) → bajo aprovechamiento de línea de caché (64 B).
**SoA transformado**:
```cpp
struct Particulas {
    std::vector<int>    id;
    std::vector<char>   active;
    std::vector<int>    data;
    std::vector<float>  score;
};
```
Inicialización: `id.resize(N); active.resize(N); ...` y rellenar cada vector contiguamente.
Bucle principal: `for (size_t i=0; i<N; ++i) suma += particulas.id[i];` → **16 enteros de 4 B por línea de 64 B** (100% útil).
Ambas versiones deben dar idéntico resultado numérico.

> Incluso utilizando vectores, el rendimiento puede ser ineficientes si el tamaño de nuestra estructura de datos es excesivo o contiene demasiados campos secundarios. Imaginemos una estructura como la de la Figura 4. Si nuestro algoritmo solo necesita operar con el campo id, cada vez que cargamos un elemento estamos subiendo el resto de los campos a la caché de forma innecesaria. Aquí es donde aplicamos la transformación de Array of Structs (AoS) a Struct of Arrays (SoA). Al separar cada campo de la estructura en su vector independiente, garantizamos que el 100% de los datos que se transfieren a la caché sean útiles para el cálculo actual, optimizando el ancho de banda de la memoria. // 1. Nueva estructura orientada a datos (SoA) Estructura Particulas { Vector de enteros: id Vector de bytes: active Vector de enteros: data Vector de flotantes: score } // 2. Llenado e inicialización Reservar espacio de golpe (N) para cada uno de los 4 vectores internos. Rellenar los datos de forma contigua para cada array. // 3. Procesamiento optimizado Para cada pasada: Para i desde 0 hasta N Hacer: suma = suma + particulas.id[i] // Máxima densidad: ¡16 ids por línea de caché! FinPara FinPara
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf` (cita sin comprobar)

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[cuando-preferir-aos-sobre-soa-en-la-practica]]
