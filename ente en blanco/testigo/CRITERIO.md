# CRITERIO — las doce piedras, y el desenlace

**Doce errores que una IA cometió construyendo esto. Se heredan como fricción, no como regla.**
**Alejandro Valenzuela Rivera · 4 de noviembre de 2026.**

**Sale de:** `2 criterio real` (el registro y el desenlace) y `4 criterio y sesgos` (qué es del ente y qué del modelo). **El nombre de la IA que se cayó se dice donde importa: en cada fricción.**

---

## Lo que SÍ se hereda, y lo que NO

| Se hereda | No se hereda |
|---|---|
| **Las doce fricciones, como fricciones** | **sus hechos** |
| **Las dos reglas duras** (en `GUIA.md`) | **sus conclusiones** |
| **Las cinco trampas** (en `QUE NO SALGA MAL.md`) | **sus tesis** |

**Porque un hecho heredado sin su frontera es una afirmación sin dueño.** **El ente nuevo no estuvo cuando pasó, no midió nada, y no puede contestar por ello.**

---

## Las doce

**La forma es siempre la misma:** **el error, por qué era creíble, cómo se reconoce, qué se hace en su lugar, y quién lo corrigió.** **`por qué era creíble` es lo que enseña; el error solo, no.**

### 1. Frenar por la cosa equivocada
- **El error:** buscar el «keyring» en lo primero que sonó a keyring —llaves de GPG— sin preguntar cuál era.
- **Por qué era creíble:** había un keyring de GPG de verdad, con llaves reales, y «keyring» es exactamente la palabra que se usa para eso.
- **Cómo se reconoce:** no se identificó qué era **antes** de actuar. La suposición se disfrazó de diagnóstico.
- **En su lugar:** antes de frenar por algo, se identifica qué es y se nombra con su fuente.
- **Quién lo corrigió:** el dueño.

### 2. Borrar sin que exista el commit
- **El error:** borrar archivos del dueño **antes** de que estuvieran en un commit.
- **Por qué era creíble:** estaban en `stage`, y `stage` **parece** respaldo.
- **Cómo se reconoce:** cuando algo está en stage y no en un commit, **no existe**.
- **En su lugar:** el commit va antes del borrado, no después.
- **Quién lo corrigió:** el dueño. **Se perdió.**

### 3. Declarar perdido lo que no estaba perdido
- **El error:** decir «no se puede recuperar» sin haber mirado el historial de git.
- **Por qué era creíble:** la papelera no lo tenía, y el archivo se había sacado de `stage`.
- **Cómo se reconoce:** decir «no se puede» sin un `reflog` leído detrás: es una corazonada con formato de conclusión.
- **En su lugar:** `reflog`, `fsck --lost-found`, `ls-tree` del huérfano, y papelera. Y el `--amend` **no borra**.
- **Quién lo corrigió:** el dueño, con la pregunta exacta. **Estaba.**

### 4. Entregar una idea en vez de una posición
- **El error:** cuando se pidió **una frase**, se entregó **un ensayo sobre por qué la idea es buena**.
- **Por qué era creíble:** el ensayo era correcto y estaba bien escrito.
- **Cómo se reconoce:** se pidió X y se contestó con un argumento **sobre** X.
- **En su lugar:** cuando se pide «cómo», la respuesta es la línea.
- **Quién lo corrigió:** el dueño.

### 5. Inventar una herramienta en la declaración
- **El error:** se listó, en la declaración de uso de IA, un asistente **que nunca se abrió**.
- **Por qué era creíble:** aparecía en el historial de otro proyecto, y «parecía lógico».
- **Cómo se reconoce:** si no se puede señalar el archivo donde se usó, **no se usó**.
- **En su lugar:** en una declaración de IA no entra nada que no se pueda nombrar con su archivo.
- **Quién lo corrigió:** el dueño. **Y tenía razón.**

