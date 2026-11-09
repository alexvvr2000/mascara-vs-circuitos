**Archivo guardado tal como estaba el 2026-11-08, antes de que esta carpeta se quitara.** **Lo que decía vive hoy, y unido, en [`../sostiene/metodo.md`](../sostiene/metodo.md); el conteo de las corridas, en [`../sostiene/corridas.md`](../sostiene/corridas.md); y los bancos, en [`../sostiene/mutantes/_dumps/`](../sostiene/mutantes/_dumps/).**

# El método de antes, sus corridas

**Cuáles se corrieron, y en qué quedaron. Y el número no vive aquí: vive en [`../corridas.md`](../sostiene/corridas.md).**

**El método B no tiene una carpeta por corrida todavía.** **Tiene trece mutantes con su script, y cada uno se corre con `python mN.py comparar`: levanta el ente bueno y el mutado, y da el veredicto.**

**Y lo que falta, y es lo que va a llenar esta carpeta, es una cosa concreta:**

```plaintext
se toma el mutante
se levanta el ente con el ensayo mutado, en una carpeta nueva con fecha
se corre
y se mira si la corrida lo nota

  lo nota      el mutante murió, y la regla tiene dientes
  no lo nota   el mutante sobrevive, y la regla no se probaba
```

**Y lo que salga se guarda con el mismo árbol que las corridas del método A:** **la documentación, el esquema y las filas en texto, y las pruebas si las hubo.** **Las filas ya están, en [`../mutantes/_dumps/`](../sostiene/mutantes/_dumps/): un `.sql` por banco, en texto y ofuscado, generado por [`../mutantes/dumps.py`](../sostiene/mutantes/dumps.py).**

**Y el criterio para no confundirlas:** **una corrida del A levanta un ente y anota lo que hubo que inventar.** **Una corrida del B levanta un ente con el ensayo cambiado, y la pregunta no es qué se inventó: es si la corrida se dio cuenta.**

---

**Falsificador:** **una corrida guardada aquí que no tenga un mutante al que corresponde.** **Eso no sería una prueba del ensayo: sería otra corrida del método A con otro nombre.**
