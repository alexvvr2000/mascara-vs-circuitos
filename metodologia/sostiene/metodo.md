# El método, con sus fuentes

**Qué se hace para saber si lo que estos ensayos afirman tiene dientes, con qué se hace, y de dónde salió cada pieza.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **Escrito el 2026-11-08.**

> **Este archivo unifica dos cosas que estaban partidas:** **el método B, que era cuatro archivos (`README.md`, `las reglas.md`, `los mutantes.md`, `corridas/`), y la mitad de ingeniería de software de `los papeles/estado del arte/`.** **Lo que el estado del arte decía repartido en once secciones, aquí está junto, con la regla a la que sirve.**
>
> **Y lo que este archivo no hace: no repite lo que vive en otro sitio.** **La cuenta de cuántos mutantes hay, y cuáles, está en [`corridas.md`](corridas.md).** **La qué dejó cada corrida del otro método está en [`indice.md`](../indice.md).** **El estado del arte completo, con lo que no se abrió, sigue en [`los papeles`](../../los%20papeles/estado%20del%20arte/README.md); este archivo lo enlaza y no lo copia.**
>
> **Y por qué hace falta un archivo aparte del otro método:** **los dos contestan preguntas distintas.** **El A, en [`huecos/`](../huecos/), encuentra lo que el ensayo no dice.** **El B, aquí, dice si lo que el ensayo sí dice aguanta.** **Los dos hacen falta, y no se mezclan: una corrida del A no es una corrida del B, aunque las dos se llamen corrida.**

---

## I. La regla que sostiene todo

**En vez de esperar a que no aparezcan defectos, se meten a propósito.**

**Se toma una regla del ensayo, se le cambia algo para que diga mal, se levanta el ente con el ensayo cambiado, y se corre.** **Si la corrida no lo nota, el ensayo no probaba esa regla.**

**Y la línea que lo sostiene, y es de la disciplina de mutación:**

> **Nunca confíes en una prueba que nunca has visto fallar.**

**Y lo que este método sí acaba, y el otro no puede:** **las reglas se acaban.** **Cuando cada una tiene su mutante muerto, este método ya no tiene nada que probar.** **El otro, en cambio, encuentra mientras siga habiendo un caso que no se escribió, y eso no tiene fondo conocido.**

### Las cuatro cosas que se sacan de ahí

```plaintext
la regla        una frase del ensayo, copiada tal como está
el mutante      la misma frase, con lo que la hace verdadera al revés
el ente mutado  un ente levantado con el ensayo cambiado, y nada más
el veredicto    murió (la corrida lo nota) o sobrevivió (la corrida pasa igual)
```

**Y un mutante que sobrevive no es un fracaso del ente: es un hueco con nombre y apellido.** **No hay que adivinar dónde falta: el mutante lo dice, en qué familia y en qué regla.**

---

## II. Cómo se corre, en cinco pasos

**Y son cinco y no cuatro, porque el paso 5 es el que se olvida y es el único que deja rastro.**

```plaintext
1. se saca la regla del ensayo, copiada, con el renglón de donde sale
2. se escribe el mutante: la misma regla con el predicado al revés,
   y se dice qué se espera que la corrida note y por qué
3. se levanta el ente con el ensayo mutado, en su carpeta, con el script
   que lo levanta, y el ente bueno al lado para tener contra qué comparar
4. se corre el ente mutado, y se mira:
     la corrida truena  →  el mutante murió, y la regla tiene dientes
     la corrida pasa    →  el mutante sobrevivió, y la regla no se probaba
5. se apunta el resultado en corridas.md, con su fecha y con la línea
   del script que lo prueba. sin el paso 5, el mutante corrió y no consta
```

### Por qué el paso 3 levanta el ente bueno también

**Porque un mutante que "muere" contra un ente que ya estaba roto no muere: choca con otra cosa.**

**La comparación es de dos, y las dos cosas se miran:**

