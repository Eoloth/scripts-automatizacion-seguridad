#!/usr/bin/env python3
"""
analizador_logs_apache.py
Autor: Rubén Luis Manríquez Salles

Descripción:
Analiza logs de Apache (formato común) para detectar IPs que podrían estar realizando escaneo o ataques de fuerza bruta según la frecuencia de solicitudes.

Uso:
    python3 analizador_logs_apache.py /ruta/al/access.log
"""

import sys
from collections import defaultdict

def analizar_logs(ruta_log, umbral=100):
    ips = defaultdict(int)

    try:
        with open(ruta_log, 'r') as f:
            for linea in f:
                partes = linea.split()
                if partes:
                    ip = partes[0]
                    ips[ip] += 1
    except FileNotFoundError:
        print(f"[!] Archivo no encontrado: {ruta_log}")
        return
    except Exception as e:
        print(f"[!] Error al analizar el archivo: {e}")
        return

    print(f"\n[+] Resultados (IPs con más de {umbral} solicitudes):\n")
    for ip, count in sorted(ips.items(), key=lambda x: x[1], reverse=True):
        if count > umbral:
            print(f"⚠️  Posible escaneo desde {ip} con {count} solicitudes")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 analizador_logs_apache.py /ruta/al/access.log")
    else:
        ruta = sys.argv[1]
        analizar_logs(ruta)
