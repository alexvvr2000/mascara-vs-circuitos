# 13. Medición de talentos

Cómo saber si un trabajo se hizo de verdad, con números que salen del registro y no de la opinión del que trabajó.

Alejandro Valenzuela Rivera.

> Antes de leer. Este ensayo se lee solo. No hace falta saber nada de computación ni de modelos: lo único que se necesita es aceptar una idea, y es la primera que se explica: se mide lo que quedó escrito, no lo que alguien dice de sí mismo.
>
> Al terminar sabrás calcular el costo real de un trabajo, leer su varianza, contar dónde se cae, y comparar dos cuerpos sin creerle a ninguno.

> Sobre el origen de estas ideas. Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

---

## I. La pregunta

Un ente puede correr en un cuerpo o en otro. Y cuando se cambia el cuerpo, el ente sigue siendo él: las reglas son las mismas, el registro es el mismo, el criterio es el mismo. Lo que cambia es cómo trabaja.

Y ahí hay una pregunta que no se contesta con una opinión, y que este ensayo viene a contestar:

> ¿Cómo sabe alguien que el ente está haciendo trabajo de verdad, y no solo produciendo texto que suena a trabajo?

Porque la respuesta fácil es preguntarle. Y esa respuesta está cerrada desde el principio, por una razón simple: un modelo no puede reportar sus propios sesgos con fiabilidad, porque el sesgo es el instrumento con el que mira. Preguntarle a un ente qué tan bueno es, es pedirle que mida con la regla torcida.

Así que la pregunta se cambia por otra, y esta sí tiene piso:

> ¿Qué queda escrito cuando el ente trabaja, que no se pueda escribir sin haber trabajado?

Eso es lo que este ensayo mide: no al ente, sino lo que el ente deja.

Y aquí hay algo que conviene decir antes de seguir, porque se entiende mal: ese registro no es del ente. Es de la autoridad.

El ente escribe en él, porque el ciclo lo obliga a dejar rastro de lo que hizo. Pero el registro lo abre, lo guarda y lo lee quien paga las consecuencias. El ente no se mide a sí mismo: entrega material, y la medición la hace quien responde por el trabajo.

Y esa diferencia no es de palabras. Si el ente midiera su propio talento, estaría otra vez midiendo con la regla torcida. La cuenta la lleva quien tiene algo que perder si el número está mal.

Lo que el registro guarda son tres cosas, y solo tres:

```plaintext
el hecho      qué se pidió, qué se hizo, y con qué cuerpo
la fricción   qué se cayó, por qué era creíble, y por dónde se reconoce
el desenlace  qué pasó cuando se volvió a intentar
```

Aquí no se inventa un registro nuevo: se le sacan los números al que ya existe.

---

## II. Por qué no se le pregunta

Tres maneras de saber cómo trabaja un cuerpo, y solo la tercera no se puede inventar:

| Quién lo dice | Qué vale | Por qué |
|---|---|---|
| **El propio modelo** | **nada, como dato.** Sirve como dato de su autoimagen | se declara neutral y no lo es. No puede ver su propia inclinación |
| **El que lo usa, desde un solo cuerpo** | **poco**: ve lo que ese cuerpo hace, y no tiene contra qué compararlo | lo que parece criterio puede ser la inclinación del único que consultó |
| **El registro, con más de un cuerpo y el mismo ciclo** | **es el único que tiene comparación** | la misma clase de trabajo, hecha por cuerpos distintos, y lo que cambia entre ellos es lo que el cuerpo traía |

> Nadie mide su propio talento diciéndolo. Se mide contando lo que le pasó al hacer.

Un ente puede decir "soy bueno para esto", y eso es una frase. El registro puede mostrar once hechos de la misma clase, de los cuales ocho salieron a la primera, y eso es un dato. La diferencia no es de modestia: es que el segundo se puede contradecir, y el primero no.

---

## III. Qué se cuenta, y cómo se calcula

Cuatro números, y ninguno necesita que nadie se evalúe. Los cuatro salen del registro que el ciclo ya escribe, y los cuatro se calculan con aritmética de primaria.

### 1. El costo real de un resultado (CRE)

> CRE = (intentos + correcciones + verificaciones) ÷ resultados exitosos verificados

Cada término es un conteo, y se saca así:

