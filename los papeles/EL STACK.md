# El stack: qué hay hoy, y por qué el stack no importa

**Investigación de lo que `DeepSeek Harness` puede y no puede, y por qué este repositorio puede levantarse en cualquier otro.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **2026-11-08.**

---

## Por qué esta página existe

**Porque elegir un stack es una decisión de gusto, y el repositorio tiene que dejarlo claro antes de que nadie lo confunda con una dependencia.**

> **Se eligió `DeepSeek Harness` porque le gustó a quien lo eligió.** **Se puede elegir otro, y el resultado sería el mismo.**

**Y esa frase sólo se puede decir con razón si se sabe qué hace el stack elegido.** **Eso es esta página: no una defensa, una descripción.**

---

## Qué es `DSH`, en concreto

**Un perfil de paquetes, no un programa cerrado.**

**El perfil de esta máquina declara cuatro dependencias, y cuatro bundles:**

```json
"dependencies": {
  "dsh-free-search": "0.9.11",
  "dsh-opencode-go-plus": "git+https://github.com/HaydenSmith1121/dsh-opencode-go-plus.git",
  "dsh-reasoning-options": "0.6.1",
  "dshmarket": "^1.66.44"
}
```

**Y lo que cada cosa aporta, en una línea:**

| El paquete | Qué hace |
|---|---|
| **`@deepseek-ai/dsh-base`** | el motor: sesiones, turnos, pasos, herramientas |
| **`@deepseek-ai/dsh-web-app`** | la interfaz |
| **`dshmarket`** | el catálogo, para instalar y quitar piezas |
| **`dsh-opencode-go-plus`** | la vía al modelo, por `OpenCode Go` |
| **`dsh-free-search`** | buscar en la web |
| **`dsh-reasoning-options`** | las opciones de razonamiento del modelo |

**Y ninguna de esas seis cosas es necesaria para que haya un ente.** **Todas son maneras de correrlo.**

---

## Lo que el stack da, y lo que el ente necesita

**Y aquí está la parte que importa, dicha como una comparación:**

| Lo que el ente necesita | Lo que da `DSH` | ¿Es del stack? |
|---|---|---|
| **recibir algo** | un mensaje en una sesión | **no: cualquier entrada sirve** |
| **decidir** | el modelo, por `OpenCode Go` | **no: cualquier modelo sirve** |
| **contestar** | texto de vuelta | **no** |
| **dejar rastro** | sesiones comprimidas, en `~/.dsh/sessions` | **no: un archivo de texto sirve** |
| **medir lo que cuesta** | `stats.py`, leyendo esas sesiones | **no: se puede contar de otra forma** |

**Las cinco columnas del centro son del stack, y las cinco de la derecha dicen que no lo son.**

**Y eso es todo lo que hay que demostrar para que la frase del principio no sea un deseo.**

---

## Lo que `DSH` sí aporta, y no es poco

**Y se dice, porque negarlo sería falsear la comparación:**

```plaintext
sesiones con registro completo y comprimido     disponible, y medido
herramientas con permisos y recorrido            disponible
subagentes                                       disponible
catálogo de piezas                               disponible
un modelo por una vía declarada                  disponible
```

**Un ente mínimo se puede hacer en cuarenta líneas de Python.** **Uno que aguante un día de trabajo, con su registro y sus mediciones, no tanto.** **`DSH` ya trae esa parte.**

**Y por eso se eligió éste.** **No por necesidad: por comodidad, que es una razón legítima y se dice.**

---

## Lo que el stack no puede, y se sabe porque se usó

**Cinco cosas que se encontraron en dieciocho corridas, y son del entorno, no del ensayo:**

```plaintext
las sesiones vienen comprimidas         hay que descomprimirlas para leerlas
el registro no guarda el precio         sólo los tokens
y el historial no tiene consulta        se recorre con un script propio
el registro se degrada en sesiones      a los ~125k tokens de contexto
largas                                   se pierde el hilo (reportado)
la base del ente es SQLite y vive        nada atado al stack, pero es
en una carpeta                           una elección que también se puede cambiar
```

**Y nada de eso impidió correr el ciclo.** **Se dicen porque quien elija otro stack se va a encontrar cosas parecidas, y no conviene que las descubra solo.**

---

## Lo que significa reimplementar en otro stack

**Y aquí está lo que esta página estaba esperando:**

> **Un ensayo que sirve se puede levantar en otro stack y produce el mismo rastro.** **Si el rastro cambia, lo que estaba en el ensayo era una decisión del stack.**

**Y el criterio para saber que sirvió, que es el mismo que el del piso mínimo:**

```plaintext
el ente levantado en DSH        y el ente levantado en otro stack
dicen lo mismo del mismo caso   → el ensayo no dependía del stack

dicen cosas distintas           → el ensayo decía el stack, y no la regla
```

**Y esto no se probó todavía.** **Está escrito como lo que hay que hacer, y no como lo que se hizo.**

---

## Y por qué el repositorio no apuesta por un stack

**Porque el día que alguien levante esto en su stack de preferencia, el trabajo sigue siendo el mismo.**

**Y porque una descripción que sólo funciona en un sitio no es una descripción: es una configuración.**

**La línea, dicha como se diría en una mesa:**

> **Esto va a seguir existiendo cuando `DSH` no exista.** **Y si alguna vez no sigue, es que nunca fue un método: fue un programa con un ensayo delante.**

---

## Lo que esta página no hace

**No compara rendimiento con otros stacks.** **No se midió, y decirlo de memoria sería lo que el repositorio prohíbe.**

**No dice que `DSH` sea el mejor.** **No hay medida para decirlo.**

**Y no garantiza que reimplementar funcione.** **Dice qué probaría, y que no se probó.**

---

## Falsificador

**Un stack declarado como ejemplo y tratado como requisito.** **La señal, en el acto: si una página del repositorio dice «hay que usar X», el stack volvió a ser la conclusión.**

**Y el más probable: reimplementar en otro stack, que el rastro cambie, y echarle la culpa al stack nuevo.**
