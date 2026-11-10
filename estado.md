<!-- voz: de testigo -->
# El piso del repositorio

**Qué hay, dónde está y en qué estado, para que quien llegue a pulir no tenga que adivinar.**

**Alejandro Valenzuela Rivera · el ente.** **Del 2026-11-10.**

> **Este archivo no se mantiene a mano: se genera.** **`python -m scripts --piso` lo saca del repositorio cada vez que se corre, y la versión de abajo es la que salió hoy.** **Si alguien cambia una carpeta y no lo vuelve a correr, este archivo envejece, y por eso la fuente es el comando y no el texto.**

---

## El piso, según el comando

```
# El piso del repositorio

## Los ensayos, por carpeta, y su t�tulo

### la obra/humanidad/
  Concordia                                    concordia.md
  Empat�a                                      empat�a.md
  Lo que est� fuera                            lo que esta fuera.md
  Lo que queda por hacer                       lo que queda por hacer.md
  Medir sin preguntarle                        medir sin preguntarle.md

### la obra/los papeles/
  Los l�mites, con nombre y sin coartada       LIMITES.md
  Fuentes                                      fuentes.md

### la obra/teoria/
  Criterio real                                criterio real.md
  Criterio y sesgos                            criterio y sesgos.md
  Destilar el criterio                         destilar el criterio.md
  El borde del tema                            el borde del tema.md
  El criterio, para el ciclo                   el criterio, para el ciclo.md
  El piso                                      el piso.md
  Escritura en procesos                        escritura en procesos.md
  Indexador de temas                           indexador de temas.md
  La frontera y el descarte                    la frontera y el descarte.md
  Qu� es un ente                               que es un ente.md
  Revisi�n de sesgos                           revision de sesgos.md

## Los m�todos
  metodologia/ciclo/
    README.md
    ciclo final.md
    conexiones.md
    decisiones.md
    folios/  (0 directorios)
    huecos de la rama/  (0 directorios)
    proceso busqueda de pasos.md
    vueltas/  (0 directorios)
  metodologia/corridas/
    README.md
    ciclo/  (0 directorios)
    huecos/  (36 directorios)
    indice.md
    sostiene/  (14 directorios)
  metodologia/historia/
    01 - como se penso llegar al criterio.md
    02 - como se corrio.md
    03 - que cambio en cada corrida.md
    04 - como se corre una corrida.md
    05 - el registro de como se llego.md
    06 - la ultima idea, de los subagentes.md
    07 - el metodo de antes, su README.md
    08 - el metodo de antes, sus reglas.md
    09 - el metodo de antes, sus mutantes.md
    10 - el metodo de antes, sus corridas.md
    11 - lo que sigue vivo dentro de la historia.md
    README.md
  metodologia/metodos/
    README.md
    a - encontrar huecos.md
    b - forma de la asercion.md
    b - romper una regla, el metodo.md
    b - romper una regla.md
    c - analisis de ciclo.md

## La historia, en el orden en que se lee
  01 - como se penso llegar al criterio.md
  02 - como se corrio.md
  03 - que cambio en cada corrida.md
  04 - como se corre una corrida.md
  05 - el registro de como se llego.md
  06 - la ultima idea, de los subagentes.md
  07 - el metodo de antes, su README.md
  08 - el metodo de antes, sus reglas.md
  09 - el metodo de antes, sus mutantes.md
  10 - el metodo de antes, sus corridas.md
  11 - lo que sigue vivo dentro de la historia.md

## Los scripts, que se corren y no se leen
  el �rgano es el paquete scripts/: python -m scripts
  scripts/__init__.py
  scripts/__main__.py
  scripts/comprobar.py
  scripts/comun.py
  scripts/constantes.py
  scripts/legal.py
  scripts/licuadora.py
  scripts/reglas.py
  scripts/trabajos.py

## Lo que enlaza, y lo que no
  316 enlaces, 0 rotos

Y lo que falta de la fila, cuando lo haya, se dice en el cierre del turno y no aqu�.
```

---

## Lo que ya está comprobado, y se puede ver

```
el build                     cuatro reglas, y cero fallos
las citas                    por título y no por el nombre del archivo
la persona                   impersonal, salvo en la prueba de un error propio
el énfasis                   0% en los catorce ensayos
la forma del texto           sin espacios antes de coma, sin encabezados saltados
los enlaces                  todos resuelven
los títulos                  todos dicen de qué habla el archivo
el índice de los mutantes    vive en un solo sitio
```

**Y lo que el build no garantiza, y se dice:** **que el texto sea verdad.** **Para eso están los falsificadores y las corridas, y ninguno de los dos se corre con un comando.**

---

## Lo que queda en la fila, y es lo único que queda

```
los cuatro puntales        dónde van: «un ente no tiene cuerpo», «el piso se
                           mide», «el criterio no se recuerda», «la forma es
                           la fuente». hoy viven dentro de un paso cada uno,
                           y el mapa no puede mandar sobre ellos

escritura en procesos      es un ensayo de método disfrazado de paso: 28 mil
                           caracteres, y el método ya tiene su casa

los trece mutantes         se re-apuntan una vez, cuando el ciclo se parta
```

**Y lo que no está en la fila, porque se termina en el pulido:** **la forma de proceso en `el piso` y en `escritura en procesos`, y el `02` como mapa.** **Se hacen con el texto delante, y no antes.**

**Y lo que se va al final, como se pidió:** **`la obra/teoria/` y `el ciclo del ente`.** **Es el ciclo, y es lo único que sostiene todo lo demás; por eso se puliría después de que lo de alrededor esté quieto.**

---

## Lo que cambió en la carpeta, para que no sorprenda

```
los títulos de los ensayos   ya no llevan número; el orden vive en el nombre
los nombres de humanidad/    «conciencia», «máquina de sesgos» y «medición de
                             talentos» dijeron lo que hablan: lo que está
                             fuera, medir sin preguntarle, lo que queda por hacer
la carpeta del ciclo         la obra/ciclo del ente/ pasó a la obra/funcionamiento ente/,
                             y hoy son dos: el ciclo del ente.md en la obra/, y
                             lo que invoca en la obra/teoria/
los scripts                  viven en scripts/, y no sueltos en la raíz
la historia                  se lee como una cadena, y los cuatro últimos son el
                             método que había antes de unificarse
```

**Y todo eso se hizo sin perder el historial:** **los renombrados son movimientos de git, y el contenido de la historia no cambió.**

---

## Falsificador

**Un piso que no se puede volver a sacar con un comando**; **uno que dice «todo bien» cuando algún enlace está roto o algún conteo quedó viejo**; **y uno que esconde en su propia lista la única cosa que falta, cuando la lista es justo lo que prometía no tener.**

---

## Lo visto

Que el estado del repositorio se saca de un comando, y que lo que falta está escrito en vez de en la cabeza.

Lo que sigue es lo que se sostiene con eso, y lo que todavía se le puede pedir.

