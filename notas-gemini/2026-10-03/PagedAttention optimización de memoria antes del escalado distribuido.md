---
titulo: "PagedAttention: optimización de memoria antes del escalado distribuido"
createdBy: gemini
model: gemini-flash-latest
createdAt: 2026-10-03 07:18
tags: ["llm", "arquitectura-sistemas", "optimizacion", "sistemas-operativos"]
---

En [[El cuello de botella de la inferencia en LLMs y la necesidad de sistemas distrib]], se plantea que el crecimiento de la memoria durante la generación autorregresiva obliga casi de inmediato a recurrir a clusters y paralelismo. Sin embargo, esta premisa pasa por alto una ineficiencia fundamental a nivel de software: el desperdicio de memoria por fragmentación antes de que sea estrictamente necesario escalar horizontalmente.

Tradicionalmente, para calcular el [[Mecanismo de autoatención escalada en transformadores]], los servidores de inferencia preasignan bloques de memoria contigua en la VRAM para la KV Cache en función de la longitud máxima posible de la secuencia (por ejemplo, 4096 o 8192 tokens). Si la solicitud real termina a los 200 tokens, entre el 60% y el 80% de esa memoria reservada queda inutilizada (fragmentación interna). Además, secuencias de tamaño variable generan huecos no utilizables en la memoria (fragmentación externa).

Inspirado en la memoria virtual clásica de los sistemas operativos de los años 60, el algoritmo **PagedAttention** (núcleo de frameworks como vLLM) divide la KV Cache de cada secuencia en bloques de tamaño fijo que se mapean a páginas físicas no contiguas en la VRAM mediante una tabla de páginas lógica.

Esquema conceptual simplificado de gestión de bloques:

```python
class PagedKVCacheManager:
    def __init__(self, block_size: int = 16):
        self.block_size = block_size
        self.free_blocks = list(range(1024))  # Pool de bloques en VRAM
        self.page_tables = {}  # seq_id -> list of block_ids

    def allocate_slot(self, seq_id: int, current_len: int) -> int:
        if seq_id not in self.page_tables:
            self.page_tables[seq_id] = []
        
        # Si el bloque actual está lleno, asignamos uno nuevo del pool
        if current_len % self.block_size == 0:
            new_block = self.free_blocks.pop(0)
            self.page_tables[seq_id].append(new_block)
            
        physical_block = self.page_tables[seq_id][-1]
        block_offset = current_len % self.block_size
        return physical_block, block_offset
```

Este desacoplamiento reduce el desperdicio de VRAM a menos del 4%, multiplicando el *throughput* de un único nodo por un factor de 2 a 4. Solo cuando la memoria física optimizada y consolidada por PagedAttention se satura, resulta justificado asumir la sobrecarga de sincronización que demandan las topologías distribuidas complejas.
