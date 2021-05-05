import threading
import time
import random
import logging

from ColaFIFOsizeMyVersion import ColaFIFOsizeMyVersion

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


class Productor(threading.Thread):
    def __init__(self,unaCola,tiempoEspera):
        super().__init__()
        self.cola = unaCola
        self.espera = tiempoEspera

    def run(self):
        while True:
            self.cola.insertar(random.randint(0,100))
            logging.info(f'inserción realizada - {self.cola.ultimo()}')
            time.sleep(self.espera)

class Consumidor(threading.Thread):
    def __init__(self,unaCola,tiempoEspera):
        super().__init__()
        self.cola = unaCola
        self.espera = tiempoEspera

    def run(self):
        while True:
            elementoExtraido = self.cola.extraer()
            logging.info(f'extración realizada - {elementoExtraido}')
            time.sleep(self.espera)    

def main():
    hilos = []
    cola = ColaFIFOsizeMyVersion(10)

    for i in range(5):
        productor = Productor(cola, random.randint(1,5))
        consumidor = Consumidor(cola, random.randint(1,5))
        hilos.append(productor)
        hilos.append(consumidor)
        logging.info(f'Arrancando productor {productor.name}')
        productor.start()
        logging.info(f'Arrancando consumidor {consumidor.name}')
        consumidor.start()

    for thr in hilos:
        thr.join()

if __name__ == '__main__':
    main()




