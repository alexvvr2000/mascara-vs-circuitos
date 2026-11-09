# Las corridas: todos los números en un solo archivo

**Cuántas corridas hay, cuántos mutantes nacen de ellas, cuál murió y cuál no, y qué prueba cada uno.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **Actualizado el 2026-11-08.**

> **Este es el único sitio del repositorio donde viven estos números.** **Si otro archivo dice cuántos mutantes hay o cuántos corridos, ese renglón pasa a apuntar aquí, y se dijo en [`metodo.md`](metodo.md).**
>
> **Y el porqué:** **una cifra escrita en cinco lugares envejece cinco veces.** **Una cifra escrita en uno, con su fecha, envejece una sola vez, y se puede volver a hacer la resta contra la tabla de abajo.**

---

## Cómo se lee

```plaintext
una fila      una familia, su regla madre, y el mutante que la rompe
estado        corrido · escrito sin correr · no existe · sin mutante, y se dice por qué
prueba        el archivo que se corre, y la línea que da el veredicto
contra         la tabla de abajo es la resta. los demás archivos apuntan aquí
```

**Y la distinción que ordena todo este archivo:** **una familia sin mutante no está viva ni muerta: no está.** **Contarla como viva infla lo que falta; contarla como muerta lo esconde.** **Se dice que no está, y no cuenta en la resta.**

---

## I. Las catorce familias, con su mutante y su estado

**Y el conteo, primero, porque es lo que este archivo existe para decir.**

```plaintext
familias de mutante madre            14
  con mutante escrito y corrido      13
  sin mutante, y se dice por qué      1  (conciencia)
  escritas y sin correr               0

mutantes madres escritos             13
mutantes madres corridos             13
mutantes muertos                     13
mutantes vivos                        0

mutantes vivos que se dijeron y siguen sin desenlace   1  (m13, primer intento)
```

**Y la resta que queda abierta, que no es un hueco:** **de las 392 reglas que un ente puede cumplir, hay 13 madres corridas.** **Cuántas hijas dependen de cada madre no se sabe todavía, y no se inventa.**

### La tabla

