# repo — el órgano del repositorio, entero, en un solo módulo

Aquí vive todo lo que el repo hace: lo que se comprueba, lo que se arregla, lo que se
lee y lo que se escribe. No hay una segunda casa: el resto del paquete es la puerta.

```plaintext
repo/
  __init__.py    el que reparte: los trabajos, y `python -m scripts`
  comun.py       la raíz, leer, caminar el árbol, glob
  constantes.py  las expresiones regulares y la forma de cada cosa
  encabezados.py el formato de proceso, leído como datos
  bloques.py     cada ensayo como una lista de bloques
  hallazgos.py   de qué ensayo sale cada corrida
  estado.py      que estado.md no envejezca
  enlaces.py     el mapa de lo que enlaza con qué
  reglas.py      lo que el repositorio tiene que cumplir
  legal.py       REUSE, licencias y zenodo
  trabajos.py    lo que se arregla sin tocar una idea
  licuadora.py   las tesis de los ensayos, agrupadas
  comprobar.py   todas las reglas de una vez
  readme.md      esto
```

Y lo que se borró, se dice una vez: los trece archivos que había antes, y el respaldo
que quedó de ellos. Un órgano se lee por lo que hace hoy, no por lo que fue. Lo que
servía de cada uno está aquí, con su razón escrita.

---

## Qué es, y qué no

Es un **lector que también arregla**: mira el repositorio, y cuando se le pide, corrige
lo que se puede corregir sin tocar una idea. No escribe prosa, no reescribe ensayos, y
no decide nada: lo que encuentra lo dice, y lo que falta lo nombra.

Y es el build: `python -m scripts` es la entrada de todo, y sí se cae.

---

## En qué ayuda, concretamente

| Lo que hoy cuesta | Lo que hace el módulo |
|---|---|
| saber si una corrida apunta a su carpeta, y si su carpeta está en el índice | `hallazgos.revisar()` lo dice, corrida por corrida |
| que `estado.md` envejezca sin que nadie lo note | `estado.comparar()` lo compara con la orden, y el build se cae con el renglón |
| saber qué dice un ensayo de 400 renglones | `bloques.mapa()` da una línea por concepto |
| saber qué le falta a un proceso | `encabezados.mapa()` da sus campos, y los que le faltan |
| ver dónde pesa el repo | `enlaces.mapa()` cuenta qué carpeta recibe cada enlace |

---

## Cómo ayuda a una máquina a pensar las ideas en bloques

Esto es lo que hace que valga la pena, y no es una metáfora.

Un ensayo escrito en prosa obliga a leerlo entero para sacar una idea. Una máquina
—esta, o cualquiera— no lee así: recorre y confía. Y lo que no está en el texto, lo
rellena. El formato de procesos existe justo por eso: **un proceso es un texto que ya
dice cómo se hace la cosa, de modo que lo único que queda es llenar los huecos.**

Un bloque es esa idea, aplicada a un concepto:

```plaintext
afirma        una oración. si ocupa dos, son dos bloques
en            el paso del ciclo. es lo que hace el ensayo conectable
sostiene la   la regla que sale de aquí
se prueba     la corrida o el mutante, o «nada», y entonces manda el borde
no cubre      el límite
enlaza        otros bloques, por su título
entra         cuándo nació
cambió        qué era antes, y por qué cambió
```

Y con eso, pensar una idea deja de ser interpretar y pasa a ser **comparar campos**:
dos bloques con el mismo `afirma` son el mismo concepto dos veces; un bloque sin
`en` no está en el ciclo; un bloque sin `no cubre` promete de más; un bloque sin
`se prueba` es una idea que nadie corrió. Eso no se puede preguntar a un párrafo.

## El criterio de crecimiento

Un concepto entra al criterio si deja las tres cosas: **su folio** (de qué ensayo sale,
y en qué línea), **su prueba** (qué lo corre, y qué se cae si se quita) y **su borde**
(qué no cubre). No crece porque haya espacio: crece cuando un bloque del ensayo no se
puede leer sin él.

---

## Lo que no puede hacer, y se dice

- **No dice si la idea es verdad.** Dice dónde está, qué la sostiene, qué no cubre, y
  cuándo cambió. La verdad la dice el desenlace, y eso no lo corre un script.
- **No inventa el dato que falta.** Hoy las 18 corridas de `huecos` no dicen de qué
  ensayo salen, y el módulo lo apunta como falta en vez de deducirlo.
- **Un bloque no abarata la escritura.** Ocho líneas por concepto es más caro que un
  párrafo. Lo que gana es que se lee sin leer el resto.
- **No parte los ensayos solo.** El trabajo de partir es del autor, un ensayo por vez.
- **No juzga el proceso de un ensayo.** La regla de los once renglones se aplica a los
  procesos, que son los que están en `metodologia/`; un ensayo que usa uno de esos
  campos como gancho no es un proceso mal escrito.
- **No parsea `humanidad/` por ideas, ni falta que hace.** Ver el alcance, abajo.

---

## El alcance: dónde sirve parsear, y dónde no

La prosa no se parsea igual en todas partes, y esto decide dónde vale la pena el
formato de bloques y dónde es trabajo perdido.

```plaintext
la obra/humanidad/    es para el lector. se lee y se entiende. no se parsea, y no
                      se toca: es del autor, y los bloques ahí no ayudan a nadie.

la obra/teoria/       está en constante mutación. sí se parsea: es la que más se
                      discute y la que se va a reescribir. once ensayos, uno por vez.

metodologia/          al final.
```

Y lo que viene después, para que no se pierda: cuando acabe el análisis de ciclo, **el
ciclo del ente se hace desde cero** y pasa a ser la lista de pasos que referencia las
ideas ya destiladas. Las piezas ya están; lo que falta es unificarlas, decir cuál no
va y cuál falta, y dejar el detalle justo para que de ahí en adelante sólo se agregue
detalle, por cualquiera de los tres métodos.

---

## Cómo se corre

```plaintext
python -m scripts                                                    el build
python -m scripts --reuse                                            el build, y reuse lint
python -m scripts --piso                                             el estado, que va a estado.md
python -m scripts --escribe forma                                    arregla la forma
python -c "from scripts.repo import estado; print(estado.comparar())"
python -c "from scripts.repo import bloques; print(bloques.mapa('la obra/teoria/el piso.md'))"
python -c "from scripts.repo import encabezados; print(encabezados.mapa())"
python -c "from scripts.repo import enlaces; print(enlaces.mapa())"
```

Y el orden en que se partirán los ensayos: `teoria/` primero, que es la que más se va a
manipular; `humanidad/` es del autor; y `metodologia/` al final.
