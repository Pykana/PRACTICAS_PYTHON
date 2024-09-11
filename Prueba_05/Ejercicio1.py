# este programa crea y manipula una estructura de datos que técnicamente
# se denomina pila, desde un paradigma de programaciun orientada a objetos

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

    def cima(self):
        if self.esta_vacia():
            return None
        return self.items[-1]


# Uso del objeto y sus métodos
pilita = Pila()
elemento = 13
print('Elemento a apilar: ', elemento)
pilita.apilar(13)
elemento = 19
print('Elemento a apilar: ', elemento)
pilita.apilar(19)
elemento = 21
print('Elemento a apilar: ', elemento)
pilita.apilar(21)

print(pilita.items)

print(pilita.desapilar())
print(pilita.desapilar())
print(pilita.desapilar())
print(pilita.desapilar())