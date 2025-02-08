import json
import pandas as pd

def parse_weather_log(log_path, output_csv, timestamp):
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
                "timestamp": timestamp,
                "coord_lon": data["coord"]["lon"],
                "coord_lat": data["coord"]["lat"],
                "weather_0_id": data["weather"][0]["id"],
                "weather_0_main": data["weather"][0]["main"],
                "weather_0_description": data["weather"][0]["description"],
                "weather_0_icon": data["weather"][0]["icon"],
                "base": data["base"],
                "main_temp": data["main"]["temp"],
                "main_feels_like": data["main"]["feels_like"],
                "main_temp_min": data["main"]["temp_min"],
                "main_temp_max": data["main"]["temp_max"],
                "main_pressure": data["main"]["pressure"],
                "main_humidity": data["main"]["humidity"],
                "main_sea_level": data["main"]["sea_level"],
                "main_grnd_level": data["main"]["grnd_level"],
                "visibility": data["visibility"],
                "wind_speed": data["wind"]["speed"],
                "wind_deg": data["wind"]["deg"],
                "wind_gust": data["wind"]["gust"],
                "clouds_all": data["clouds"]["all"],
                "sys_type": data["sys"]["type"],
                "sys_id": data["sys"]["id"],
                "sys_country": data["sys"]["country"],
                "sys_sunrise": data["sys"]["sunrise"],
                "sys_sunset": data["sys"]["sunset"],
                "timezone": data["timezone"],
                "id": data["id"],
                "name": data["name"],
                "cod": data["cod"],
                "Lluvia_1h": data.get("rain", {}).get("1h", 0),  
                "Nieve_1h": data.get("snow", {}).get("1h", 0)   
            }
            data_list.append(row)
        except json.JSONDecodeError:
            print("Error al decodificar una entrada, saltando...")
        except KeyError as e:
            print(f"Clave no encontrada en los datos: {e}, saltando...")

    df = pd.DataFrame(data_list)
    df.to_csv(output_csv, index=False, sep=';')
    print(f"Datos guardados en {output_csv}")
