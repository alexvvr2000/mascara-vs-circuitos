# El aproximado para terminar lo que se empezó

**Cuánto falta, medido con lo que ya se hizo.** **Y el número, dicho con lo que se sabe y con lo que no.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **2026-11-08.**

---

## Lo que ya se hizo, y con eso se estima

**Trece mutantes corridos.** **Y los trece se hicieron igual, así que cada uno costó lo mismo y se puede medir.**

| Lo que hay | Cuánto | De dónde sale |
|---|---|---|
| **reglas contadas** | **486** | los catorce ensayos, contados por renglón de proceso, bloque y afirmación |
| **mutantes corridos** | **13** | uno por familia, y todos murieron |
| **código por mutante** | **~123 líneas de Python** | 1,606 líneas entre los trece |
| **calidad del dato** | **buena para el código, mala para el tiempo** | el código se cuenta; el tiempo no se apuntó |

---

## El aproximado

**Y se da de dos maneras, porque hay dos preguntas distintas.**

### Si se corre una regla por una

```plaintext
486 reglas
  13 corridas
─────
473 por correr

a ~123 líneas cada una      58.179 líneas de código
y a una corrida por renglón 473 corridas
```

**Y a un ritmo de diez o quince por sesión, que es lo que se sostuvo hoy:**

```plaintext
        473 ÷ 10  =  47 sesiones
        473 ÷ 15  =  32 sesiones
```

**Entre treinta y cincuenta sesiones.** **Y cada sesión es un día de trabajo de este tamaño, no un rato.**

### Si se acepta lo que la tabla de inclusión encontró

**De las 486, 25 no afirman nada de un ente y no tienen mutante.** **Quedan 461.**

**Y de esas, la inclusión mata cero:** **cada regla es su propia madre.** **Así que la cuenta no baja por ahí.**

**Y hay una tercera opción, que es la honesta y hay que decirla:**

```plaintext
no se corre una regla por una, y se dice que no se corrió
se corre un mutante por familia (13, ya hechos)
y se declara que 461 reglas quedan sin probar
```

**Eso ya está hecho, y el repositorio lo dice.** **La pregunta es si se quiere cerrar el hueco o declararlo.**

---

## El número que importa, y no es el de las reglas

**Porque correr 473 mutantes no es lo que falta.** **Lo que falta es esto, y no se mide en mutantes:**

| Lo que falta | Cuánto |
|---|---|
| **los mutantes** | **entre 30 y 50 sesiones** |
| **la segunda mitad de la tabla de inclusión** | **12 familias por revisar, media sesión** |
| **el código de la implementación** | **no se estima: no se empezó** |
| **que alguien que no sea el autor lo levante** | **no tiene estimación, y no depende del trabajo** |

**Y las dos últimas no tienen número porque no hay con qué sacarlo.** **Decir «dos semanas» sería inventar, y el repositorio no lo va a hacer.**

---

## Lo que este aproximado no dice

- **No dice cuánto se tarda.** **El tiempo no se apuntó en ninguna de las dieciocho corridas, y estimarlo de memoria es lo que el repositorio prohíbe.**
- **No dice cuántos mutantes van a sobrevivir.** **Los trece murieron, y eso puede significar que las reglas tienen dientes o que los mutantes los escribió quien sabía la respuesta.**
- **Y no incluye lo que puede salir de los mutantes que sobrevivan**, porque si sobrevive uno, el hueco que abre no tiene tamaño conocido.

---

## Y lo que se recomienda para la parte que viene

**Cada stack es un mundo, y meter un ente en uno que no se conoce es trabajo de semanas.** **Y hay gente que sólo quiere trabajar rápido.**

**Así que la recomendación, y es una sola:**

> **Busca antes de construir. Y busca en internet, no en la memoria.**

**Y por qué:** **las piezas cambian de versión, cada una tiene su forma de instalarse, y la que sirve hoy no es la que sirvió hace un año.** **Un stack mal elegido cuesta más que el trabajo que iba a ahorrar.**

**Lo que hay que buscar, en este orden:**

| Antes de | Buscar |
|---|---|
| **elegir motor** | qué harness se puede instalar hoy, y cuál deja que el rastro viva fuera de él |
| **elegir base** | si el índice es un grafo, qué base de grafos es embebida y tiene binding para el lenguaje que ya se usa |
| **elegir catálogo** | cómo llega una implementación a otras manos sin que el usuario compile nada |
| **meter el ente** | cómo lee ese stack sus archivos de instrucciones, y con qué nombre exacto |
| **y al final** | si eso se puede instalar en una máquina limpia, y en cuánto tiempo |

**Y la regla que lo cierra:** **si no se puede instalar en una máquina limpia siguiendo lo que se encontró, lo que se encontró está viejo.** **Se busca otra vez, y no se rellena con lo que uno creía.**

---

## Falsificador

**Un aproximado sin número, o con un número que nadie midió.** **Y una recomendación que dice «investiga» sin decir qué buscar.**

**El de esta página, dicho sin adornos:** **el código se midió, y el tiempo no.** **Así que el número de líneas es real y el de sesiones es una cuenta sobre el ritmo de un día, que puede no ser el ritmo de un mes.**
