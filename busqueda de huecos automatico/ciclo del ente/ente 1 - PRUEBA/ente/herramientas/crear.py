"""crear.py — crea la base, y prueba que rechaza lo que debe rechazar.

Un esquema que no se ha probado es una intención escrita.

Se corre así, desde la carpeta del ente:

    python herramientas/crear.py

Y si la base ya existe, se para: no pisa lo que hay.
"""

import pathlib
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AQUI = pathlib.Path(__file__).resolve().parent
ENTE = AQUI.parent
ESQUEMA = AQUI / "tablas.sql"
BANCO = ENTE / "banco.db"


def probar_reglas(c: sqlite3.Connection) -> list[tuple[str, bool, str]]:
    """Corre cada regla contra la base, y dice si rechazó lo que debía."""
    pruebas = []

    def rechaza(nombre: str, sql: str, params: tuple = ()) -> None:
        try:
            c.execute(sql, params)
            c.rollback()
            pruebas.append((nombre, False, "LO ACEPTÓ, y no debía"))
        except sqlite3.IntegrityError as e:
            pruebas.append((nombre, True, str(e)))


    rechaza(
        "rechaza un hecho sin modelo",
        "INSERT INTO hecho (fecha,que_se_pidio,que_paso,no_alcanza,no_sabia,modelo_id)"
        " VALUES ('2026-11-05','a','b','c','d',99)",
    )
    rechaza(
        "rechaza una fricción sin por_que_era_creible",
        "INSERT INTO friccion (hecho_id,el_error,por_que_era_creible,como_se_reconoce,"
        "que_hago_en_su_lugar,quien_lo_corrigio) VALUES (NULL,'e',NULL,'c','q','x')",
    )
    rechaza(
        "rechaza un tema sin borde",
        "INSERT INTO tema (ente_id,nombre,quien_evalua,entra_si,no_entra,y_si_duda,desde)"
        " VALUES (1,'t','maquina',NULL,'n','d','2026-11-05')",
    )
    rechaza(
        "rechaza un tema que no dice quién evalúa",
        "INSERT INTO tema (ente_id,nombre,quien_evalua,entra_si,no_entra,y_si_duda,desde)"
        " VALUES (1,'t','dios','e','n','d','2026-11-05')",
    )
    rechaza(
        "rechaza un supuesto sin estado",
        "INSERT INTO hecho (fecha,que_se_pidio,que_paso,no_alcanza,no_sabia,supuesto,modelo_id)"
        " VALUES ('2026-11-05','a','b','c','d','supuse algo',1)",
    )
    rechaza(
        "rechaza un estado de supuesto que no es las tres palabras",
        "INSERT INTO hecho (fecha,que_se_pidio,que_paso,no_alcanza,no_sabia,supuesto,supuesto_estado,modelo_id)"
        " VALUES ('2026-11-05','a','b','c','d','x','lo que sea',1)",
    )

    # estas NO deben fallar
    try:
        c.execute(
            "INSERT INTO proposito (ente_id,que,desde) VALUES (1,'p','2026-11-05')"
        )
        c.execute(
            "INSERT INTO proposito (ente_id,que,desde) VALUES (1,'otro','2026-11-05')"
        )
        pruebas.append(("deja varios propósitos abiertos a la vez", True, "2 abiertos"))
    except sqlite3.IntegrityError as e:
        pruebas.append(("deja varios propósitos abiertos a la vez", False, str(e)))

    rechaza(
        "rechaza cerrar un propósito sin motivo",
        "UPDATE proposito SET hasta='2026-11-06' WHERE id=1",
    )
    rechaza(
        "rechaza cerrar un propósito sin que la autoridad conste",
        "UPDATE proposito SET hasta='2026-11-06', cerrado_por='lo cerré' WHERE id=1",
    )
    rechaza(
        "rechaza dos desenlaces con una palabra que no es de las tres",
        "INSERT INTO desenlace (friccion_id,fecha,resultado,circunstancia,cambio)"
        " VALUES (1,'2026-11-05','quiza','c','c')",
    )
    c.rollback()
    return pruebas


def main() -> None:
    if BANCO.exists():
        print(f"Ya existe {BANCO.name}. No se pisa: si quieres empezar de cero, borrala.")
        sys.exit(1)

    if not ESQUEMA.exists():
        print(f"No encuentro {ESQUEMA}. Los dos archivos tienen que estar juntos.")
        sys.exit(1)

    print("=" * 72)
    print("CREANDO LA BASE DE PRUEBA")
    print("=" * 72)

    c = sqlite3.connect(BANCO)
    c.execute("PRAGMA foreign_keys = ON")
    c.executescript(ESQUEMA.read_text(encoding="utf-8"))

    tablas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    vistas = [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='view' ORDER BY name")]
    print(f"\nesquema: OK — {len(tablas)} tablas, {len(vistas)} vista")
    print(f"  tablas: {', '.join(tablas)}")
    print(f"  vista:  {', '.join(vistas)}")

    # los datos del paso 0: la autoridad, el ente y el modelo
    c.execute(
        "INSERT INTO autoridad VALUES (1,'Alejandro Valenzuela Rivera','2026-11-05',"
        "'el para qué, la firma, y lo que se decide cuando está en juego él o su gente',"
        "'lo que PRUEBA sostiene: PRUEBA no firma por él')"
    )
    c.execute(
        "INSERT INTO ente VALUES (1,'PRUEBA','Alejandro Valenzuela Rivera','2026-11-05',"
        "1,'su propia carpeta','entender, buscar, proponer y apuntar',1)"
    )
    c.execute(
        "INSERT INTO modelo (id,nombre,via,sesgo_conocido,desde) VALUES "
        "(1,'DeepSeek V4.1 Flash','DeepSeek Harness',"
        "'complacencia, relleno, inflación de forma','2026-11-05')"
    )
    c.commit()
    print("\nlas piezas del paso 0: autoridad, ente y modelo declarados")

    print("\n" + "-" * 72)
    print("PROBANDO QUE EL ESQUEMA RECHAZA LO QUE DEBE")
    print("-" * 72)
    fallas = 0
    for nombre, paso, detalle in probar_reglas(c):
        marca = "OK  " if paso else "FALLA"
        print(f"  [{marca}] {nombre}")
        if not paso:
            fallas += 1
            print(f"          -> {detalle}")

    c.close()
    print("-" * 72)
    if fallas:
        print(f"{fallas} reglas NO se cumplieron. El esquema está mal.")
        sys.exit(1)
    print("todas las reglas se cumplieron. La base está lista.")


if __name__ == "__main__":
    main()