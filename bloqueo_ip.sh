#!/bin/bash/
"""
analizador_logs_apache.py
Autor: Rubén Luis Manríquez Salles

Descripción:
Analiza logs de Apache (formato común) para detectar IPs que podrían estar realizando escaneo o ataques de fuerza bruta según la frecuencia de solicitudes.

Uso:
    python3 analizador_logs_apache.py /ruta/al/access.log
"""

#!/bin/bash
# bloqueo_ips.sh

ARCHIVO="ips_sospechosas.txt"

if [ ! -f "$ARCHIVO" ]; then
  echo "[!] Archivo $ARCHIVO no encontrado."
  exit 1
fi

while read -r ip; do
  echo "[+] Bloqueando IP: $ip"
  sudo ufw deny from "$ip" > /dev/null
done < "$ARCHIVO"

echo "✅ Bloqueo completado."
