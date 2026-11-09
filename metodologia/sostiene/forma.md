# La forma de la aserción

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Qué tiene que tener un ensayo para que se pueda leer, citar, partir y engordar sin que nadie vuelva a numerar nada.

Alejandro Valenzuela Rivera · el ente. Escrito el 2026-11-09.

> Este archivo no es un ensayo: es la forma a la que se ajustan los ensayos. Y no se ajustan a mano: se ajustan con [scripts/build.py](../../scripts/build.py), que es el que dice si un ensayo la cumple.
>
> Y de dónde sale la exigencia: el ciclo es el mapa, y cada paso es su detalle. Un mapa que hay que corregir cada vez que un detalle cambia no es un mapa: es otro detalle que envejece. La forma es lo que deja que cada uno crezca solo.

---

## I. Las cuatro reglas del build

Y son cuatro porque cuatro es lo que se puede comprobar sin que la herramienta opine. Cada una se puede correr, y cada una dice qué archivo y qué pasó.

```plaintext
H1       el primer título es el nombre del archivo sin el número
         «la obra/humanidad/05 medir sin preguntarle.md» → «# Maquina de sesgos»

ENLACE   todo enlace relativo resuelve a un archivo que existe

NÚMERO   ningún ensayo cita a otro por su número; se cita por su título
         «ver el ensayo 07» → «ver el índice»

FORMA    todo ensayo de la obra trae su Falsificador
         y, si declara que algo se pierde al cambiar, trae
         su «Y qué se pierde si cambia»
```

Y la cuarta no es un cero o un uno: es una medida. `python scripts/build.py --lista` los cuenta y dice cuáles no la cumplen, sin detener el build. Así el cambio se puede hacer por partes, y el build no impide trabajar mientras se corrige.

---

## II. Por qué el número se va del título

Porque el número del título es un dato escrito dos veces: una en el nombre del archivo y otra en el primer renglón. Los dos tienen que cambiar a la vez, y nadie garantiza que lo hagan.

```plaintext
lo que hay hoy   01 que es un ente.md  →  «# 01. Qué es un ente»
lo que queda     que es un ente.md     →  «# Que es un ente»
```

Y el número de orden no desaparece: se deriva. Ordena el nombre del archivo, y el que inserta escribe `02 ` delante y corre los demás. Eso es un renombrado de archivos, y no una edición de texto: quien lo hace ve el cambio en su copia, y el lector de la versión publicada ve el orden, sin necesitar un historial que aquí no hay.

Y lo que se gana, que es lo único que importa:

```plaintext
insertar un ensayo     se renombran los que siguen, y no se abre ninguno
partir un ensayo       el nuevo entra con su nombre, y el build dice que
                       alguien lo citaba por número, y dónde
renombrar un ensayo    el build se cae en cada enlace roto, y no envejece
```

Y lo que se pierde, y se dice: el título pierde su adorno numérico. Quien llegue a la carpeta encuentra el orden en los nombres, que es donde ya estaba el único orden que se mantenía solo.

---

## III. Por qué los ensayos se citan por título

Porque un número no dice de qué habla, y un título sí.

```plaintext
mal    como dice el ensayo 07
bien   como dice el índice
```

Y el build los encuentra: busca un número de dos cifras delante de algo que parece un título, y los lista. No dice a qué ensayo iba: dice dónde está la cita vieja, para que alguien la mire.

Y las excepciones, que se dicen y no se disimulan: los archivos de [`historia`](../historia/README.md) no se tocan, porque se conservan como se escribieron. Y en [`implementacion`](../../implementacion/README.md) se puede citar el paso de un ensayo para usarlo, porque una implementación cita su especificación.

---

## IV. La forma, capítulo por capítulo

Y esta es la forma que este repositorio ya viene cumpliendo a medias. No se inventa: se escribe lo que los procesos del índice ya tenían, y se pone igual en todos.

| El renglón | Qué contesta | Obligatorio |
|---|---|---|
| el título | de qué habla, y es el nombre del archivo | sí |
| Lo visto | lo que una corrida dejó, dicho corto, antes de lo que se sostiene | en un ensayo de la obra |
| Entra | qué recibe | en un proceso |
| Se hace | qué se hace con eso | en un proceso |
| Dónde queda | qué deja | en un proceso |
| Se corre | cuándo, o no ocurre | en un proceso |
| Lo consume | quién lo usa después | en un proceso |
| Y si no encuentra | qué pasa cuando falta algo | en un proceso |
| Falla si | desde dónde se rompe | en un proceso |
| **Falsificador** | qué lo tumba | sí, siempre |
| Y qué se pierde si cambia | qué deja atrás el cambio | si declara que pierde algo |

