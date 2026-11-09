import os, re, sqlite3, glob
BASE = r"C:\Users\Alex\git\Mascara vs Circuitos\metodologia\huecos"
def try_load(schema, filas):
    db = sqlite3.connect(":memory:")
    db.executescript(open(schema, encoding="utf-8").read())
    err = None
    try:
        db.executescript(open(filas, encoding="utf-8").read())
    except Exception as e:
        err = e
    n_tablas = db.execute("SELECT count(*) FROM sqlite_master WHERE type='table'").fetchone()[0]
    n_filas = 0
    for (t,) in db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall():
        n_filas += db.execute("SELECT count(*) FROM %s" % t).fetchone()[0]
    fk = db.execute("PRAGMA foreign_key_check").fetchall()
    db.close()
    return err, n_tablas, n_filas, fk
for d in sorted(os.listdir(os.path.join(BASE, "corridas"))):
    p = os.path.join(BASE, "corridas", d)
    s = os.path.join(p, "banco_esquema.sql"); f = os.path.join(p, "banco_filas.sql")
    err, t, n, fk = try_load(s, f)
    txt = open(os.path.join(p, "documentacion.md"), encoding="utf-8").read()
    m = re.search(r"(\d+)\s+tablas", txt)
    dice = m.group(1) if m else "?"
    print("%-24s esquema=%d tablas · filas=%d · doc dice=%s · fk=%s · %s" % (d, t, n, dice, "ok" if not fk else fk[:2], "CARGA OK" if not err else "ERROR: %s" % err))
