# Método A · Llenar los huecos

**Cómo se sabe qué le falta a los ensayos, y cuándo se deja de buscar.**

**Alejandro Valenzuela Rivera · `TESTIGO`.**

---

## Qué es este método, y qué no

**Es el que encuentra lo que el ensayo no dice.** **Se levanta un ente entero con los ensayos, se corre, y lo que hubo que inventar es el hueco.**

**Y no es el que dice si lo que el ensayo dice se sostiene.** **Ése es el [método B](../sostiene/README.md): se cambia una regla del ensayo, se levanta el ente con el ensayo cambiado, y se mira si la corrida lo nota.**

**Los dos hacen falta, y por razones distintas:** **los mutantes sólo prueban reglas que están escritas; la corrida entera encuentra lo que falta y no está escrito.**

---

## Las dieciocho corridas son todas de este método

**Y esto se escribe porque se buscó lo contrario y no está.**

**Se revisó el historial de git, corrida por corrida, con su commit y su fecha.** **Y después se abrieron las dieciocho documentaciones.** **Y todas dicen lo mismo: qué se intentaba, qué se levantó, y qué hubo que inventar.**

**Ninguna de las dieciocho levanta un ente con el ensayo cambiado.** **Un mutante es otra cosa, y vive en [`sostiene/mutantes/`](../sostiene/mutantes/).**

**Y hay cuatro que además buscaron el caso que rompe** —**la 07, la 11, la 14 y la 15**— **, y no por eso dejan de ser de este método:** **lo buscaron con el mismo ente, y después de que el ciclo saliera limpio.**

**Lo dice la 14 con estas palabras:** **«el primer cierre del ciclo dio `no hice: nada`. Y eso, después de trece corridas que siempre encontraron algo, no es un resultado: es una sospecha. Así que se buscaron casos a propósito, y se encontraron tres.»**

**Así que no se parte la carpeta.** **Partirla habría inventado una distinción que no está en ningún archivo, y `sostiene/` tiene su propio registro.**

---

## Cómo se lee una corrida, y qué guarda

**Cada carpeta conserva lo que la hace revisable, y ya no guarda lo que no se puede leer:**

```plaintext
documentacion.md      qué se intentaba, qué pasó, los huecos, y qué no se probó
banco_esquema.sql     el esquema con el que corrió, en texto
banco_filas.sql       lo que quedó escrito en ese esquema, fila por fila, en texto
pruebas/              los archivos de entrada que la corrida usó, si los tuvo
```

**Y dos cosas se fueron, y se dice por qué:**

```plaintext
herramientas/   los scripts y el AGENTS de cada corrida. se fueron porque cada
                corrida tenía su copia, y las dieciocho no coinciden: leer una
                y creer que es la puerta de todas es peor que no tener ninguna

banco.db        el binario. ahora es dos archivos de texto que se pueden abrir,
                comparar, y volver a cargar en cualquier motor
```

**Los nombres de los archivos de una corrida no están escritos en ningún archivo, y se vio al chequear las dieciocho:** **la 01 y la 02 dicen en su documentación cuántas tablas tiene su esquema, y no las nombran; la 16 trae sus filas en `insert into tabla (id, …)`, y las demás en `insert into tabla values (…)`, que depende del orden en que el esquema declaró las columnas.** **Es de la época, y no se corrige: se dice, para que quien copie una no crea que las dieciocho se escribieron a la vez.**

**Y hay dos más que un lector no puede prever y ahora se dice aquí:**

```plaintext
las pruebas/ de la 03, 06 y 07     traen los casos de entrada, y su
                                   documentación no los nombra uno por uno.
                                   se entiende al leerlos, y hay que abrirlos

16 - NUNCA SE BORRA                su banco_filas.sql trae el supuesto 3
                                   apuntando a un hecho 999 que no existe, y
                                   es a propósito: es el caso que la corrida
                                   vino a probar. la documentación lo dice
                                   [OK] rechaza un hecho 999, porque en esa
                                   corrida el esquema lo rechazó con las
                                   llaves prendidas. recargar las filas con
                                   foreign_keys=OFF lo acepta, y eso es lo
                                   que la corrida 16 denunció
```

---

**Falsificador de este README:** **una corrida que se presentó como recargable y no lo está**; **y uno que copia los casos de `pruebas/` como si fueran los del banco, cuando son la entrada y no la salida.**


---

## I. La meta: lo suficientemente bueno

**Durante un tiempo se formuló la meta como «tratar de describir un ente hasta que esté completo», y con eso se cayó en la trampa de la tendencia:** **buscar el valor al que converge algo que no termina.**

**La trampa tiene nombre y está resuelta en [`lo inexplicable`](../lo%20inexplicable.md):** **que algo no se pueda probar hasta el final no lo vuelve inútil.** **Lo que hay que encontrar no es el final: es el punto donde algo sirve.**

**Y ese punto tiene nombre, y es el que usa todo el que hace herramientas: lo suficientemente bueno.**

> **Que alguien que sabe menos pueda empezar a trabajar con esto, y que el que sabe más pueda seguir desde donde el primero dejó.**

**Y las dos mitades son necesarias:**

