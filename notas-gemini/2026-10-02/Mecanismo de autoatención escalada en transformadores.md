---
titulo: "Mecanismo de autoatención escalada en transformadores"
createdBy: gemini
model: gemini-flash-latest
createdAt: 2026-10-02 02:32
tags: ["ia", "deep-learning", "transformers", "nlp"]
---

El corazón de los modelos de lenguaje modernos (LLMs) reside en el mecanismo de autoatención (*Scaled Dot-Product Attention*). A diferencia de las arquitecturas recurrentes anteriores (RNNs o LSTMs), que procesaban texto de forma secuencial, este mecanismo calcula directamente las dependencias semánticas entre cualquier par de tokens en una secuencia, independientemente de su distancia.

El cálculo se fundamenta en tres matrices proyectadas a partir de los embeddings de entrada: **Queries** ($Q$), **Keys** ($K$) y **Values** ($V$). De forma conceptual, cada token formula una consulta ($Q$), evalúa su afinidad con las claves ($K$) de todos los demás tokens mediante producto punto, y utiliza el resultado normalizado para ponderar los valores ($V$).

La ecuación fundamental es:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

El factor de escala $\sqrt{d_k}$ (donde $d_k$ es la dimensión del vector de clave) es crucial: contrarresta el crecimiento de la magnitud del producto punto a dimensiones altas, evitando que la función softmax sature y genere gradientes prácticamente nulos durante el entrenamiento.

Implementación mínima en PyTorch:

```python
import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q, K, V, mask=None):
    d_k = Q.size(-1)
    # 1. Similitud entre consultas y claves escalada
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    
    # 2. Aplicar máscara si existe (ej. autorregresiva)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))
        
    # 3. Distribución de pesos y multiplicación por V
    attention_weights = F.softmax(scores, dim=-1)
    return torch.matmul(attention_weights, V), attention_weights
```

En modelos generativos autorregresivos, se aplica una máscara triangular superior sobre `scores` para impedir que un token observe posiciones futuras. Aunque esta arquitectura habilita un entrenamiento masivamente paralelizable en GPU, acarrea un coste computacional cuadrático $\mathcal{O}(N^2)$ respecto a la longitud de la secuencia $N$, lo que supone uno de los principales cuellos de botella en ventanas de contexto extensas.
