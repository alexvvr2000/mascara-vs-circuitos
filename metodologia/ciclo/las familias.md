# Las familias de mutantes

**Las reglas, agrupadas por familia, para saber cuál es la fuerte y cuáles son casos.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **Escrito el 2026-11-08.**

---

## Cómo leer esto

**Cada fila es una familia: un grupo de reglas del mismo tipo. Y cada familia tiene sentido mutarla de una sola manera, porque sus miembros se rompen igual.**

**Y ahí está el ahorro, y es el que la jerarquía de inclusión dice en una línea: si el mutante que rompe la familia entera muere, los que rompen un caso también.**

**Por eso no se corre un mutante por regla.** **Se corre uno por familia, y lo que sobreviva se abre.**

---

## Las familias, y de dónde salen

**Y vienen de dos grupos, que no se tocan igual.** **Los ensayos de `ciclo del ente/` se pulen con esta metodología.** **Los de `humanidad/` no: no afirman cómo funciona un ente, y por eso no se pueden romper a propósito.**

### Del ciclo del ente, y son las que se pulen

| Familia | Dónde vive | Reglas | Qué rompe el mutante fuerte |
|---|---|---|---|
| **El ciclo, paso por paso** | [`02`](../../la%20obra/ciclo%20del%20ente/02%20el%20ciclo%20del%20ente.md) | 145 | borra el paso entero, o el campo que lo hace verificable |
| **El piso** | [`03`](../../la%20obra/ciclo%20del%20ente/03%20el%20piso.md) | 58 | el piso miente: dice `hay` sin haberlo medido |
| **El borde del tema** | [`08`](../../la%20obra/ciclo%20del%20ente/08%20el%20borde%20del%20tema.md) | 54 | el borde acepta lo que debía salir |
| **Los sesgos** | [`09`](../../la%20obra/ciclo%20del%20ente/09%20criterio%20y%20sesgos.md) | 38 | el sesgo no se declara, o se declara neutral |
| **Escritura en procesos** | [`04`](../../la%20obra/ciclo%20del%20ente/04%20escritura%20en%20procesos.md) | 22 | el proceso no dice cuándo se corre |
| **El índice** | [`07`](../../la%20obra/ciclo%20del%20ente/07%20indexador%20de%20temas.md) | 14 | el índice se arma a mano y no se puede reconstruir |
| **La frontera** | [`06`](../../la%20obra/ciclo%20del%20ente/06%20la%20frontera%20y%20el%20descarte.md) | 13 | las cuatro columnas se llenan con lo primero que aparezca |
| **Qué es un ente** | [`01`](../../la%20obra/ciclo%20del%20ente/01%20que%20es%20un%20ente.md) | 12 | el ente se define por lo que tiene dentro |
| **El criterio real** | [`05`](../../la%20obra/ciclo%20del%20ente/05%20criterio%20real.md) | 1 | el desenlace se da por hecho |

**Y una que no vive en un ensayo, sino en la lista de afirmaciones:**

| Familia | Dónde vive | Reglas | Qué rompe el mutante fuerte |
|---|---|---|---|
| **Las afirmaciones** | [`la obra/README.md`](../../la%20obra/README.md) | 13 | una afirmación sin dónde vive, o sin qué la tumba |

### De humanidad, que no se pulen con corridas

| Familia | Dónde vive | Reglas | Por qué no tiene mutante |
|---|---|---|---|
| **La medición de talentos** | [`13`](../../la%20obra/humanidad/13%20medicion%20de%20talentos.md) | 33 | mide trabajo hecho, y un mutante no produce trabajo |
| **La máquina de sesgos** | [`10`](../../la%20obra/humanidad/10%20maquina%20de%20sesgos.md) | 25 | afirma qué no se puede probar |
| **Empatía** | [`11`](../../la%20obra/humanidad/11%20empatía.md) | 2 | su prueba es una persona contestando una pregunta |
| **Conciencia** | [`12`](../../la%20obra/humanidad/12%20conciencia.md) | 0 | no afirma cómo funciona un ente |

**Y esto es lo que hay:** **las familias del ciclo del ente son las que la metodología puede pulir.** **Las de humanidad se leen, y no entran en esa cuenta.**

**Y el total de reglas es lo que suma la columna de arriba, y los ensayos son la fuente.** **Ese total es el único número que el repositorio mantiene.**


---

## Por qué una por familia y no una por regla

**Porque una familia se rompe de una manera.**

**Ejemplo con la familia del piso:** **«el piso se mide antes de prometer» es la madre.** **«el piso se mide antes de prometer cuando no hay red» es un caso.**

**Y si el ente promete sin haber medido, el mutante de la madre lo nota.** **El del caso también, por inclusión.**

**Y lo contrario no vale:** **si el ente mide bien cuando no hay red pero no cuando la hay, la madre truena y el caso no.** **Por eso el caso se corre igual si la madre sobrevive.**

---

## Lo que falta para que esto esté completo

**Esto es la lista de familias. No es la lista de mutantes.**

```plaintext
hecho      las familias, con sus reglas contadas
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