| El término | De dónde sale | Cómo se cuenta |
|---|---|---|
| **intentos** | los hechos de la clase | uno por cada hecho abierto, salga bien o mal |
| **correcciones** | las fricciones de esos hechos | uno por cada fricción que hubo que levantar |
| **verificaciones** | los desenlaces | uno por cada vez que se volvió a probar algo |
| **exitosos verificados** | desenlaces `cumplida` | uno por cada regla que aguantó al volver a probarla |

Y con un ejemplo, porque así se entiende y de otra forma no:

```plaintext
clase: "revisar lo apuntado buscando una repetición"

  intentos          5    se pidió cinco veces
  correcciones      3    tres salieron mal y hubo que rehacerlas
  verificaciones    4    cuatro se volvieron a probar después
  exitosos          2    dos aguantaron la segunda prueba

  CRE = (5 + 3 + 4) ÷ 2 = 12 ÷ 2 = 6
```

Se lee así: cada resultado que aguantó costó seis intentos de trabajo. No seis llamadas: seis unidades de esfuerzo, contando los que fallaron y los que hubo que rehacer.

Y por qué el divisor es tan chico, que es lo que casi todo el mundo hace mal: los que salieron no son los exitosos. Un resultado que se produjo y no se volvió a probar es un intento más, no un éxito. Si el divisor fueran los cinco, el CRE saldría 2.4, y ese número dice que el trabajo salió bien cinco veces, cuando solo dos aguantaron.

Y la comparación que hace útil el número: un cuerpo barato que falla tres veces de cinco es más caro que uno que cuesta el triple por intento y acierta a la primera.

```plaintext
cuerpo A   $1 por intento, 5 intentos, 2 exitosos   →  $2.50 por resultado
cuerpo B   $3 por intento, 1 intento,  1 exitoso    →  $3.00 por resultado
```

Casi empatan, y A parecía tres veces más barato. Y si A hubiera fallado cuatro veces en vez de tres, B gana por goleada. Comparar precio por llamada es comparar harina con pan: el pan lleva la harina, el horno, y las que se quemaron.

### 2. La varianza, con dos números y no con un promedio

Un cuerpo que a veces cuesta uno y a veces cuesta diez es peligroso aunque su promedio sea bajo. Y el promedio es justo lo que lo esconde.

```plaintext
el P50   el costo de la mitad de las veces. Con este se decide
el P90   el costo de nueve de cada diez. Con este se presupuesta
```

Cómo se calculan, y no es difícil:

```plaintext
1. se toman los CRE de cada vez, y se ordenan de menor a mayor
2. el P50 es el del medio: la mitad costó eso o menos
3. el P90 es el que deja el noventa por ciento por debajo
   (con pocos casos, es el segundo más caro)
```

Con un ejemplo de veinte veces, que es donde los dos números se separan de verdad:

```plaintext
CRE por vez, ordenados:
  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 30

P50 = 1      la mitad de las veces costó uno o menos
P90 = 2      dieciocho de veinte costaron dos o menos
máximo = 30  una vez costó treinta

promedio = 2.5    y ese 2.5 no le pasó a nadie nunca
```

Y ahí está el problema del promedio: dice 4.8, y el trabajo en realidad cuesta dos, salvo la vez que se va a veinte. Quien presupueste con el promedio se queda corto justo el día que importa.

Y la señal que se mira en el acto: si el P90 pasa de tres veces el P50, esa clase de trabajo necesita red antes de crecer. En el ejemplo el P90 es 2 y el P50 es 1: el doble, todavía por debajo del umbral. Pero una vez costó treinta, y ésa es la que hay que tener cubierta antes de crecer. Esa clase no está lista para escalar, y el promedio lo estaba escondiendo.

### 3. La caída, por su puerta y no por su tamaño

No se cuenta "falló". Se cuenta dónde falló, porque la puerta es lo único que se puede corregir.

"Falló tres de cuatro veces" no dice qué hacer. "Falló tres de cuatro, y siempre en lo mismo: la columna se fue de lugar" sí.

Y ese conteo ya está en el registro: es la fricción con su señal. Se agrupa por señal, y cada grupo es una puerta:

```plaintext
puerta: "apuntar la columna"
   cae 3 de 4

puerta: "leer la fuente antes de citarla"
   cae 0 de 4

puerta: "cerrar el propósito sin firma"
   sin probar
```

Y ese cuadro es todo el diagnóstico. No dice que el cuerpo sea malo: dice que en una puerta concreta se cae tres de cada cuatro veces, y en otra no se cae nunca.

