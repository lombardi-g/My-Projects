import requests
from datetime import datetime

current_time = datetime.now()
formatted_time = current_time.strftime("%d/%m/%Y")
taxas = "https://brasilapi.com.br/api/taxas/v1"

response = requests.get(taxas)
data = response.json()

print(f'Response at {formatted_time}: {response.status_code}')
for _ in data:
    print (_)