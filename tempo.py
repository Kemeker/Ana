import requests

def get_weather(api_key, city_name, units="metric"):
   
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}&units={units}"
    response = requests.get(complete_url)
    


    if response.status_code == 200:
        # Solicitação bem-sucedida
        data = response.json()
        temp_info = {
            "cidade": data["name"],
            "temperatura": data["main"]["temp"],
            "descrição": data["weather"][0]["description"]
        }
        return temp_info
    else:
        # Problema na solicitação
        return {"erro": "Não foi possível obter a previsão do tempo."}

