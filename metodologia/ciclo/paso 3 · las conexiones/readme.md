<!-- voz: de testigo -->
# Paso 3 · Las conexiones

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Prueba cada arista entre dos pasos: el paso de destino se corre sin lo que le entrega el de origen, y tiene que decir que no puede en vez de inventarlo. Es el tercer paso de la cadena, y se abre cuando los dos pasos que se conectan tienen su prueba.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

---

Se corre:      cuando dos fichas nombran un `recibe` y un `entrega` que se tocan, y las dos ya tienen su prueba en verde del paso 2. Se corre por arista, y el paso se cierra cuando todas las aristas exigidas están probadas.
Entra:         el `recibe` y el `entrega` de cada ficha; las pruebas del paso 2, en `vNN/pruebas/`; y `conexiones.md`, que es donde se apunta lo que hay.
Sale:          una línea por arista en `conexiones.md`, con su prueba, y su estado; el `.py` de la arista en `vNN/pruebas/`; y la corrida de este paso, que dice cuáles quedaron sin probar y cuáles son huérfanas.
Lo consume:    el paso 4, que cuenta las aristas exigidas, las probadas y las huérfanas; y quien lee el ciclo, que se fija en si es un ciclo o una lista de pasos.
La búsqueda:   por el par de pasos, y no por el nombre del archivo: se busca el `entrega` de uno y el `recibe` del otro, y se mira si nombran lo mismo. Si no lo nombran, no hay arista que probar.
Y si no encuentra: si una entrega no la recibe nadie, no se inventa su receptor: se apunta como huérfana en `conexiones.md`, y la cuenta sube. Si una entrada no la da nadie, se apunta igual.
Falla si:      se escribe una conexión sin su `.py`; se da por probada una arista cuyo script no corre; se cuenta como conexión una mención en el texto de otra ficha; o se deja un paso sin ninguna arista y no se apunta como isla.
Falsificador:  una conexión en la tabla sin su script; un paso que entrega algo que nadie recibe y no se apunta como huérfana; y una isla que se calla.
Y qué se pierde si cambia: se pierde lo único que dice si el ciclo es un ciclo. Sin este paso, el ciclo final es una lista de pasos bien escritos, y la costura entre ellos se rellena a mano otra vez, que es justo lo que el método vino a cerrar.
Invoca:        [paso 4 · las cuentas](../paso%204%20%C2%B7%20las%20cuentas/readme.md), que es lo que se lee al terminar este paso.

---

## 1. La conexión, y por qué se prueba

```plaintext
una conexión se prueba      el paso de destino se corre sin lo que el otro entrega,
                            y dice que no puede en vez de inventarlo
la mención no es una arista, la prueba sí
un paso que no se conecta con ningún otro es una isla, y se apunta
```

Y las palabras que se usan siempre, porque son las que se cuentan:

```plaintext
arista exigida       el recibe y el entrega que nombran los pasos
arista probada       la que tiene su script en verde
arista sin probar    exigida y sin script: se cuenta
huérfana             una entrega que nadie recibe, o una entrada que nadie da
isla                 un paso que no se conecta con ninguno
```

## 2. La tabla de `conexiones.md`

```plaintext
de               a                qué pasa        prueba                          estado
```

Y lo que no basta para escribir una conexión: que los dos pasos estén en el mismo archivo, o que uno mencione al otro en su texto.

## 3. Cómo se corrobora este paso

```plaintext
1. la tabla          una línea por arista, y ninguna sin su `.py`
2. el script          el de destino se corre sin la entrega, y dice que no puede
3. las huérfanas      cada entrega que nadie recibe está apuntada, y cada entrada
                      que nadie da también
4. las islas          cada paso que no se conecta con ninguno está apuntado
```

## 4. Cómo se pasa al paso 4

```plaintext
el paso 4 se abre cuando       todas las aristas exigidas tienen su `.py` en verde, y
                               las huérfanas y las islas están apuntadas
el paso 4 no se abre si        una arista exigida no tiene script, o hay una huérfana
                               sin apuntar
```

Y cuando se abre, se lee [paso 4 · las cuentas](../paso%204%20%C2%B7%20las%20cuentas/readme.md).

## 5. Lo que hoy no está

```plaintext
conexiones.md        dice «ninguna todavía: las conexiones salen de los pasos, y no hay
                     pasos», y ya hay doce fichas: la tabla no está al día
las aristas           las nombran las fichas, y ninguna tiene su `.py`
```

Y se dice aquí, y no en otro sitio, porque este es el paso que lo tiene que resolver.
