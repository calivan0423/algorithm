# import packages
from bluetooth import *
from multiprocessing import Process
import time
import os

start = time.time() # start clock


def recv(client_socket):
    while True:
        msg = client_socket.recv(1024)
        print("received message:{}".format(msg))

def send(client_socket):
    while True:
        msg = input("Send : ")
        print(client_socket+" : "+msg)
        client_socket.send(msg)


def counter(cnt):
    pid = os.getpid()
    for i in range(cnt):
        print("Process ID : ", pid, " -- ", i)

# main Function
if __name__ == '__main__':

    client_socket1 = BluetoothSocket(RFCOMM)
    client_socket1.connect(("98:D3:31:FC:AF:A5", 1))

    case_size = [100000, 10000000, 1000000, 1000000]
    p = []

    # Run Test Cases
    '''
    for index, number in enumerate(case_size):
        # Make Child Process for Function 'count(number)'
        process = Process(target=counter, args=(number,))
        p.append(process)
        process.start() # Fork
    '''
    process_1_recv = Process(traget=recv(),args=(client_socket1,))
    p.append(process_1_recv)
    process_1_recv.start()
    process_1_send = Process(traget=send(), args=(client_socket1,))
    p.append(process_1_send)
    process_1_send.start()

    # Wait for synchronization
    for proc in p:
        proc.join() # Wait for Process
        temp = time.time()
        print(proc, " joined at", temp-start) # show process finished time

end = time.time() # end clock

print(end-start, "seconds taken")
