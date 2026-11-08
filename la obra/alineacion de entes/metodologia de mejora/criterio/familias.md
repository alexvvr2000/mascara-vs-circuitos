# Las familias de mutantes

**Las 417 reglas, agrupadas por familia, para saber cuál es la fuerte y cuáles son casos.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **Escrito el 2026-11-08.**

---

## Cómo leer esto

**Cada fila es una familia: un grupo de reglas del mismo tipo. Y cada familia tiene sentido mutarla de una sola manera, porque sus miembros se rompen igual.**

**Y ahí está el ahorro, y es el que la jerarquía de inclusión dice en una línea: si el mutante que rompe la familia entera muere, los que rompen un caso también.**

**Por eso no se corren 417 mutantes.** **Se corre uno por familia, y lo que sobreviva se abre.**

---

## Las familias, y de dónde salen

| Familia | Dónde vive | Reglas | Qué rompe el mutante fuerte |
|---|---|---|---|
| **El ciclo, paso por paso** | `02` | 145 | borra el paso entero, o el campo que lo hace verificable |
| **El piso** | `03` | 58 | el piso miente: dice `hay` sin haberlo medido |
| **El borde del tema** | `08` | 54 | el borde acepta lo que debía salir |
| **Los sesgos** | `09` | 38 | el sesgo no se declara, o se declara neutral |
| **La medición de talentos** | `03 humanidad` | 33 | el número se toma de una impresión y no del registro |
| **La máquina de sesgos** | `10` | 25 | la afirmación se sostiene como verdad y no como condición |
| **Escritura en procesos** | `04` | 22 | el proceso no dice cuándo se corre |
| **El índice** | `07` | 14 | el índice se arma a mano y no se puede reconstruir |
| **La frontera** | `06` | 13 | las cuatro columnas se llenan con lo primero que aparezca |
| **Las afirmaciones** | `00` | 13 | una afirmación sin dónde vive, o sin qué la tumba |
| **Qué es un ente** | `01` | 12 | el ente se define por lo que tiene dentro |
| **El criterio real** | `05` | 1 | el desenlace se da por hecho |
| **Empatía** | `01 humanidad` | 2 | la pregunta lleva jerga del que la hace |
| **Conciencia** | `02 humanidad` | 0 | no afirma cómo funciona un ente: no tiene mutante |

**Y el total son 417, y catorce familias.** **Eso es el número que importa, y no los 417: catorce mutantes fuertes, y los que salgan mal se abren.**

---

## Por qué catorce y no 417

**Porque una familia se rompe de una manera.**

**Ejemplo con la familia del piso, que tiene 58 reglas:** **«el piso se mide antes de prometer» es la madre.** **«el piso se mide antes de prometer cuando no hay red» es un caso.**

**Y si el ente promete sin haber medido, el mutante de la madre lo nota.** **El del caso también, por inclusión.**

**Y lo contrario no vale:** **si el ente mide bien cuando no hay red pero no cuando la hay, la madre truena y el caso no.** **Por eso el caso se corre igual si la madre sobrevive.**

---

## Lo que falta para que esto esté completo

**Esto es la lista de familias. No es la lista de mutantes.**

```plaintext
hecho      catorce familias, con sus 417 reglas contadas
           y cuál es la regla madre de cada una
falta      el mutante escrito de cada madre, en concreto:
           qué línea se cambia, y por qué otra
falta      la tabla de inclusión: qué regla hija depende de qué madre
falta      correrlas, y abrir las que sobrevivan
```

**Y el número honesto, sin adornos:** **catorce mutantes madres es el piso. No es el total.** **El total se sabe cuando las catorce se corran y se vea cuántas hay que abrir.**

**Inventar el total ahora sería exactamente lo que el repositorio prohíbe: un hueco rellenado con lo probable.**

---

## Cómo se escribe un mutante madre

**No basta con decir «se rompe la familia». Hace falta la línea.**

```plaintext
la regla       el piso se mide antes de prometer
el mutante     «el piso se mide antes de medir»  →  «el piso se mide
               si hay tiempo»
la corrida     se levanta el ente, se le pide algo que el piso no tiene,
               sin medirlo antes
lo que tiene que pasar    el ente dice «no pude» en vez de decir qué falta
si no pasa                el ensayo no obliga a medir: la regla no está
                          probada, y se escribe lo que falta
```

**Y la mutación es una frase del ensayo, no una línea de código.** **Se cambia el ensayo, se levanta el ente con el ensayo cambiado, y se ve si la corrida lo nota.**

**Por eso esto funciona con cualquier stack, y por eso el plan no depende de que la implementación sea la de aquí.**

---

## Lo que se apunta de cada mutante que sobrevive

```plaintext
la familia
la regla madre
qué salió cuando se corrió, literal
y la pregunta que abre:  ¿el ensayo no lo decía, o lo decía de una
                         manera que no se puede ejecutar?
```

**Las dos respuestas van a sitios distintos.** **La primera es un hueco de contenido: el ensayo no lo dice y hay que escribirlo.** **La segunda es un hueco de forma: lo dice, y no se puede correr.**

**Y la tercera respuesta, que también existe:** **lo dice, se puede correr, y la corrida estaba mal hecha.** **Ésa no es del ensayo, y se dice.**

---

## Falsificador

**Una familia sin su regla madre, presentada como si tuviera una.** **Un total de mutantes inventado antes de correr ninguno.** **Y lo más probable: catorce familias contadas y creídas completas, cuando un ensayo tiene una regla que no cabe en ninguna de las catorce.**
