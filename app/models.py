import random

class Pokenea:
    def __init__(self, id, nombre, altura, habilidad, imagen, frase):
        self.id = id
        self.nombre = nombre
        self.altura = altura
        self.habilidad = habilidad
        self.imagen = imagen
        self.frase = frase

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "altura": self.altura,
            "habilidad": self.habilidad
        }

POKENEAS = [
    Pokenea(1, "Neocho", "1.2m", "Fuga", "https://storage.googleapis.com/pokeimagenes/pokeneas/1.jpg", "La rapidez lo es todo."),
    Pokenea(2, "Brayan", "1.6m", "Hoja afilada", "https://storage.googleapis.com/pokeimagenes/pokeneas/7.jpg", "El filo de tus acciones define tu camino."),
    Pokenea(3, "Kevin", "1.7m", "Levantar pollitas", "https://storage.googleapis.com/pokeimagenes/pokeneas/6.png", "El carisma es un arma poderosa."),
    Pokenea(4, "Brittany", "1.5m", "Mentir", "https://storage.googleapis.com/pokeimagenes/pokeneas/2.jpeg", "La verdad es relativa para quien sabe usarla."),
    Pokenea(5, "Ñeron", "1.8m", "Intimidación", "https://storage.googleapis.com/pokeimagenes/pokeneas/4.jpg", "El poder está en la presencia."),
    Pokenea(6, "Jhesid", "1.6m", "Estilismo", "https://storage.googleapis.com/pokeimagenes/pokeneas/5.jpeg", "La apariencia habla más fuerte que las palabras."),
    Pokenea(7, "Junior", "1.4m", "Humareda", "https://storage.googleapis.com/pokeimagenes/pokeneas/8.jpg", "Donde hay humo, hay estrategia."),
    Pokenea(8, "El can", "1.0m", "Marcar territorio", "https://storage.googleapis.com/pokeimagenes/pokeneas/11.jpeg", "El control del terreno asegura la victoria."),
    Pokenea(9, "Milloz", "1.7m", "Fanatismo", "https://storage.googleapis.com/pokeimagenes/pokeneas/9.jpeg", "La pasión mueve montañas."),
    Pokenea(10, "Felipe", "1.5m", "Grindr", "https://storage.googleapis.com/pokeimagenes/pokeneas/3.jpeg", "Conexiones inesperadas pueden cambiar el juego."),
]

def get_random_pokenea():
    return random.choice(POKENEAS)
