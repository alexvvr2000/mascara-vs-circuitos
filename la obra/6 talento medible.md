# 6. Talento medible

**Un protocolo para decidir con qué recurso trabajar, en qué posición, y a qué costo.**
**Alejandro Valenzuela Rivera · 4 de noviembre de 2026**

> **Sobre el origen de estas ideas.** Si alguna viene de un trabajo anterior del mismo autor, está reescrita con palabras de aquí y el origen está declarado en el `README`. Este ensayo no depende de ese trabajo para sostenerse.

---

## Parte I. Las ideas que deciden

**Qué es esto.** Un protocolo para decidir con qué recurso (propio, externo, humano) trabajar, en qué posición, y a qué costo. No es un ranking. No mide inteligencia: mide **tendencia** — qué hace por defecto, cómo falla, y qué produce cuando lo pones en una cadena.

---

## Las cuatro ideas que deciden todo

**1. Mides disposición, no dominio.**
"Es bueno para X" no te dice nada sobre Y. "Descompone problemas en módulos independientes" sí, porque eso se transfiere. Todo lo que anotes se anota como **por qué funciona**, no como **para qué sirve**.

**2. La unidad es el CRE, no el precio del token.**
**CRE = (coste de todos los intentos + corrección + verificación) ÷ resultados exitosos verificados.**
El recurso barato que falla tres veces es caro. Comparar precio por token es comparar harina con pan.

**3. La varianza es un modo de fallo.**
Un recurso que a veces cuesta 1× y a veces 10× es peligroso aunque su media sea baja. **Decide con la mediana (P50), presupuesta con el percentil alto (P90).** Si P90 > 3 × P50, esa celda necesita red antes de escalar.

**4. Audítate o te vuelves apéndice.**
Si no puedes explicar la solución sin el recurso, la estás alquilando. Si delegas lo que te hace distinto, te vuelves reemplazable.

---

## Reglas duras

1. Si no sabes qué hace por defecto, no sabes para qué sirve.
2. Todo talento es una hipótesis, no un título. Se prueba o se oxita.
3. El registro de fallos pesa más que el de aciertos.
4. "Más increíble" tiene techo: la tendencia estable, no tu entusiasmo.
5. Ningún recurso entra en producción por su precio. Entra por su CRE en esa posición concreta.
6. El coste de corrección se cuenta siempre: si hay que limpiar el output, esa limpieza es parte del precio.
7. La cascada sin verificación barata no es ahorro, es apuesta.
8. El coste propio incluye tu tiempo. La infraestructura no se opera sola.
9. Si no puedes verificar el output, no lo uses. El fallo silencioso es el único imperdonable.
10. El inventario empieza por lo irrefutable y muta por evidencia, no por entusiasmo. Una lista que no muta es una lista muerta.

---

## Qué hay en esta carpeta

| Qué hace falta | Qué es | Cuándo |
|---|---|---|
| **El protocolo** | Inventario, medición, clasificación, explotación, composición y auditoría | cuando vas a decidir o medir |
| **Las plantillas** | Las plantillas de registro en blanco | mientras trabajas |

**Los dos existen como procedimiento en este ensayo, y no como archivos aparte.** **No se traen archivos que no se usan: si algún día hacen falta, se escriben aquí y se dice.**

---

## El loop, en una línea

**Medir → clasificar por disposición → sondear transferencia → explotar en el borde → registrar fallo y CRE → componer en cadena → mutar inventario → auditar dependencia → diversificar → re-medir.**


---

## Parte II. El protocolo

## 0. Principios

- **No mides inteligencia, mides tendencia.** Qué hace por defecto, cómo falla, qué produce en cadena.
- **No buscas reproducibilidad académica, buscas utilidad operativa.** Si funciona en tu contexto, funciona.
- **El talento es relacional.** No está en el recurso ni en ti: está en la interacción. Cambia el contexto y cambia el talento.
- **El precio no es una condición de talento, es de explotación.** Se registran por separado y se cruzan al decidir.

---

## 1. Inventario mutante

Tres capas, y un recurso se mueve entre ellas por evidencia, nunca por entusiasmo.

