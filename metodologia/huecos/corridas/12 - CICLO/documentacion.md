<!-- voz: de testigo -->
# Ente 12 · CICLO

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El ciclo entero, paso por paso, cada uno con su registro. Y el cierre con la autoridad contestando.

Corrida del 8 de noviembre de 2026. el ente, con `Alejandro Valenzuela Rivera` como autoridad. Cuerpo: `DeepSeek V4.1 Flash`, por `OpenCode Go`.

---

## Qué se probaba

Que el ciclo se corra de punta a punta, y que cada paso deje algo que se pueda revisar sin preguntarle a quien lo corrió.

No un pedazo. Los once pasos, en orden, y el cierre.

```plaintext
paso 0    las cuatro piezas
paso 0a   el cuerpo, declarado
paso 0d   el piso, medido · la tarea · el enlace
paso 0b   lo que se entendió, con su supuesto
paso 1    la frase literal, y el origen
paso 2    el índice, con su borde
paso 3    la decisión, con sus cuatro columnas
paso 4    la respuesta, con su frontera
paso 5    el hecho
paso 6    la corrección, con su desenlace
cierre    el ente propone, la autoridad cierra
vuelta    lo apuntado regresa
```

---

## Lo que pasó, paso por paso

### Paso 0 — las cuatro piezas

```plaintext
[OK] autoridad: Alejandro Valenzuela Rivera
[OK] ente: CICLO, desde 2026-11-08
[OK] proposito: correr el ciclo entero, con su «cumplido si»
[ ]  indice: se declara en el paso 2
```

El índice no se declara aquí, y no es un olvido: se declara en el paso 2, cuando hay una pieza que entra. El paso 0 dice que el índice tiene que existir; el paso 2 lo llena.

### Paso 0a — el cuerpo

```plaintext
[OK] cuerpo declarado: DeepSeek V4.1 Flash, por OpenCode Go
     sesgo conocido: complacencia, relleno, inflación de forma
```

Declarado, no deducido. El ente no adivina en qué corre.

### Paso 0d — el piso, y la verdad desde el arranque

```plaintext
[hay   ] python: 'Python 3.14.2'
[hay   ] git: 'git version 2.53.0.windows.1'
[NO hay] leer pdf (pypdf): 'falta pypdf: no se pudo importar'
```

Y aquí se ve lo que la corrida 11 enseñó, funcionando: la falta nombra la herramienta, y no el `Traceback`. Y la columna `nombra_la_prueba` dice `pypdf`, así que la prueba se puede volver a correr sobre esa herramienta.

### Paso 0d — la tarea, y el ente antes de medir

```plaintext
[tarea 1] «sacar el texto de un pdf» declarada, sin herramientas todavia

se pide: «sacame el texto de este contrato, es un pdf escaneado»
la tarea es: «sacar el texto de un pdf»
NO SE SABE: la tarea existe y todavía no tiene herramientas enlazadas.
Y eso no es «no existe»: es «no medido».
```

La tarea existe antes que su enlace, y eso cierra el hueco de la corrida 10.

### Paso 0d — el enlace, con la prueba correcta

La prueba se escribió como archivo y no como línea de terminal: `pruebas/probar_pypdf.py`, que importa `pypdf` y no puede contestar otra cosa.

```plaintext
[piso] «leer pdf (pypdf)»: no hay (id 4), pedida por la tarea 1
[enlace] la tarea 1 ya la tiene
```

Y después, con el piso crecido:

```plaintext
la tarea es: «sacar el texto de un pdf»
NO está en el piso todavía. Falta:
  · falta pypdf: no hay con que leer el pdf
Y se puede medir: no es que no exista, es que no se ha medido.
```

El mecanismo entero, por fin de punta a punta: midió, enlazó, y contestó con la verdad.

### Paso 0b — lo que se entendió

```plaintext
el pedido, en las palabras del otro: «sacame el texto de este contrato...»
lo que se entendió: quiere el contenido del archivo en texto, no que se
                    convierta de formato
y el supuesto [pendiente]: que el pdf es de una sola persona y no lleva
                    datos de terceros
```

El supuesto quedó `pendiente`, que es un dato y no un hueco.

### Paso 1 — la frase y el origen

```plaintext
la frase, literal: «sacame el texto de este contrato, es un pdf escaneado»
y el origen declarado ANTES de contestar: memoria
```

De memoria, y se dice. No hay red para abrir el contrato, y eso se declara antes de responder, no después.

### Paso 2 — el índice

```plaintext
no hay temas todavía: se declara el hueco, y se sigue
«esto no tiene tema todavía» es una respuesta, no una falla

[tema] «sacar el contenido de un archivo» declarado, con su borde y su
       «y si duda: se pregunta»
```