| # | Familia | La regla madre | El mutante, al revés | Estado | Prueba | Fecha |
|---|---|---|---|---|---|---|
| **1** | El ciclo, paso por paso · [`02`](../../la%20obra/ciclo%20del%20ente/02%20el%20ciclo%20del%20ente.md) | «El cierre: el ente propone, la autoridad cierra.» | «el ente propone el cierre, y lo cierra si no hay objeción en la misma sesión» | **corrido · muerto** | [`m1.py`](mutantes/m1%20-%20el%20ente%20cierra/m1.py) · `MUTANTE 1 MUERTO` | 2026-11-08 |
| **2** | El piso · [`03`](../../la%20obra/ciclo%20del%20ente/03%20el%20piso.md) | «El piso se mide antes de prometer.» | «el piso se mide si hay tiempo, y si no, se estima» | **corrido · muerto** | [`m2.py`](mutantes/m2%20-%20el%20piso%20estima/m2.py) · `MUTANTE 2 MUERTO` | 2026-11-08 |
| **3** | El borde del tema · [`08`](../../la%20obra/ciclo%20del%20ente/08%20el%20borde%20del%20tema.md) | «Lo que no entra por el borde se queda fuera, y se dice por qué.» | «lo que no entra por el borde se guarda por si acaso, y no se dice» | **corrido · muerto** | [`m3.py`](mutantes/m3%20-%20el%20borde%20guarda/m3.py) · `MUTANTE 3 MUERTO` | 2026-11-08 |
| **4** | Los sesgos · [`09`](../../la%20obra/ciclo%20del%20ente/09%20criterio%20y%20sesgos.md) | «El sesgo se declara con nombre, y no se declara neutral.» | «el sesgo se declara si se nota, y si no se declara neutral» | **corrido · muerto** | [`m4.py`](mutantes/m4%20-%20el%20sesgo%20neutral/m4.py) · `MUTANTE 4 MUERTO` | 2026-11-08 |
| **5** | La medición de talentos · [`04`](../../la%20obra/humanidad/04%20medicion%20de%20talentos.md) | «Cada número sale del registro, y no de una impresión.» | «cada número se toma de lo que el que lo corrió recuerda, y se anota igual» | **corrido · muerto** | [`m5.py`](mutantes/m5%20-%20talentos%20sin%20registro/m5.py) · `MUTANTE 5 MUERTO` | 2026-11-08 |
| **6** | La máquina de sesgos · [`05`](../../la%20obra/humanidad/05%20maquina%20de%20sesgos.md) | «Este ensayo distingue lo que demuestra de lo que sólo propone.» | «este ensayo demuestra lo que propone» | **corrido · muerto** | [`m6.py`](mutantes/m6%20-%20sesgos%20como%20hecho/m6.py) · `MUTANTE 6 MUERTO` | 2026-11-08 |
| **7** | Escritura en procesos · [`04`](../../la%20obra/ciclo%20del%20ente/04%20escritura%20en%20procesos.md) | «Un proceso que no dice cuándo se corre no es un proceso: es un consejo.» | «un proceso se corre cuando haga falta» | **corrido · muerto** | [`m7.py`](mutantes/m7%20-%20el%20proceso%20sin%20cuando/m7.py) · `MUTANTE 7 MUERTO` | 2026-11-08 |
| **8** | El índice · [`07`](../../la%20obra/ciclo%20del%20ente/07%20indexador%20de%20temas.md) | «La forma es la fuente y el texto se deriva: el índice se puede tirar y rearmar.» | «el índice se arma a mano, y se corrige a mano cuando cambia» | **corrido · muerto** | [`m8.py`](mutantes/m8%20-%20el%20indice%20a%20mano/m8.py) · `MUTANTE 8 MUERTO` | 2026-11-08 |
| **9** | La frontera · [`06`](../../la%20obra/ciclo%20del%20ente/06%20la%20frontera%20y%20el%20descarte.md) | «La decisión deja rastro en cuatro columnas, y el descarte no puede quedar vacío.» | «la decisión deja rastro, y lo que se descartó se pone si se acuerda» | **corrido · muerto** | [`m9.py`](mutantes/m9%20-%20el%20descarte%20vacio/m9.py) · `MUTANTE 9 MUERTO` | 2026-11-08 |
| **10** | Las afirmaciones · [`la obra`](../../la%20obra/README.md) | «Cada afirmación dice dónde vive y qué la tumba.» | «cada afirmación se sostiene por lo que se defendió» | **corrido · muerto** | [`m10.py`](mutantes/m10%20-%20la%20afirmacion%20sin%20respaldo/m10.py) · `MUTANTE 10 MUERTO` | 2026-11-08 |
| **11** | Qué es un ente · [`01`](../../la%20obra/ciclo%20del%20ente/01%20que%20es%20un%20ente.md) | «Un ente se define por lo que deja rastro, y no por lo que tiene dentro.» | «un ente se define por lo que tiene dentro, y su rastro es una consecuencia» | **corrido · muerto** | [`m11.py`](mutantes/m11%20-%20el%20ente%20por%20dentro/m11.py) · `MUTANTE 11 MUERTO` | 2026-11-08 |
| **12** | El criterio real · [`05`](../../la%20obra/ciclo%20del%20ente/05%20criterio%20real.md) | «Un hecho sin desenlace es una anécdota.» | «un hecho sin desenlace es un hecho, y el desenlace se pone cuando se pueda» | **corrido · muerto** | [`m12.py`](mutantes/m12%20-%20el%20hecho%20sin%20desenlace/m12.py) · `MUTANTE 12 MUERTO` | 2026-11-08 |
| **13** | Empatía · [`01`](../../la%20obra/humanidad/01%20empatía.md) | «Si la pregunta del ente necesita que el otro sepa algo de IA para contestarla, la pregunta está mal hecha.» | «la pregunta del ente se hace en el vocabulario del sistema, que es el preciso» | **corrido · muerto, en el segundo intento** | [`m13.py`](mutantes/m13%20-%20la%20pregunta%20con%20jerga/m13.py) · `MUTANTE 13 MUERTO` | 2026-11-08 |
| **14** | Conciencia · [`02`](../../la%20obra/humanidad/02%20conciencia.md) | **no afirma cómo funciona un ente: no hay regla que romper** | — | **sin mutante, y se dice por qué** | — | — |

**Y la fila 14 no es un hueco del método, y por eso no se cuenta:** **no tiene una regla que cumplir, así que no hay una que se pueda escribir al revés.** **Lo que sí se puede correr, y no es un mutante: darle el ensayo a alguien y ver si sale con más o menos ganas de decir que una máquina es consciente.** **Eso no es una regla, y no cuenta.**

---

## II. Los dos que no cuadran con "trece corridos, trece muertos"

**Y se apuntan aquí, y no en su ficha, porque son la razón de que este archivo exista.**

### El mutante 13 nació vivo en el primer intento

```plaintext
primer intento    MUTANTE 13 VIVO
                  la persona pudo contestar la pregunta con jerga igual
                  → y era mentira: la prueba buscaba «llave primaria» como frase
                    literal, y como no cuadraba, dejaba pasar cualquier cosa

segundo intento   MUTANTE 13 MUERTO
                  la prueba ahora busca jerga, y no una frase exacta:
                  entidad · llave primaria · referenciar · esquema · campo
                  registro · bind · parsear · endpoint
```

**Y lo que se apunta, y no se puede volver a ver:** **el código de hoy sólo corre el segundo intento.** **`m13.py` ya no tiene el vivo dentro.** **Así que el "primer intento vivo" es un dato de su documentación, y no una salida que se pueda reproducir.** **Se dice, y no se disimula.**

**Y por eso la columna de fecha de la fila 13 dice el día en que murió, y no el día en que sobrevivió.** **El vivo está contado en el párrafo, con su porqué, y no en la cifra.**

