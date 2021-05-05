import threading


class ColaFIFOsizeMyVersion:

    def __init__(self,tamanio):
        self.elementos = []
        self.tamanio = tamanio
        self.condicion = threading.Condition()

    def insertar(self, dato):
        self.condicion.acquire() # adquiere
        if len(self.elementos) == self.tamanio:
            # debe esperar que haya un espacio para insertar.
            self.condicion.wait()
        self.elementos.append(dato)
        self.condicion.notify() # notifica
        self.condicion.release() # libera
        
    def extraer(self):
        self.condicion.acquire()
        while len(self.elementos) == 0:
            # debe esperar que haya algo para extraer
            self.condicion.wait()
        elemento = self.elementos.pop(0)
        self.condicion.notify() # notifica
        self.condicion.release() # libera
        return elemento

    def ultimo(self):
        return self.elementos[-1]

    def primero(self):
        return self.elementos[0]

    def cola_vacia(self):
        return len(self.elementos) == 0

    def cantidad_elementos(self):
        return len(self.elementos)


def main():
    cola = ColaFIFOsizeMyVersion(6)

    print(cola.cola_vacia())

    for i in range (1,6):
        cola.insertar(i)

    print(cola.cola_vacia())
    print(cola.cantidad_elementos())

    print(cola.primero(),cola.ultimo())
    cola.extraer()
    print(cola.primero(),cola.ultimo())


    cola.extraer()
    cola.extraer()
    cola.extraer()
    cola.extraer()

    print(cola.cola_vacia())
    print(cola.cantidad_elementos())

if __name__ == '__main__':
    main()

