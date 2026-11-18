# Control del conocimiento

Aquí decides qué sabe el cerebro. Crea una nota en esta carpeta con una o varias órdenes (una por línea).
En la siguiente ejecución del cerebro (como mucho en una hora, antes que todo lo demás) se ejecutan y
debajo aparece **«## Hecho por el cerebro»** con lo que ha hecho. No usa IA: es inmediato y exacto.

## Órdenes

| Orden | Qué hace |
|---|---|
| `olvidar tema: ac` | Borra todas las notas de ese tema |
| `olvidar fuente: temarios/AC/Tema2` | Borra lo aprendido de esa carpeta o archivo (si una nota viene también de otras fuentes, solo le quita esa) |
| `olvidar nota: Predictor gselect` | Borra una nota concreta (por título o nombre) |
| `olvidar proyecto: memoria-procesos` | Borra lo aprendido en ese proyecto |
| `no aprender: temarios/AC/examenes` | A partir de ahora eso no se aprende |
| `reaprender: temarios/AC/Tema2` | Lo olvida y lo vuelve a aprender en la próxima tanda |
| `aprender:` + texto debajo | Guarda ese texto como nota verificada (lo dices tú). Opcional, justo debajo: `tipo: receta`, `temas: ac, cache`, `privado: si`. El título es el de la nota |

Pon `simular` en la primera línea para ver qué haría sin tocar nada. Lo borrado sigue en el historial de
GitHub, así que se puede recuperar.

## Ejemplo de nota «Olvidar los exámenes de AC»

```
simular
olvidar fuente: temarios/AC/examenes
no aprender: temarios/AC/examenes
```

## Al momento, en tu PC

`py scripts/control.py "olvidar tema: ac"` (desde la carpeta del vault) hace lo mismo sin esperar.
