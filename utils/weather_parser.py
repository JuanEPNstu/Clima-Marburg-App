import json
import pandas as pd

def parse_weather_log(log_path, output_csv):
    """
    Versión corregida manteniendo todas las columnas originales.
    Incluye mejor manejo de errores para campos opcionales.
    """
    data_list = []
    
    with open(log_path, "r") as file:
        # Leer cada línea como un JSON independiente
        raw_entries = [line.strip() for line in file if line.strip()]
    
    for entry in raw_entries:
        try:
            data = json.loads(entry)
            
            # Usar .get() para campos opcionales y anidados
            row = {
                "timestamp": data["timestamp"],
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
                "main_sea_level": data["main"].get("sea_level"),  # Campo opcional
                "main_grnd_level": data["main"].get("grnd_level"), # Campo opcional
                "visibility": data["visibility"],
                "wind_speed": data.get("wind", {}).get("speed"),  # Usar get() anidado
                "wind_deg": data.get("wind", {}).get("deg"),
                "wind_gust": data.get("wind", {}).get("gust"),
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
            
        except json.JSONDecodeError as e:
            print(f"Error decodificando JSON: {str(e)}")
        except KeyError as e:
            print(f"Campo faltante: {e} en entrada: {entry[:100]}...")
        except IndexError:
            print(f"Falta elemento en lista 'weather': {entry[:100]}...")

    if data_list:
        df = pd.DataFrame(data_list)
        df.to_csv(output_csv, index=False, sep=';', encoding='utf-8')
        print(f"CSV creado exitosamente: {output_csv}")
    else:
        print("No se procesaron datos válidos")
