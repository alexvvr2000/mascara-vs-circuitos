<!-- voz: de testigo -->
# Metodología

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Tres métodos, cada uno contesta una pregunta distinta, y ninguno tiende al infinito. Y una carpeta de corridas, que es donde se apuntó lo que cada uno encontró.

Alejandro Valenzuela Rivera · el ente.

> Esta página es la puerta, y no el método. Si buscas un método, está en `metodos/`. Si buscas qué se encontró, en `corridas/`. Si buscas cómo se llegó, en `historia/`. Un renglón por sitio, y nada más: lo que diga dos veces el mismo método envejece dos veces.

---

## Los tres, y no se mezclan

| El método | La pregunta que contesta | Cuándo se acaba |
|---|---|---|
| [A · Encontrar huecos](metodos/a%20-%20encontrar%20huecos.md) | ¿qué le falta al ensayo? | cuando el ente se puede levantar sin preguntar nada |
| [B · Mutaciones](metodos/b%20-%20mutaciones.md) | ¿lo que el ensayo dice tiene dientes? | cuando lo que sobrevive está nombrado |
| [C · Análisis de ciclo](metodos/c%20-%20analisis%20de%20ciclo.md) | ¿todo se conecta, sin ambigüedad? | cuando no queda un bloque suelto ni una lectura doble |

Y por qué hacen falta los tres, en una línea: el A encuentra lo que no está escrito, el B prueba lo que sí está escrito, y el C junta lo que sale de los dos en un ciclo que se puede correr. Uno solo deja dos lados sin mirar.

Y por qué esto no tiende al infinito: el A se acaba por el uso, no por el número de huecos; el B se acaba porque las reglas se acaban; y el C se para cuando dos vueltas seguidas no encuentran más que detalle. Lo que no tiene final es la autonomía, y ésa no se mide: se firma.

---

## El árbol, y dónde está cada cosa

```plaintext
metodologia/
  README.md               esta página: la puerta
  como se corre.md        el único sitio con los comandos y el orden

  metodos/                los tres métodos, uno por archivo
    a - encontrar huecos.md          qué le falta al ensayo
    b - mutaciones.md                qué tiene dientes, y la forma de la aserción
    c - analisis de ciclo.md         qué se conecta, y cómo se parte en ideas
    la forma del bloque.md           las ocho líneas de una idea
    los dos puntos iniciales.md      prosa o partido, al mismo bloque
    ensayos que mutan.md             cuántos ensayos, y de qué tamaño
    el reparto.md                    el detalle y el resumen

  corridas/               lo que cada método encontró, y su índice
    indice.md             una línea por corrida: las del A, los mutantes del B, y las vueltas del C
    huecos/               las corridas del método A
    sostiene/             los mutantes del método B, con su .py y sus bancos
    ciclo/                las vueltas del método C, y su estado actual

  ciclo/                  lo que el método C va armando: su puerta, el índice
    README.md             criterio.md, y las fichas de criterio/, una por paso.
                          el tablero de su puerta lo escribe `python -m scripts --paso`
    criterio.md
    criterio/             001 - <.md>, 002 - <.md>, … una ficha por paso
    conexiones.md
    decisiones.md
    folios/
    vNN/                  una vuelta: su registro, su lápida, su grafo y sus pruebas

  historia/               cómo se llegó: los cuadernos, en el orden en que se leen
  lo inexplicable.md      cómo se persigue algo que no se termina
```

---

## Las tres puertas, y por qué se lee en este orden

```plaintext
1. como se corre.md       qué se teclea, y en qué orden. es el único que dice comandos
2. metodos/               qué pregunta contesta cada método, y cuándo se para
3. corridas/indice.md     qué se encontró, corrida por corrida, y de qué ensayo sale
```

Y `historia/` se lee al final, porque no se corre: se lee.

---

## Y la regla que los mantiene legibles

Los números viven en un solo sitio: [el índice de corridas](corridas/indice.md). Ni esta página ni los tres métodos hacen cuentas. El que las necesite las hace contra las carpetas, y las puede volver a hacer.

Porque una resta que se puede rehacer no envejece; una cifra escrita sí.

---

## Y el órgano que deja crecer todo esto sin tocarlo

La obra se corrige sola con un comando, no con memoria: `python -m scripts` comprueba los títulos, los enlaces, las citas por número, la forma, las licencias y REUSE, y se cae con el archivo y el renglón. La forma, con su porqué y con lo que el build no comprueba, está en [la forma de la aserción](metodos/b%20-%20mutaciones.md).

---

Falsificador: una metodología con un método solo. Si sólo se llenan huecos, no se sabe si lo que queda tiene dientes; si sólo se rompen reglas, no se encuentra lo que nunca se escribió; y si sólo se junta un ciclo sin haberse caído antes, lo que se junta es una idea ordenada y no probada.

---

## Lo visto

Que los tres métodos se pueden correr sin pedir permiso, y que ninguno se acaba por sí solo.

Lo que sigue es lo que se sostiene con eso, y lo que todavía se le puede pedir.

---

## Prueba

¿Cada método dice qué entra, qué sale, cuándo se corre y cuándo se para, sin abrir otro archivo? ¿El índice de corridas apunta a la carpeta de cada una, y dice de qué ensayo sale? ¿El árbol cabe en una página, y cada carpeta tiene su puerta?
