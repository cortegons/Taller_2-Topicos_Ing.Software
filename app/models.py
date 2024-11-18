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
    Pokenea(1, "Neocho", "1.8m", "Fuga","https://storage.googleapis.com/pokeimagenes/pokeneas/1.jpg", "El tiempo es oro."),
    Pokenea(2, "Brayan", "1.5m", "Hoja afilada", "https://storage.googleapis.com/pokeimagenes/pokeneas/7.jpg", "La unión hace la fuerza."),
    Pokenea(3, "Kevin", "1.5m", "Levantar pollitas", "https://storage.googleapis.com/pokeimagenes/pokeneas/6.png", "La unión hace la fuerza."),
    Pokenea(4, "Brittany", "3m", "Mentir", "https://storage.googleapis.com/pokeimagenes/pokeneas/2.jpeg", "La unión hace la fuerza."),
    Pokenea(5, "Ñeron", "1.5m", "Intimidación", "https://storage.googleapis.com/pokeimagenes/pokeneas/4.jpg", "La unión hace la fuerza."),
    Pokenea(6, "Jhesid", "1.5m", "Estilismo", "https://storage.googleapis.com/pokeimagenes/pokeneas/5.jpeg", "La unión hace la fuerza."),
    Pokenea(7, "Junior", "1.5m", "Humareda", "https://storage.googleapis.com/pokeimagenes/pokeneas/8.jpg", "La unión hace la fuerza."),
    Pokenea(8, "El can", "1.5m", "Marcar territorio", "https://storage.googleapis.com/pokeimagenes/pokeneas/11.jpeg", "La unión hace la fuerza."),
    Pokenea(9, "Milloz", "1.5m", "Fanatismo", "https://storage.googleapis.com/pokeimagenes/pokeneas/9.jpeg", "La unión hace la fuerza."),
    Pokenea(10, "Felipe", "1.5m", "Grindr", "https://storage.googleapis.com/pokeimagenes/pokeneas/3.jpeg", "La unión hace la fuerza."),
]

def get_random_pokenea():
    return random.choice(POKENEAS)