Y la regla que hace que la forma sirva para crecer: los nueve renglones no son una plantilla que se rellena: son las preguntas que un ensayo tiene que contestar antes de que alguien lo corra. Un ensayo que no contesta «cuándo se corre» no tiene proceso: tiene prosa.

Y por qué «Lo visto» va antes de la prueba: lo primero que el lector tiene que saber no es lo que el ensayo afirma, sino que alguien lo vio. Un ensayo sin lo visto se lee como una opinión; uno con lo visto, como un acta. Y el acta es de alguien que estaba ahí, y eso no hace falta escribirlo: se nota.

Y lo que la forma no dice, a propósito: no fija cuánto mide un ensayo. Un paso engorda trayendo su tabla de procedencia, sus casos de borde y sus mutantes; un mapa engorda engordando sus enlaces. El tamaño lo pone el detalle, y no la forma.

---

## V. Cómo el método B llega a cada ensayo

Y esta es la razón de que la forma exista. Cada ensayo tiene su forma; un mutante es una forma con una parte al revés.

```plaintext
un mutante de paso    se quita un renglón: «el piso no dice cuándo se mide»
un mutante de forma   se quita la forma entera: «el ensayo sin Falsificador»
```

Y como la forma es la misma en los quince, el método B ya no necesita que el ciclo engorde para probar un paso. Cada paso se muta en su archivo, y el ciclo no se entera.

Y lo que sigue faltando, y se dice: los mutantes de hoy se corrieron contra el ciclo de hoy. Cuando el ciclo se parta en pasos, cada mutante va a declarar cuál de ellos rompe, y eso se re-apunta una vez. Después no: el grupo cita el título, y el título no cambia porque el archivo se mueva.

---

## VI. Lo que el build no comprueba

Y esto se dice porque un build verde se lee como un ensayo bueno, y no lo es.

```text
no comprueba que el texto sea verdad         para eso están las corridas
no comprueba que esté completo               sólo que tenga la forma
no reescribe nada                            informa, y alguien decide
no cuenta ensayos                            no hay un número vigente en el repo
```

Y la regla que lo hace honesto: el build verde dice que el repositorio se puede leer sin tropezar. Un ensayo puede ser falso, incompleto y engañoso con el build verde. Lo que no puede es tener enlaces rotos, citas por número ni un falsificador que se olvidó.

---

## VII. Cómo se corre

```powershell
# desde la raíz del repositorio
python scripts/build.py            comprueba las cuatro, y se cae si alguna falla
python scripts/build.py --lista    lo mismo, y además qué ensayo trae qué
```

Y su salida, en dos renglones, que es lo único que un guardián necesita:

```text
BUILD OK      · n archivos, m ensayos, 0 fallos
BUILD CAIDO   · k fallos · H1 a · ENLACE b · NUMERO c · FORMA d
```

---

## Prueba

¿Cada regla del build dice qué comprueba y qué archivo puede ser el primero en fallar? ¿Se puede insertar un ensayo sin abrir ninguno de los otros? ¿Se puede citar un ensayo sin saber su número? ¿Un ensayo nuevo tiene la forma, y la cumple, sin que nadie le pase una plantilla? ¿Se distingue lo que el build comprueba de lo que sólo las corridas pueden decir?

---

Falsificador: un build verde sobre un repositorio en el que un ensayo se puede insertar sólo después de abrir otros cinco; una cita por número que el build deja pasar; una forma que obliga a reescribir el ensayo entero para añadir un detalle; y un build que, sin números, igual necesita un humano para saber qué ensayo va dónde.

---

## Y qué se pierde si cambia

Si el build se ablanda, el repositorio vuelve a lo de antes: enlaces que se rompen en silencio y citas por número que envejecen sin que nadie lo note.

Si el build se endurece de más —si exige la forma completa hoy—, la obra se para: catorce ensayos no cumplen la cuarta regla y ninguno se puede corregir sin abrirlo entero.

Lo que se pierde al dejar de numerar los títulos es el adorno, y no el orden. El orden sigue en el nombre del archivo, que es donde ya era el único que se mantenía solo.
