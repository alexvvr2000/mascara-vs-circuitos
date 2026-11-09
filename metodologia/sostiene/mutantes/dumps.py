import glob
import os
import sqlite3

AQUI = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.join(AQUI, "_dumps")
LIMITE = 40


def ofuscar(v):
    if v is None:
        return "NULL"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, bytes):
        return "x'" + v.hex() + "'"
    s = str(v)
    if len(s) > LIMITE:
        s = "[texto %d chars]" % len(s)
    return "'" + s.replace("'", "''") + "'"


def dump(banco):
    carpeta = os.path.basename(os.path.dirname(banco))
    nombre = os.path.basename(banco).replace(".db", ".sql")
    con = sqlite3.connect(banco)
    tablas = [r[0] for r in con.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    lineas = ["-- dump ofuscado de %s/%s" % (carpeta, os.path.basename(banco)),
              "-- sin texto largo: se sustituye por su tamano. sin rutas, sin usuarios, sin fechas del sistema.",
              "-- se vuelve a cargar con sqlite3: python -c \"import sqlite3; db=sqlite3.connect('x.db'); db.executescript(open('este.sql', encoding='utf-8').read())\"",
              ""]
    for t in tablas:
        cols = [r[1] for r in con.execute("PRAGMA table_info(%s)" % t)]
        filas = con.execute("SELECT * FROM %s" % t).fetchall()
        lineas.append("-- tabla %s (%d columnas, %d filas)" % (t, len(cols), len(filas)))
        lineas.append("CREATE TABLE %s (%s);" % (t, ", ".join(cols)))
        for f in filas:
            lineas.append("INSERT INTO %s VALUES (%s);" % (t, ", ".join(ofuscar(v) for v in f)))
        lineas.append("")
    con.close()
    with open(os.path.join(DESTINO, nombre), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lineas))
    return nombre


def main():
    os.makedirs(DESTINO, exist_ok=True)
    bancos = sorted(glob.glob(os.path.join(AQUI, "*", "*-bueno.db")) +
                    glob.glob(os.path.join(AQUI, "*", "*-mutado.db")))
    for b in bancos:
        print(dump(b))


if __name__ == "__main__":
    main()
