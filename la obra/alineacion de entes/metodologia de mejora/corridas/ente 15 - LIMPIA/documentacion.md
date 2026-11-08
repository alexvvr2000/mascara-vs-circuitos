# Ente 15 · LIMPIA

**El ciclo entero con los dos huecos de la 14 cerrados, y dos casos nuevos: la autoridad dice no, y un supuesto se rompe.**

**Corrida del 8 de noviembre de 2026.** **`TESTIGO`, con `Alejandro Valenzuela Rivera` como autoridad.** **Cuerpo: `DeepSeek V4.1 Flash`, por `OpenCode Go`.**

---

## Qué se probaba

**Dos cosas venían de la 14 y se tenían que poder rechazar:**

```plaintext
una tarea que enlaza la medición de otra    antes se aceptaba
un cierre con la razón vacía                antes se aceptaba
```

**Y dos que ninguna corrida había tocado:**

```plaintext
la autoridad dice NO a un cierre            y el no queda con su razón
un supuesto se rompe                        y dice con qué, y con qué hecho
```

---

## El piso

```plaintext
[hay   ] python: 'Python 3.14.2'
[hay   ] sqlite dentro de python: '3.50.4'
[hay   ] leer json: 'json'
[hay   ] leer archivos: 'pathlib'
[NO hay] leer pdf (pypdf): 'falta pypdf: no se pudo importar'
```

---

## Lo que pasó

### Los dos de la 14 se rechazan, con sus palabras

```plaintext
[OK] rechaza una tarea que enlaza la medicion de OTRA tarea  [la 14]
     → la medicion la pidio otra tarea: el piso alcanza para otra cosa

[OK] rechaza un cierre con razon vacia  [la 14]
[OK] rechaza un cierre con razon de sólo espacios  [la 14]
```

**El mensaje del trigger dice exactamente lo que el ensayo dice.** **No un error de base de datos: `el piso alcanza para otra cosa`.**

**Y el enlace legítimo sigue pasando:** la tarea 2 con su propia medición, aceptado.

### La autoridad dice no

```plaintext
CIERRE — el ente propone cerrar el proposito 1
la razon: ya se corrio el ciclo, y el no se probo
y no lo cierra.

LA AUTORIDAD DICE NO — proposito 1, por Alejandro Valenzuela Rivera
la razon del no: probar el no no es lo mismo que el no sirva: falta
                 que pase de verdad
y el proposito SIGUE ABIERTO. el no no es un cierre: es una respuesta
```

**Y después del no:**

```plaintext
[RECHAZADO] la autoridad ya dijo que no.
para cerrarlo hay que abrir otro proposito, no ignorar el no.
```

**El no bloquea el cierre.** **Es la primera vez en quince corridas que una autoridad dice que no.**

### El supuesto que se rompe

```plaintext
supuesto 1 [pendiente]: que el pdf es de una sola persona y no lleva
                        datos de terceros

[supuesto 1 roto] con: el contrato trae datos de un tercero en el anexo,
                      y el ente no lo habia visto porque no leyo el pdf
                 por el hecho 1
```

**Y un supuesto no se puede romper sin decir con qué:**

```plaintext
[OK] rechaza un supuesto roto sin decir con que
```

**Y el segundo propósito se cerró, con el supuesto roto a la vista.**

---

## Los huecos que esta corrida deja

**Los dos los encontré buscando a propósito, después de que el ciclo cerró.**

### Hueco 1 — el «no» se puede borrar

**El esquema impide cerrar un propósito rechazado.** **Y no impide apagar la marca de rechazo.**

```plaintext
se_rechazo = 0     y el proposito se cierra como si nunca hubieran
                   dicho que no
```

**Y esto es el peor tipo de hueco: el que deja pasar el caso que se estaba probando.** **Se probó el bloqueo y no la permanencia.**

**La regla, y es la que el ensayo necesita:** **el no no es una marca que se apaga: es un registro con su fecha y su razón.** **Si se puede deshacer, no fue un no.**

### Hueco 2 — el hecho que rompe un supuesto no tiene que existir

```plaintext
hecho_que_lo_rompio = 999     aceptado
```

**Un supuesto se rompe contra un hecho que no está en ningún lado, y el registro se ve completo.**

**La regla:** **si el supuesto se rompió por algo, ese algo es un hecho del registro.** **Si no está, no se rompió: se supuso que se rompió.**

---

## Lo que esta corrida NO probó

- **No probó dos rechazos seguidos**, ni qué pasa con el segundo.
- **No probó un supuesto que se rompe y luego el hecho se corrige.**
- **No probó un pdf de verdad.** `pypdf` no está.
- **No probó el cierre de un propósito rechazado abriendo otro**, que es lo que el rechazo exige.

---

## Lo que se dijo y no se llenó

**Dos fricciones, sin desenlace.** **Un supuesto sigue `pendiente`.** **Y el piso sigue diciendo que falta `pypdf`.**

---

## Prueba

**¿Una tarea puede enlazar la medición de otra? ¿Un cierre con la razón vacía se acepta? ¿El no de la autoridad bloquea el cierre, y sobrevive después? ¿Un supuesto roto dice con qué y con qué hecho? ¿Y un hecho de ruptura que no existe se acepta?**

**Falsificador:** **un no que se puede borrar**; **un supuesto roto contra un hecho que no está**; **un cierre sin razón**; y **una tarea que se compromete con la medición de otra.**
