#!/usr/bin/env python3
"""
notificador_alerta.py
Autor: Rubén Luis Manríquez Salles

Descripción:
Envía una alerta por correo electrónico si se detectan IPs sospechosas en un archivo de texto.
Utiliza SMTP para enviar notificaciones básicas con Python.

Requisitos:
- Archivo 'ips_sospechosas.txt' generado previamente.
- Acceso SMTP (ej: cuenta Gmail con contraseña de aplicación).
- Python 3.x y la biblioteca 'smtplib'.

Nota: Este script es educativo y debe adaptarse para producción.
"""

import smtplib
from email.mime.text import MIMEText

# Configuración de envío (modificar)
SMTP_SERVIDOR = "smtp.gmail.com"
SMTP_PUERTO = 587
SMTP_USUARIO = "tu_correo@gmail.com"
SMTP_CLAVE = "tu_contraseña_aplicacion"

DESTINATARIO = "destinatario@correo.com"

def cargar_ips(path="ips_sospechosas.txt"):
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

def enviar_alerta(mensaje):
    msg = MIMEText(mensaje)
    msg['Subject'] = "⚠️ Alerta: IPs sospechosas detectadas"
    msg['From'] = SMTP_USUARIO
    msg['To'] = DESTINATARIO

    with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PUERTO) as server:
        server.starttls()
        server.login(SMTP_USUARIO, SMTP_CLAVE)
        server.send_message(msg)
        print("✅ Alerta enviada con éxito.")

if __name__ == "__main__":
    contenido = cargar_ips()
    if contenido:
        enviar_alerta(f"Se detectaron las siguientes IPs sospechosas:

{contenido}")
    else:
        print("No se encontraron IPs sospechosas o no existe el archivo.")
