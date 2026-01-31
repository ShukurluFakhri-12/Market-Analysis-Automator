import requests
import pandas as pd
import os
url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
response = requests.get(url).json()
df = pd.DataFrame(response)
increasing = df[(df['current_price'] > 500) & (df['price_change_percentage_24h'] > 0)]
folder = 'Market_reports'
if not os.path.exists(folder):
    os.mkdir(folder)
filepath = os.path.join(folder, 'topgainers.xlsx')
increasing.to_excel(filepath, index=False)
print('Process is completed! File is downloaded to folder')
