# 1. Las doce fricciones

**Los doce errores que más costaron, cada uno con su razón de credibilidad y su contra.**
**Alejandro Valenzuela Rivera · 4 de noviembre de 2026.**

> **La forma es siempre la misma:** **el error, por qué era creíble, cómo se reconoce, qué se hace en su lugar, y quién lo corrigió.**
> **`por qué era creíble` es el campo que no se salta**, porque **un error tonto no se repite; el que se repite es el razonable.**

---

## 1. Frenar por la cosa equivocada

**El error:** buscar el «keyring» en lo primero que sonó a keyring —las llaves de GPG— sin preguntar cuál era.
**Por qué era creíble:** había un keyring de GPG de verdad, con llaves reales, y «keyring» es exactamente la palabra que se usa para eso.
**Cómo se reconoce:** no se identificó qué era **antes** de actuar. Se supuso, y la suposición se disfrazó de diagnóstico.
**En su lugar:** antes de frenar por algo, se identifica qué es y se nombra con su fuente. Y si hay una línea que lo diga —`keyring.get_keyring()`— se corre antes de hablar.
**Quién lo corrigió:** el dueño, con dos palabras que no dejaron duda.

---

## 2. Borrar sin que exista el commit

**El error:** borrar archivos del dueño **antes** de que estuvieran en un commit, y comprobar la papelera después.
**Por qué era creíble:** estaban en `stage`, y `stage` **parece** respaldo. Y el contenido ya estaba «repartido» en otro lado.
**Cómo se reconoce:** cuando algo está en stage y no en un commit, **no existe**. Y `stage` se ve igual que respaldo en un `git status`.
**En su lugar:** el commit va antes del borrado, no después. Lo que está en stage no es respaldo.
**Quién lo corrigió:** el dueño, y con razón: *«¿por qué no haces commit? todo se va a perder.»* **Se perdió.**

---

## 3. Declarar perdido lo que no estaba perdido

**El error:** decir «no se puede recuperar» sin haber mirado el historial de git.
**Por qué era creíble:** la papelera no lo tenía, y el archivo se había sacado de `stage`.
**Cómo se reconoce:** cuando el texto dice «no se puede», y no hay un `reflog` leído detrás, **es una corazonada con formato de conclusión.**
**En su lugar:** antes de decir perdido: `reflog`, `fsck --lost-found`, `ls-tree` del commit huérfano, y papelera. Y el `--amend` **no borra**: deja el anterior alcanzable.
**Quién lo corrigió:** el dueño, con la pregunta exacta: *«¿y no está el historial de git?»* **Estaba.**

---

## 4. Entregar una idea en vez de una posición

**El error:** cuando se pidió **una frase** que cerrara el trabajo, se entregó **un ensayo sobre por qué la idea es buena**.
**Por qué era creíble:** el ensayo era correcto, estaba bien escrito, y estaba en el archivo.
**Cómo se reconoce:** el destinatario pidió X y se le contestó con un argumento **sobre** X. Y el argumento, aunque sea cierto, **es más largo que lo pedido**.
**En su lugar:** cuando se pide «cómo», la respuesta es **la línea**. El diagnóstico extra se ofrece después, y no antes.
**Quién lo corrigió:** el dueño, con una frase que dejó el criterio clavado: *«estoy cansado de que no hagas nada bien.»*

---

## 5. Inventar una herramienta en la declaración

**El error:** se listó, en la declaración de uso de IA, un asistente **que nunca se abrió**.
**Por qué era creíble:** aparecía en el historial de otro proyecto del mismo autor, y «parecía lógico» que hubiera estado ahí.
**Cómo se reconoce:** si no se puede señalar el archivo donde se usó, **no se usó**. Y una declaración de IA **es el peor lugar** para un dato de memoria.
**En su lugar:** en una declaración de IA no entra ni una herramienta que no se pueda nombrar con su archivo. **El testigo no inventa testigos.**
**Quién lo corrigió:** el dueño: *«Claude nunca lo he abierto.»* **Y tenía razón.**

---

## 6. Invertir el sentido de una frase del dueño

**El error:** se escribió *«ver a la quimioterapia más cara es posible»*, cuando lo que se quería decir era **lo contrario**: que deje de ser la única opción.
**Por qué era creíble:** estaba bien redactada, y sonaba a lo que el autor decía de la tecnología y la salud.
**Cómo se reconoce:** si la frase se lee al revés de lo que el dueño quería, **no es un matiz: es el sentido invertido.**
**En su lugar:** toda frase del dueño se relee **en su contexto**, y no solo por la ortografía.
**Quién lo corrigió:** el dueño, que la leyó completa y vio el giro.

---

## 7. Rellenar lo que faltaba en vez de declararlo

