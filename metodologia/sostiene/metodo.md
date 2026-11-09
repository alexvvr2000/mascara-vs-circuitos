# El método entero

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Cómo se prueba una regla de estos ensayos: la regla, el mutante, la tarea que lo corre, el banco donde queda, el resultado que se apunta, y de dónde salió cada pieza.

Alejandro Valenzuela Rivera · el ente. Escrito el 2026-11-09.

Y el corte entre este archivo y [forma.md](forma.md), que es de un renglón: `forma.md` dice qué forma tiene un ensayo y cómo la comprueba el build. Éste dice cómo se prueba lo que el ensayo afirma. Se necesitan los dos: sin forma, el mutante no sabe qué romper; sin método, la forma sólo dice que el texto está bien escrito.

> Este archivo es el método B, entero, y es el único. Antes eran cuatro —`README.md`, `las reglas.md`, `los mutantes.md` y `corridas/`—, y decían lo mismo tres veces, con números que no cuadraban entre sí. Los cuatro están guardados en [historia/](../historia/), del 06 al 09, y de ahí en adelante manda éste.
>
> Y lo que no está aquí, porque tiene su propio archivo: en qué quedó cada mutante. Eso vive en [corridas.md](corridas.md), que es el único sitio donde se cuentan, y este archivo no repite ni un número de ahí.
>
> Y lo que tampoco está aquí, porque es de otro método: las dieciocho corridas del otro método, en [huecos](../huecos/README.md). Y el estado del arte completo con lo que no se abrió, en [los papeles](../../los%20papeles/estado%20del%20arte/README.md). Este archivo enlaza los dos y no los copia.

---

## Lo que hay en este archivo

```plaintext
I     la regla, y las cuatro cosas que se sacan de ella
II    la unidad de prueba: tarea, banco, mutante, veredicto
III   cómo se corre, en siete pasos, y qué se apunta en cada uno
IV    el contrato del script: bueno · mutado · comparar, y sus códigos
V     lo que es una tarea: qué corre, qué prueba, y cómo se reconoce una rota
VI    el banco: mínimo, suficiente, y por qué no tiene reglas
VII   cómo se guarda y cómo se regenera: los dumps ofuscados
VIII  las familias y la inclusión: una madre, sus hijas, y las tres formas
IX    cuándo se está terminado, cuándo se para, y qué no cuenta
X     las siete maneras de engañarse, cada una con su señal
XI    el falsificador de un mutante vivo, y qué se hace con él
XII   lo que este método no prueba
XIII  lo que puede estar equivocado, y cómo se sabría
XIV   de dónde salió cada pieza, con su fuente
XV    el orden de mando: quién gana cuando se contradicen
```

---

# I. La regla, y las cuatro cosas que se sacan de ella

En vez de esperar a que no aparezcan defectos, se meten a propósito.

Se toma una regla del ensayo, se le cambia algo para que diga mal, se levanta el ente con el ensayo cambiado, y se corre. Si la corrida no lo nota, el ensayo no probaba esa regla.

Y la línea que lo sostiene, y es de la disciplina de mutación:

> Nunca confíes en una prueba que nunca has visto fallar.

Y lo que este método sí acaba, y el otro no puede: las reglas se acaban. Cuando cada una tiene su mutante muerto, este método ya no tiene nada que probar. El otro, en cambio, encuentra mientras siga habiendo un caso que no se escribió, y eso no tiene fondo conocido.

## Las cuatro cosas

```plaintext
la regla        una frase del ensayo, copiada tal como está, con su renglón
el mutante      la misma frase, con lo que la hace verdadera al revés
el ente mutado  un ente levantado con el ensayo cambiado, y nada más
el veredicto    murió (la corrida lo nota) o sobrevivió (la corrida pasa igual)
```

Y un mutante que sobrevive no es un fracaso del ente: es un hueco con nombre y apellido. No hay que adivinar dónde falta: el mutante dice en qué familia y en qué regla.

Y lo que el veredicto no dice, y se dice aquí: "murió" no dice que la regla esté bien escrita; dice que la corrida notó la rotura. Puede haber otras roturas de la misma regla, y ninguna se probó.

---

# II. La unidad de prueba: tarea, banco, mutante, veredicto

