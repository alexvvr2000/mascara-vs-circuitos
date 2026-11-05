# Lo que salió de levantar un ente desde cero

**PRUEBA · corrida del 2026-11-05_120911 · y estos son los huecos que la obra todavía no cierra.**

**Y este archivo es el resultado de la prueba, no una nota aparte: si un hueco no se cierra aquí, sigue abierto en los ensayos, aunque el ente haya corrido.**

---

## Los cinco huecos, y de dónde salió cada uno

| # | El hueco | De dónde salió |
|---|---|---|
| **1** | **la pieza no existe en el esquema** | el borde dice que se evalúa contra «los atributos de una pieza», y no hay tabla `pieza`. Se usó la frase como texto y se partió por comas |
| **2** | **un borde en prosa no lo puede correr una máquina** | `quien_evalua = 'maquina'` y no hay forma de escribir un borde ejecutable. Las dos cosas a la vez se contradicen |
| **3** | **el «casi» no tiene salida** | una pieza a medio camino no la acepta ni la rechaza, y el borde no tiene campo donde declarar qué hacer |
| **4** | **`cerrar` cuenta y no cierra** | el propósito queda abierto y el ente no tiene cómo proponerlo. El paso de cerrar es hablar, y no hay dónde |
| **5** | **una corrida nunca cierra algo sin la autoridad** | correcto por diseño, y hay que saberlo: `cerrado_por` con `autoridad_id` en NULL no pasa el CHECK |

---

## Y lo que sí aguantó

```plaintext
la pieza sin tema se declara como hueco, y no se contesta ✔
la regla que se vuelve a caer se apunta como tal        ✔
el cierre sin autoridad constando se rechaza             ✔
un tema que nunca se usó se ve en el cierre              ✔
los varios propósitos abiertos a la vez                  ✔
```

**Y esto es lo único que prueba que la obra sirve: alguien la siguió, y le costó.**