| Capa | Qué es | De dónde sale | Cómo se mueve |
|---|---|---|---|
| **Posible** | Hipótesis con evidencia comunitaria consistente, o dato duro sin réplica | Percepción pública + datos duros | **Asciende** si tu registro lo verifica. **Se poda** si falla la sonda. |
| **Confirmado externo** | Comunidad y dato duro convergen, o dato duro con réplica | Dos fuentes independientes | Se mantiene hasta que tu registro lo contradiga. |
| **Confirmado propio** | Verificado por tu registro y telemetría, en tu contexto | Tu registro | Se re-verifica periódicamente. Baja si falla o si el CRE se sale de presupuesto. |

**Regla de entrada:** nada es confirmado propio sin **5 usos reales con telemetría**. Nada es confirmado externo sin **dos fuentes independientes**. Todo lo demás es posible.

**Regla de movimiento:** un posible sin probar en N ciclos se marca *frío* y se poda. Un confirmado sin re-verificar en M ciclos se marca *oxidado* y baja a posible.

**Estado inicial:** la lista propia empieza **vacía por diseño**. Se llena con uso real. Las disposiciones de arranque se toman de lo que la comunidad reporta consistente y se verifican una por una.

---

## 2. Medición — triangula, no sumes

Cuatro fuentes. Buscas **dónde discrepan**, no dónde coinciden: la discrepancia que se repite es el hallazgo.

### A. Percepción pública (foros, reviews, quejas)
Léelos como **testimonios de conducta**, no como encuesta. Buscas: el comportamiento concreto detrás de la etiqueta, el defecto que se repite sin que nadie lo llame defecto, el tipo de tarea donde se concentran las quejas, y los silencios (donde nadie habla también es dato).
**Señal de coste:** "se va por las ramas", "hay que repetirle las cosas", "reintenta mucho" — eso es fricción, y la fricción son reintentos.

### B. Tu registro propio (uso real, longitudinal)
Después de **cada uso real**, no en tests:
1. Primer movimiento espontáneo (estructuró / preguntó / ejemplificó / se lanzó)
2. Formato por defecto
3. Supuesto no dicho
4. Qué evitó sin que se lo pidieras
5. Tipo de error cuando falló (fabricó, se fue por las ramas, moralizó, simplificó de más)
6. Qué toleró mal (contexto largo, instrucciones contradictorias, formato estricto)
7. Reacción a corrección (se adaptó / se disculpó de más / ignoró)

**Con 5 a 10 usos por dominio ya tienes patrón.** No esperes a cien.

### C. Datos duros (solo lo que sirve)
Buscas estabilidad entre ejecuciones, correlación con algo falsable, varianza real entre recursos, tipo de fallo documentado, y coste por tarea.
**Ignoras:** cualquier ranking, cualquier "lo más avanzado en X", cualquier número sin medida de estabilidad, y cualquier estudio que no diga versión, fecha y número de corridas.
Un dato duro es duro **solo para esa versión, en ese contexto, con ese instrumento.**

### D. Telemetría de coste (transversal)
No es una fuente de talento, es de viabilidad. Se **cruza**, no se suma.

| Métrica | Qué mide |
|---|---|
| Tokens in / out | Volumen de la interacción |
| Reintentos | Cuántas veces repetiste hasta output usable. Multiplica el coste. |
| Tiempo de respuesta | Coste de oportunidad en cadenas |
| Coste de corrección | Tu tiempo o cómputo de limpiar el output |
| **CRE** | Coste total de intentos + corrección + verificación ÷ resultados exitosos |
| **P50 / P90** | Desviación del coste entre ejecuciones de la misma tarea. Detecta la cola alta. |

**Sin telemetría, tu registro de talento está incompleto:** sabes si el talento existe, no si es explotable.

