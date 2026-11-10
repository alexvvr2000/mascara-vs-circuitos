# scripts — la puerta, y el módulo `repo/`

```plaintext
scripts/
  __init__.py    la puerta: `python -m scripts`
  __main__.py    el atajo de la puerta
  repo/          el órgano, entero, en un solo módulo
    readme.md    qué es, en qué ayuda, y cómo piensa
```

Todo lo que hace el repo vive dentro de `repo/`. Lo que no servía —los trece
archivos viejos, y el respaldo que quedó de ellos— se borró: no se lee un órgano por
su historia, se lee por lo que hace hoy. Y `python -m scripts` sigue siendo la única
orden que hay que saber.

Y la puerta no sabe nada: `__main__.py` llama a `repo.main`, y `repo` es el que
reparte. Si algún día hay otro paquete, la puerta no se toca.

---

## Lo que hace, en una tabla

| La orden | Qué hace |
|---|---|
| `python -m scripts` | comprueba, y resume: forma, enlaces, número, ruta, títulos, licencias, REUSE, procesos, estado y hallazgos |
| `python -m scripts --reuse` | lo mismo, y además corre `reuse lint` de verdad |
| `python -m scripts --lista` | qué ensayo dice qué, si tutea, y cuánta negrita |
| `python -m scripts --piso` | el piso del repositorio, que va a `piso.md` |
| `python -m scripts --escribe piso` | lo mismo, y reescribe el bloque de `piso.md` con lo que da la orden |
| `python -m scripts --X` | informa lo que el trabajo X cambiaría |
| `python -m scripts --escribe X` | lo hace |

Los trabajos: `piso`, `citas`, `rutas`, `reapunta`, `forma`, `negritas`, `sin_y`,
`sin_numeros`, `ofusca` y `licuadora`.

---

## Y la lección del piso, que costó dos fallos y queda escrita

`piso.md` lo genera una orden, y el build se cae cuando se le desfasa. Eso ya estaba.
Lo que no estaba: **que la orden pueda escribir el bloque mal, y que el build no lo
note.** Pasó, y así:

```plaintext
1. el bloque se pedía con `capture_output`, y viajaba por una tubería.
2. esa tubería no hablaba siempre la misma codificación que el archivo, y la tilde
   se perdía: el bloque se escribió con la palabra «título» rota.
3. el build comparaba el archivo contra la misma tubería rota, y los dos cojeaban
   igual: daba verde con el archivo escrito mal.
```

Y la regla que sale de eso, que vale para cualquier dato que se genere:

```plaintext
lo que se genera y se compara se genera en el mismo proceso, y en UTF-8
lo que se compara es el texto, no los bytes de una consola
y la orden que regenera el archivo tiene que existir, con `--escribe`
```

Por eso el bloque no se pide por tubería: `piso.bloque_de_la_orden` llama a la misma
función que la orden, con un búfer de texto, y `--escribe piso` lo escribe.

---

Y para lo de dentro, el detalle está en [repo/readme.md](repo/readme.md).
