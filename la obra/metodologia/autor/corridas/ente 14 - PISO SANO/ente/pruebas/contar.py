import sqlite3
c = sqlite3.connect("pruebas/registro.db")
n = c.execute("SELECT COUNT(*) FROM hecho").fetchone()[0]
print(f"   el registro tiene {n} hechos")
c.close()
