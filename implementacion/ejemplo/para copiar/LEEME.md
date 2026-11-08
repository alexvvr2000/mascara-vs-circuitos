# Lo que se copia

**Una carpeta, y seis pasos.** **Los dos primeros son renombrar, y sin ellos no funciona.**

**Y el stack ya viene puesto: no hay que elegir motor, catálogo ni base.**

---

## Los pasos

**1 · Se copia esta carpeta entera al proyecto.**

**2 · Se renombran dos archivos.** **Y hay que hacerlo, porque el nombre que el motor lee no puede estar aquí dentro:**

```plaintext
hoja de reglas.md   ->  AGENTS.md          en la raíz del proyecto
skills/ente/la habilidad.md  ->  skills/ente/SKILL.md
```

**Y por qué se renombran al copiar y no vienen ya puestos:** **si estos dos archivos tuvieran su nombre dentro de este repositorio, el motor de cualquiera que lo abriera los leería como si fueran sus instrucciones.** **Y aplicaría las reglas de un ente a un proyecto que no es ese ente, sin que nadie se lo pidiera.**

**3 · Se llenan los renglones vacíos** de `autoridad.md`, `proposito.md` y `cuerpo.md`.

**4 · Se escriben los temas en `indice/`**, uno por archivo, cuando aparezcan.

**5 · Se crea `registro.db`.** **Nace vacío la primera vez.**

**6 · Y se trabaja.**

---

## Cómo se ve el proyecto después

```plaintext
mi-proyecto/
  AGENTS.md              ← era "hoja de reglas.md"
  autoridad.md
  proposito.md
  cuerpo.md
  indice/
  skills/ente/SKILL.md   ← era "la habilidad.md"
  registro.db
```

**Y los seis pasos de arriba son todo.** **No hay nada que instalar, ni qué registrar, ni qué configurar en ningún lado.**

---

## Qué stack trae

**Una versión con un stack ya elegido:** **un motor donde el ente vive, un catálogo de lo que se puede instalar, y una base donde vive el criterio.**

**Y el catálogo no es para instalar esto: es para instalar lo que el ente necesite usar.**

**Si se quiere otro stack, se cambia ahí.** **La carpeta funciona igual, porque lo que pide es una carpeta de texto y un registro.**

---

## Lo que hay que saber antes de empezar

**`AGENTS.md` es inmutable.** **No se edita: se obedece.** **Si algo no cabe, o el proyecto no es para esto, o la hoja está mal.**

**Y las tres piezas se llenan una vez.** **Si cambia la autoridad o el propósito, se cambia ahí, y el registro dirá cuándo.**

---

## Si algo no funciona

**Se dice qué falta, con nombre.** **Y no se rellena el hueco con lo que parecía.**

**Y si lo que falla es el stack y no la hoja, eso también se dice: es del stack, y no del ente.**

**Falsificador:** una carpeta copiada sin renombrar los dos archivos. **La señal, en el acto:** **el motor no lee nada y el ente trabaja sin reglas.**