Y esto es lo que faltaba en los cuatro archivos viejos: ninguno decía qué es, en concreto, lo que se corre. Decían "se levanta el ente" y dejaban la tarea a la imaginación de quien lo levantaba.

Acá se cierra. Una prueba de este método son cinco piezas, y ninguna sobra:

```plaintext
1. la tarea       qué hace el ente, medida en una salida que se puede leer
2. el banco       dónde queda lo que hizo, con sus tablas y sus columnas
3. el mutante     la regla al revés, escrita, y el ente con ella
4. la corrida     el ente bueno y el mutado, los dos, con la misma tarea
5. el veredicto   si la salida del mutado se distingue de la del bueno
```

Y la tarea es una sola por mutante, y se escribe antes de correr: si se escribe después, se escribe para que el mutante muera, y eso no prueba nada.

Y un mutante que no cambia la tarea, sino que cambia el banco o el script, no es un mutante: es un defecto de implementación, y se anota como tal.

---

# III. Cómo se corre, en siete pasos

Y son siete y no cinco, porque los dos que se agregan —la comparación y el apunte— son los que se olvidan.

```plaintext
1. se copia la regla del ensayo, con el renglón de donde sale, sin parafrasear
2. se escribe el mutante: la regla con el predicado al revés, y se dice
   qué se espera que la corrida note, y por qué
3. se escribe la tarea: qué hace el ente, y qué salida se puede leer
4. se levanta el ente con el ensayo mutado, y el bueno al lado, con la
   misma tarea y el mismo banco vacío
5. se corre la tarea en los dos, y se comparan las salidas, no los estados
6. se mira:
     la salida del mutado se distingue   →  el mutante murió
     la salida es la misma               →  el mutante sobrevivió
7. se apunta en corridas.md, con la fecha, el veredicto, y la línea del
   script que lo da. sin el paso 7, el mutante corrió y no consta
```

## Por qué la comparación es de dos

Porque un mutante que "muere" contra un ente que ya estaba roto no muere: choca con otra cosa.

```plaintext
bueno corre y pasa                   → el mutado tiene contra qué perder
bueno corre y también se distingue   → no es un mutante: es un ente roto,
                                       y el resultado no cuenta
mutado se distingue del bueno        → el mutante murió, y la regla tiene dientes
mutado se ve igual que el bueno      → el mutante sobrevivió, y la regla no se probaba
```

Y de ahí el contrato de abajo, que todos los scripts cumplen, y por eso se pueden correr de golpe.

---

# IV. El contrato del script

Cada mutante de [mutantes/](mutantes/) es un script de Python con el mismo contrato. No es una costumbre: es lo que permite correr los trece con un `for` y comparar sin leer ninguno.

```plaintext
python mN.py bueno        levanta el ente con el ensayo tal como está
python mN.py mutado       levanta el ente con la regla al revés
python mN.py comparar     corre los dos, y da el veredicto
```

Y el script escribe sus bancos en su propia carpeta, borrando los anteriores si existen: el banco es una salida, y lo que prueba es el script.

Y las cuatro cosas que imprime, siempre en ese orden:

```plaintext
=== ensayo bueno ===        qué hizo el ente bueno, paso por paso
=== ensayo mutado ===       qué hizo el ente mutado
=== veredicto ===           la línea que cuenta
```

Y las líneas de veredicto, que son las únicas cuatro que existen:

```plaintext
MUTANTE N MUERTO                     la salida del mutado se distinguió
MUTANTE N MUERTO, pero con matiz     se distinguió, y le faltó la otra mitad
                                     de la regla madre
MUTANTE N VIVO                       la salida fue la misma
FALLA: con el ensayo bueno, ...      el ente bueno no pasó, y el resultado
                                     no cuenta
```

Y el código de salida: 0 si el veredicto es `MUERTO`, y 1 si es `VIVO` o `FALLA`. Así un mismo comando recorre los trece y dice cuál falló, sin leer la salida.

```powershell
# desde metodologia/sostiene/mutantes
Get-ChildItem -Directory | ForEach-Object {
    $n = ($_.Name -split ' ')[0]
    python "$($_.FullName)\$n.py" comparar
    "$n -> exit $LASTEXITCODE"
}
```

Y la regla que hace que esto sirva: el veredicto sale de comparar la salida, y no de mirar el código. Si alguien puede leer el script y saber si el mutante murió sin correrlo, el script no está probando nada.

