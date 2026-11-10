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
| `python -m scripts --piso` | el estado del repositorio, que va a `estado.md` |
| `python -m scripts --X` | informa lo que el trabajo X cambiaría |
| `python -m scripts --escribe X` | lo hace |

Los trabajos: `piso`, `citas`, `rutas`, `reapunta`, `forma`, `negritas`, `sin_y`,
`sin_numeros`, `ofusca` y `licuadora`.

---

Y para lo de dentro, el detalle está en [repo/readme.md](repo/readme.md).