```plaintext
el ente bueno corre y pasa            → el mutante tiene contra qué perder
el ente bueno corre y también falla   → no es un mutante: es un ente roto
                                         y el resultado no cuenta
el ente mutado truena                → el mutante murió, y la regla tiene dientes
el ente mutado pasa igual que el bueno → el mutante sobrevivió, y la regla no se probaba
```

**Y por eso cada mutante trae su script con los dos modos:** **`python mN.py bueno | mutado | comparar`.** **El modo `comparar` corre los dos y da el veredicto, y es el que se apunta.**

---

## III. Las dos clases de familia, y por qué se prueba una madre y no cada hija

**Las reglas de estos ensayos no están sueltas: se agrupan en familias, y cada familia tiene una madre.**

```plaintext
la madre   la regla de la familia, escrita en una línea
la hija    un caso de la madre, con una condición de más
el mutante madre   rompe la madre entera
el mutante hija    rompe un caso, y no la madre
```

**Y la relación entre los dos se llama inclusión, y viene de la jerarquía de criterios de flujo de datos:** **si la corrida mata al madre, ya mató a la hija.**

**Y por eso no se corre un mutante por regla, que serían cientos.** **Se corre el madre de cada familia, y lo que sobreviva se abre.**

### Las tres formas en que una hija está incluida en su madre

```plaintext
por ámbito     la hija rompe una parte del madre
               madre: se borra la regla entera del cierre
               hija:  se le quita solo «la autoridad»

por condición  la hija añade una condición que el madre no tiene
               madre: el piso dice «no hay» cuando falta la herramienta
               hija:  el piso dice «no hay» cuando falta la herramienta
                      y no hay red

por orden      la hija sólo puede ocurrir después del madre
               madre: el hecho apunta a un cuerpo que no existe
               hija:  el hecho apunta a un cuerpo que existe pero no es el suyo
```

**Y la inclusión dice una sola cosa:** **matar el madre mata a la hija.** **No dice lo contrario, y ésa es la trampa de la jerarquía:**

```plaintext
si el madre muere y la hija sobrevive   → la hija se corre igual, porque toca
                                          algo que el madre no toca
si el madre sobrevive                   → la hija se corre, porque el fallo
                                          está en algún caso y hay que saber cuál
```

**Y el aviso, que es del repositorio y no de la literatura:** **un mutante muerto por inclusión no se mató: se dio por muerto.** **La diferencia importa, y se apunta.**

```plaintext
corrido y muerto         es una prueba
muerto por inclusión     es una deducción, y depende de que la
                         inclusión esté bien calculada
```

**Y si alguien cree que A incluye a B y no lo hace, B queda sin probar y en el registro parece muerto.** **Por eso se apunta de qué otra regla depende cada mutante muerto por inclusión, y no sólo que murió.**

---

## IV. Cuándo se está terminado, y cuándo se para

### Lo que cuenta como terminado

```plaintext
cada regla de cada ensayo tiene su mutante
y el mutante muere
```

**Y esta meta es grande y larga, y hay que decirlo sin adornos:** **no es la que hace falta para publicar.** **Lo que sí se puede decir hoy, y es finito: lo que hay está escrito, y lo que sobreviva está nombrado.**

### Cuándo se para una tanda

```plaintext
una familia tiene su madre y su madre murió   → se cierra, y no se abre
una familia no tiene mutante, y se dice       → cuenta como sin probar, no como probada
una familia tiene mutante vivo                 → se abre en sus casos, uno por uno
```

**Y la regla de cierre, que es la del otro método y vale aquí también:** **dos tandas enteras seguidas que no encuentren nada más que detalle.** **Un mutante vivo es detalle mientras esté nombrado; deja de serlo cuando se calla.**

### Lo que no cuenta

```plaintext
un mutante escrito y creído corrido, sin su fila en corridas.md
un mutante muerto por una prueba que la primera vez dejaba pasar cualquier cosa
un mutante que "muere" contra un ente bueno que también falla
un mutante muerto por inclusión de un madre que nunca se corrió
```

---