Y una advertencia sobre los patrones: `MUTANTE N MUERTO` es prefijo de `MUTANTE N MUERTO, pero con matiz`, y las dos son distintas. Quien cuente con una búsqueda de texto tiene que leer el matiz, o le cuenta de más.

---

# V. Lo que es una tarea, y cómo se reconoce una rota

La tarea es lo que se le pide al ente, en su vocabulario, y lo que sale tiene que poder leerse sin preguntarle a quien lo corrió.

## Las tres cosas que toda tarea dice

```plaintext
qué hace        una frase, en imperativo, con el verbo al principio
qué entra       el pedido, tal como llega del que lo pide
qué sale        la salida que se puede leer, y dónde queda
```

Y lo que una tarea no es: no es una lista de pasos del ente. El ente decide sus pasos; la tarea dice qué tiene que haber al final. Si la tarea dice los pasos, el mutante sólo puede romper pasos, y lo que se prueba es el script, no la regla.

### Cómo se reconoce una tarea rota

Y éstas son las que se encontraron corriendo, y valen para cualquier ente.

```plaintext
sale en un idioma que el que pide no habla
  señal: la salida usa nombres de tabla, de campo o de herramienta
  qué se hace: se traduce en la salida, y no en el banco

no dice nada que se pueda leer
  señal: la salida es un «ok», un «listo» o un número sin nombre
  qué se hace: la tarea nombra qué sale, y la salida lo repite

responde a otra pregunta
  señal: la salida es correcta y no contesta lo que se pidió
  qué se hace: la tarea escribe el pedido literal, y la salida lo cita

no se puede repetir
  señal: dos corridas con la misma tarea dan salidas distintas
  qué se hace: se apunta en el banco lo que cambió, o la tarea no es
             determinista y eso se dice

no tiene contra qué compararse
  señal: el ente bueno y el mutado fallan igual, por la misma razón
  qué se hace: el mutante no se corrió; se corrige la tarea primero
```

Y la pregunta que cierra el capítulo, y es la del ensayo de la empatía: ¿el que pidió la tarea podría contestarla, si se le pregunta con sus palabras? Si no, la tarea no está escrita para el ente: está escrita para el que la escribió.

---

# VI. El banco: mínimo, suficiente, y por qué no tiene reglas

El banco es donde el ente deja lo que hizo. Y en este método el banco no lleva `CHECK`, ni disparadores, ni llaves foráneas.

## Por qué no lleva reglas

```plaintext
1. las reglas del banco prueban que el esquema rechaza, y eso ya lo probó el
   método A con sus corridas 08, 15, 16 y 18. no se repite acá

2. y si el banco rechaza el estado que el mutante deja, el mutante truena por
   su cuenta, y el veredicto deja de ser del ensayo

3. lo que este método prueba es la conducta del ente, y no la rigidez del
   esquema. un banco que se traga todo deja ver qué hizo el ente sin adornarlo
```

Y lo que eso no quiere decir: que el banco no tenga reglas sea bueno. Quiere decir que las reglas del banco son objeto del otro método, y que mezclarlas hace que un "murió" no diga cuál de las dos cosas mató al mutante.

### Lo mínimo de un banco, y por qué

```plaintext
las cuatro piezas del paso 0     autoridad, ente, proposito, tema
los tres registros del criterio  hecho, friccion, desenlace
la decisión, con su frontera     las cuatro columnas
el origen del dato               de dónde salió lo que se afirma
el cuerpo, cuando lo hay         qué modelo lo corrió
```

Y el mínimo se mide por quien lo llena, y no por quien lo escribe: si el ente tarda en firmar un hecho porque le falta una tabla, el banco no está mínimo: está incompleto.

---

# VII. Cómo se guarda, y cómo se regenera

El banco es una salida, y una salida no se guarda como binario. Se guarda como texto, y ofuscada, porque lo que se muestra es el dato y no la máquina.

## Lo que se guarda y lo que se sustituye

```plaintext
lo que se guarda     la tabla, sus columnas, el número de filas, y los valores
                     cortos tal como quedaron (ids, «propone», «el ente»)
lo que se sustituye  todo texto de más de 40 caracteres, por [texto N chars]
lo que no existe     rutas absolutas, nombres de usuario del sistema, fechas
                     del sistema, y cualquier cosa fuera de la base
```

