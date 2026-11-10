"""Las expresiones regulares y los nombres fijos del repositorio.

Y por qué en su propio módulo: la misma `TITULO` la usan las reglas, el piso y los
trabajos, y una regla copiada en dos lugares crece hasta decir dos cosas distintas.
"""

import re


# Donde el build se cae: ni historia (se conserva como se escribió) ni
# implementacion (puede citar el paso de un ensayo para usarlo).
SIN_EDAD = ("metodologia/historia", "implementacion")

TITULO = re.compile(r"^# (.+)$", re.M)
FALSIFICADOR = re.compile(r"\bFalsificador\b")
PIERDE = re.compile(r"(?:Y )?qué se pierde si cambia", re.I)
NUMERO = re.compile(r"(?:ensayos?|pasos?)\s+`?(\d\d)\b|`(\d\d)\s+[a-záéíóúñ]")
POSICION = re.compile(r"^(\d\d)\s+-\s+")
TRAMO = re.compile(r"(?:^|/)\d\d\s+")
ENLACE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
CITA = re.compile(r"`([^`\n]+)`")

# La ruta de la máquina del autor, que no entra al repositorio.
RUTA_MAQUINA = re.compile(
    r"[A-Za-z]:[\\/]+Users[\\/]+Alex(?:[\\/]+(?:git|Documents|Downloads|Desktop|AppData|\.dsh))*"
    r"(?:[\\/]+[^'\"\n,;)]*)?"
)
SUSTITUTO = "[ruta del autor]"

# Y la persona, que es la regla del ATTRIBUTION: el texto describe, y por eso no le
# habla a nadie. Quedan fuera las citas, y las palabras que dice un personaje.
PERSONA = {
    "tuteo": re.compile(r"\b(tu|tienes|puedes|quieres|haces|sabes|dices|debes)\b", re.I),
    "voseo": re.compile(r"\b(vos|tenes|podes|sabes|queres|haces|sos)\b", re.I),
    "primera persona": re.compile(r"\b(yo|digo|pienso|creo|quiero|he visto)\b(?!\s+en\b)", re.I),
}

MARCA_NEGRITAS = "<!-- negritas: revisadas. lo que queda en negrita es lo que tiene que saltar -->"
NEGRITA = re.compile(r"\*\*(.+?)\*\*")
CAMPOS = re.compile(
    r"^\s*(\*\*)?(Se corre|Entra|Se hace|Sale|Dónde queda|Lo consume|Y si no encuentra|"
    r"Falla si|Falsificador|Prueba|Qué la tumba|Qué lo sostiene|Qué sostiene|Vive en|"
    r"La regla|El mutante|Se delega|No se delega|Recibe|Entrega)(\*\*)?\s*:", re.I)
MULETILLAS = {"y", "o", "pero", "que", "ni", "sino", "en", "por", "para", "con", "si",
              "cuando", "como", "de", "la", "el", "los", "las", "un", "una"}
NO_ES_PROSA = re.compile(r"^(```|\||-->|#{1,6} |<!--|> )")

OFUSCA_EXT = (".md", ".sql", ".py", ".txt", ".cff", ".json", ".yml", ".yaml", ".sh")