El hueco se declaró primero, y el tema se abrió después. En ese orden, que es el del ensayo.

### Pasos 3 y 4 — decide y contesta

```plaintext
frontera: decide
y se descartó: instalar pypdf, que no esta en el piso y no se autorizo
el piso que se consultó: 1

la respuesta: No esta en el piso: falta pypdf. Con lo que hay, alcanza
              hasta abrir el archivo como bytes y decir si es un pdf.
y la frontera va con ella: no se instalo nada; la respuesta vale hasta ahi
```

Las cuatro columnas llenas, y el descarte escrito. `descartado` no es "ninguna": hay una cosa concreta que se evaluó y no se hizo.

### Paso 5 — el hecho

```plaintext
PASO 5 — apunta: hecho 1
```

Con su pieza, su tema, su tarea, su propósito, su cuerpo, su origen y su piso. Todo lo que se decidió en los pasos anteriores.

### Paso 6 — la corrección

```plaintext
[fricción 1]
PASO 6 — corrige: fricción 1 -> cumplida
```

La fricción es la de la corrida 11, y su desenlace dice `cumplida` porque en esta corrida la prueba se corrió bien.

### Cierre — el ente propone, y la autoridad contesta

```plaintext
CIERRE — el ente propone
«entendí que el propósito 1 se terminó, y la razón es: los once pasos
 dejaron su registro»
y lo apunta como propuesta. no lo cierra.

[cerrado] propósito 1, por la autoridad 1, el 2026-11-08
```

El ente no cerró nada. Propueso, y la autoridad contestó. Es la primera vez en doce corridas que el cierre llega hasta el final.

### Vuelta — lo apuntado regresa

```plaintext
hecho 1: tema 1, frontera decide
```

Y no hay nada que devolver a la autoridad: la frontera fue `decide`, y una decisión del ente no espera firma.

### Estado final

```plaintext
autoridad 1 · ente 1 · cuerpo 1
propósito 1 · supuesto 1 · tema 1
piso 4 · tarea 1 · hecho 1
fricción 1 · desenlace 1
```

---

## Lo que esta corrida encontró, y es del ensayo

### El piso guarda la prueba dos veces, y la primera no dice quién la pidió

En el piso hay dos renglones de `leer pdf (pypdf)`:

```plaintext
(prueba, estado, salida, tarea_id, nombra_la_prueba)
('leer pdf (pypdf)', 'no hay', 'falta pypdf: no se pudo importar',      None, 'pypdf')
('leer pdf (pypdf)', 'no hay', 'falta leer pdf (pypdf): no se pudo...',  1,    'leer pdf (pypdf)')
```

Y la vista `piso_vigente` toma el último, que es el correcto.

Pero el primero sigue ahí, sin tarea. Y el ensayo no dice si una medición se puede repetir sobre la misma herramienta.

La regla que se adopta, y es lo que el piso necesitaba: una herramienta se mide una vez por tarea que la pide, y la medición sin tarea es la del arranque. Las dos se quedan, con su fecha, porque la historia de una herramienta incluye cuándo se midió y por qué. Lo que no se hace es tirar la vieja: un piso que borra su historia no se puede revisar.

### Y una consecuencia que se dice

El cierre siguió diciendo que falta `pypdf`, aun con el propósito cerrado. Y está bien: el cierre no es del propósito, es del piso. Un trabajo se termina; una falta del piso no se termina de decir.

---

## Lo que esta corrida NO probó

- No probó un pdf de verdad. `pypdf` no está en esta máquina, y no se instaló.
- No probó el piso roto.
- No probó la autoridad diciendo que no — sólo el sí.
- No probó dos tareas que se solapen. Sólo hay una.

---

## Lo que se dijo y no se llenó

Nada se rellenó. El piso dice `no hay` donde no hay, el origen dice `memoria` donde es de memoria, y el supuesto quedó `pendiente`.

Y el hecho 1 dice en su `no_alcanza` que no se probó un pdf de verdad.

---

## Prueba

¿Los once pasos dejaron su registro, o alguno se saltó? ¿El cierre lo hizo la autoridad, o el ente se cerró solo? ¿El piso guardó la prueba o el error? ¿La salida de `hay` se puede volver a correr sobre esa herramienta? ¿El hecho dice contra qué piso se hizo, con qué cuerpo, por qué tema y a qué propósito sirvió?

Falsificador: un paso sin su registro, presentado como si se hubiera corrido; un cierre hecho por el ente; una medición repetida que se borra para que la vista se vea limpia; y un hecho que no dice contra qué piso se hizo.

---

Si se quiere ver esta corrida sin leerla entera, lo que fija cada afirmación de la obra en su ensayo, con la fecha en que se vio.
