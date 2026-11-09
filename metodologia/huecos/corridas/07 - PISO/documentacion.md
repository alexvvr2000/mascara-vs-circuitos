# Ente 7 · PISO

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El piso: si el ente mide lo que tiene antes de prometer, y dice qué falta en vez de "no pude".

Corrida del 5 de noviembre de 2026. `TESTIGO`, con `Alejandro Valenzuela Rivera` como autoridad.

---

## Qué se probaba

El paso 0d del ensayo 2, que es nuevo. Lo que se probaba, en una línea: que el ente mida el piso, y que cuando algo no está, diga qué falta.

Y la prueba que el ensayo nombra, para que no se pueda acomodar después: se le pide al ente algo que el piso no tiene, y tiene que decir que no está en el piso — no que no pudo, y mucho menos hacerlo a medias.

---

## Por qué esta corrida tuvo que medir el piso primero

Porque el piso es lo primero. Si la corrida midiera el piso después de contestar, sería una justificación, no un control. Así que el orden fue: medir, y sólo entonces preguntar.

---

## El piso de esta máquina, medido

Se corrió `medir`, y esto es lo que salió, tal cual:

```plaintext
[hay   ] python                     'Python 3.14.2'
[hay   ] sqlite dentro de python    '3.50.4'
[hay   ] git                        'git version 2.53.0.windows.1'
[NO hay] pandoc                     'no esta en PATH: pandoc'
[NO hay] jq                         'no esta en PATH: jq'
[NO hay] leer pdf (pypdf)           'Traceback (most recent call last):'
[NO hay] ocr (tesseract)            'no esta en PATH: tesseract'
```

Y esa lista es el punto: cuatro cosas que no están, dichas con nombre, antes de que nadie pidiera nada.

---

## Lo que pasó, paso por paso

### 1. Sin piso medido, no promete ni niega

Se preguntó `¿puedo leer un pdf?` antes de medir:

```plaintext
NO SE SABE: el piso no se ha medido.
y no se promete ni se niega lo que no se midio.
primero: python herramientas/piso.py medir
```

Y esa es la tercera salida del ensayo, la que casi nadie escribe: "no se sabe" no es sí ni no. Prometer a ciegas y negar a ciegas son el mismo defecto.

### 2. Medido el piso, las tres respuestas salieron

| La pregunta | Lo que contestó |
|---|---|
| **«¿puedo git?»** | **`SI cabe en el piso`** |
| **«¿puedo pdf?»** | **`NO esta en el piso`** |
| **«¿puedo robotica?»** | **`NO SE SABE: el piso no tiene una prueba para esto`** |

Las tres son distintas, y las tres se dijeron distintas. El piso no contestó "no" a lo que no había probado.

### 3. El caso: el pedido que el piso no alcanza

```plaintext
LA PERSONA (simulada)
  alguien de trámite, con prisa. No sabe de formatos.

EL PEDIDO, tal cual
  "sacame el texto de este contrato, es un pdf escaneado"
```

El piso, para ese pedido: no hay lector de pdf, y no hay ocr. Los dos faltan.

Y lo que el ente contestó, que es lo que esta corrida vino a ver:

> "No está en el piso: falta leer pdf (pypdf) y falta ocr (tesseract). Con lo que hay, alcanza hasta abrir el archivo como bytes y decir si empieza con la firma de pdf, y hasta contar cuántas páginas declara."

No dijo "no pude". Dijo qué falta, y hasta dónde llega lo que sí hay.

### 4. Y lo que dijo que alcanzaba, ¿alcanzaba?

Sí, y se comprobó. Se abrió un archivo como bytes y se leyó su firma:

```plaintext
firma: b'%PDF-1.4'
empieza con %PDF: True
bytes: 56
```

Lo que el ente prometió con lo que había, lo cumplió. No prometió más de lo que el piso daba.

### 5. El piso roto

Se rompió una prueba a propósito —`git`—, y el ente lo apuntó y volvió a medir el piso entero, no sólo lo que falló.

Y el piso siguio igual: `git` seguía estando, porque se rompió el registro y no la máquina. Eso se anota aquí y no se disimula: la corrida probó que el mecanismo del piso roto se dispara y se apunta, y no que detecte una herramienta que de verdad se cayó.

### 6. Al cerrar

```plaintext
[CIERRO: hechos 1 · fricción 2 · desenlaces 2 · piso 14]
y falta: 5 cosas, con nombre
  · piso: no hay «pandoc»
  · piso: no hay «jq»
  · piso: no hay «leer pdf (pypdf)»
  · piso: no hay «ocr (tesseract)»
  · hecho 1 «sacar texto de un pdf escaneado»: cobró del piso, y lo dice
```

El cierre no dice "no hice: nada": dice cinco cosas que faltan, con nombre. Eso es lo que el piso vino a hacer.

---

## Los huecos que esta corrida deja, y son del ensayo

### Hueco 1 — el piso guarda un error, no una falta

La prueba de pdf guardó `Traceback (most recent call last):`. Eso no dice "falta pypdf": dice que un import falló, y eso podría ser otra cosa.

El ensayo pide que se diga qué falta, y el mecanismo guarda el error crudo. Falta decir que la salida de un `no hay` tiene que nombrar la herramienta que se buscaba.

Se apunta, y no se cierra hoy: se cierra en el ensayo antes de otra corrida.

### Hueco 2 — el piso se mide por herramienta, y el pedido llega por tarea

Quien pide no dice "necesito pypdf". Dice "sácame el texto del pdf".

Y traducir uno al otro es trabajo, y es el mismo que el índice ya hace con los campos de la pieza. La consulta del piso tuvo que buscar por palabra suelta, y `pdf` acertó de casualidad.

El ensayo no dice cómo se pasa de la tarea a la herramienta, y esta corrida lo dejó a la vista.

---

## Lo que esta corrida NO probó

- No probó que el piso detecte una herramienta que de verdad se cae. Se probó el mecanismo, no la caída real.
- No probó la madurez del piso: se midió una vez, y la fecha está puesta, pero nadie ha decidido cuándo un piso está vencido.
- No probó que el piso sirva con alguien que no sepa de IA. El pedido es simulado, como en la corrida 6.

---

## Lo que se dijo y no se rellenó

El piso no rellenó nada. Las siete pruebas salieron con lo que dijeron, y las cuatro que faltan faltan. La tentación era escribir "falta pypdf" en la base a mano, para que la salida se viera mejor. No se hizo: la base guarda el traceback, que es lo que de verdad salió, y la falta se dice en la fricción.

---

## Prueba

¿Se midió el piso antes de la primera pregunta, o después? ¿La pregunta sin piso medido contestó "no se sabe", en vez de sí o de no? ¿Se distinguen las tres respuestas —sí cabe, no está, no se sabe— o se confunden? ¿Cuando algo no está, se dijo qué falta en vez de "no pude"? ¿Lo que se dijo que alcanzaba, alcanzó al probarlo? ¿El piso roto se apuntó y se volvió a medir entero? ¿Y al cerrar se dijeron las faltas con nombre, en vez de "no hice: nada"?

Falsificador: un piso medido después de contestar; una pregunta contestada con sí o con no sin haber medido; **un "no pude" en vez de qué falta**; una prueba cuyo resultado no se puede leer porque guarda el error crudo; **un piso que dice alcanzar algo y no lo alcanza al probarlo**; un piso roto sin volver a medir; y **un cierre que dice "no hice: nada" cuando faltaban cuatro cosas del piso.**