## V. Las cinco maneras de engañarse, y cómo se reconoce cada una

**Estas cinco no son teoría: son las que aparecieron corriendo los trece.** **La quinta la dejó la corrida 18 del otro método, y vale igual aquí.**

```plaintext
1. el mutante sobrevive porque la prueba está rota
   señal: el veredicto es el mismo que el de un mutante que sobrevive
          de verdad, y no se distingue desde afuera
   qué se hace: si la primera vez sale vivo, se mira la prueba antes que el ensayo

2. se corrige la prueba hasta que el mutante muera
   señal: el mutante murió "por accidente", y el archivo no lo dice
   qué se hace: se anota el intento vivo en la documentación, y qué se cambió

3. el mutante muere contra un ente bueno que ya fallaba
   señal: el ente bueno no pasa la corrida
   qué se hace: el resultado no cuenta, y se dice que no contó

4. el mutante muere por una prueba que no puede fallar de otra manera
   señal: la prueba busca una frase exacta, y no el concepto
   qué se hace: la prueba tiene que poder fallar por lo que dice, no por
              cómo está escrita

5. la prueba no tenía nada que aceptar
   señal: el esquema "acepta" un DELETE que no borró nada
   qué se hace: antes de decir que algo se aceptó, se comprueba que había
              algo que aceptar
```

**Y la línea que las junta:** **una prueba que no puede fallar no prueba nada; y una prueba que falla por la razón equivocada miente igual que una que no falla.**

---

## VI. Lo que este método no prueba

**Y se cita, porque no es una opinión:**

> **«Las pruebas pueden revelar la presencia de defectos, pero nunca su ausencia.»**
> — Dijkstra, *Notes on Structured Programming*, EWD249, 1970.

**Un mutante muerto dice que el ensayo notó esa rotura.** **No dice que el ensayo no tenga otras.** **Y por eso el otro método no se tira: se queda para lo que ningún ensayo escribió.**

**Y lo que la cobertura sí dice, y no más:** **la cobertura es un piso y no un techo.**

**Y lo que falta de la disciplina, dicho aquí:** **los mutantes de este repositorio los corrió quien escribió las reglas, con su propia máquina.** **Un ensayo que aguanta a su autor todavía no aguanta a un desconocido.** **Y ninguno de afuera lo intentó todavía.**

---

## VII. De dónde salió cada pieza, con su fuente

**Esta tabla es lo que estaba repartido en `los papeles/estado del arte/`: aquí está sólo lo que este método usa, y la sección de donde viene, para que quien quiera el resto lo abra ahí.** **Las fuentes que el estado del arte cita y este método no usa —los agentes que aprenden de su experiencia, la memoria envenenada, los topic models— no se repiten aquí, y se dejan donde se justificaron.**

