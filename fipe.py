import requests

tipos_veiculos = ["caminhoes","carros","motos"]
codigo_fipe = {"onix":"004425-3"
               }

marcas = f"https://brasilapi.com.br/api/fipe/marcas/v1/{tipos_veiculos[1]}"
precos = f"https://brasilapi.com.br/api/fipe/preco/v1/{codigo_fipe["onix"]}"

# fetching
response = requests.get(marcas)
# parsing json into dict
data = response.json()

print(response.status_code)
for _ in data:
    print (_)