#!/bin/bash

# ==========================================================
# @file get-weather.sh
# @brief Obtiene datos del clima y los guarda en un archivo log.
# @author Juan M,
# @date 2025-02-08
# @version 1.0
# ==========================================================

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
API_KEY="a2bf02c552258a864af174c79d421d35" # Reemplazar con API key real
CITY="Marburg"
URL="https://api.openweathermap.org/data/2.5/weather?q=$CITY&appid=$API_KEY&units=metric"
LOG_FILE="$SCRIPT_DIR/output.log"

# Obtener datos y formatear correctamente el JSON
response=$(curl -s "$URL")

# Usar jq para combinar el timestamp con la respuesta
if ! command -v jq &> /dev/null; then
    echo "Error: jq no está instalado. Instálalo con 'sudo apt install jq'"
    exit 1
fi

echo "$response" | jq --arg ts "$TIMESTAMP" '. + {timestamp: $ts}' -c >> "$LOG_FILE"