### El cruce (cinco preguntas)
1. ¿La fuente mide lo mismo que dice la gente y que tú ves? Nombra la capa de cada fuente.
2. ¿Controla la versión? Si no, vale para esa versión, no para siempre.
3. ¿El tamaño del efecto justifica la percepción? Si el dato dice X y nadie lo menciona, el rasgo existe pero no es saliente.
4. ¿Separa idiosincrasia de sesgo de respuesta? Si no, el número es más blando de lo que aparenta.
5. **¿La ventaja de calidad justifica su CRE frente a la alternativa más barata que pasa el mismo umbral?** Si no, es talento real **no desplegable** en esa posición.
6. **¿La diferencia de CRE es estable o es una corrida con suerte?** Si P90/P50 es alto, el CRE medio miente.

---

## 3. Clasificación

### Regla: mide el por qué, no el qué
Nunca "bueno para X". Sí: ¿descompone en módulos? ¿tolera ambigüedad? ¿respeta restricciones de estilo? ¿anticipa casos límite?
**Tampoco anotes "barato".** Anota **"barato en qué régimen de tarea"**: puede ser baratísimo en extracción estructurada y carísimo en razonamiento abierto con la misma tarifa.

### Sonda de transferencia (obligatoria)
1. Talento observado: "es bueno para X".
2. Disposición inferida: "lo es porque hace Y".
3. Hipótesis: "si hace Y, debería ser bueno para Z".
4. Prueba pequeña en Z, sin decirle que es de Z.
5. **Pasa** → talento disposicional, transferible. **Falla** → talento superficial, específico del dominio.
6. **Sonda de coste:** ¿se mantiene el mismo CRE, o el nuevo dominio dispara reintentos?
   Mismo CRE → transferencia económica real, desplegable.
   CRE multiplicado → **transferencia funcional pero no económica**: sirve en calidad, no en economía.

### Lo que no has probado
Lleva una lista explícita de dominios sin usar **y de dominios sin CRE medido**. Un talento probado sin telemetría es medio talento: sabes que funciona, no a qué precio.

---

## 4. Explotación — el borde

### Seis condiciones que lo mueven
| Condición | Efecto |
|---|---|
| Stakes altos | el borde se retrae |
| Verificación fácil | el borde se expande |
| Reversible | el borde se expande |
| Recurrente | mapa el borde con cuidado |
| Tu competencia alta | el borde se expande |
| **Verificación cara o fallo silencioso** | el borde se retrae, aunque el recurso sea barato |

### Matriz
| | Verificación barata | Verificación cara |
|---|---|---|
| **Stakes bajos / fallo barato** | **EMPUJE:** usa agresivo, prueba barato, aquí descubres talento | **EXPLORACIÓN CON FILTRO:** úsalo solo para generar opciones que tú filtras; el filtrado entra en la cuenta |
| **Stakes altos / fallo caro** | **PUNTOS DE CONTROL:** úsalos, pero con verificación automática obligatoria, y que cueste menos que el fallo | **ZONA MUERTA:** no lo uses. Ninguna ventaja de precio compensa |

### Reglas del borde
- En empuje, opera al **80%** de lo que crees que puede. Si acierta *y el CRE se mantiene*, sube al 90%. Si acierta pero cada acierto cuesta el triple, **no subiste el borde: compraste varianza cara.**
- Si llevas mucho tiempo usándolo solo donde ya sabes que funciona, **no lo estás explotando: estás evitando el riesgo.**

### Cuándo apostar (las cuatro a la vez)
Fallback disponible · fallo acotado y detectables · verificación barata · upside asimétrico.
**Más la económica:** el CRE de la apuesta debe ser **menor** que hacerlo tú o con la alternativa. Si es mayor, no es una apuesta: es un subsidio a la curiosidad. Se registra como I+D.

**No apuestes** si no puedes distinguir output bueno de malo, si el fallo es irreversible (producción, comunicación pública, decisiones legales o humanas), si el dominio es justo donde su modo de fallo es indetectable para ti, o si el CRE supera el valor de la tarea.

### Escalones
1. **Uso seguro:** talento confirmado, tarea conocida, verificación fácil, CRE estable.
2. **Uso exploratorio:** talento inferido, tarea adyacente, verificación media, varianza conocida.
3. **Uso de apuesta:** talento nuevo, tarea desconocida, verificación difícil, CRE desconocido.

