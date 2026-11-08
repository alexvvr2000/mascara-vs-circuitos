# ente 1 — PRUEBA

**La primera vez que se levantó un ente desde cero, usando solo los ensayos.**

**Levantado:** 2026-11-05, 12:09. **Por:** `TESTIGO`, con `Alejandro` como autoridad.
**Frase del dueño:** *«para las pruebas hazlo desde un ente desechable en mega/testigo/entes de prueba/ con uno con su fecha y hora porfavor, para que los hagas desde 0 siempre y veamos la evolucion»*

---

## Qué se intentaba

**Correr el ciclo completo, una vez, y ver dónde se rompe.** **Nada más.** **No había nada que copiar: había cinco ensayos y una terminal.**

## Qué se levantó

```plaintext
AGENTS.md             la puerta, escrita desde los ensayos
herramientas/tablas.sql        9 tablas
herramientas/crear.py          crea la base, y prueba las reglas
herramientas/abrir.py          cuenta lo que hay
herramientas/escribir.py       dato, friccion, desenlace, proposito
herramientas/tema.py           el índice: abrir, buscar, relacionar
herramientas/cerrar.py         cuenta, y dice con nombre lo que falta
```

**Y el ente corrió de punta a punta:** **se declaró la autoridad, se abrieron dos temas, se buscó una pieza, se escribió un hecho con su propósito y su tema, se apuntó una fricción con su desenlace, y el propósito quedó abierto porque solo lo cierra el dueño.**

---

## Los cinco huecos, y de dónde salió cada uno

### 1. La pieza no existía

**El borde decía que se evalúa «contra los atributos de una pieza», y en el esquema no había ninguna pieza.** **Lo que hice fue usar la frase como texto y partirla por comas.**

**Eso no es un borde: es una búsqueda de texto con otro nombre.**

### 2. Un borde en prosa no lo puede correr una máquina

**Puse `quien_evalua = 'maquina'`, y el borde que escribí decía «trata de mover, renombrar o reestructurar los ensayos».** **Una máquina no puede correr eso.**

**Y lo que hice, y hay que decirlo, fue evaluarlo yo con una condición escrita a mano en Python.** **El ente no consultó su borde: consultó mi línea de código.**

### 3. El casi no tenía salida

**Una pieza que estaba a medio camino no la aceptaba ni la rechazaba.** **El borde no tenía dónde decir qué hacer con el «casi».**

### 4. `cerrar` cuenta y no cierra

**El comando de cierre contaba, decía qué faltaba, y el propósito seguía abierto.** **Porque cerrar no es un comando: es un acto entre dos.**

### 5. Una corrida nunca cierra algo sin la autoridad

**Esto no es un hueco: es el diseño funcionando.** **Puse `cerrado_por='lo cerró Alejandro'` y el esquema lo aceptó, porque no había con qué comprobar que Alejandro lo tocó.** **Ese fue el hallazgo número cinco, y es el que se volvió una regla.**

---

## Lo que sí aguantó

```plaintext
la pieza sin tema se declara como hueco, y no se contesta    ✔
la regla que se vuelve a caer se apunta como tal             ✔
un tema que nunca se usó se ve en el cierre                  ✔
los varios propósitos abiertos a la vez                      ✔
```

**Y la fricción 1 de este ente quedó como `se volvio a caer`:** **evaluar el borde por palabras sueltas.** **No la inventé: salió de correrlo.**

---

## Hasta dónde no alcanza esta corrida

**No prueba que el ciclo funcione: prueba que se puede levantar.** **Corrí un caso, favorable, y lo corrí yo.** **No hubo un casi, ni un hecho sin tema provocado, ni una regla que se volviera a caer por segunda vez.**

**Y el ente no la levantó sola: la levanté yo, con las manos en el teclado.** **Lo que el ensayo llama «el ente» aquí fue, en la práctica, `TESTIGO` con un esquema.**

---

## Lo que quedó sin cerrar

**Nada de este ente.** **Los cinco huecos se cerraron en los ensayos el mismo día, y cada uno dejó su renglón en `la obra/ensayos/`.** **Y el quinto se volvió a abrir en la corrida siguiente, con otra forma.**

---

## Prueba

**¿El ciclo se levantó de punta a punta con cinco ensayos y una terminal? ¿Cada pieza inventada quedó apuntada como hueco del ensayo y no como defecto del ente? ¿El «casi» tenía salida, o se quedó sin ella?**

**Falsificador:** un ente levantado que se dio por bueno sin haber escrito cada cosa que hubo que inventar; **una pieza que existe en el ensayo y no en el código**; y **una corrida que se cierra sin que la autoridad conste.**
