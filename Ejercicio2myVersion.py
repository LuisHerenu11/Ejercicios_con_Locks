import threading
import time
import random
import logging

from ColaFIFO import ColaFIFO

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
    elementos = ColaFIFO()

    productor = Productor(elementos,2)
    consumidor = Consumidor(elementos,2)

    logging.info(f'iniciando el productor {productor.name}')
    productor.start()
    logging.info(f'iniciando el consumidor {consumidor.name}')
    consumidor.start()

    productor.join()
    consumidor.join()

if __name__ == '__main__':
    main()