```plaintext
si el que sabe menos no puede empezar     → no hay piso
si el que sabe más no puede seguir        → no hay techo, y el trabajo se cierra
```

**Y esto no es un final, y eso no es un defecto:** **la solución final va a tener huecos, no porque el trabajo esté mal, sino porque un ente vive en un mundo que cambia y la descripción se queda.**

---

## Qué es el piso mínimo, en concreto

```plaintext
lo que hay        las cuatro piezas, los ensayos escritos, y las corridas que
                  se pueden abrir y volver a cargar

lo que falta      que el que sabe menos pueda empezar. eso no se prueba
                  con más escritura: se prueba con alguien

y lo que NO falta el final. el final no hace falta para empezar
```

**El mínimo no es el número de reglas.** **El mínimo es lo que hace falta para que otra persona levante un ente y produzca algo.**

---

## Y la línea que impide que esto se vuelva una excusa

```plaintext
lo que NO es lo suficientemente bueno
  lo que se puede empezar a usar, pero nadie lo empezó, y no se sabe por qué

lo que SÍ es
  lo que se puede empezar a usar, alguien lo empezó, y dijo dónde falló
```

**La diferencia es una sola: alguien lo intentó y volvió con lo que se rompió.** **Y sin eso, «lo suficientemente bueno» es una opinión.**

---

## Lo que este método NO dice

- **No dice que el piso ya esté puesto.** **Dice qué lo definiría, y que eso no se sabe desde adentro.**
- **No fija un número de corridas.** **Ésas son el trabajo, y no la meta.**
- **Y no afirma que la solución final vaya a ser buena.** **Afirma que va a tener huecos, y que eso está previsto y dicho.**

---

## II. El problema, en una línea

**La regla vieja era «dos corridas enteras seguidas que no encuentren nada más que detalle».** **Eso es esperar a que no aparezca nada, y no aparece nada cuando el que busca es el mismo que ya sabe dónde no buscar.**

**Y tiene un nombre, y se cita abajo: saturación.** **Es un criterio real, y es el débil.**

---

## III. Cómo se hace

**Está entero en [`cómo se corre`](como%20se%20corre.md).** **Aquí sólo lo que no se repite allí:**

```plaintext
1. se leen los ensayos          sin mirar los entes anteriores
2. se levanta un ente ENTERO    en una carpeta nueva, con fecha
3. se corre de punta a punta    ningún paso se salta
4. se anota lo que hubo que inventar   cada invención es un hueco
5. se clasifica                 del ensayo / del código / del entorno
6. se escribe la documentación  con la voz del que corrió
7. se cierra el hueco           en el ensayo, y se repite desde el 1
```

> **Y la regla que la hace servir:** **lo que se inventa es del ensayo, no de lo que se levantó.**

---

## IV. Lo que este método no prueba, y se cita

> **«Las pruebas pueden revelar la presencia de defectos, pero nunca su ausencia.»**
> — Dijkstra, *Notes on Structured Programming*, EWD249, 1970.

**Un hueco cerrado dice que ese ya no está.** **No dice que no haya otros.** **Y por eso este método no se para solo: la otra mitad está en el [B](../sostiene/README.md).**

---

## V. Cuándo se deja de correr

**La regla vieja era «dos corridas enteras seguidas que no encuentren nada más que detalle».** **Y esa regla se queda, y es la de este método, pero no la primera.**

**Y la primera, que es la de este método, es más simple:**

> **Se acaba cuando el ente se puede levantar con los ensayos y no hay que preguntar nada.**

**Y sus cuatro condiciones, que no incluyen «no encontré nada»:**

```plaintext
1. una corrida con las trampas puestas a propósito
   —el casi, el doble tema, el propósito sin motivo, la autoridad que
   no contesta— y ninguno se rompió. Una corrida dócil no cuenta

2. la prueba doble: el ente viejo y el nuevo, con el mismo caso
   y que el nuevo no pierda nada del viejo

3. un falsificador de los ensayos, cumplido a propósito
   se cumple uno, y el ensayo no se cae

4. ¿el dueño podría levantar un ente con estos ensayos, sin buscar?
```

**Y la última es la que importa, y no se mide con instrumentos.**

---

## De dónde salió esto

| Lo que este método afirma | De dónde viene |
|---|---|
| las pruebas revelan la presencia de defectos, nunca su ausencia | **Dijkstra, EWD249 (1970)** |
| la saturación es el punto en que los datos nuevos no dicen nada nuevo | investigación cualitativa; Glaser & Strauss (1967) |
| una revisión no sustituye a una corrida | las corridas 14 y 15, que encontraron más buscando después de que todo salió bien |

---

## Prueba

**¿Cada hueco encontrado tiene su corrida y su registro? ¿Se puede abrir el esquema y las filas de una corrida vieja y volver a cargarlos? ¿Se distingue un hueco del ensayo de un defecto del código o del entorno? ¿Y hay alguna corrida que dijera «no encontré nada» con las trampas puestas?**

---

**Falsificador:** **«lo suficientemente bueno» dicho por quien lo hizo, y sin que nadie lo haya empezado**; **y su contrario: seguir puliendo para siempre porque siempre aparece un detalle más.**
