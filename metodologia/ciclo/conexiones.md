<!-- voz: de testigo -->
# Las conexiones

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Los pares de pasos que se conectan, cada uno con la prueba que lo demuestra. Es lo único que dice si el ciclo es un ciclo o una lista de pasos.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Una conexión no se declara: se prueba. El par entra en la tabla cuando su script corre el paso de destino sin el entregable del de origen, y el de destino dice que no puede en lugar de inventarlo.

---

## La tabla

```plaintext
de               a                qué pasa        prueba                          estado
ninguna todavía: las conexiones salen de los pasos, y no hay pasos
```

## Las palabras, que son las que se cuentan

```plaintext
arista exigida       el recibe y el entrega que nombran los pasos
arista probada       la que tiene su script en verde
arista sin probar    exigida y sin script: se cuenta
huérfana             una entrega que nadie recibe, o una entrada que nadie da
isla                 un paso que no se conecta con ninguno
```

Y lo que no basta para escribir una conexión: que los dos pasos estén en el mismo archivo, o que uno mencione al otro en su texto. La mención no es una arista; la prueba sí. Y mientras la tabla diga «ninguna todavía», el recuento es **cero de un tablero vacío**, y no de uno limpio.

---

Falsificador: una conexión en la tabla sin su script; un paso que entrega algo que nadie recibe y no se apunta como huérfana; y una isla que se calla.
