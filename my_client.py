#!/usr/bin/env python3

#client

import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    s.send(input().encode("utf-8"))
    dat = s.recv(1024)
    print(dat.decode("utf-8"))

if __name__ == '__main__':
    main()
