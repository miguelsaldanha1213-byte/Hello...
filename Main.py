import requests

def buscar_localizacao_atual():
    try:
        meu_ip = requests.get('https://api.ipify.org').text
        url = f"http://ip-api.com/json/{meu_ip}"
        resposta = requests.get(url)
        dados = resposta.json()
        
        if dados.get('status') == 'success':
            print(f"IP: {dados.get('query')}")
            print(f"Cidade: {dados.get('city')}")
            print(f"Estado: {dados.get('regionName')}")
            print(f"País: {dados.get('country')}")
            print(f"Latitude: {dados.get('lat')}")
            print(f"Longitude: {dados.get('lon')}")
            print(f"Provedor: {dados.get('as')}")
        else:
            print("Erro ao processar os dados do IP.")
            
    except Exception as e:
        print(f"Erro de conexão: {e}")

if __name__ == "__main__":
    buscar_localizacao_atual()