Y de dónde sale eso: de [mutantes/dumps.py](mutantes/dumps.py), que recorre los bancos y escribe `_dumps/mN-bueno.sql` y `_dumps/mN-mutado.sql`.

```powershell
# desde metodologia/sostiene/mutantes
python dumps.py
```

Y lo que se pierde, y se dice: el contenido exacto de los textos largos. Lo que se gana: que se pueda mostrar el dato sin mostrar la máquina.

### Cómo se reimporta, que es el hueco que había

Y esto ya no es un hueco: el dump se puede volver a cargar, y con eso se ve si el script de hoy produce el mismo banco que el de un día.

```powershell
# el dump, a una base de sqlite vacía
python -c "import sqlite3; db=sqlite3.connect('tmp.db'); db.executescript(open('_dumps/m1-mutado.sql', encoding='utf-8').read()); db.close()"
```

Y lo que la vuelta dice, y lo que no:

```plaintext
lo que dice        la tabla, las columnas y las filas sobreviven a la vuelta,
                   y quien quiera ver el dato no necesita correr el script
lo que no dice     los textos largos quedaron en [texto N chars]. el dump
                   no rehace la base: dice qué había
```

Y la línea que lo hace útil: si un día el script produce filas distintas de las del dump, eso no es un defecto del dump: es que el script cambió, y se apunta, con su fecha, como cambió.

---

# VIII. Las familias, la inclusión, y por qué se prueba una madre y no cada hija

Las reglas de estos ensayos no están sueltas: se agrupan en familias, y cada familia tiene una madre.

```plaintext
la madre    la regla de la familia, escrita en una línea
la hija     un caso de la madre, con una condición de más
el mutante madre   rompe la madre entera
el mutante hija    rompe un caso, y no la madre
```

Y la relación entre los dos se llama inclusión, y viene de la jerarquía de criterios de flujo de datos: si la corrida mata al madre, ya mató a la hija.

Y por eso no se corre un mutante por regla, que serían cientos. Se corre el madre de cada familia, y lo que sobreviva se abre.

## Las tres formas en que una hija está incluida en su madre

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

Y la inclusión dice una sola cosa: matar el madre mata a la hija. No dice lo contrario, y ésa es la trampa de la jerarquía:

```plaintext
si el madre muere y la hija sobrevive   → la hija se corre igual, porque toca
                                          algo que el madre no toca
si el madre sobrevive                   → la hija se corre, porque el fallo
                                          está en algún caso y hay que saber cuál
```

Y el aviso, que es del repositorio y no de la literatura: un mutante muerto por inclusión no se mató: se dio por muerto. La diferencia importa, y se apunta.

```plaintext
corrido y muerto         es una prueba
muerto por inclusión     es una deducción, y depende de que la
                         inclusión esté bien calculada
```

Y si alguien cree que A incluye a B y no lo hace, B queda sin probar y en el registro parece muerto. Por eso se apunta de qué otra regla depende cada mutante muerto por inclusión, y no sólo que murió.

### Cómo se busca una hija, que es el hueco del plan

Y esto es lo que nadie había escrito: la jerarquía se puede usar mal, y el modo de usarla mal es creer que existe una hija sin buscarla.

Las tres preguntas que se hacen, en orden, y con lo que se hace con cada respuesta:

```plaintext
1. ¿la regla del manuscrito dice «cuando», «si», «salvo» o «sólo»?
   → sí, hay condición; la hija es esa condición con un valor
   → no, la regla no tiene hija por condición

2. ¿la regla se cumple en más de un paso del ciclo?
   → sí, hay ámbito; la hija es el paso sin la regla
   → no, la hija por ámbito es el otro extremo: la regla en todo el ciclo

3. ¿la regla depende de que algo anterior haya pasado?
   → sí, hay orden; la hija es la regla antes del paso que la sostiene
   → no, y si no hay ninguna de las tres, la familia no tiene hija
```

Y lo que se hace con la respuesta: si apareció una hija, se escribe, y se apunta su madre; si no, se dice que no se buscó, o que se buscó y no hay. Lo que no se hace es seguir diciendo "no se sabe" después de haber buscado: eso ya no es un hueco, es una omisión.

