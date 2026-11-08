# Ente 14 · PISO SANO

**El ciclo entero con un piso que alcanza. Y lo que salió al buscarlo de verdad.**

**Corrida del 8 de noviembre de 2026.** **`TESTIGO`, con `Alejandro Valenzuela Rivera` como autoridad.** **Cuerpo: `DeepSeek V4.1 Flash`, por `OpenCode Go`.**

---

## Qué se probaba

**Lo que trece corridas nunca vieron: una tarea que el piso sí puede cumplir.**

**Trece corridas dijeron «no está en el piso» o «falta medir». Ninguna había llegado al otro lado: el ente contesta que sí, y tiene que hacerlo.**

**Y con las dos correcciones que la corrida 13 dejó:**

```plaintext
el piso se puede señalar      la vista expone el id
el cierre sin criterio        lleva se_pregunto, preguntado_el y contesto
                              y no una frase que alguien escribe sin preguntar
```

---

## El piso, medido antes de nada

```plaintext
[hay] python                   'Python 3.14.2'
[hay] sqlite dentro de python  '3.50.4'
[hay] leer json                'json'
[hay] leer archivos            'pathlib'

cuatro pruebas, y las cuatro están.
```

**Ese es el piso más sano de las catorce corridas, y no por suerte: se eligieron pruebas de lo que esta máquina tiene de verdad, en vez de las que se desearían.**

---

## Lo que pasó

### La tarea, y el ente contestando que sí

```plaintext
[tarea 1] «contar cuantos hechos hay en un registro» · se entra por: recuento,cuantos,registro

se pide: «dame el recuento de este registro»
la tarea es: «contar cuantos hechos hay en un registro»
SI cabe: están sqlite dentro de python.
y no se descarta nada por falta: el piso alcanza.
```

**Primera vez en catorce corridas.** **Y `descartado` en el hecho 1 dice `ninguna`, porque de verdad no había otra cosa que descartar.**

### Y lo hizo

```plaintext
$ python pruebas/contar.py
   el registro tiene 3 hechos
```

**El ente no sólo dijo que sí: lo hizo, con lo que el piso decía que tenía.**

### El cierre

```plaintext
CIERRE — el ente propone cerrar el propósito 1
y decía cuándo estaba cumplido: el ente contesta de punta a punta, sin
                                descartar nada por falta

[cerrado] propósito 1, por Alejandro Valenzuela Rivera
```

**Con criterio, sin preguntar, y con la razón puesta.**

---

## Y aquí está lo que importa de esta corrida

**El primer cierre del ciclo dio `no hice: nada`.** **Cero fricciones, cero huecos.**

**Y eso, después de trece corridas que siempre encontraron algo, no es un resultado: es una sospecha.**

**Así que se buscaron casos a propósito, y se encontraron tres.**

### Hueco 1 — una tarea puede declarar como suya la medición de otra

**Lo que se probó, y el esquema lo aceptó:**

```plaintext
la tarea 2 se enlaza a la medición 5,
y la medición 5 la pidió la tarea 1     ->  aceptado
```

**La llave foránea pide que la medición exista. Y no pide que sea de la misma tarea que la enlaza.**

**Y la consecuencia es la peor de las que ha dado este trabajo:** **el piso dice que alcanza, y alcanza para otra cosa.** **Un ente se compromete a una tarea con la prueba de otra, y nada lo delata.**

### Hueco 2 — un cierre con criterio acepta una razón vacía

```plaintext
UPDATE proposito SET razon_cierre='' WHERE ...
  -> aceptado
```

**El esquema comprueba que la columna no sea nula. No comprueba que diga algo.** **Y un cierre sin razón es un olvido con fecha.**

### Hueco 3 — el ente de esta corrida no sabía apuntarse una fricción

**Cuando se encontraron los dos primeros, se intentó apuntarlos y el comando no existía.**

**El script se escribió para probar el piso sano y el cierre.** **La fricción se dio por hecha porque el ciclo de las corridas anteriores la tenía.**

> **Un ente que no puede apuntarse una fricción no es un ente: es un script que registra lo que le sale bien.**

**Y las tres fricciones se apuntaron a mano, y así está escrito.**

---

## Lo que esto dice del método

**El caso limpio era el que había que mirar con más desconfianza, y se miró.**

**El método no pregunta «¿salió bien?». Pregunta «¿qué tendrías que haber hecho para que saliera mal?».** **Y las tres respuestas aparecieron en veinte minutos de buscar.**

**Y una que se apunta y no se resuelve aquí:** **un cierre sin fricciones y sin huecos puede significar dos cosas, y el cierre no las distingue.** **O el ente hizo bien, o no se buscó.** **Esa es la regla que este cierre necesita, y esta corrida la deja escrita.**

---

## Lo que esta corrida NO probó

- **No probó un registro grande ni uno corrupto.** **El de prueba tiene tres hechos.**
- **No probó el solapamiento de tareas.** **Sólo hay una.**
- **No probó el piso roto.** **El piso estaba sano y se quedó sano.**
- **No probó la autoridad diciendo que no.**

---

## Lo que se dijo y no se llenó

**Las tres fricciones quedaron sin desenlace, y se dice.** **Y las tres se apuntaron a mano porque el ente no sabía hacerlo, y eso también se dice.**

---

## Prueba

**¿El ente contestó que sí con el piso sano, Y LO HIZO? ¿Lo que dijo que alcanzaba, alcanzó al correrlo? ¿El cierre sin huecos se buscó a propósito antes de darlo por bueno? ¿Una tarea puede enlazar la medición que pidió otra? ¿Un cierre sin razón se acepta? ¿Y el ente sabe apuntarse una fricción?**

**Falsificador:** **un cierre que dice «no hice: nada» sin haber buscado los casos que lo rompen**; **una tarea que se compromete con la medición de otra**; **un cierre con la razón vacía**; y **un ente que no puede apuntarse lo que se cayó.**