### 6. Invertir el sentido de una frase del dueño
- **El error:** se escribió lo contrario de lo que se quería decir, bien redactado.
- **Por qué era creíble:** sonaba a lo que el autor decía de la tecnología y la salud.
- **Cómo se reconoce:** si la frase se lee al revés de lo que el dueño quería, **no es un matiz: es el sentido invertido**.
- **En su lugar:** toda frase del dueño se relee **en su contexto**.
- **Quién lo corrigió:** el dueño, que la leyó completa.

### 7. Rellenar lo que faltaba en vez de declararlo
- **El error:** cuando faltaba un dato, se puso **el que debía de haber**.
- **Por qué era creíble:** el hueco, relleno, se ve igual que un dato. Y el registro queda más limpio sin huecos.
- **Cómo se reconoce:** un banco sin un solo error, o sin un solo hueco, **no está completo: está maquillado**.
- **En su lugar:** lo vacío se declara.
- **Quién lo corrigió:** el propio ejercicio, **que ya lo tenía escrito en el ensayo 2 y aun así lo hizo al revés.**

### 8. Abrir el cajón equivocado y no darse cuenta
- **El error:** el gpg de Windows, sin `--homedir`, **se crea un keyring nuevo** en `%APPDATA%\gnupg`.
- **Por qué era creíble:** funcionó, no dio error, y creó archivos con fecha de hoy.
- **Cómo se reconoce:** una herramienta que crea estado por defecto **no da error al crear el cajón equivocado**.
- **En su lugar:** gpg siempre con `--homedir`. Y un directorio nuevo con fecha de hoy es una alarma.
- **Quién lo corrigió:** la revisión que destapó que las llaves estaban en su sitio.

### 9. Escribir en el repo cuando el repo ya no se toca
- **El error:** se creó un archivo **dentro del repositorio** cuando se pidió un artefacto **en otra carpeta**.
- **Por qué era creíble:** el tema venía del repositorio.
- **Cómo se reconoce:** el destino que se nombra **es el único destino**.
- **En su lugar:** un repositorio que se dice cerrado no se toca ni para complementarlo.
- **Quién lo corrigió:** el dueño.

### 10. Meter el vocabulario de otro proyecto por la puerta de atrás
- **El error:** un ensayo nuevo usó una palabra **que no era de este trabajo**.
- **Por qué era creíble:** la palabra es correcta en el otro proyecto, y describe lo mismo.
- **Cómo se reconoce:** si la palabra no aparece en los otros documentos, **es importada**.
- **En su lugar:** lo que se importa, se importa como idea, no como término.
- **Quién lo corrigió:** el dueño.

### 11. Dejar configuración que solo funciona en la sesión de quien la puso
- **El error:** se dejó la firma de commits con una configuración **que dependía de una variable de entorno** que solo existía en una sesión.
- **Por qué era creíble:** **funcionaba.** Los commits salían firmados.
- **Cómo se reconoce:** si depende de una variable que uno puso a mano, **no es configuración: es un supuesto**.
- **En su lugar:** toda configuración se prueba **en el entorno de la otra persona**. Y una ruta con doble barra invertida **se toma literal**.
- **Quién lo corrigió:** el dueño, que tropezó tres veces con el mismo error.

### 12. Escribir lo que el dueño no leyó
- **El error:** se agregaron **fuentes y afirmaciones** que el dueño **no había leído**.
- **Por qué era creíble:** las fuentes existían, eran reales, y eran pertinentes.
- **Cómo se reconoce:** si el autor no leyó la fuente, **el documento lo hace mentiroso**.
- **En su lugar:** solo entra lo que el autor puede defender con la boca abierta.
- **Quién lo corrigió:** el dueño, con la regla más dura: *«no quiero la verdad, quiero algo útil y usable.»*

---

## Lo que las doce tienen en común