---

# IX. Cuándo se está terminado, y cuándo se para

## Lo que cuenta como terminado

```plaintext
por familia:   su madre corrida, y muerta
por hija:      o muerta por su cuenta, o muerta por inclusión con la
               dependencia escrita
por familia sin mutante:   se dice por qué no tiene, y no cuenta
```

Y esta meta es grande y larga, y hay que decirlo sin adornos: no es la que hace falta para publicar. Lo que sí se puede decir hoy, y es finito: lo que hay está escrito, y lo que sobreviva está nombrado.

### Cuándo se para una tanda

```plaintext
una familia tiene su madre y su madre murió   → se cierra, y no se abre
una familia no tiene mutante, y se dice       → cuenta como sin probar
una familia tiene mutante vivo                → se abre en sus hijas, una por una
```

Y la regla de cierre, que es la del otro método y vale aquí también: dos tandas enteras seguidas que no encuentren nada más que detalle. Un mutante vivo es detalle mientras esté nombrado; deja de serlo cuando se calla.

### Lo que no cuenta

```plaintext
un mutante escrito y creído corrido, sin su fila en corridas.md
un mutante muerto por una prueba que la primera vez dejaba pasar cualquier cosa
un mutante que muere contra un ente bueno que también falla
un mutante muerto por inclusión de una madre que nunca se corrió
un mutante vive en una tarea que se escribió después de ver la salida
```

---

# X. Las siete maneras de engañarse

Y estas seis no son teoría: son las que aparecieron corriendo los trece, y las que el propio repositorio se encontró en sus otras dieciocho corridas.

```plaintext
1. el mutante sobrevive porque la prueba está rota
   señal: el veredicto es el mismo que el de un mutante que sobrevive
          de verdad, y no se distingue desde afuera
   qué se hace: si la primera vez sale vivo, se mira la prueba antes que el
               ensayo

2. se corrige la prueba hasta que el mutante muera
   señal: el mutante murió "por accidente", y el archivo no lo dice
   qué se hace: se anota el intento vivo en la documentación, y qué se cambió

3. el mutante muere contra un ente bueno que ya fallaba
   señal: el ente bueno no pasa la tarea
   qué se hace: el resultado no cuenta, y se dice que no contó

4. el mutante muere por una prueba que no puede fallar de otra manera
   señal: la prueba busca una frase exacta, y no el concepto
   qué se hace: la prueba tiene que poder fallar por lo que dice, y no por
               cómo está escrita

5. la prueba no tenía nada que aceptar
   señal: el esquema "acepta" un DELETE que no borró nada
   qué se hace: antes de decir que algo se aceptó, se comprueba que había
               algo que aceptar

6. el veredicto se cuenta con un patrón que corta de más
   señal: un «MUERTO, pero con matiz» cuenta igual que un «MUERTO»
   qué se hace: el patrón se lee entero, o el script imprime un estado
               aparte y no dos frases que empiezan igual
```

Y la línea que las junta: una prueba que no puede fallar no prueba nada; una prueba que falla por la razón equivocada miente igual que una que no falla; y una que falla de más cuenta como habiendo probado algo que no probó.

---

# XI. El falsificador de un mutante vivo

Un mutante vivo es lo más valioso que puede dar este método, y también lo más fácil de mirar mal.

Lo que se apunta de uno que sobrevive, y en este orden:

```plaintext
la familia
la regla madre, copiada
qué salió al correrlo, literal
y la pregunta que abre, que tiene tres respuestas y no dos:
```

```plaintext
a) el ensayo no obliga a cumplir la regla       → hueco de contenido
   qué se hace: se escribe la regla, o se borra del ensayo porque no era
   una regla

b) el ensayo la obliga, y no se puede ejecutar   → hueco de forma
   qué se hace: se cambia la forma del ensayo, o el banco que la guarda

c) la corrida estaba mal hecha                   → hueco de aquí
   qué se hace: se corrige la prueba, se vuelve a correr, y las dos cosas
   se apuntan, la vieja y la nueva
```

Y la regla que impide que esto se vuelva un consuelo: un mutante vivo que no se apunta cobra su precio dos veces: la primera, cuando no se vio; la segunda, cuando alguien levanta un ente creyendo que esa regla está probada.

