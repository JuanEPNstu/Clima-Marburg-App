import json
import pandas as pd

def parse_weather_log(log_path, output_csv):
    """
    Lee output.log, extrae datos del clima y los convierte en un archivo CSV.

    Args:
        log_path (str): Ruta del archivo de log con los datos en JSON.
        output_csv (str): Nombre del archivo CSV de salida.

    Returns:
        None
    """
    data_list = []
    
    with open(log_path, "r") as file:
        raw_data = file.read().strip().split("\n\n") 
    
    for entry in raw_data:
        try:
            data = json.loads(entry)
            row = {
                "timestamp": pd.Timestamp.now(),
                "Pais": data["sys"]["country"],
                "Ciudad": data["name"],
                "Latitud": data["coord"]["lat"],
                "Longitud":data["coord"]["lon"],
                "temp": data["main"]["temp"],
                "FeelsLike": data["main"]["feels_like"],
                "temp_min": data["main"]["temp_min"],
                "temp_max": data["main"]["temp_max"],
                "Humedad": data["main"]["humidity"],
                "Presion": data["main"]["pressure"],
                "Velocidad_viento": data["wind"]["speed"],
                "Descripcion": data["weather"][0]["description"],
                "Lluvia_1h": data.get("rain", {}).get("1h", 0),  
                "Nieve_1h": data.get("snow", {}).get("1h", 0)  
            }
            data_list.append(row)
        except json.JSONDecodeError:
            print("Error al decodificar una entrada, saltando...")

    df = pd.DataFrame(data_list)
    df.to_csv(output_csv, index=False, sep=';')
    print(f"Datos guardados en {output_csv}")
