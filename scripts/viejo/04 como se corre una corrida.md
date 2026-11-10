# Cómo se corre una corrida

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

El mecanismo que quedó de la práctica: los comandos, el orden, y lo que se escribe en cada momento.

Alejandro Valenzuela Rivera · el ente. Escrito el 2026-11-08, en cuaderno aparte el 2026-11-09.

---

## Entra

Lo que hace falta para levantar un ente desde cero y anotar lo que hubo que inventar.

Y la primera cosa no es un comando: es medir el piso. Versiones que hay, y la salida tal como salió.

```plaintext
lo que se mide    el lenguaje, la base, las herramientas que la corrida va a usar
cómo se mide      cada una con su comando, y se apunta lo que respondió
por qué           un piso medido de memoria es una promesa, no una medición
```

El cómo ampliado, en [Ejercicio: cómo se ve lo que los ensayos no dicen](../../metodologia/como%20se%20corre.md).

## Lo que pasó

Se aprendió a decir el blanco antes de empezar, y a escribirlo.

Una corrida sin blanco es un diario. El blanco sale de lo que dejó abierta la anterior; si no hay nada abierto, de un caso que ningún ensayo tocó. Y se dice cuánto va a durar, en pasos: sin eso la corrida se estira hasta que se acaba el tiempo.

Se aprendió que el orden importa más de lo que parece:

```plaintext
1. se leen los ensayos             sin mirar los entes anteriores
2. se levanta un ente ENTERO       no el pedazo que se prueba
3. se corre de punta a punta       crear, medir, abrir, usar, cerrar
4. se anota lo que hubo que inventar
5. se clasifica                    ensayo / código / entorno
6. se escribe la documentación     con la voz del que corrió
7. se cierra el hueco en el ensayo, y se repite
```

Lo que más se repitió, que fue lo que no se esperaba: lo que hubo que inventar casi nunca era del código. Era del ensayo. El ente hizo lo que pudo con lo que había, y el hueco quedó en el texto que no lo decía.

Y la forma de acusar al ensayo y no al terminal, que es una regla antes que un consejo: cada cosa que sale se clasifica antes de apuntarla. Achacar al ensayo un defecto del terminal estropea el ensayo.

## Dónde queda ahora

- el procedimiento completo del otro método: [Método A · Llenar los huecos](../../metodologia/metodos/a%20-%20encontrar%20huecos.md)
- los comandos, con el ciclo extendido: [Ejercicio: cómo se ve lo que los ensayos no dicen](../../metodologia/como%20se%20corre.md)
- las corridas hechas, cada una en su carpeta: [huecos/corridas](../../metodologia/corridas/huecos/)

## Falsificador

Un procedimiento que se escribió antes de correr y no se corrigió ningún día después. Y su contrario: uno que se corrige cada vez y termina siendo la bitácora de quien lo escribió, y no un procedimiento.

---

## Lo que este cuaderno conserva, y por qué

Los comandos exactos de aquel día no se repiten aquí: dependen de la máquina y envejecen. Lo que no envejece es el orden, y la razón de cada paso.