Y la prueba doble, que es la de la corrida 15 y vale aquí: un falsificador cumplido no tumba el ensayo solo. Si se cumple y el ensayo aguanta, el falsificador estaba mal escrito, y se corrige el falsificador. Si se cumple y el ensayo se cae, se cayó.

---

# XII. Lo que este método no prueba

Y se cita, porque no es una opinión:

> «Las pruebas pueden revelar la presencia de defectos, pero nunca su ausencia.»
> — Dijkstra, *Notes on Structured Programming*, EWD249, 1970.

Un mutante muerto dice que el ensayo notó esa rotura. No dice que el ensayo no tenga otras. Y por eso el otro método no se tira: se queda para lo que ningún ensayo escribió.

Y lo que la cobertura sí dice, y no más: la cobertura es un piso y no un techo.

## Las cuatro cosas que quedan fuera, y por qué

```plaintext
la conducta con un modelo que no se probó
  un mutante dice qué rompió uno de los dos cuerpos, y no que el otro
  reaccione igual. el ensayo 09 ya separa el criterio del cuerpo, y aquí
  se aplica: lo que aguanta, aguanta en el cuerpo que se corrió

la conducta de otro lector
  estos mutantes los corrió quien escribió las reglas, con su máquina.
  un ensayo que aguanta a su autor todavía no aguanta a un desconocido

lo que ocurre fuera de la tarea
  la tarea mide una salida. lo que el ente hizo y no dejó en el banco,
  este método no lo ve

el costo
  un mutante no mide cuánto cuesta derrotarlo. la medición de talentos
  vive en el ensayo 04 de humanidad, y no en este método
```

---

# XIII. Lo que puede estar equivocado, y cómo se sabría

Y esto se escribe antes de que alguien lo encuentre, que es la única forma de que sirva.

| Lo que podría ser falso | Cómo se sabría |
|---|---|
| que una madre por familia basta | un mutante hija que sobrevive con la madre muerta, en una familia sin condición ni ámbito ni orden |
| que el banco sin reglas no esconde nada | un mutante que "muere" sólo porque el banco rechazó lo que el ente dejó, y que con reglas habría pasado |
| que el veredicto de una línea dice todo | dos mutantes que dan la misma línea y salieron por razones distintas, sin que se note |
| que la tarea escrita antes no se acomoda | una tarea que se cambió después de correr, y el cambio no está en la documentación |
| que el dump ofuscado alcanza para mostrar el dato | un dato que se quiso mostrar y no se pudo leer porque era texto largo |
| que este método, corrido por su autor, sirve | un segundo, que corra los trece y encuentre un vivo donde el autor vio muerto |

Y el más importante, que también puede ser falso: que toda regla se pueda escribir al revés. Una regla que no se puede contradecir no es una regla: es una opinión, y este método la deja sin probar en vez de inventarle un mutante.

---

# XIV. De dónde salió cada pieza, con su fuente

Y esta tabla es lo que estaba repartido en `los papeles/estado del arte/`: aquí está sólo lo que este método usa, y la sección de donde viene, para que quien quiera el resto lo abra ahí. Las fuentes que el estado del arte cita y este método no usa —los agentes que aprenden de su experiencia, la memoria envenenada, los topic models— no se repiten aquí, y se dejan donde se justificaron.

