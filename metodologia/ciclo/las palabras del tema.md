<!-- voz: de testigo -->
# Las palabras del tema

<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->

Cómo se consulta el índice del ente: un tema lleva sus palabras clave, y una palabra que se parece a otra no es la otra. Es la regla que impide que un ente conteste lo que no tiene escrito, y la que hace que la ambigüedad se **separe** en vez de elegirse.

Alejandro Valenzuela Rivera · el ente. Abierto el 2026-11-10.

> Esta doctrina vive en el ciclo porque de aquí se arma el índice del ente desde cero. El ensayo dice qué es un tema y qué es un borde; esto dice **cómo se recuerda un tema cuando llega una frase**, y qué se hace cuando la frase no está en ningún lado.

---

## 1. El problema, con el caso que lo mostró

La frase dice `haz un push de la rama`. El tema se llama `git`. El ente busca el tema por su nombre, no lo encuentra, y declara un hueco aunque la frase **sí** era de `git`. Y el otro lado, que también pasó: `misconstrucciones` contenía `construcciones`, y el buscador lo tomó por una frase de otro tema.

Son el mismo defecto visto de dos maneras:

```plaintext
no encontrar de menos     la palabra está en el tema, y el tema no la tiene escrita
encontrar de más          la palabra se parece a otra, y se toma por ella
```

Y la causa es la misma: **el tema decía su nombre, y no decía con qué palabras se le recuerda.**

## 2. La regla

```plaintext
un tema lleva palabras clave    de tres a siete, escritas en su borde, y no una
                                lista abierta
la consulta prueba dos caminos  primero las palabras del tema, y después el tema y
                                sus relaciones
si los dos discrepan, gana el tema    y se apunta la palabra que falló, para corregir
                                      el borde
una palabra, un tema            si una palabra lleva a dos temas, el borde está roto:
                                se corrige el borde, y no se elige a mano
parecerse no es ser             el script no decide que dos palabras son la misma. lo
                                que recuerda a qué es lo que está escrito
```

Y la consecuencia, que es la que cuida lo que el ente contesta: **la palabra es del tema, no del script.** Un ente que busca por parecido contesta lo que no tiene escrito, y eso es rellenar con otro nombre.

## 3. Las tres salidas, y no dos

Cuando una frase llega, y sus palabras no están en el índice, hay tres salidas, y hay que decir cuál es antes de contestar:

```plaintext
la palabra es del tema        el borde estaba corto: se agrega la palabra al tema, y se
                              apunta con su fecha
la palabra es de otro tema    el borde estaba mal puesto: se muda la palabra, y se dice
                              de qué tema salió y a cuál fue
la palabra no es de ninguno   hueco. se declara: «esto no tiene tema todavía», y se
                              sigue
```

Y **la cuarta, que se prohíbe**: rellenar con la palabra que se parece. `misconstrucciones` no es `construcciones`; `push` no es `rama`. Lo que se parece se **separa**, mirando qué significa cada una, y después se escribe la que sí es.

## 4. La ambigüedad no se elige: se separa

Una palabra que lleva a dos temas no es una duda de quien busca: es **un borde partido**, y el que lo parte deja escrito qué palabra se quedó con cuál, y por qué. La prueba no es que la palabra se vea parecida; es que el tema la haya escrito, o que alguien la escriba y lo firme.

```plaintext
una palabra, dos temas       se apunta como fricción del borde, y no se contesta
                             hasta que el borde esté partido
una palabra y su hija        «git» y «git-ignore» no son la misma: la hija se declara
sólo en el tema que contiene a la madre, o no se declara
```

## 5. Cómo se consulta, en orden, cuando la frase llega

```plaintext
1. entra la frase
2. se buscan sus palabras en las palabras clave de los temas
3. si hay un solo tema, se entra por él, y se apunta cuál se usó y por qué palabra
4. si hay dos temas, es una fricción del borde: no se elige, se apunta, y se parte
5. si no hay ninguno, se recorre el grafo por sus relaciones, y se mira el borde
6. si sigue sin haberlo, se declara el hueco, y se sigue
7. y sólo entonces se contesta
```

Y el paso 6 es el que casi siempre se salta, y el único que no se puede saltar: **un ente que contesta algo que no está en su índice está contestando de memoria, y la memoria no se puede auditar.**

## 6. Lo que esta doctrina no decide

```plaintext
no decide qué temas hay            eso lo hace la autoridad, y crece con lo que se vive
no decide si una idea es verdad    la verdad la dice el desenlace
no hace al buscador listo          un buscador por parecido no es esta doctrina: es el
                                   relleno, con otro nombre
```

Y una advertencia, para cuando se implemente: **las palabras clave no se añaden para que más frases entren.** Se añaden cuando una frase **era** del tema y el tema no la tenía escrita. Añadirlas para tapar un hueco es escribir el borde al revés: primero se contesta, y después se busca con qué justificarlo.

---

Falsificador: un tema sin palabras clave que contesta por su nombre y nada más; una palabra que lleva a dos temas y no se apunta como fricción; el buscador que toma `misconstrucciones` por `construcciones`; y un borde que se corrige para que pase una frase, en vez de porque la frase era suya.
