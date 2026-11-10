# repo — el órgano del repositorio, en módulos

Este módulo es lo que me deja revisar el repo en una pasada: qué dice cada ensayo,
qué se probó y de qué ensayo sale, y si `estado.md` sigue diciendo la verdad. El resto
del órgano —las reglas, la legalidad y los trabajos que arreglan— sigue en el paquete,
y aquí no se repite.

```plaintext
repo/
  __init__.py   el mapa
  bloques.py    cada ensayo como una lista de bloques
  estado.py     que estado.md no envejezca
  hallazgos.py  de qué ensayo sale cada corrida
  readme.md     esto
```

---

## Qué es, y qué no

Es un **lector**: mira el repositorio y dice lo que ve. No escribe prosa, no reescribe
ensayos, y no decide nada: lo que encuentra lo dice, y lo que falta lo nombra.

Y no es el build: el build es `python -m scripts`, y sí se cae. Esto son las lentes que
el build usa de aquí en adelante, y que se pueden correr solas para mirar una cosa.

---

## En qué ayuda, concretamente

| Lo que hoy cuesta | Lo que hace el módulo |
|---|---|
| saber si una corrida apunta a su carpeta, y si su carpeta está en el índice | `hallazgos.revisar()` lo dice, corrida por corrida |
| que `estado.md` envejezca sin que nadie lo note | `estado.comparar()` lo compara con la orden, y el build se cae con el renglón |
| saber qué dice un ensayo de 400 renglones | `bloques.mapa()` da una línea por concepto |

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

---

## Cómo se corre

```plaintext
python -m scripts                        el build, que ya usa esto
python -c "from scripts.repo import estado; print(estado.comparar())"
python -c "from scripts.repo import hallazgos; print(hallazgos.revisar()[1][:5])"
python -c "from scripts.repo import bloques; print(bloques.mapa('la obra/teoria/el piso.md'))"
```

Y el orden en que se leerán los ensayos: `teoria/` primero, que es la que más se va a
manipular; `humanidad/` es del autor; y `metodologia/` al final.
