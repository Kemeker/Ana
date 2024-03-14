import requests

def get_weather(api_key, city_name, units="metric"):
   
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}&units={units}"
    response = requests.get(complete_url)
    


    if response.status_code == 200:
        # Solicitação bem-sucedida
        data = response.json()
        weather_info = {
            "cidade": data["name"],
            "temperatura": data["main"]["temp"],
            "descrição": data["weather"][0]["description"]
        }
        return weather_info
    else:
        # Problema na solicitação
        return {"erro": "Não foi possível obter a previsão do tempo."}

# Exemplo de uso
if __name__ == "__main__":
    api_key = "cc97ce14bd7ad1f9faf2644f05a3b145"
    city_name = "New York"
    weather = get_weather(api_key, city_name)
    print(weather)



#testar api de clima para ver se obtivemos resultado