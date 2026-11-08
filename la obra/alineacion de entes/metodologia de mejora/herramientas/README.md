# `stats.py` — qué costó una sesión, en números medidos

**Lee el registro que `DeepSeek Harness` ya guarda, y saca lo que se puede contar sin adivinar.**

**Alejandro Valenzuela Rivera · `TESTIGO`.**

---

## Qué cuenta, y de dónde lo saca

**`DSH` guarda cada sesión en `~/.dsh/sessions/`, comprimida con `zstd`, y cada mensaje del modelo trae su consumo, su proveedor y su modelo.**

**El script lee eso y nada más.** **No pide permisos, no habla con ningún servicio, y no se conecta a internet.**

```plaintext
turnos · completados · fallidos
pasos · llamadas al modelo · reintentos
tokens de entrada, de salida, de caché leída y escrita
entrada real (entrada + caché, que es lo que de verdad se pagó)
ratio de caché
herramientas usadas, y cuántas veces
errores del modelo, por código
tokens por resultado exitoso
```

---

## Cómo se corre

```bash
python stats.py                          # la sesión más reciente
python stats.py --all                    # todas, con el total
python stats.py --session <id>            # una en concreto
python stats.py --tabla                  # una línea por turno
python stats.py --cre                    # sólo tokens por resultado
python stats.py --json                   # para otro programa
```

**Y el requisito, uno:** `pip install zstandard`.

---

## Y lo que no cuenta, a propósito

**No cuenta dinero.** **Y no es una omisión: es la única forma de que el número no envejezca mal.**

**Un precio cambia, un plan cambia, una tarifa promocional se acaba, y el script que dice «esto costó tres pesos» se vuelve mentira el día que sube, sin que nadie se entere.**

**Los tokens no cambian.** **Un token es un token.** **Lo que cambia es cuánto cuesta, y eso no es del script: es de quien lo corre, con su plan y de su bolsillo.**

**Si quieres pesos, multiplica.** **Y el factor que uses no sale de aquí.**

---

## Lo que hay que saber del campo de entrada

**`inputTokens` no incluye la caché.** **Viene después de restarla, y eso confunde a cualquiera la primera vez.**

**Un ejemplo real, de una llamada de esta misma máquina:**

```plaintext
inputTokens       164
cacheReadTokens 19200
outputTokens       79
```

**La entrada de esa llamada fueron 19,364 tokens, y 19,200 se volvieron a leer.** **Contar sólo `inputTokens` deja fuera el 99% de lo que de verdad se pagó.**

**Por eso el script muestra las dos cosas: la entrada, y la entrada real.** **Y no las mezcla en un solo número sin decirlo.**

---

## El costo por resultado exitoso

**Es el del ensayo de la medición de talentos, aplicado a tokens y no a pesos.**

```plaintext
CRE (en tokens) = (entrada real + salida) ÷ turnos completados
```

**Y lo que entra y lo que no, que es la mitad de la cuenta:**

```plaintext
entran        todos los intentos, incluidos los turnos que fallaron
no se resta   la corrección: corregir es parte del costo
y el resultado no cuenta
              si no se completó
```

**Un turno fallido es un intento, y los intentos son el numerador.** **Un turno completado es lo único que se puede atar a un resultado, y no dice si el resultado servía: dice que se terminó.**

**Y esa diferencia se dice, porque es la que hace que el número se lea bien o se lea mal.**

---

## Cómo se lee un ratio de caché alto

**99% de caché no significa que estés ahorrando el 99%.** **Significa que el 99% de lo que mandaste ya lo había mandado antes, y el modelo lo leyó de su lado.**

**Un ratio de caché bajo no es un error: es una sesión que cambió mucho de contexto.**

**Y un ratio de caché que sube turno a turno dice algo que ningún otro número dice: que la sesión se está repitiendo.**

---

## Lo que este script no puede ver

```plaintext
lo que costó antes de que DSH lo apuntara   no está, y no se reconstruye
el precio de cada token                     no está en el registro
si el resultado servía                      eso no lo dice un turno completado
y el tiempo de trabajo                      no se apunta, y no es prueba
```

---

## Falsificador

**Un informe de estadísticas que da dinero sin decir de qué precio.** **Y su contraria: uno que da tokens y los presenta como si fueran un resultado, cuando un token es un costo y no una cosa hecha.**
