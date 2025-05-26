#!/bin/bash
# verificador_integridad.sh
# Autor: Rubén Luis Manríquez Salles

# Archivos críticos a monitorear
ARCHIVOS="/etc/passwd /etc/shadow /etc/ssh/sshd_config"
HASH_FILE="hash_baseline.txt"

# Generar o comparar hashes
if [ "$1" == "--generar" ]; then
  echo "[+] Generando baseline..."
  md5sum $ARCHIVOS > "$HASH_FILE"
  echo "✅ Baseline guardado en $HASH_FILE"
else
  echo "[+] Comparando integridad..."
  md5sum -c "$HASH_FILE" 2>/dev/null
fi