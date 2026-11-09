# Método A · Llenar los huecos

**Cómo se sabe qué le falta a los ensayos, y cuándo se deja de buscar.**

**Alejandro Valenzuela Rivera · `TESTIGO`.**

---

## Qué es este método, y qué no

**Es el que encuentra lo que el ensayo no dice.** **Se levanta un ente entero con los ensayos, se corre, y lo que hubo que inventar es el hueco.**

**Y no es el que dice si lo que el ensayo dice se sostiene.** **Ése es el [método B](../sostiene/README.md): se rompe una regla a propósito y se mira si la corrida lo nota.**

**Los dos hacen falta, y por razones distintas, y está escrito en [`cómo se corre`](como%20se%20corre.md):** **los mutantes sólo prueban reglas que están escritas; la corrida entera encuentra lo que falta y no está escrito.**

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

```plaintext
el proceso no termina       cada generación sigue desde la anterior
lo que sí termina           lo que una generación necesita para empezar
y eso se puede decir        y se puede tocar, y se ve cuando está
```

---

## Qué es el piso mínimo, en concreto

```plaintext
lo que hay        las cuatro piezas, el ciclo del ensayo 02, un registro de
                  hecho · fricción · desenlace, los ensayos escritos, y
                  las corridas que se puedan abrir

lo que falta      que el que sabe menos pueda empezar. eso no se prueba
                  con más escritura: se prueba con alguien

y lo que NO falta el final. el final no hace falta para empezar
```

**El mínimo no es el número de reglas.** **El mínimo es lo que hace falta para que otra persona levante un ente y produzca algo.**

**Y eso puede ser mucho menos de lo que la cuenta sugiere.** **Puede ser una página, con las cuatro piezas y un ejemplo.**

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

## III. Por qué hay un número, y por qué no es una cuenta

**En las fórmulas se usa el infinito, y el infinito no está en la fórmula: es la tendencia.** **Nadie escribe todas las cifras de un número que no termina; se escribe lo que sigue, y con eso ya se puede trabajar.**

**Con la descripción de un ente pasa lo mismo.** **No hay un día en que un ensayo diga todo lo que hay que decir sobre un ente.**

**Lo que sí termina es la lista de lo que el ensayo afirma, y cada cosa que afirma se puede romper a propósito.** **Pero eso es el otro método: el [B](../sostiene/README.md).**

**Y este método no cuenta reglas.** **Cuenta huecos encontrados, y eso se puede contar porque cada uno tiene su corrida.**

---

## IV. Cómo se hace

**Está entero en [`cómo se corre`](como%20se%20corre.md), y es el método de este lado de la línea.** **Aquí sólo lo que no se repite allí:**

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

## V. Lo que este método no prueba, y se cita

> **«Las pruebas pueden revelar la presencia de defectos, pero nunca su ausencia.»**
> — Dijkstra, *Notes on Structured Programming*, EWD249, 1970.

**Un hueco cerrado dice que ese ya no está.** **No dice que no haya otros.** **Y por eso este método no se para solo: la otra mitad está en el [B](../sostiene/README.md).**

---

## VI. Cuándo se deja de correr

**La regla vieja era «dos corridas enteras seguidas que no encuentren nada más que detalle».** **Y esa regla se queda, y es la de este método, pero no la primera.**

**Porque esperar a que no aparezca nada es esperar a que el que ya sabe dónde no buscar no busque.**

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

**¿Cada hueco encontrado tiene su corrida y su registro? ¿Se puede abrir el ente de una corrida vieja y correrlo? ¿Se distingue un hueco del ensayo de un defecto del código o del entorno? ¿Y hay alguna corrida que dijera «no encontré nada» con las trampas puestas?**

---

**Falsificador:** **«lo suficientemente bueno» dicho por quien lo hizo, y sin que nadie lo haya empezado**; **y su contrario: seguir puliendo para siempre porque siempre aparece un detalle más.**