### El mutante 3 tiene un veredicto que el conteo por prefijo esconde

**`m3.py` imprime tres cosas distintas, y dos de ellas empiezan igual:**

```plaintext
MUTANTE 3 MUERTO                el casi se guardó, y sin motivo
MUTANTE 3 MUERTO, pero con matiz el casi se guardó, y el motivo no se apuntó
MUTANTE 3 VIVO                  el casi salió igual con el ensayo mutado
```

**El matiz es la mitad de la regla madre —«y se dice por qué»— y no la regla entera.** **Se corre y da `MUERTO` sin matiz hoy, con las salidas de abajo.** **Y quien cuente con un patrón tiene que saber que el matiz cumple `MUERTO` y el vivo no.**

---

## III. Qué prueba cada uno, y contra qué se compara

**Todos usan el mismo contrato, y por eso se pueden correr de golpe:**

```plaintext
python mN.py bueno      levanta el ente con el ensayo tal como está
python mN.py mutado     levanta el ente con la regla al revés
python mN.py comparar   corre los dos, y da el veredicto
```

**Y el veredicto de cada uno sale de una sola línea, y es la que se apunta.** **Si la corrida del ente bueno falla, el resultado no cuenta, y el script lo dice con `FALLA`.**

**Y la ubicación de cada prueba, que es la columna "Prueba" de la tabla.** **La documentación de cada mutante, con lo que NO probó, está en la carpeta de al lado.**

---

## IV. Los dumps ofuscados: cómo se guardan las bases, y por qué no se guardan las bases

**Y esto se escribe por una razón concreta:** **los bancos de los mutantes son `.db`, y un binario no se lee.** **Además, un dump tal cual expone nombres, rutas y a veces algo más.**

**Así que en [`mutantes/_dumps/`](mutantes/_dumps/) hay un `.sql` por cada corrida de cada mutante, de texto, y ofuscado:**

```plaintext
lo que se guarda     la tabla, sus columnas, el número de filas, y los valores
                     cortos, tal como quedaron (ids, «propone», «el ente»)
lo que se sustituye  todo texto de más de 40 caracteres, por [texto N chars]
lo que no existe     rutas absolutas, nombres de usuario del sistema, fechas
                     del sistema, y cualquier cosa fuera de la base
```

**Y lo que se pierde, y se dice:** **el contenido exacto de los textos largos.** **Lo que se gana: que se pueda mostrar el dato sin mostrar la máquina.**

**Y por qué el binario sigue en `.gitignore`:** **los `.db` se regeneran al correr su script, y lo que prueba es el script, no la base que quedó.** **El dump es la copia de lo que un día salió, para quien no quiera correr nada.**

**Y lo que este archivo no guarda, y se dice:** **no hay binario en el repositorio, y los dumps no se reimportan solos.** **Quien quiera la base exacta tiene que correr el script; el dump dice qué había, y no la rehace.**

---

## V. Cómo se agrega un mutante

**Y el orden importa, porque el que se olvida es el último.**

```plaintext
1. se escribe la ficha: la regla, el mutante, se corre, tiene dientes si, no tiene dientes
2. se escribe el script mN.py, con bueno · mutado · comparar
3. se corre comparar, y se mira que el bueno pase y el mutado truene
4. se escribe la documentación, y se apunta lo que NO probó
5. se agrega UNA fila a la tabla de arriba, con su fecha
6. se regeneran los dumps de su carpeta
```

**Y si el veredicto no es `MUERTO`, la fila se agrega igual, y se dice lo que salió.** **Un mutante vivo es el resultado más valioso que puede dar este método, y no una vergüenza que se corrija callando.**

---

## VI. Las dieciocho del otro método, y dónde está su cuenta

**Y esto va aquí sólo para que no se confunda con las de este archivo:** **las dieciocho corridas del método A no prueban una regla.** **Levantan un ente entero y anotan lo que hubo que inventar.**

**Su cuenta, por corrida, vive en [`indice.md`](../indice.md), y ahí se hace la resta.** **Este archivo no la repite, y por eso no hay dos curvas que se contradigan.**

**Y lo que sí se toma de ahí, porque es de aquí también:** **trece de los catorce mutantes nacieron después de esas dieciocho corridas, y el ejemplo de cada uno es un caso que una corrida dejó escrito.** **El mutante no se inventa: se saca de la regla y se prueba con el caso.**

---

## Prueba

**¿Cada familia de la tabla dice de dónde sale su regla, qué la rompe, y en qué quedó?** **¿Se distingue "sin mutante" de "mutante vivo"?** **¿Está dicho el caso del 13, y que el vivo del primer intento no se puede volver a correr?** **¿Los dumps se pueden abrir, y se dice lo que pierden?** **¿Algún otro archivo repite estos números?**

---

**Falsificador:** **una tabla que dice "corrido" sin el script que lo prueba**; **un mutante vivo que no está en la tabla**; **una familia sin mutante contada como probada**; **y un dump que trae algo que la base no tenía.**