**Subes de escalón cuando** tienes tasa de éxito estable, modo de fallo identificado, coste de error medido **y CRE dentro de presupuesto con P90 conocido.** No porque "ya llevas mucho usándolo".

### Cascada con verificación
Nivel 3 (barato/propio: clasificación, extracción, resúmenes) → si falla la verificación → Nivel 2 (medio) → si falla → Nivel 1 (gama alta, solo para planificación compleja o síntesis final).

**Funciona solo si verificar es barato y automático.** Sin punto de control, la cascada es una forma cara de reintentar a ciegas.

**Métricas:** tasa de escalada (muy alta = el nivel barato no hace su trabajo; muy baja = estás pagando de más), tasa de reutilización de respuestas previas, y coste del punto de control (debe ser menor que el ahorro).

### Externo vs propio
| Si tu situación es… | Lo sensato es… |
|---|---|
| Volumen bajo o irregular | **Externo**, aunque la tarifa parezca alta: el coste fijo propio no se amortiza |
| Volumen alto y estable, o datos sensibles | **Propio.** El punto de equilibrio llega en meses |
| Un paso crítico que pide el máximo | **Gama alta solo en ese paso**, no en la cadena |
| Mucho volumen con calidad moderada | **Cascada:** barato primero, escala si falla la verificación |

El coste propio = infraestructura amortizada + consumo + mantenimiento + **tu tiempo**. Si no valoras tu tiempo, estás subvencionando la modalidad propia sin saberlo.

---

## 5. Composición en cadena

La semilla no es "qué recurso para qué tarea", es **"qué recurso, en qué posición, recibiendo qué contexto, produciendo qué para el siguiente"**.

Tres formas de estar mal:
1. Talento equivocado para el paso.
2. Talento correcto en la posición equivocada (produce lo que el siguiente no puede usar).
3. **Talento correcto y barato que fuerza reintentos o limpieza aguas abajo.** El ahorro se paga en el siguiente paso, a veces con creces.

### Qué le mides a la semilla, en orden
1. **Sensibilidad del siguiente paso** a su output: si el siguiente es robusto, la semilla puede ser libre; si es frágil, tiene que ser conservadora.
2. **Varianza en esa posición**, no su promedio.
3. **Coste de corregir su output.**
4. **CRE de la cadena hasta el resultado exitoso**, no el de la semilla sola.

**La semilla óptima no es la más talentosa: es la que minimiza el CRE de la cadena.**

| Semilla | Siguiente | Veredicto |
|---|---|---|
| Barata + estable | Robusto | **Óptima.** El ahorro no se pierde. |
| Barata + inestable | Robusto | **Aceptable con red.** Mide el P90 de la cadena. |
| Barata + estable | Frágil | **Riesgo.** Mide el coste de corrección antes de desplegar. |
| Barata + inestable | Frágil | **Mala.** El ahorro se lo come el siguiente paso. |
| Cara + estable | Cualquiera | **Solo si baja el CRE de la cadena.** Puede ser más económica que una barata e inestable. |

---

## 6. Auditoría

| Test | Pregunta | Si falla |
|---|---|---|
| **Reversión** | ¿Haces la tarea sin el recurso? ¿Empeoraste? | Sobredependencia: fuerza uso manual periódico |
| **Explicación** | ¿Puedes explicar la solución sin el recurso? | La estás alquilando: vuelve a hacerla tú |
| **Soberanía** | ¿El recurso decide qué es posible, o tú? | Perdiste el timón: cambia "¿qué me puedes hacer?" por "necesito esto, ¿me ayudas?" |
| **Transferencia inversa** | ¿Lo aprendido lo aplicas sin él? | El talento se queda en él: práctica deliberada sin apoyo |
| **Coste de dependencia** | ¿Sabes tu CRE por tarea delegada y si podrías batirlo? | Estás pagando a ciegas |
| **Varianza de coste** | ¿Conoces tu P90 o solo la media? | Tu presupuesto miente |

