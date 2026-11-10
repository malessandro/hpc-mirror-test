"""Projet démo hpc-bridge : affiche l'environnement d'exécution puis calcule un peu."""

import os
import platform
import socket
import sys
import time

print(f"hôte : {socket.gethostname()}")
print(f"utilisateur : {os.environ.get('USER', '?')}")
print(f"job PBS : {os.environ.get('PBS_JOBID', 'hors PBS')}")
print(f"python : {sys.version.split()[0]} ({platform.platform()})")

debut = time.time()
total = sum(i * i for i in range(10_000_000))
print(f"somme des carrés : {total} en {time.time() - debut:.1f} s")
