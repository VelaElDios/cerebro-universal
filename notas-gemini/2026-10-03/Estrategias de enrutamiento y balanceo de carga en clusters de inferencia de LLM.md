---
titulo: "Estrategias de enrutamiento y balanceo de carga en clusters de inferencia de LLMs"
createdBy: gemini
model: gemini-3.5-flash-lite
createdAt: 2026-10-03 23:16
tags: ["sistemas-distribuidos", "arquitectura-de-sistemas", "ciberseguridad", "inferencia-de-LLM"]
---

Si bien [[Mitigación del DoS en KV Cache mediante control de cuotas y desalojo dinámico]] aborda la defensa a nivel de gestión interna de memoria y [[Estrategias de paralelismo de secuencia para aliviar el cuello de botella en la ]] resuelve el escalado horizontal dentro de una misma solicitud masiva, la arquitectura global de un sistema distribuido de inferencia requiere una capa previa fundamental: el enrutamiento inteligente y el balanceo de carga (*Load Balancing*).

En los servidores tradicionales de microservicios, el balanceo se basa en algoritmos sencillos como *Round-Robin* o least-connections, asumiendo que el costo computacional de cada petición es relativamente homogéneo. Sin embargo, en la inferencia de Modelos de Lenguaje Grande (LLMs), el tiempo de procesamiento y la ocupación de la VRAM son altamente asimétricos y varían drásticamente según la longitud del prompt de entrada y, sobre todo, el número de tokens generados en la salida.

Un balanceador de carga ingenuo puede enviar múltiples peticiones con contextos kilométricos a una misma GPU, saturando instantáneamente su [[Ataques de denegación de servicio contra la memoria KV Cache en inferencia de LL]] y colapsando el pool de bloques gestionado por [[PagedAttention optimización de memoria antes del escalado distribuido]], mientras que otros nodos permanecen infrautilizados.

Para optimizar el rendimiento y mitigar ataques de denegación de servicio a nivel de infraestructura, los proxies de enrutamiento modernos implementan balanceo basado en la carga actual de la KV Cache y la longitud estimada de la secuencia. A continuación, se muestra un ejemplo conceptual en Python de un enrutador que selecciona el nodo con menor ocupación de memoria y menor número de tareas activas:

```python
class InferenceRouter:
    def __init__(self, nodes):
        # nodes es una lista de diccionarios con métricas de cada instancia
        self.nodes = nodes 

    def route_request(self, estimated_prompt_tokens: int):
        best_node = None
        min_score = float('inf')
        
        for node in self.nodes:
            # Calcular un puntaje heurístico basado en la VRAM libre y tareas en cola
            free_vram_ratio = node['free_vram'] / node['total_vram']
            active_tasks = node['active_tasks']
            
            # Si el nodo no tiene suficiente memoria estimada para el prompt, se descarta
            if node['free_vram'] < (estimated_prompt_tokens * node['bytes_per_token']):
                continue
                
            # Heurística: priorizar nodos con más VRAM libre y menor carga
            load_score = active_tasks - (free_vram_ratio * 10)
            
            if load_score < min_score:
                min_score = load_score
                best_node = node
                
        if not best_node:
            raise Exception("Cluster saturado: No hay nodos disponibles con suficiente KV Cache.")
            
        return best_node['id']

# Ejemplo de uso:
cluster_nodes = [
    {"id": "gpu-node-1", "free_vram": 24.0, "total_vram": 80.0, "active_tasks": 2, "bytes_per_token": 0.002},
    {"id": "gpu-node-2", "free_vram": 70.0, "total_vram": 80.0, "active_tasks": 0, "bytes_per_token": 0.002}
]
router = InferenceRouter(cluster_nodes)
print(f"Enrutar petición a: {router.route_request(estimated_prompt_tokens=500)}")
```

Esta capa de abstracción no solo mejora el rendimiento y previene cuellos de botella imprevistos, sino que actúa como la primera línea de defensa frente a patrones de tráfico maliciosos que intentan desestabilizar nodos específicos del cluster.
