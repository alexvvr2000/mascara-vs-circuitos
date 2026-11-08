# `SKILL.md` — la plantilla

**Este archivo no se llama `SKILL.md` a propósito.** **Si se llamara así en esta carpeta, el harness de quien abriera el repositorio lo cargaría como una habilidad suya, sin que nadie se lo pidiera.**

---

## Antes de copiar: los dos nombres

```plaintext
este archivo        AGENTS/SKILL.plantilla.md
donde va            <proyecto>/.dsh/skills/ente/SKILL.md
y se renombra       SKILL.md, exactamente así
```

**Y el `AGENTS.plantilla.md` de esta misma carpeta va a la raíz de ese proyecto, renombrado `AGENTS.md`.**

**Los dos pasos, sin saltarse ninguno:**

```plaintext
1. copiar los dos archivos al proyecto donde se va a usar
2. renombrarlos: AGENTS.md en la raíz, y SKILL.md dentro de .dsh/skills/ente/
```

**Y la señal de que se hizo mal:** **el proyecto donde se copiaron empieza a comportarse como si tuviera un ente que no eligió.**

---

## El encabezado, y por qué tiene seis campos

**`DSH` lee el encabezado para saber qué es esta habilidad y cuándo usarla.** **Tres son obligatorios y tres no:**

```yaml
---
name: ente
description: Levanta un ente con sus cuatro piezas y deja rastro de lo que decide, con su piso medido y su frontera declarada. Úsalo cuando haya que decidir algo y poder revisarlo después.
license: CC-BY-4.0
compatibility: Bash y Python 3. Una base de datos embebida, cualquiera.
metadata:
  version: "1.0"
  autores: Alejandro Valenzuela Rivera
allowed-tools: Read Write Edit Bash
---
```

| El campo | Obligatorio | Qué va ahí |
|---|---|---|
| **`name`** | **sí** | minúsculas, números y guiones simples; 1 a 64 caracteres |
| **`description`** | **sí** | **qué hace y cuándo usarlo**; 1 a 1024 caracteres |
| `license` | no | el nombre de la licencia, o un archivo de licencia |
| `compatibility` | no | qué necesita el entorno; hasta 500 caracteres |
| `metadata` | no | pares de clave y valor |
| `allowed-tools` | no | herramientas preaprobadas, separadas por espacios |

---

# SKILL.md

## Qué hace

**Levanta un ente: una unidad que recibe, decide, contesta, y deja rastro de haber contestado.**

**Y lo que lo distingue de un asistente cualquiera:** **cada paso deja un registro que se puede revisar sin preguntarle al ente qué hizo.**

---

## Cuándo usarlo

```plaintext
se usa cuando    hay que decidir algo, y después poder decir por qué
                 el trabajo va a durar más de una sesión
                 y alguien que no estuvo va a tener que revisarlo

no se usa cuando el pedido es una respuesta corta que no se va a revisar
```

---

## Lo que hace falta antes

**Cuatro piezas, y sin ellas no se empieza:**

```plaintext
1. la autoridad     quién decide lo que el ente no decide, con nombre
2. el ente          qué es y hasta dónde llega
3. el propósito     para qué existe, y cómo se sabe que se cumplió
4. el índice        dónde vive lo que sabe, con su borde
```

**Y una opcional:** **el cuerpo.** **Sin él el ente trabaja y pierde la comparación.**

---

## El procedimiento

**En nueve pasos, y cada uno con lo que deja.**

```bash
# 0. las cuatro piezas: se declaran antes de correr nada
# 0a. el cuerpo: se declara, no se deduce
# 0d. el piso: se mide, no se estima
# 0b. lo que se entendió, y el supuesto con su estado
# 1. la frase literal, y de dónde sale lo que se va a decir
# 2. el índice: primero el hueco, después el tema con su borde
# 3. la decisión, con sus cuatro columnas
# 4. la respuesta, con su frontera
# 5. el hecho: qué se pidió, qué pasó, qué falta, qué se aprendió
# 6. la corrección, con su desenlace
```

**Y el cierre:** **el ente propone, la autoridad cierra.** **El ente no se cierra solo, nunca.**

---

## Dónde vive el criterio

**En `ente/`, y no en el modelo.** **Por eso el cuerpo se puede cambiar sin perder nada.**

**Y en un grafo, porque el índice no es una tabla:**

```cypher
// los nodos
CREATE (h:Hecho {que_se_pidio: "...", fecha: "..."})
CREATE (f:Friccion {el_error: "..."})
CREATE (d:Desenlace {resultado: "cumplida"})
CREATE (t:Tema {nombre: "..."})

// y las tres relaciones
(h)-[:TUVIERON]->(f)
(f)-[:TUVIERON]->(d)
(t)-[:CONTIENE]->(t2)
(t)-[:ASOCIA]->(t3)
(t)-[:SUPERA]->(t4)
```

**Y si la base es otra, se cambia el archivo de configuración.** **Lo que no se cambia es la forma.**

---

## Lo que falla si no se corre

```plaintext
sin piso        el ente promete lo que no tiene
sin frontera    el ente decide lo que le tocaba a la autoridad
sin desenlace   el registro queda lleno de anécdotas
y sin cuerpo    los hechos no dicen con qué se hicieron
```

---

## El falsificador de esta habilidad

**Un ente que contesta bien y no deja registro.** **Si eso pasa, esta habilidad no se usó: se usó un asistente con su nombre.**

**Y el que es más probable:** **un registro lleno, con todos los campos, y sin un solo "no sé" — porque el ente rellenó en vez de declarar.**
