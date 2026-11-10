<!-- voz: de testigo -->
# Las conexiones

<!-- negritas: revisadas. lo que queda en negro es lo que tiene que saltar -->

Los pares de pasos que se conectan, cada uno con su nombre y con la prueba que lo demuestra.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Una conexión no se declara: se prueba. Un par de pasos entra en esta tabla sólo cuando su script corre el segundo paso sin el entregable del primero, y el segundo dice que no puede en lugar de inventarlo.

---

## La tabla

```plaintext
de               a                qué pasa        prueba                          estado
ninguno todavía: las conexiones salen de los pasos, y no hay pasos
```

## Las reglas

```plaintext
una arista existe      sólo si su script desde cero pasa y el paso de destino,
                       sin la entrada, dice que no puede
arista exigida         el recibe y el entrega que nombran los pasos
arista sin probar      está exigida y no tiene script en verde: se cuenta
huérfana               una entrega que nadie recibe, o una entrada que nadie da
isla                   un paso que no se conecta con ninguno: se apunta
```

Y lo que no basta para escribir una conexión: que los dos pasos estén en el mismo archivo, o que uno mencione al otro en su texto. La mención no es una arista; la prueba sí.

---

## El recuento que se lleva a `estado actual.md`

```plaintext
exigidas     probadas     sin probar     huérfanas     islas
```

Y mientras sean cero porque no hay pasos, el recuento dice eso: **cero de un tablero vacío**, que no es lo mismo que cero de un tablero limpio.

---

Falsificador: una conexión en la tabla sin su script; un paso que entrega algo que nadie recibe y no se apunta como huérfana; y una isla que se calla.
