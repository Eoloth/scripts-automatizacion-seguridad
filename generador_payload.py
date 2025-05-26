#!/usr/bin/env python3
"""
generador_payload.py
Autor: Rubén Luis Manríquez Salles

Genera variantes codificadas de un payload para pruebas de XSS o Command Injection.
"""

import base64
import urllib.parse

def encode_payload(payload):
    print("[Original]")
    print(payload)
    print("\n[Base64]")
    print(base64.b64encode(payload.encode()).decode())
    print("\n[URL encoded]")
    print(urllib.parse.quote(payload))

if __name__ == "__main__":
    sample = input("🔧 Ingrese el payload a codificar: ")
    encode_payload(sample)