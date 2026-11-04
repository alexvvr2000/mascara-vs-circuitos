# 3. Lo que te puede salir mal

**Cinco trampas que se repiten, para el que venga. Y son de entendimiento, no de implementación.**
**Alejandro Valenzuela Rivera · 4 de noviembre de 2026.**

---

## Por qué este archivo va aquí y no en la guía

**Porque no se arregla con un archivo:** se arregla **sabiendo que existe.** **Estas no fallan por la herramienta: fallan porque el que las hace cree que ya terminó.**

---

## Las cinco

### 1. La tabla perfecta y vacía

**Se construye todo —el `AGENTS.md`, la base, las vistas— y no se apunta nada**, porque apuntar da flojera y las primeras cinco veces salió bien.

**Un registro vacío cumple todos los requisitos y no prueba nada.**

**Cómo se reconoce:** la base está creada y tiene **cero filas después de una semana.**

---

### 2. El registro de aciertos

**Se apunta lo que salió bien y no lo que se cayó.** Es más cómodo, **y es un archivo de buena reputación, no un criterio.**

**Cómo se reconoce:** **no hay una sola fricción**, o todas son de cosas triviales.

---

### 3. El hueco rellenado

**Cuando falta un dato, se pone el que debía de haber.**

**Un banco que se completa con lo probable deja de ser prueba y se vuelve costumbre.**

**Cómo se reconoce:** **no hay ni un `no sé`, ni un `no lo abrí`, ni un `no se probó` en todo el registro.** **Esa ausencia es la señal, no la virtud.**

---

### 4. La copia del que vino antes

**Se copia una implementación ajena —o una plantilla— tal cual, sin saber por qué es así.**

**Funciona mientras la realidad sea la misma; el día que cambie, no hay quien sepa qué parte se puede mover y qué parte no.**

**Cómo se reconoce:** **no puedes explicar por qué cada pieza está donde está, sin leer el archivo.**

---

### 5. El desenlace que nunca llega

**Se escriben las fricciones y se ponen sus reglas, y **nunca se vuelve a probar nada**. Se lee como un criterio completo.

**Es un diario.** Registra; no pondera.

**Cómo se reconoce:** **ningún `se volvió a caer` en el banco.** **Y si nunca hay uno, la regla no se está usando.**

---

## De las cinco, la más peligrosa es la tercera

**Porque no se ve.** Las otras cuatro se notan: la tabla vacía, el registro sin fricciones, la copia, el diario. **El hueco rellenado se ve exactamente igual que un dato.**

**Y por eso el esquema de la base tiene `NOT NULL` y `CHECK`:** **no para castigar, sino para que el hueco tenga dónde verse.**

---

## La prueba de esta carpeta

**¿Cuál de las cinco estás haciendo ahora mismo?**

**Si no puedes contestar, es la tercera.**
