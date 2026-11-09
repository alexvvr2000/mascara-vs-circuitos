# Cómo se corre una corrida, paso por paso

**Los comandos, el orden, y lo que se escribe en cada momento.**

**Alejandro Valenzuela Rivera · el ente.** **Escrito el 2026-11-08.**

---

## Antes de escribir nada

**1. Medir el piso de la máquina, no el que se recuerda.**

```plaintext
python --version
git --version
python -c "import sqlite3; print(sqlite3.sqlite_version)"
python -c "import pypdf"
```

**Lo que salga, no lo que se cree.** **Y si algo de eso se va a usar en la corrida, se apunta con su salida.**

**2. Decir el blanco antes de empezar, y escribirlo.**

**Una corrida sin blanco es un diario.** **El blanco sale de lo que la corrida anterior dejó abierto, y si no hay nada abierto, de un caso que ningún ensayo tocó.**

**3. Decir cuánto va a durar, en pasos.** **Sin esto, la corrida se estira hasta que se acaba el tiempo.**

---

## Levantar el ente

**4. Carpeta nueva: `corridas/ente N - NOMBRE/`**, con `ente/` y `documentacion.md`.** **Ente nuevo desde cero: no se corrige el anterior, porque el anterior ya tiene las piezas que se inventaron la vez pasada.**

**5. Escribir `tablas.sql` con el ciclo entero**, y el orden importa:

```plaintext
autoridad · ente · modelo · proposito · rechazo
tarea · piso · piso_roto · tarea_pieza
tema · tema_relacion · pieza
hecho · supuesto · friccion · desenlace
```

**Y las vistas: `piso_vigente` (con `id`, porque romper el piso es escribir sobre él) y, si hay correcciones, `hecho_vigente` y `cadena`.**

**6. Escribir el script con un comando por paso.** **No un comando que hace todo: uno por paso.** **Si un paso no se corre, se ve, porque la base queda sin su registro.**

```plaintext
crear | paso0 | paso0a | medir | pide | alcanza | aprende
supuesto | rompe | hecho | corrige | cadena
propone-cierre | cierra | rechaza | vuelve
estado | cerrar
```

**7. Probar que el esquema rechaza lo que debe, ANTES de correrlo.**

**Y aquí van tres pruebas que se aprendieron a golpes:**

```plaintext
con las llaves foráneas PRENDIDAS, y también con ellas APAGADAS
la prueba tiene que tener algo que probar (un DELETE que no borra
  nada no prueba nada)
y el mensaje del rechazo tiene que ser del ensayo, no del motor
```

**Si el esquema rechaza pero el mensaje dice `FOREIGN KEY constraint failed`, el mensaje no sirve: el que lo lea no va a saber qué regla del ensayo se rompió.**

---

## Correr

**8. El ciclo entero, en orden, sin saltarse ninguno.**

```plaintext
paso 0    las cuatro piezas, y en el acto mirar si faltan
paso 0a   el cuerpo, DECLARADO y no deducido
paso 0d   el piso, medido con pruebas que nombran su herramienta
          la tarea, declarada ANTES de su enlace
          el enlace, y su prueba tiene que ser de esa misma tarea
paso 0b   lo que se entendió, y el supuesto con su estado
paso 1    la frase literal, y el origen declarado antes de contestar
paso 2    el índice: primero el hueco, y después el tema con su borde
paso 3    la decisión, y lo que se descartó, escrito
paso 4    la respuesta, y su frontera
paso 5    el hecho, con pieza, tema, tarea, propósito, cuerpo y piso
paso 6    la corrección, y su desenlace
cierre    el ente propone, y la autoridad contesta
vuelta    lo apuntado regresa al índice y a la autoridad
```

**9. Y buscar a propósito ANTES de cerrar.**

**Esto no es opcional, y es lo que más ha encontrado.** **Las corridas 14 y 15 salieron de ahí, y sus huecos eran peores que los de las corridas que fallaron solas.**

**La forma:** **preguntarse qué tendría que pasar para que el esquema aceptara lo que no debe, y probarlo.** **Y antes de decir «se acepta», comprobar que había algo que aceptar.**

---

## Cerrar

**10. Clasificar cada hallazgo en el acto, no al final.**

```plaintext
el ensayo no dice algo            →  al ensayo
el ensayo lo dice y el esquema    →  al ensayo igual, porque el esquema
  no lo puede guardar                 es una implementación posible, no la única
el defecto es del script          →  a la documentación de la corrida
el defecto es del entorno         →  a la documentación, y NO se toca el ensayo
lo que necesita nombrar una       →  a la documentación: es del stack
  herramienta
```

**11. Escribir `documentacion.md` con seis renglones, y en este orden:**

```plaintext
el blanco, dicho antes de escribir
lo que se intentaba
lo que pasó, paso por paso, con las salidas literales
los huecos, con su nombre y su regla
lo que esta corrida NO probó
lo que no se llenó, y se dice
y el Falsificador, al final
```

**12. Llevar cada hallazgo a su ensayo, y decir en qué sección.**

**Y si el hallazgo es una regla de cómo se corre el ejercicio, va al método, con puntero.** **Pero eso es la excepción: el producto son los ensayos.**

**13. Actualizar los números:** la serie de huecos, la tabla del readme, y el estado del método.

---

## Lo que no se hace

```plaintext
no se rellena un hueco para que la corrida se vea completa
no se achaca al ensayo un defecto del código o del entorno
no se cierra con «no hice: nada» sin haber buscado a propósito
no se dice «ya casi» ni «falta mucho»: se dice el número
no se corrige el ente anterior: se levanta otro
no se recorta la corrida: recortar es decidir dónde está el hueco
```

---

## Falsificador

**Una corrida que se puede contar sin haber quedado su salida en algún lado.** **Y su contrario: un procedimiento que dice «busca a propósito» sin decir qué buscar.**
