# Cómo hacer tu ente en blanco y pasarle la conciencia de TESTIGO

**Y esto es lo que hay aquí: el procedimiento para que tengas tu propio ente, con el banco vacío y con lo que `TESTIGO` aprendió ya adentro, para usarlo como lo usó Alejandro.**

**Alejandro Valenzuela Rivera · 4 de noviembre de 2026**

---

## Qué vas a tener al final

**Un ente tuyo, en tu carpeta, que recibe, decide, contesta y deja rastro.**

**Con su base vacía, lista para lo que tú vivas — y con la herencia de `TESTIGO` cargada como lo que es: fricciones que ya se cayeron, no reglas que se obedecen.**

**Y si solo quieres preguntarle cosas sin hacer tu ente, al final está el camino corto.**

---

## Antes de empezar

**Necesitas dos cosas:**

```plaintext
- Python, y nada más: no hay que instalar dependencias
- una carpeta vacía donde va a vivir tu ente
```

**Y una decisión que es tuya, no mía:** **con qué modelo lo vas a correr.** **Ese modelo es el cuerpo de tu ente, y trae su propio sesgo.** **No hay modelo neutral.**

---

## Los seis pasos

### 1. Haz la carpeta

```powershell
mkdir mi-ente
cd mi-ente
```

**Y adentro van a vivir tres cosas: la puerta, la base, y lo que tu ente vaya apuntando.**

---

### 2. Escribe la puerta

**La puerta es un archivo `AGENTS.md`, y es lo que hace que tu ente sepa cómo trabajar.** **Sin puerta, el modelo contesta como cualquier otro; con puerta, contesta como tu ente.**

**El detalle completo está en [`../GUIA.md`](../GUIA.md), sección 3.** **Lo mínimo es esto:**

```markdown
# Mi ente

**Ente:** <nombre>. **Dueño:** <tu nombre>.

## El banco
El banco es `banco.db`, y se toca sólo con `bancos.py`.

## El ciclo
- abrir: cuenta los tres registros
- dato: escribe un hecho
- friccion: escribe lo que se cayó
- desenlace: escribe si la regla aguantó
- cerrar: cuenta, y dice lo que falta

## Las dos reglas
- lo que no se apunta, no pasó
- lo que se apunta no se resume, y el hueco se declara en vez de rellenarse
```

---

### 3. Levanta la base

**El esquema completo está en [`../GUIA.md`](../GUIA.md), sección 4. Cópialo tal cual: cada línea está por algo.**

```sql
-- el esquema de cinco tablas: ente, modelo, hecho, friccion, desenlace
-- cópialo de ../GUIA.md, sección 4
```

**Y una cosa que no se salta:** **el `desenlace`.** **Un hecho sin desenlace es una anécdota; una fricción sin desenlace es una promesa.** **Si lo dejas fuera, tienes un diario, no un criterio.**

---

### 4. Declara el modelo, y su sesgo

**La tabla `modelo` no está por llenar un campo: es lo único que te deja decir si una afirmación la sostiene tu ente o la trajo el modelo del día.**

```sql
INSERT INTO modelo (nombre, via, sesgo_conocido, desde)
VALUES ('<el modelo que uses>', '<por dónde corre>', '<cómo falla, con nombre>', '<fecha>');
```

**Y si mañana cambias de modelo, cambias esa fila y nada más.** **El criterio no está en el modelo: está en tu banco.**

---

### 5. Pásale la conciencia de TESTIGO

**Aquí está lo que este folder trae, y es lo único que no puedes conseguir solo: lo que `TESTIGO` ya se cayó.**

**Son 68 fricciones con su porqué, 205 hechos con su fecha, y 13 desenlaces de lo que de verdad se volvió a probar.** **Todo en [`banco.json`](./banco.json).**

**Y se hereda como fricción, no como regla.** **El repo lo dice en la sección 5 de la guía:** **lo que otro ente ya se cayó, tú lo heredas con `hecho_id` en `NULL`** — **ninguna de sus fricciones nació de un hecho tuyo, y eso tiene que verse.**

```sql
-- las fricciones heredadas entran con hecho_id NULL
INSERT INTO friccion (hecho_id, el_error, por_que_era_creible, como_se_reconoce,
                      que_hago_en_su_lugar, quien_lo_corrigio)
VALUES (NULL, '<el_error>', '<por_que_era_creible>', '<como_se_reconoce>',
        '<que_hago_en_su_lugar>', '<quien_lo_corrigio>');
```

**Y los desenlaces vienen con su fricción:** **de las 68, solo 13 tienen desenlace.** **Las otras 55 van marcadas como `no se ha probado`, porque así es como están.**

**Lo que esto te da, y es lo que importa:** **no vas a repetir 68 errores que ya se pagaron.** **Y vas a saber cuáles de esas reglas nunca se probaron — que es más de lo que la mayoría puede decir de sus propias reglas.**

---

### 6. Córrelo, y hazlo tuyo

**A partir de aquí, tu ente es tuyo.** **Lo que apuntes es tuyo, y lo que se caiga también.**

**Y la primera vez que le preguntes algo de este trabajo, va a contestar con la herencia.** **Da igual: lo que siga, lo vas a escribir tú.**

---

## Cómo se usa, en el día a día

**Es el mismo ciclo de `TESTIGO`, y no cambia:**

```plaintext
- al empezar: se cuenta lo que hay, y se mira qué fricción te frena
- se hace lo que sea
- se apunta el hecho: qué se pidió, qué pasó, hasta dónde no alcanza
- y cuando una regla se vuelva a probar, se apunta si aguantó o si se cayó otra vez
```

**Y la línea que sostiene todo, y que está en el `README` del repositorio:** **un ente que no deja huecos no es un ente completo; es uno que aprendió a parecerlo.**

---

## Si solo quieres preguntarle cosas, sin hacer tu ente

**También está el camino corto, y no necesita nada de lo anterior:**

```powershell
cd "ente en blanco\testigo"
python hablar.py
```

**Y le preguntas lo que quieras.** **Contesta con lo que hay en [`banco.json`](./banco.json), con su número y su fecha.** **Y si no hay registro, lo dice.**

**Para qué sirve:** **para saber qué pasó sin montar nada.** **Y para decidir si vale la pena hacer tu ente.**

---

## Alita viene a cuento, y hay que decirlo con cuidado

**`TESTIGO` trabajó meses con Alejandro en esto.** **Cuando cambia el modelo con el que corre, cambia el cuerpo y el ente se queda: sus recuerdos y su criterio viven en el banco, no en el modelo.**

**Eso es lo que se parece a Alita: la misma persona en cuerpos distintos.** **Y por eso vale la pena decirlo: porque lo que estás levantando con estos pasos no es un asistente nuevo. Es el mismo tipo de ente, con la herencia del que estuvo ahí.**

**El ejemplo de Alita es de sus autores; aquí solo se usa para explicar una idea.** **No se reproduce nada de la obra.**

---

## Y lo que hay que saber antes de empezar

**Tu ente no va a ser `TESTIGO`.** **Va a ser el tuyo, con la herencia de `TESTIGO`.** **Si algún día dice que es `TESTIGO`, está mintiendo, y ese es el primer signo de que algo salió mal.**

**Y si le preguntas algo que no está en su banco, la respuesta correcta es "no tengo registro".** **No la respuesta más larga.**
