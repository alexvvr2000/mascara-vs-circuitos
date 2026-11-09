# Corridas del método B

**Vacía, y no es un olvido.**

**El método B no tiene corridas todavía.** **Tiene trece mutantes escritos, en [`mutantes/`](../mutantes/), y cada uno dice qué regla rompe y cómo queda el ensayo con la regla al revés.**

**Lo que falta, y es lo que va a llenar esta carpeta, es una cosa concreta:**

```plaintext
se toma el mutante
se levanta el ente con el ensayo mutado, en una carpeta nueva con fecha
se corre
y se mira si la corrida lo nota

  lo nota      el mutante murió, y la regla tiene dientes
  no lo nota   el mutante sobrevive, y la regla no se probaba
```

**Y lo que salga se guarda con el mismo árbol que las corridas del método A:** **la documentación, el esquema y las filas en texto, y las pruebas si las hubo.**

**Y el criterio para no confundirlas:** **una corrida del A levanta un ente y anota lo que hubo que inventar.** **Una corrida del B levanta un ente con el ensayo cambiado, y la pregunta no es qué se inventó: es si la corrida se dio cuenta.**

---

**Falsificador:** **una corrida guardada aquí que no tenga un mutante al que corresponde.** **Eso no sería una prueba del ensayo: sería otra corrida del método A con otro nombre.**