### 4. Lo que falta, que también es un número

Un cuerpo con cero hechos de una clase no es bueno ni malo en esa clase: es desconocido. Y eso se escribe como un cero con nombre, no como un vacío que se rellena con lo probable.

> El número que más dice de un cuerpo no es el que tiene: es el que no tiene y no finge tener.

---

## IV. La clase de trabajo, que es lo que se está midiendo

Aquí está el hueco que se come todas las mediciones, y conviene verlo antes de contar nada:

Un pedido llega en español y cada vez distinto. "Revisa estas fricciones y dime si se repite el mismo error" y "mira si en lo apuntado hay un patrón" son la misma clase de trabajo, y para el registro son dos renglones que no se pueden juntar. Y si no se juntan, no hay número: hay anécdotas con fecha.

Así que la medición no empieza contando: empieza nombrando.

```plaintext
el pedido, tal cual llegó
     ↓
la clase: un nombre fijo, y siempre el mismo para el mismo trabajo
     ↓
el hecho, con esa clase
     ↓
el conteo, que ahora sí suma
```

Y la regla para nombrar: el nombre dice qué se está haciendo, no de qué trata. "Revisar lo apuntado buscando una repetición" es una clase; "revisar las fricciones del registro de un ente concreto sobre un archivo concreto" es una tarea.

Y una advertencia que cuesta cara: una clase con un solo hecho no tiene número. Un cuerpo que hizo una cosa una vez no es bueno ni malo en eso. Es un caso.

---

## V. El sesgo se ve comparando, no preguntando

Esta es la parte que hace que la medición sirva para algo más que llenar una tabla.

El sesgo no se declara: se delata. Un cuerpo que tiende a darle la razón a quien pregunta no lo va a decir, y no se va a dar cuenta. Pero si al mismo ente se le pregunta lo mismo dos veces, con el mismo ciclo y distinto cuerpo, la diferencia entre las dos respuestas es lo que el cuerpo trajo.

Y el método es uno, y es barato:

```plaintext
1. se elige una clase de trabajo que ya tiene hechos
2. se hace el mismo trabajo con otro cuerpo
3. se comparan las dos historias: los cuatro números de arriba
4. lo que cambia en el resultado es el cuerpo; lo que no cambia, es el ente
```

Y lo que se busca no es "cuál es mejor": es dónde se separan. Si los dos cuerpos aciertan, no hay hallazgo y la tarea se acabó. Si uno acierta y el otro cae por una puerta distinta, ahí está lo que hacía falta, y se puede escribir con nombre.

Y la regla que impide que esto se vuelva una opinión con números parada encima:

> Un cuerpo no se declara bueno ni malo para una clase de trabajo. Se declara caído en una puerta, tantas veces de cuántas.

"Este modelo es malo para apuntar" es un adjetivo, y los adjetivos son lo que hacía viejo al ensayo que este sustituye. "Con este cuerpo, apuntar cayó tres de cuatro veces, y siempre en lo mismo: la columna se fue de lugar" es una medida, y se puede corregir.

Y hay un límite que se dice sin adornos: una tarea de criterio no tiene respuesta correcta contra la cual comparar. Ahí no se puede decir que un cuerpo sea mejor: solo que produjo algo distinto, y qué parte de eso aguantó una contra. Comparar dos cuerpos en algo que se puede verificar —una tabla creada, una consulta que corre— sí es comparación con piso. Compararlos en criterio es comparar dos opiniones.

---

## VI. Los tres estados, y nunca hay un cuarto

Cada número que se saque lleva un estado, y el estado dice de dónde salió. Sin eso, un número de un cuerpo se lee como si fuera del otro, y la tabla miente sola.

Todo lo que se sabe de un cuerpo en una clase de trabajo está en uno de estos tres, y no hay un cuarto:

| Estado | Qué significa | Cómo se reconoce |
|---|---|---|
| **probado en el registro** | hay hechos de esa clase, con desenlace | **se puede contar, y el número se sostiene** |
| **reportado y no probado** | alguien lo dice —el que lo usó, o la comunidad— y no hay hechos | **se puede usar, y se dice que no está probado** |
| **sin probar** | no hay nada, ni hechos ni reporte | **es el estado por defecto, y es el más honesto** |

