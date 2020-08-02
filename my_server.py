#!/usr/bin/env python3
# tratando de escribir el stdout a un archivo
import os, socket, subprocess

#Server

def main():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234)) # socket.gethostname() = localhost
    s.listen(1)

    conn, addr = s.accept()
    print(f"connected by {addr}")

    #proc = 

    while(1):
        data = conn.recv(1024) # data is binary type, must be decoded and converted to string to read received content
        #print(type(data))
        #print(data.decode("utf-8")) #used for debugging pruposes
        if not data: break
        while True:
            if (data.decode("utf-8")) == 'ls':
                print(data)
                x = socket.os.listdir()
                for i in x:
                    conn.sendall(''.join(map(str,i + '\n')).encode())
                    #because the executed command is a list, we have to strip the format and convert it to string and adding a newLine
            if (data.decode('utf-8')) == 'uname':
                x = socket.os.uname()
                print(x)
                conn.sendall(''.join(x).encode()) # just stripping the list format with the ''.join() function
            if (data.decode('utf-8')) == 'pwd':
                x = socket.os.getcwd()
                conn.sendall(''.join(x).encode())

    conn.close

if __name__=='__main__':
    main()