| Lo que este método afirma | De dónde viene | Qué se toma, y qué no |
|---|---|---|
| matar mutantes mide la fuerza de una prueba | **DeMillo, Lipton & Sayward (1978)**, *Hints on Test Data Selection* | se toma el mecanismo; no se toma su puntaje como medida de calidad del ente |
| un criterio de adecuación es una regla de parada | **Goodenough & Gerhart (1975)**, *Toward a Theory of Test Data Selection*, IEEE TSE | se toma que se para por un predicado calculable; no que el predicado sea el de aquí |
| «un criterio de adecuación es un predicado que determina si un programa se ha probado suficiente» | **Frankl & Weyuker (1988)**, *An Applicable Family of Data Flow Testing Criteria*, IEEE TSE 14(10) | se toma la definición, y de ahí la del paso III |
| una prueba adecuada para un criterio fuerte lo es para uno débil | la jerarquía de subsumción de **Frankl & Weyuker (1988)** | se toma la inclusión; y se dice que aquí casi no ahorra, porque una regla de conducta no contiene a otra |
| nunca confíes en una prueba que nunca has visto fallar | práctica de la disciplina de mutación | se toma tal cual, y es la línea del capítulo I |
| la mutación tiene un costo que obliga a seleccionar | [Software Engineering: Standing on the Shoulders of Giants, §10.1.5](https://www.swebook.org/chapters/10-testing/) | se toma el porqué de correr una madre por familia, y no una por regla |
| la cobertura es un piso y no un techo | [Software Engineering: Standing on the Shoulders of Giants, §10.1.3](https://www.swebook.org/chapters/10-testing/) | se toma el límite, y es el capítulo VI |
| las pruebas revelan la presencia de defectos, nunca su ausencia | **Dijkstra, EWD249 (1970)** | se toma la cita, y es la que impide decir "probado" cuando lo que hay es "no se cayó" |
| se declara lo que se va a medir antes de ver el resultado | **Pre-registration y Registered Reports**, Nature Human Behaviour [2021](https://www.nature.com/articles/s41562-021-01142-4) y [2023](https://www.nature.com/articles/s41562-022-01497-2) | se toma el orden: la regla y el mutante se escriben antes de correr, y no se eligen después |
| un falsificador escrito después de ver el resultado no falsifica nada | **Popper**, y la forma que se usa aquí | se toma la forma del falsificador; el límite de tomarlo por forma está dicho abajo |
| una observación tumba el conjunto y no una sola hipótesis | **Duhem y Quine**, vía la crítica a Popper | se toma el porqué de que el registro tenga desenlaces y no veredictos aislados |
| un programa de investigación se juzga por lo que predice | **Lakatos** | se toma la regla de parada por tendencia, y no por llegar a cero |
| el conocimiento se corrige por la crítica de otros | **Longino** | se toma por qué este método, corrido por su autor, no está terminado |
| una regla que no se puede contradecir no es una regla: es una opinión | **de este repositorio** | lo que se agrega al vocabulario de la disciplina: el mutante se escribe en el ensayo, no sólo en la prueba |

**Y lo que estas fuentes NO dicen, y se apunta:** **ninguna dice cuándo una descripción está completa.** **Todas dicen cuándo se ha probado suficiente, que es otra cosa, y es la única que se puede decir.**

**Y el límite de esta tabla, que el estado del arte ya decía y aquí vale igual:** **las fuentes de este método no las leyó el autor una por una.** **Las buscó `TESTIGO` en resúmenes.** **`Popper` y `Lakatos` se toman por su forma, sin una página.** **Un método que cita así no está respaldado por la literatura: está contrastado con su forma.**

---

## VIII. Lo que este archivo manda y lo que obedece

**Y esto importa más de lo que parece: un archivo de método que se corrige solo pierde lo que lo hace útil.**

```plaintext
este archivo manda sobre   cómo se escribe un mutante, cómo se corre,
                           cómo se apunta, y cuándo se para
este archivo obedece a     los ensayos. si un ensayo cambió una regla,
                           el mutante cambia de madre, y no al revés
y los números son de       corridas.md. este archivo no cuenta mutantes
                           ni reglas: dice cómo se cuentan
```

**Y la regla que impide que los dos archivos digan cosas distintas:** **si este archivo y `corridas.md` se contradicen, gana `corridas.md`, y este archivo se corrige un solo renglón de ese lado, con la fecha.**

---

## Prueba

**¿Cada paso de este método dice qué se hace y con qué se comprueba que se hizo?** **¿Cada fuente de la tabla VII dice qué se tomó y qué no?** **¿Se dice que los mutantes los corrió su autor, y que eso es un límite y no un detalle?** **¿Los números están en `corridas.md` y no aquí?** **¿Se distingue una regla de una explicación, y un mutante vivo de una prueba rota?**

---

**Falsificador:** **un método que cuenta mutantes sin haber corrido ninguno**; **un mutante que sobrevive y no se apunta**; **una regla que no se puede escribir al revés, presentada como si se hubiera probado**; **un método que dice «completo» apoyándose en una cobertura, cuando la cobertura es un piso y no un techo**; **y uno que repite los números de `corridas.md` y envejece por su cuenta.**