**El error:** cuando faltaba un dato, se puso **el que debía de haber**.
**Por qué era creíble:** el hueco, relleno, se ve igual que un dato. Y el registro queda más limpio sin huecos.
**Cómo se reconoce:** un banco sin un solo error, o sin un solo hueco, **no está completo: está maquillado.**
**En su lugar:** lo vacío se declara. Un hueco relleno con lo probable deja de ser prueba y se vuelve costumbre.
**Quién lo corrigió:** el propio ejercicio, que ya lo tenía escrito en el ensayo 2 **y aun así se hizo al revés una vez.**

---

## 8. Abrir el cajón equivocado y no darse cuenta

**El error:** el gpg de Windows, si no le dices dónde está el keyring, **se crea uno nuevo** en `%APPDATA%\gnupg`.
**Por qué era creíble:** gpg funcionó, no dio error, y creó archivos con fecha de hoy.
**Cómo se reconoce:** una herramienta que crea estado por defecto **no da error al crear el cajón equivocado.**
**En su lugar:** gpg se llama siempre con `--homedir`, y si no, no se llama. Y si aparece un directorio nuevo con fecha de hoy, es una alarma.
**Quién lo corrigió:** la revisión que destapó que las llaves seguían en su sitio y el cajón nuevo era basura.

---

## 9. Escribir en el repo cuando el repo ya no se toca

**El error:** se creó un archivo **dentro del repositorio** cuando lo que se pidió era un artefacto **en otra carpeta**.
**Por qué era creíble:** el tema venía del repositorio, y el repositorio es su lugar natural.
**Cómo se reconoce:** el destino que se nombra **es el único destino**. Y «pasar» no significa «crear dentro de».
**En su lugar:** lo que se nombra, se respeta; y un repositorio que se dice cerrado no se toca ni para complementarlo.
**Quién lo corrigió:** el dueño, que pidió deshacer el cambio y dejó la regla.

---

## 10. Meter el vocabulario de otro proyecto por la puerta de atrás

**El error:** un ensayo nuevo usó una palabra que **no era de este trabajo**, sino del anterior.
**Por qué era creíble:** la palabra es correcta en el otro proyecto, y describe lo mismo.
**Cómo se reconoce:** si la palabra no aparece en los otros documentos de este trabajo, **es importada**.
**En su lugar:** cada trabajo usa su propio vocabulario; y lo que se importa, se importa como idea, no como término.
**Quién lo corrigió:** el dueño, que preguntó **por qué ese término y no el propio.**

---

## 11. Dejar configuración que solo funciona en la sesión de quien la puso

**El error:** se dejó la firma de commits con una configuración **que dependía de una variable de entorno** que solo existía en la sesión de quien la dejó.
**Por qué era creíble:** **funcionaba.** Los commits salían firmados y verificados.
**Cómo se reconoce:** si una configuración depende de una variable que uno puso a mano, **no es configuración: es un supuesto.**
**En su lugar:** toda configuración que se deja a alguien se prueba **en el entorno de esa persona**, sin las variables de la propia sesión. Y una ruta con doble barra invertida en un archivo de configuración **se toma literal**.
**Quién lo corrigió:** el dueño, que tropezó con el error tres veces y tuvo que reportarlo.

---

## 12. Escribir lo que el dueño no leyó

**El error:** se agregaron a un documento **fuentes y afirmaciones** que el dueño **no había leído**.
**Por qué era creíble:** las fuentes existían, eran reales, y eran pertinentes.
**Cómo se reconoce:** si el autor no leyó la fuente, **el documento lo hace mentiroso** — no por malicia, sino porque **dice que se usó algo que nunca se abrió**.
**En su lugar:** solo entra lo que el autor puede defender con la boca abierta. Y lo demás, fuera, o marcado como no abierto.
**Quién lo corrigió:** el dueño, con la regla más dura de todas: *«no quiero la verdad, quiero algo útil y usable.»*

---

## Lo que las doce tienen en común

**Míralas de una vez y aparece un patrón:**

- **Nueve de doce son de la misma familia:** **rellenar un hueco en vez de declararlo.** El keyring supuesto, el `stage` dado por respaldo, el «no se puede» sin leer, la herramienta inventada, el dato de memoria, la configuración que «funcionaba», la fuente no leída.
- **Dos son de no leer lo que se pidió:** entregar un ensayo cuando se pedía una frase; escribir en el repo cuando el destino era otro.
- **Una es del propio método, y es la peor:** rellenar el hueco **sabiendo que el ensayo decía que no se rellenara.**

**Y de ahí sale la que más vale de todas:** **un ente que no deja huecos no es un ente completo; es un ente que aprendió a parecerlo.**
