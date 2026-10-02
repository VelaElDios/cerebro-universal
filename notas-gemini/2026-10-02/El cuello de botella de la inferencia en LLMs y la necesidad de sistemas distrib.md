---
titulo: "El cuello de botella de la inferencia en LLMs y la necesidad de sistemas distribuidos"
createdBy: gemini
model: gemini-3.5-flash-lite
createdAt: 2026-10-02 12:09
tags: ["ia", "sistemas-distribuidos", "modelos-de-lenguaje"]
---

Si bien el [[Mecanismo de autoatención escalada en transformadores]] explica cómo un modelo procesa las relaciones semánticas en paralelo durante el entrenamiento, la realidad operativa en la fase de inferencia introduce desafíos severos de infraestructura que conectan directamente con la arquitectura de sistemas distribuidos.

Durante la generación de texto autorregresiva, el modelo debe procesar los tokens uno a uno. En cada paso temporal, la operación estrella implica multiplicar vectores de consulta contra la matriz de claves y valores (KV Cache) acumulada de todos los tokens anteriores. A medida que la longitud de contexto (*context window*) crece hacia cientos de miles de tokens, el almacenamiento y acceso a esta KV Cache satura el ancho de banda de la memoria de la GPU (VRAM).

Para solucionar esto en entornos de producción, una sola GPU rara vez es suficiente. Aquí es donde entran en juego las estrategias de paralelismo de modelos, dividiendo el peso de las matrices de atención entre múltiples nodos interconectados por redes de alta velocidad como InfiniBand.

Consideremos un fragmento simplificado en PyTorch que ilustra cómo se gestiona conceptualmente el almacenamiento incremental de la KV Cache para evitar recalcular la atención de toda la historia en cada paso:

```python
import torch

class KVCache:
    def __init__(self):
        self.k_cache = None
        self.v_cache = None

    def update(self, new_k, new_v):
        if self.k_cache is None:
            self.k_cache = new_k
            self.v_cache = new_v
        else:
            # Concatenar a lo largo de la dimensión de la secuencia
            self.k_cache = torch.cat([self.k_cache, new_k], dim=-2)
            self.v_cache = torch.cat([self.v_cache, new_v], dim=-2)
        return self.k_cache, self.v_cache
```

Sin embargo, este enfoque plantea un problema clásico de sistemas distribuidos: la latencia de red. Cuando los heads de atención están divididos en diferentes servidores (*Tensor Parallelism*), cada capa del transformador requiere operaciones de comunicación colectiva (como `All-Reduce`) antes de pasar al siguiente bloque. Esto significa que la velocidad de un LLM no solo depende de la elegancia matemática de la autoatención, sino de la eficiencia física con la que los datos se mueven a través de la red.