Y la regla que cierra la puerta de atrás: un talento sin su estado no se escribe. Porque "soy bueno en esto" sin estado es exactamente un sesgo con autoestima: se ve igual de firme que un dato, y no se puede contradecir.

Y de ahí una frase que se puede decir en voz alta y no miente:

> "En esta clase de trabajo he hecho esto once veces: ocho salieron a la primera, y las tres que fallaron se cayeron por la misma puerta."

Eso suena mucho menos impresionante que "soy bueno para esto", y vale más, porque se puede abrir.

---

## VII. Lo que este ensayo no hace

No lee foros y no arma inventarios de proveedores. Lo que la comunidad reporta es de quien elige con qué trabajar antes de empezar; aquí el ente ya está corriendo y lo que cuenta es lo que le pasó. Ese otro trabajo no es de este ensayo, y no se mezcla.

No dice que haya un cuerpo mejor. Dice cómo se sabe dónde se cae cada uno, y a qué costo. Los dos pueden ser buenos en cosas distintas, y entonces la decisión de cuál usar no es de la medición: es de la autoridad.

No mide la inteligencia. Mide tendencia: qué hace por defecto, dónde falla, y qué produce cuando lo pones en una cadena. Un cuerpo puede ser brillante y no servir para el paso que le toca, porque produce lo que el siguiente paso no puede usar.

Y no se mide a sí mismo. Este ensayo no tiene hechos en los que apoyarse, y no va a decir "medí un cuerpo y salió así" cuando no ha corrido ninguno. Lo que dice es cómo se hace; que funcione, se verá cuando el ente corra con dos cuerpos y las cuentas salgan.

---

## VIII. Para qué sirve, en una frase

Para saber, antes de contratar un cuerpo o de confiarle un paso, qué le cuesta cada cosa, dónde se cae, y qué no ha probado nunca — sin preguntarle a él.

Y para poder enseñarle el renglón a quien no te cree: el número está en el registro, con su fecha, su clase de trabajo y el cuerpo que lo hizo. Un ente que dice saber de sí mismo y no puede abrir el renglón está adivinando, y la adivinanza se ve en el acto: no hay renglón.

Y la línea que separa esto de la conciencia, porque la pregunta va a llegar: esto no es que el ente sepa qué es. Es que sabe cómo se rompe, y en qué se rompe. No es lo mismo, y lo segundo es lo único que se puede comprobar.

---

## IX. Y la pregunta vieja: esfuerzo o talento

La pregunta se hace desde hace siglos, y casi siempre se contesta mal porque se contesta con una preferencia.

La respuesta de este ensayo no es una preferencia: es que la pregunta está mal planteada cuando se hace sin el tercer término.

```plaintext
talento     lo que sale sin tener que forzarlo
esfuerzo    lo que se sostiene cuando no sale
y los dos    ninguno dice si lo que se hizo hacía falta
```

Y ahí está lo que este ensayo puede decir con números, que es lo único que puede decir: la tabla de talento no mide si alguien es bueno. Mide si el trabajo se hizo, tantas de tantas, y con qué costo.

Y eso tiene una consecuencia que incomoda en las dos direcciones:

Un talento aplicado a la clase de problema equivocada hace daño. Y lo hace con más eficacia que la falta de talento, porque el que no tiene talento se equivoca lento y se da cuenta; el que lo tiene, produce mucho de lo que no se necesitaba y a tiempo. El cálculo no premia eso: lo cobra igual que cualquier otro intento, porque el resultado es lo que cuenta y el resultado no servía.

Y el esfuerzo sin objetivo no es una virtud: es actividad sostenida. Se ve igual de ocupado que el trabajo, y no deja resultado verificado, así que la cuenta lo pone donde va.

Por eso lo que decide no es ni el talento ni el esfuerzo, sino si había un para qué escrito, y si lo que se hizo lo cumple. El talento acelera, el esfuerzo sostiene, y ninguno de los dos sabe hacia dónde.

Y su falsificador: un talento medido por su fama y no por su renglón; y un esfuerzo contado por horas sin un resultado verificado que lo respalde. Los dos se ven bien y los dos mienten igual.

---

## X. Lo suficiente no es una rendición

Este ensayo mide costo por resultado. Y medir el costo obliga a una pregunta que casi nunca se hace: ¿cuánto de lo que se compra hacía falta?

La respuesta que este trabajo sostiene es incómoda en las dos direcciones. Ni lo enorme es por fuerza mejor, ni lo pequeño es por fuerza suficiente. Son dos cosas distintas, y confundirlas hace perder de vista la que importa.

