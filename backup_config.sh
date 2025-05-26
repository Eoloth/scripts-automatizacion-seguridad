#!/bin/bash
# backup_config.sh
# Autor: Rubén Luis Manríquez Salles

DESTINO="$HOME/backups_config"
mkdir -p "$DESTINO"

ARCHIVOS="/etc/ssh/sshd_config /etc/passwd /etc/group /etc/hosts"
FECHA=$(date +%Y%m%d_%H%M)

TARFILE="$DESTINO/backup_config_$FECHA.tar.gz"
tar -czf "$TARFILE" $ARCHIVOS

echo "✅ Backup creado: $TARFILE"