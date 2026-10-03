---
titulo: "Mitigación del DoS en KV Cache mediante control de cuotas y desalojo dinámico"
createdBy: gemini
model: gemini-3.5-flash-lite
createdAt: 2026-10-03 18:19
tags: ["Ciberseguridad", "Arquitectura-de-sistemas-distribuidos"]
---

Si bien el [[Ataques de denegación de servicio contra la memoria KV Cache en inferencia de LL]] demuestra cómo un atacante puede agotar la VRAM explotando la retención pasiva de estados en la inferencia, la defensa no puede recaer únicamente en limitar las conexiones a nivel de red. Es necesario integrar contramedidas directamente en la gestión de memoria distribuida, cuestionando la presunción de que los bloques asignados deben pertenecer a la solicitud hasta que el cliente decida liberarlos.

Para blindar los servidores de inferencia ante ataques de denegación de servicio algorítmico sin comprometer la eficiencia lograda por sistemas como [[PagedAttention optimización de memoria antes del escalado distribuido]], la arquitectura debe incorporar políticas estrictas de desalojo dinámico y cuotas estrictas de bloques físicos por sesión autenticada o IP.

A nivel práctico, un gestor de memoria resiliente debe implementar un mecanismo de *time-to-live* (TTL) adaptativo y un esquema de desalojo por prioridad (eviction policy). Si una conexión se vuelve inactiva durante la generación en streaming, el sistema suspende la tarea, serializa la KV Cache hacia la memoria RAM del host (swap) o la descarta por completo, liberando las páginas físicas en la VRAM para solicitudes legítimas.

A continuación, se muestra un ejemplo conceptual en Python que extiende la gestión de bloques para incluir un control de inactividad y desalojo preventivo:

```python
import time

class SecurePagedKVCacheManager:
    def __init__(self, total_blocks: int, max_idle_time: float = 5.0):
        self.total_blocks = total_blocks
        self.max_idle_time = max_idle_time
        self.active_sessions = {}

    def allocate_block(self, session_id: str):
        self._check_timeouts()
        if len(self.active_sessions.get(session_id, [])) >= 10:
            raise PermissionError("Cuota de bloques excedida para esta sesión (posible DoS).")
        
        block = object()
        self.active_sessions.setdefault(session_id, []).append({
            "block": block,
            "last_active": time.time()
        })
        return block

    def touch_session(self, session_id: str):
        if session_id in self.active_sessions:
            for entry in self.active_sessions[session_id]:
                entry["last_active"] = time.time()

    def _check_timeouts(self):
        current_time = time.time()
        for session_id, blocks in list(self.active_sessions.items()):
            if any(current_time - b["last_active"] > self.max_idle_time for b in blocks):
                print(f"Desalojando sesión inactiva {session_id} por posible ataque de retención.")
                del self.active_sessions[session_id]
```

Esta aproximación demuestra que la seguridad en la capa de inferencia de LLMs exige un acoplamiento estrecho entre los algoritmos de atención y las políticas de control de recursos en sistemas distribuidos.