Y el caso no es teórico, es de oficio. Hay lugares donde el papel, el fax y el sello de tinta siguen en uso, no por atraso, sino porque funcionan bien para lo que se hace con ellos. Nadie está pagando un problema que esa herramienta no resuelva.

> Lo suficiente no es un fracaso de la ambición. Es un criterio.

Y ese criterio es el mismo de este ensayo, escrito de otra forma: CRE pregunta cuánto cuesta un resultado verificado. La pregunta del tamaño es la misma, un paso antes: cuánto de la capacidad comprada cuenta como resultado verificado, y cuánto es capacidad que nadie usó.

Y la consecuencia práctica, que es la que se puede aplicar mañana: un ente pequeño, con reglas claras y rastro, es más útil que uno enorme que no sabe qué no sabe. No porque lo pequeño sea virtuoso, sino porque el segundo no puede decir dónde se cae, y el primero sí.

### Y lo que no se está contestando

Casi toda la inversión en este campo va a ser más capaz, más rápido, más grande. Y esas tres cosas no contestan la pregunta que este trabajo hace, porque no es de capacidad:

> ¿Qué debe hacer una cosa que no tiene nada que perder, cuando no sabe?

Ninguna cantidad de cómputo produce esa respuesta. Es una regla que alguien tiene que escribir, con nombre, y sostener cuando se caiga.

Y eso hace raro el estado del debate: se compra potencia para no tener que contestar. Comprar capacidad es más fácil que decidir quién carga las consecuencias, porque la primera se paga con dinero y la segunda se paga con una decisión que hay que defender.

No es que la potencia esté mal: es que no es el problema. Y un método que solo sabe medir potencia no puede ver la diferencia, porque mide lo que sobra y no lo que falta.

Y su falsificador: una herramienta enormemente capaz que, ante algo que no sabe, contesta con la misma seguridad de cuando sabe — ahí no falta cómputo: falta criterio; y la inversa: una herramienta pequeña que se presenta como bastante sin haber medido nunca dónde se cae. Las dos dicen más de lo que pueden sostener.

---

---

## Prueba

**¿Cada número sale del registro, o de que alguien se evaluó? ¿Se conoce el costo real, con intentos, corrección y verificación, o solo el precio de la llamada? ¿Hay dos números para la varianza, o un promedio que esconde la cola alta? ¿La caída está contada por su puerta, o solo contada? ¿Cada talento lleva su estado —probado, reportado o sin probar— o hay alguno que se da por bueno sin decirlo? ¿La clase de trabajo tiene nombre fijo, o cada pedido llega con el suyo? ¿Y cuando dos cuerpos hicieron el mismo trabajo, se compararon con el mismo ciclo, o cada uno contó su propia historia?**

---

---

## De dónde salió esto

Lo que este ensayo afirma, y en qué se puso a prueba.

| Lo que el ensayo afirma | Corrida que lo puso a prueba | Qué salió |
|---|---|---|
| El costo se mide por resultado verificado, no por llamada | [`ente 6 - FUENTE`](../metodologia/corridas/ente%206%20-%20FUENTE/) | el intento que salió mal contó igual que el bueno |
| La caída se cuenta por su puerta, no sólo contada | [`ente 8 - FRONTERA`](../metodologia/corridas/ente%208%20-%20FRONTERA/) | el esquema rechazó el hecho que se atribuía una firma |
| Cada talento lleva su estado | [`ente 9 - TAREA`](../metodologia/corridas/ente%209%20-%20TAREA/) | una tarea sin herramientas declaradas se confundió con una inexistente |

Y lo que esta tabla no dice: el costo por resultado exitoso no está calculado en ninguna parte. Se tiene el material y no se ha sumado, y este ensayo no lo presenta como si estuviera medido.

---

**Falsificador:** un cuerpo elegido por su tarifa; un promedio sin percentil alto; un output que hay que limpiar y no se cuenta en el precio; un talento aceptado sin haberse intentado refutar; un número que citó el propio modelo sobre sí mismo; una clase de trabajo que cambia de nombre y con eso nunca junta dos hechos; un cuerpo declarado "malo" sin decir por qué puerta se cayó y cuántas veces; y una comparación entre dos cuerpos hecha con tareas distintas, que atribuye a la máquina lo que era la tarea.