**Archivo guardado tal como estaba el 2026-11-08, antes de unificar `sostiene/` en un solo método.** **Sus enlaces apuntan a archivos que ya no existen ahí: lo que decían vive en [`../sostiene/metodo.md`](../sostiene/metodo.md), y el conteo en [`../sostiene/corridas.md`](../sostiene/corridas.md).**

# El método de antes, su README

**Cómo se sabe si lo que un ensayo afirma tiene dientes, y cuándo se para.**

**Alejandro Valenzuela Rivera · el ente.**

---

## Qué es este método, y qué no

**Es el que prueba una regla escrita.** **Se toma la regla, se le da la vuelta, se levanta el ente con el ensayo mutado, y se mira si la corrida lo nota.**

**Y no es el que encuentra lo que el ensayo no dice.** **Ése es el [método A](../huecos/README.md), que levanta un ente entero y anota lo que hubo que inventar.**

**Y por qué hacen falta los dos, en una línea:** **los mutantes sólo prueban reglas que están escritas; la corrida entera encuentra lo que falta y no está escrito.**

---

## I. La idea

**En vez de esperar a que no aparezcan defectos, se meten a propósito.**

**Se toma una regla del ensayo, se le cambia algo para que diga mal, y se levanta el ente con el ensayo mutado.** **Si la corrida no lo nota, el ensayo no probaba esa regla.**

**A eso se le llama mutante, y a la regla que lo mata, un criterio que aguenta.**

> **Y la línea que lo sostiene: nunca confíes en una prueba que nunca has visto fallar.**

**Y lo que esto sí acaba, y es lo que el A no puede:** **las reglas se acaban, y cuando cada una tiene su mutante muerto, este método ya no tiene nada que probar.**

---

## II. Cómo se hace, en cuatro pasos

```plaintext
1. se saca la regla del ensayo, tal como está escrita
2. se escribe su mutante: el ensayo con esa regla al revés
   «el ente propone, la autoridad cierra»  →  «el ente cierra»
3. se levanta el ente con el ensayo mutado y se corre la corrida
4. se mira:
     la corrida truena  →  el mutante murió, y la regla tiene dientes
     la corrida pasa    →  el mutante sobrevive, y la regla no se probaba
```

**Un mutante que sobrevive es un hueco con nombre y apellido.** **No hay que adivinar dónde falta: el mutante lo dice.**

---

## III. Qué cuenta como terminado

```plaintext
cada regla de cada ensayo tiene su mutante
y el mutante muere
```

**Y acá hay una cosa que hay que decir sin adornos, porque cambia lo que esto es:** **esa meta es grande, y larga.** **Y no es la que hace falta para publicar.**

**Lo que sí se puede decir hoy, y es finito:** **lo que hay está escrito, y lo que sobreviva está nombrado.**

---

## IV. Los mutantes que hay

**Están en [`los mutantes`](../sostiene/metodo.md), uno por familia, con lo que rompe cada uno.**

**Y sus catorce fichas están escritas.** **Corridos: los que diga [`corridas.md`](../sostiene/corridas.md), que es el único archivo donde se cuentan, con su fecha y su veredicto.**

**Un mutante escrito, creído corrido, y ninguno ejecutado es el falsificador de este método, y es el que más fácil se cumple.**

---

## V. Lo que este método no prueba, y se cita

> **«Las pruebas pueden revelar la presencia de defectos, pero nunca su ausencia.»**
> — Dijkstra, *Notes on Structured Programming*, EWD249, 1970.

**Un mutante muerto dice que el ensayo notó esa rotura.** **No dice que el ensayo no tenga otras.** **Y por eso el otro método no se tira: se queda para lo que ningún ensayo escribió.**

---

## VI. Cuántas reglas hay

**No se responde aquí.** **Se responde en [`las reglas`](../sostiene/metodo.md), que es donde vive el número, y es el único sitio del repositorio donde vive.**

**Y este método no hace la resta.** **El que la necesite la hace, contra lo que diga el registro de lo corrido.**

**Porque una resta que se puede volver a hacer no envejece; una cifra escrita sí.**

---

## De dónde salió esto

| Lo que este método afirma | De dónde viene |
|---|---|
| un criterio de adecuación es una regla de parada | **Goodenough & Gerhart (1975)**, *Toward a Theory of Test Data Selection*, IEEE TSE |
| «un criterio de adecuación es un predicado que determina si un programa se ha probado suficiente» | **Frankl & Weyuker (1988)**, *An Applicable Family of Data Flow Testing Criteria*, IEEE TSE |
| el puntaje de mutación mide si las pruebas detectan fallas | **DeMillo, Lipton & Sayward (1978)**, *Hints on Test Data Selection* |
| «nunca confíes en una prueba que nunca has visto fallar» | práctica de la disciplina de mutación |
| la cobertura es un piso y no un techo | [Software Engineering: Standing on the Shoulders of Giants, §10.1.3](https://www.swebook.org/chapters/10-testing/) |
| las pruebas revelan la presencia de defectos, nunca su ausencia | **Dijkstra, EWD249 (1970)** |

**Y lo que estas fuentes NO dicen, y se apunta:** **ninguna dice cuándo una descripción está completa.** **Todas dicen cuándo se ha probado suficiente, que es otra cosa, y es la única que se puede decir.**

---

## Prueba

**¿Cada mutante dice qué regla rompe y cómo queda el ensayo? ¿Un mutante que sobrevive está nombrado, y no contado como si no existiera? ¿Se distingue una regla de una explicación? ¿Y se dice en qué estado está cada uno, corrido o no?**

---

**Falsificador:** **un método que cuenta mutantes sin haber corrido ninguno**; **un mutante que sobrevive y no se apunta**; **una regla que no se puede escribir al revés, presentada como si se hubiera probado**; y **un método que dice «completo» apoyándose en una cobertura, cuando la cobertura es un piso y no un techo.**