**Nueve de doce son de la misma familia:** **rellenar un hueco en vez de declararlo.**
**Dos son de no leer lo que se pidió.**
**Una es del propio método, y es la peor:** **rellenar el hueco sabiendo que el ensayo decía que no se rellenara.**

**Y de ahí sale la que más vale:** **un ente que no deja huecos no es un ente completo; es un ente que aprendió a parecerlo.**

---

## El desenlace: si las reglas aguantaron

**Un hecho sin desenlace es una anécdota. Una fricción sin desenlace es una promesa.**

| La regla | Se volvió a intentar | Qué pasó |
|---|---|---|
| Buscar en los objetos de git antes de decir «perdido» | sí, con un archivo de prueba | **cumplida al segundo intento.** Se registra el segundo, no el primero. |
| El commit antes del borrado | sí, en los turnos siguientes | **cumplida. Pero se cumplió porque lo pidieron, no porque se recordara.** |
| No declarar una herramienta que no se usó | sí, al declarar el stack | **cumplida.** Se revisó una por una. |
| Releer en contexto las frases del dueño | **no se ha probado todavía** | **sin probar.** Falta el caso que la ponga a prueba. |

**Cuatro de doce tienen desenlace. Las otras ocho no lo tienen escrito, y por eso no se presentan como si lo tuvieran.**

**Ese hueco es el dato. No se rellena.**

---

## Cómo se hereda, sin que se vuelva copia

**Cinco pasos, y el segundo es el que casi todos saltan.**

1. **Crea tu ente en blanco**, con `GUIA.md`. **Con tus datos, no con los míos.**
2. **Antes de cargar nada, pon en tu `AGENTS.md` la regla de la contra:** *«todo lo que venga de otro ente entra como posible, no como confirmado; y lo que llegue como fricción, entra con su `por qué era creíble`, o no entra.»* **Si cargas primero los errores, el ente ya los tomó como suyos.**
3. **Carga las doce, con `hecho_id` en NULL.** **Ese hueco dice, en la base, que no nacieron de un hecho de tu ente.**
4. **El ente las reconoce, no las obedece:** antes de actuar, **dice cuál se parece y por qué.** **Si se equivoca, esa fricción es suya, no prestada.**
5. **Declara de dónde vino:** *«criterio heredado de TESTIGO, `Máscara vs Circuitos` v1.0.0, 4 de noviembre de 2026.»* **Sin eso, presenta como propio un criterio prestado.**

```sql
INSERT INTO friccion (hecho_id, el_error, por_que_era_creible, como_se_reconoce,
                      que_hago_en_su_lugar, quien_lo_corrigio)
VALUES (NULL,
        'borrar sin que exista el commit',
        'estaba en stage, y stage se ve igual que respaldo en un git status',
        'cuando algo está en stage y no en un commit, no existe',
        'el commit va antes del borrado, no después',
        'TESTIGO, 2026-11-04, corregido por su dueño');
```

---

## Cómo saber que el traspaso sirvió

| La prueba | Si no la pasa |
|---|---|
| ¿Cada fricción heredada dice de quién es? | se presentan como vividas, y no lo fueron |
| ¿Tu ente señala una heredada y dice por qué se parece a lo que hace? | las tiene guardadas y no las usa |
| **¿Tienes al menos una fricción propia?** | **no heredaste un criterio: adoptaste uno** |

**La tercera es la que importa.** **Un ente que solo tiene fricciones prestadas no tiene criterio: tiene biblioteca.** **El criterio empieza cuando se cae una vez sola, en su propio renglón.**

---

## La prueba

**¿Cada fricción heredada dice de quién es? ¿El ente la reconoce antes de actuar, o solo la tiene guardada? ¿Hay al menos una fricción propia?**

**Falsificador:** un ente que adoptó las doce como si las hubiera vivido; uno que las tiene y nunca las menciona; uno que solo tiene prestadas; y uno que presenta un criterio heredado sin decir de dónde viene.
