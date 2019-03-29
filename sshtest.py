#!/bin/python

import time
import socket
import subprocess
import sys

### Recuperation du hostname et sauvegarde de l'ancien
Oldhostname = socket.gethostname().upper()
Hostname = sys.argv[1].upper()

### Constantes pour la creation du escape sequence
Title = "\x1b" + "];" + Hostname + "\x07"
RestoreTitle = "\x1b" + "];" + Oldhostname + "\x07"

ClientSocket = socket.socket()
ClientSocket.settimeout(5)

### Essaie en SSH puis telnet si erreur avec ssh
try:
    try:
        ClientSocket.connect((Hostname, 22))
        print(Title)
        time.sleep(1)
        subprocess.call(['ssh', Hostname])
        print(Title)
    except socket.error:
        print(Title)
        print("\n\n\nSSH Failed... Trying telnet...\n\n\n")
        time.sleep(1)
        subprocess.call(['telnet', Hostname])

### Gestion du ctrl+c pour quitter les sessions problematiques
except KeyboardInterrupt:
    print(RestoreTitle)
    ClientSocket.close()
else:
    print(RestoreTitle)
    ClientSocket.close()