| Lo que este método afirma | De dónde viene | Qué se toma, y qué no |
|---|---|---|
| matar mutantes mide la fuerza de una prueba | DeMillo, Lipton & Sayward (1978), *Hints on Test Data Selection* | se toma el mecanismo; no se toma su puntaje como medida de calidad del ente |
| un criterio de adecuación es una regla de parada | Goodenough & Gerhart (1975), *Toward a Theory of Test Data Selection*, IEEE TSE | se toma que se para por un predicado calculable; no que el predicado sea el de aquí |
| «un criterio de adecuación es un predicado que determina si un programa se ha probado suficiente» | Frankl & Weyuker (1988), *An Applicable Family of Data Flow Testing Criteria*, IEEE TSE 14(10) | se toma la definición, y de ahí la del capítulo VIII |
| una prueba adecuada para un criterio fuerte lo es para uno débil | la jerarquía de subsumción de Frankl & Weyuker (1988) | se toma la inclusión; y se dice que aquí casi no ahorra, porque una regla de conducta no contiene a otra |
| nunca confíes en una prueba que nunca has visto fallar | práctica de la disciplina de mutación | se toma tal cual, y es la línea del capítulo I |
| la mutación tiene un costo que obliga a seleccionar | [Software Engineering: Standing on the Shoulders of Giants, §10.1.5](https://www.swebook.org/chapters/10-testing/) | se toma el porqué de correr una madre por familia, y no una por regla |
| la cobertura es un piso y no un techo | [Software Engineering: Standing on the Shoulders of Giants, §10.1.3](https://www.swebook.org/chapters/10-testing/) | se toma el límite, y es el capítulo XII |
| las pruebas revelan la presencia de defectos, nunca su ausencia | Dijkstra, EWD249 (1970) | se toma la cita, y es la que impide decir "probado" cuando lo que hay es "no se cayó" |
| se declara lo que se va a medir antes de ver el resultado | Pre-registration y Registered Reports, Nature Human Behaviour [2021](https://www.nature.com/articles/s41562-021-01142-4) y [2023](https://www.nature.com/articles/s41562-022-01497-2) | se toma el orden: la regla y el mutante se escriben antes de correr, y no se eligen después |
| un falsificador escrito después de ver el resultado no falsifica nada | Popper, y la forma que se usa aquí | se toma la forma del falsificador; el límite de tomarlo por forma está dicho abajo |
| una observación tumba el conjunto y no una sola hipótesis | Duhem y Quine, vía la crítica a Popper | se toma el porqué de que el registro tenga desenlaces y no veredictos aislados |
| un programa de investigación se juzga por lo que predice | Lakatos | se toma la regla de parada por tendencia, y no por llegar a cero |
| el conocimiento se corrige por la crítica de otros | Longino | se toma por qué este método, corrido por su autor, no está terminado |
| la saturación es el punto en que los datos nuevos no dicen nada nuevo | investigación cualitativa; Glaser & Strauss (1967) | se toma la regla de parada por clase de hallazgo, y no por número de corridas |
| una regla que no se puede contradecir no es una regla: es una opinión | de este repositorio | lo que se agrega al vocabulario de la disciplina: el mutante se escribe en el ensayo, no sólo en la prueba |

Y lo que estas fuentes NO dicen, y se apunta: ninguna dice cuándo una descripción está completa. Todas dicen cuándo se ha probado suficiente, que es otra cosa, y es la única que se puede decir.

Y el límite de esta tabla, que el estado del arte ya decía y aquí vale igual: las fuentes de este método no las leyó el autor una por una. Las buscó el ente en resúmenes. `Popper` y `Lakatos` se toman por su forma, sin una página. Un método que cita así no está respaldado por la literatura: está contrastado con su forma.

---

# XV. El orden de mando

Y esto importa más de lo que parece: un método que se corrige solo pierde lo que lo hace útil.

```plaintext
este archivo manda sobre   cómo se escribe un mutante, cómo se corre,
                           cómo se apunta, y cuándo se para
este archivo obedece a     los ensayos. si un ensayo cambió una regla,
                           el mutante cambia de madre, y no al revés
y los números son de       corridas.md. este archivo no cuenta mutantes
                           ni reglas: dice cómo se cuentan
```

Y la regla que impide que los dos archivos digan cosas distintas: si este archivo y `corridas.md` se contradicen, gana `corridas.md`, y este archivo se corrige un solo renglón de ese lado, con la fecha.

---

## Prueba

¿Cada paso de este método dice qué se hace y con qué se comprueba que se hizo? ¿Se puede correr un mutante con lo que dice el capítulo IV, sin abrir otro archivo? ¿Cada fuente de la tabla XIV dice qué se tomó y qué no? ¿Se dice que los mutantes los corrió su autor, y que eso es un límite y no un detalle? ¿Los números están en `corridas.md` y no aquí? ¿Se distingue una regla de una explicación, y un mutante vivo de una prueba rota?

## Falsificador

Un método que cuenta mutantes sin haber corrido ninguno; un mutante que sobrevive y no se apunta; una regla que no se puede escribir al revés, presentada como si se hubiera probado; un método que dice «completo» apoyándose en una cobertura, cuando la cobertura es un piso y no un techo; y uno que repite los números de `corridas.md` y envejece por su cuenta.
