import threading
from rwlock import RWLock
import time
import random

marker = RWLock()

WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
today = 0

def calendar_reader(id_number):
    global today
    name = 'Reader-' + str(id_number)
    #while today < len(WEEKDAYS)-1:
    while True:
        #   print(today)
        time.sleep(random.randint(1,5))
        marker.r_acquire()
        try:
            print(name, 'sees that today is', WEEKDAYS[today])
        finally:
            marker.r_release()


def calendar_writer(id_number):
    global today
    name = 'Writer-' + str(id_number)
    #while today < len(WEEKDAYS)-1:
    while True:
        time.sleep(random.randint(5,10))
        marker.w_acquire()
        try:
            # today = (today + 1) % 7
            today = random.randint(0,6)
            print(name, 'updated date to ', WEEKDAYS[today])
        finally:
            marker.w_release()



if __name__ == '__main__':
    threads = []

    for i in range(3):
        reader = threading.Thread(target=calendar_reader, args=(i,))
        threads.append(reader)
        reader.start()

    for i in range(1):
        writer = threading.Thread(target=calendar_writer, args=(i,))
        threads.append(writer)
        writer.start()

    for t in threads:
        t.join()