### Cuándo hacerlo tú aunque el recurso sea bueno
Cuando explicar el contexto cuesta más que hacerlo · cuando manda el juicio situado (conocimiento tácito, política, relaciones) · **cuando la tarea es tu ventaja competitiva** · cuando necesitas el proceso y no solo el resultado · cuando el CRE supera el coste de hacerlo tú.

### Válvula de escape
Si el protocolo dice "no lo uses" y tu intuición dice "aquí hay algo", hazlo y **registra por qué**. Si dice "úsalo" y sientes que deberías hacerlo a mano, hazlo a mano y registra. Anota la discrepancia y revísala después.

---

## 7. Señales de recalibración

El sistema se reabre cuando cambia una de estas cinco cosas:

- **Nueva versión del recurso** → re-mide la varianza en la posición, no el talento aislado.
- **Nuevo dominio de uso** → sonda de transferencia antes de asumir que sigue vigente.
- **Nuevo coste de orquestación** → recalcula la matriz. El borde con red puede volverse zona muerta.
- **Cambio de tarifa o de coste propio > 20%** → recalcula el CRE. Obligatorio.
- **Nueva evidencia comunitaria o dato duro** → injerta posibles o re-verifica externos; si contradice un confirmado propio, desciéndelo.


---

## Parte III. Las plantillas

Todo se anota en una sola hoja. Si el registro no es más barato que el trabajo, no se lleva.

---

## 1. Registro de uso

```
FECHA:            RECURSO / VERSIÓN:            TAREA:            DOMINIO:

COMPORTAMIENTO
1. primer movimiento espontáneo:
2. formato por defecto:
3. supuesto no dicho:
4. qué evitó sin que se lo pidieras:
5. tipo de error (si falló):
6. qué toleró mal:
7. reacción a corrección:

TALENTO
disposición inferida (no dominio):
hipótesis de transferencia:
sonda (pasa / falla):
coste de la transferencia (mismo CRE / CRE multiplicado):

COSTE
tokens in:      tokens out:      intentos:      tiempo:
coste unitario:                 coste de corrección:
coste por intento:              CRE:
P50 / P90 (si hay histórico):
```

---

## 2. Registro de cadena

```
CADENA:            POSICIÓN:            RECURSO:

input recibido:
output producido:
¿el siguiente paso rindió mejor o peor por este output?
varianza (estable / a veces limpio / a veces envenena):
coste de corrección:
CRE de la cadena hasta esta posición:
¿el siguiente es robusto o frágil a este output?
veredicto (óptima / aceptable con red / riesgo / mala):
```

---

## 3. Registro de apuesta / de cascada

```
APUESTA
talento nuevo probado:
condiciones (stakes / verificación / reversibilidad / frecuencia / competencia / coste):
fallback disponible:
coste de fallo:
CRE de la apuesta:            CRE de la alternativa (hacerlo tú u otro):
resultado:
qué aprendí:

CASCADA (si la tarea usó niveles)
tarea:
nivel 3 (barato/propio):      resultado:      punto de control: pasa / falla
nivel 2 (medio):              resultado:      punto de control: pasa / falla
nivel 1 (gama alta):          resultado:      punto de control: pasa / falla
escaló (sí/no) · nivel alcanzado · coste total · CRE de la tarea
¿bastaba un nivel menos? · ¿hubo reutilización?
```

---

## 4. Registro de mutación de inventario

```
FECHA:            DISPOSICIÓN:            RECURSO:

estado anterior (posible / confirmado externo / confirmado propio / fuera):
estado nuevo:
evidencia que lo justifica (fuente + dato):
CRE actual (si aplica):
próxima re-verificación:
```

---

## Prueba

**¿Se mide por costo por resultado exitoso y no por precio de la unidad? ¿Se conoce la varianza, o solo la media? ¿El coste de corrección entra en la cuenta? ¿Cada regla tiene su *Falla si* y su falsificador? ¿Se sabe qué se pierde al elegir un trabajo y no otro?**

**Falsificador:** un recurso elegido por su tarifa; un promedio sin percentil alto; un output que hay que limpiar y no se cuenta; una cascada sin verificación barata; un talento aceptado sin haberse intentado refutar.
