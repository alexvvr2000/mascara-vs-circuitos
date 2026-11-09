# Metodología

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Dos métodos, y cada uno contesta una pregunta distinta. Y ninguno de los dos tiende al infinito.

Alejandro Valenzuela Rivera · `TESTIGO`.

---

## Los dos, y no se mezclan

| El método | La pregunta que contesta | Cuándo se acaba |
|---|---|---|
| **[A · Llenar los huecos](huecos/README.md)** | **¿qué le falta al ensayo?** | **cuando el ente se puede levantar sin preguntar nada** |
| **[B · Ver si se sostiene](sostiene/README.md)** | **¿lo que el ensayo dice tiene dientes?** | **cuando lo que sobrevive está nombrado** |

Y por qué hacen falta los dos, en una línea: los mutantes sólo prueban reglas escritas; la corrida entera encuentra lo que falta y no está escrito. Una sin la otra deja un lado sin mirar.

Y por qué esto no tiende al infinito: el A se acaba por el uso, no por el número de huecos. Y el B se acaba porque las reglas se acaban. Lo que no tiene final es la autonomía, y ésa no se mide: se firma.

---

## El A, y qué hay adentro

```
A · llenar los huecos     se levanta un ente con el ejemplo, se corre,
                          y lo que hubo que inventar es el hueco

  README.md               la meta, cuándo se deja de correr, y por qué las
                          dieciocho corridas son todas de este método
  como se corre.md        los comandos, el orden, y lo que se escribe
  corridas/               una carpeta por corrida: la documentación, el
                          esquema y las filas en texto, y las pruebas
```

## El B, y qué hay adentro

```
B · ver si se sostiene    se rompe una regla a propósito, y se mira
                          si la corrida lo nota

  README.md               la idea, los cuatro pasos, y cuándo se para
  metodo.md               el método entero: la regla, las tareas, el contrato,
                          los bancos, y de dónde sale cada pieza
  forma.md                la forma de la aserción, y las cuatro reglas que
                          comprueba scripts/build.py
  corridas.md             en qué quedó cada mutante: el único conteo
  mutantes/               el código de cada uno, y sus bancos en dumps
```

---

## Lo que no es de ninguno de los dos

| Qué | Dónde | Por qué no es un método |
|---|---|---|
| **[`historia/`](historia/)** | **el registro con fecha, y los errores propios** | **no se corre: se lee** |
| **[`lo inexplicable.md`](lo%20inexplicable.md)** | **cómo se persigue algo que no se termina** | **es el porqué de que haya dos métodos y no uno** |
| **[`indice.md`](indice.md)** | **la lista de las corridas** | **es un índice, no un método** |

---

## Y la regla que los mantiene legibles

Los números viven en dos sitios, y ninguno más: las reglas, en [`metodo.md`](sostiene/metodo.md) §III y §VIII; y las corridas, en [`corridas.md`](sostiene/corridas.md).

Ni este archivo ni los dos métodos hacen cuentas. El que las necesite las hace contra el registro, y las puede volver a hacer.

Porque una resta que se puede rehacer no envejece; una cifra escrita sí.

---

## Y el órgano que deja crecer la obra sin tocarla

La obra se corrige sola con un comando, no con memoria: [`scripts/build.py`](../scripts/build.py) comprueba cuatro reglas —el título, los enlaces, las citas por número, y la forma— y se cae con el archivo y el renglón.

Y la forma, con su porqué y con lo que el build no comprueba, está en [`sostiene/forma.md`](sostiene/forma.md). Sin los números en los títulos, insertar un ensayo deja de ser un mantenimiento: es un renombrado, y el build dice si algo quedó citando al que se movió.

---

Falsificador: **una metodología con un método solo.** **Si sólo se llenan huecos, no se sabe si lo que queda tiene dientes; si sólo se rompen reglas, no se encuentra lo que nunca se escribió.**
