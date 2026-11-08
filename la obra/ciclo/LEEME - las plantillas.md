# Las plantillas, y el renombrado que hay que hacer

**Dos archivos, dos nombres, y una advertencia que no es formalidad.**

---

## El problema, que es real

**Un harness como `DSH` lee `AGENTS.md` y `SKILL.md` por su nombre.** **No pregunta si el archivo es una plantilla.**

**Si este repositorio tuviera un `AGENTS.md` en la raíz, o un `SKILL.md` en una carpeta de habilidades, el harness de quien lo abriera los cargaría como si fueran para él.**

**Y eso produce el peor de los malentendidos:** **un ente que recibe las reglas de otro proyecto, y las cumple.** **Sin que nadie lo haya pedido, y sin que se vea.**

**Por eso aquí no existen esos dos nombres.** **Existen estas dos plantillas, y se renombran al copiarlas.**

---

## Los dos pasos

```plaintext
1. copiar al proyecto donde se va a usar
2. renombrar, exactamente así:

     AGENTS.plantilla.md   ->   <proyecto>/AGENTS.md
     SKILL.plantilla.md    ->   <proyecto>/.dsh/skills/ente/SKILL.md
```

**Y no al revés:** **no se renombran dentro de este repositorio.**

---

## Cómo se comprueba que se hizo bien

```bash
# en el proyecto, no en este repositorio
ls AGENTS.md                          # tiene que existir
ls .dsh/skills/ente/SKILL.md          # tiene que existir
# y en este repositorio:
ls AGENTS.md                          # NO tiene que existir
ls .dsh/skills                        # NO tiene que existir
```

**Y la señal de que se hizo mal, que se reconoce en el acto:** **el proyecto empieza a comportarse como si tuviera un ente que no se eligió.** **Contesta con un procedimiento, pide autoridad para cosas que no la pedían, o habla de hechos y fricciones cuando se le pidió una línea de código.**

---

## Lo que cada plantilla lleva dentro

| El archivo | Qué lleva |
|---|---|
| **`AGENTS.plantilla.md`** | **la puerta:** qué es el ente, las cuatro piezas, el ciclo, los tres registros, los dos procesos, y el cierre |
| **`SKILL.plantilla.md`** | **la habilidad:** el encabezado con sus seis campos, cuándo usarla, el procedimiento, y dónde vive el criterio |

**Y los dos dicen el nombre que tienen que tener cuando se copien.** **Si alguien los abre sin leer la primera línea, el archivo se lo dice igual.**

---

## Lo que falta, y se dice

- **No se probó en un `DSH` limpio.** **Se escribieron con el formato que la documentación de `DSH` y de sus plugins describen, y no con el resultado de haberlos cargado.**
- **Y hay una condición que puede impedirlo, ya apuntada:** **un `AGENTS.md` afecta al modelo sólo si el cargador de instrucciones está habilitado en el perfil.** **Si no lo está, el archivo se copia bien y no se lee.**

---

## Falsificador

**Una plantilla que se copia con el nombre puesto y el harness la carga en el repositorio equivocado.**

**Y el más probable: alguien renombra el archivo y no lo mueve, así que este repositorio empieza a comportarse como un ente.**
