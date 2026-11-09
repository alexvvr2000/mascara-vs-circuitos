# La jerarquía de inclusión

**Por qué no hay que correr un mutante por regla, y cómo se sabe cuántos se pueden saltar.**

**Alejandro Valenzuela Rivera · `TESTIGO`.** **Escrito el 2026-11-08.**

---

## El problema, en números

**Las reglas de los ensayos, contadas.** **Las de conducta se prueban con un caso.**

**Y el resto, corrido uno por uno, son decenas de sesiones a mano.**

**Y la mitad no hace falta correrla, por una razón que existe desde 1988.**

---

## La idea

**Dos mutantes pueden estar relacionados, y no es lo mismo el fuerte que el débil:**

```plaintext
el fuerte   rompe la REGLA ENTERA
            «el ente propone, la autoridad cierra»
            →  «el ente cierra»

el débil    rompe UN CASO de la regla
            «el ente propone, la autoridad cierra»
            →  «el ente cierra cuando la autoridad no está»
```

**Si la corrida mata el fuerte, ya mató al débil.** **No hay que correr el débil: es un caso del fuerte.**

**Y a eso se le llama inclusión:** **el mutante fuerte incluye al débil, y matar uno mata al otro.**

---

## Lo que eso cambia

**No se corren 357.** **Se corre el más fuerte de cada familia, y los demás se dan por muertos si el fuerte murió.**

**Y si el fuerte sobrevive, ahí sí hay que correr los débiles**, porque el ensayo ya falló en lo grande y hay que saber en qué caso.

---

## Las tres formas de estar incluido

**Un mutante está incluido en otro de tres maneras, y no son lo mismo:**

### Uno. Por ámbito

**El débil rompe una parte del fuerte.**

```plaintext
fuerte   se borra la regla entera del cierre
débil    se le quita solo «la autoridad»
```

**Matar el fuerte mata al débil, porque el débil es un pedazo del fuerte.**

### Dos. Por condición

**El débil añade una condición que el fuerte no tiene.**

```plaintext
fuerte   el piso dice «no hay» cuando falta la herramienta
débil    el piso dice «no hay» cuando falta la herramienta Y no hay red
```

**El débil nunca puede fallar si el fuerte no falla: es el fuerte con algo más.**

### Tres. Por orden

**El débil sólo puede ocurrir después del fuerte.**

```plaintext
fuerte   el hecho apunta a un cuerpo que no existe
débil    el hecho apunta a un cuerpo que existe pero que no es el suyo
```

**Si el fuerte no se nota, el débil tampoco: para llegar al débil hay que pasar por el fuerte.**

---

## Lo que la jerarquía NO dice

**Y esto es lo que hay que dejar claro antes de usarla:**

**Mutar el fuerte no es lo mismo que mutar el débil.** **Un ensayo puede decir la regla entera y fallar en un caso, sin que romper la regla entera lo note.**

**La inclusión dice que matar el fuerte mata al débil.** **No dice lo contrario.**

**Si el fuerte muere y el débil sobrevive — y puede pasar, si el débil toca algo que el fuerte no toca — entonces el débil tiene que correrse igual.**

**Por eso la jerarquía ahorra trabajo y no quita trabajo.** **Quita el que es redundante, y deja el que no lo es.**

---

## Cómo se aplica, en el orden que importa

```plaintext
1. se listan los mutantes de cada ensayo
2. se marca, para cada uno, quién lo incluye y quién está incluido en él
3. se corre el más fuerte de cada familia
4. y los débiles:
     si el fuerte murió   →  se apuntan como muertos por inclusión,
                             y se dice que se mataron por inclusión
                             y no corriéndolos
     si el fuerte sobrevivió  →  se corren los débiles, porque el fallo
                                 está en algún caso y hay que saber cuál
```

**Y el paso 4 es el que se olvida.** **Un mutante muerto por inclusión no se mató: se dio por muerto.** **La diferencia importa, y se apunta.**

---

## Lo que se dice cuando se usa

**Un mutante muerto por inclusión no es lo mismo que un mutante que se corrió y murió.**

```plaintext
corrido y muerto         es una prueba
muerto por inclusión     es una deducción, y depende de que la inclusión
                         esté bien calculada
```

**Y la inclusión puede estar mal calculada.** **Si alguien cree que A incluye a B y no lo hace, B queda sin probar y en el registro parece muerto.**

**Por eso se apunta de qué otra regla depende cada mutante muerto por inclusión, y no sólo que murió.**

---

## Lo que esto hace con el número

**No se puede decir de antemano cuántos se ahorran, y no se va a inventar.** **Se sabe cuando se hace:**

```plaintext
un mutante por regla
  menos los que están incluidos en otro
  = los que se corren de verdad
```

**Y lo único honesto mientras no se haga es esto: la jerarquía existe, sirve, y su efecto exacto depende de cómo estén escritas las reglas — y no se ha contado todavía.**

---

## De dónde salió

| Lo que este apartado afirma | De dónde viene |
|---|---|
| una prueba adecuada para un criterio fuerte lo es para uno débil | la jerarquía de subsumción de los criterios de flujo de datos: **Frankl & Weyuker (1988)**, *An Applicable Family of Data Flow Testing Criteria*, IEEE TSE 14(10) |
| el criterio de adecuación como regla de parada | **Goodenough & Gerhart (1975)**, *Toward a Theory of Test Data Selection*, IEEE TSE |
| matar mutantes mide la fuerza de una prueba | **DeMillo, Lipton & Sayward (1978)**; ver también el [Mutation Testing Repository](https://mutationtesting.uni.lu/theory.php) |
| la mutación tiene un costo que obliga a seleccionar | [Software Engineering: Standing on the Shoulders of Giants, §10.1.5](https://www.swebook.org/chapters/10-testing/) |

**Y lo que estas fuentes no dicen, y se apunta:** **ninguna cuenta cuántos mutantes hay en estos trece ensayos.** **Ese número es de aquí, y se contó aquí.**

---

## Falsificador

**Una jerarquía que se usa para no correr nada.** **Y su contraria: una que se ignora y corre un mutante por regla para descubrir que la mitad eran casos de la otra mitad.**

**Y el más probable, que también se apunta:** **una jerarquía mal calculada, donde un mutante se da por muerto porque otro murió, sin que la inclusión fuera cierta.**
