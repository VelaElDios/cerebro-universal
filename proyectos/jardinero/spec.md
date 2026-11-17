# Jardinero: cuidar la memoria del cerebro

Proyecto especial (`"tipo": "jardin"`, una vez al día). No construye nada: cuida `memoria/` para que crecer
no la llene de ruido (ver `scripts/cerebro/jardin.py`).

1. **Comprueba citas** de notas «propuestas» contra su fuente: si la frase está casi igual, pone la cita
   literal y la nota pasa a «verificado». Sin IA.
2. **Fusiona notas repetidas** (embeddings muy parecidos y mismo tipo): una IA las junta sin perder datos;
   la otra se borra y los enlaces del vault pasan a la que queda.
3. **Marca contradicciones** entre notas parecidas con cifras («⚠️ Posible contradicción con…»), que bajan a
   «propuesto» hasta que se aclaren.
4. **Enlaza** las notas que hablan de lo mismo y todavía no se enlazaban (el grafo se densifica).
