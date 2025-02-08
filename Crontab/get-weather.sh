#!/bin/bash

# ==========================================================
# @file get-weather.sh
# @brief Obtiene datos del clima y los guarda en un archivo CSV.
# @author Juan M, 
# @date 2025-02-08
# @version 1.0
# ==========================================================

SCRIPT_DIR="$(dirname "$(realpath "$0")")"
API_KEY="a2bf02c552258a864af174c79d421d35" #Aqui va tu clave API.
CITY="Madrid" #Escribir la ciudad objetivo.
URL="https://api.openweathermap.org/data/2.5/weather?q=$CITY&appid=$API_KEY&units=metric"
LOG_FILE="$SCRIPT_DIR/output.log" #Ruta donde se guardara el log.


# Obtener datos de la API y guardarlos en output.log
curl -s "$URL" >> "$LOG_FILE"
echo -e "\n" >> "$LOG_FILE"
