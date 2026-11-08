# La implementación del autor

**El stack que se eligió, en una tabla que se llena a mano.** **No es una configuración: nadie la va a leer con un programa.**

---

## Lo que hay que llenar

**Cada renglón, uno. Lo que está en blanco se llena, y lo que está puesto se respeta o se cambia.**

| El campo | Qué va ahí | El valor |
|---|---|---|
| **el ente** | un nombre corto | |
| **el dueño** | quién decide, con nombre | |
| **el motor** | dónde vive | `DeepSeek Harness` |
| **el catálogo** | cómo llega a otros | `dshmarket` |
| **la base** | dónde vive el criterio | `graphdblite` |
| **el cuerpo** | qué modelo piensa | |
| **el sesgo del cuerpo** | lo que hace mal ese modelo | |
| **la autoridad** | quién firma | |
| **lo que la autoridad no decide** | lo que el ente no decide nunca | |

**Y una sola cosa que se dice y no se llena:** **la base está puesta en `graphdblite`, y no es un gusto como el motor y el catálogo.** **El índice es un grafo con tres relaciones —contiene, asocia, supera— y la consulta que más se va a hacer es por dónde se llega de un tema a otro.** **En una tabla de renglones eso es un recorrido escrito a mano; en un grafo es una arista.**

---

## La forma de la carpeta

**Y se reconoce en el acto cuál de las cuatro existe.**

| La carpeta o el archivo | Qué es | ¿Existe? |
|---|---|---|
| **`template.md`** | el `AGENTS.md`, inmutable: qué ejecutar y cuándo | **no** |
| **`skills/`** | lo que el ente sabe hacer | **no** |
| **`scripts/`** | lo que el ente corre | **no** |
| **`entity/`** | la base, y nace al soltar la implementación en un proyecto | **no** |

**Y cuando algo de esa lista se escriba, cambia a «sí», y no antes.** **Eso no lleva un archivo de control: se cambia en esta tabla.**

---

## Falsificador

**Un stack del autor presentado como requisito del trabajo.** **La señal, en el acto:** **si una página del repositorio dice «hay que usar» alguna de estas tres cosas.**
