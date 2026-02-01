import requests
import pandas as pd
import os
def market_analysis():
    try:
        url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
        response = requests.get(url, timeout = 10)
        data = response.json()
        df = pd.DataFrame(data)
        df = df.rename(columns={'current_price' : 'Price_USD' , 'price_change_percentage_24h' : 'Change_24h_pct'})
        df.loc[df['Change_24h_pct'] > 0 , 'Status'] = 'Bullish'
        df.loc[df['Change_24h_pct'] <= 0 , 'Status'] = 'Bearish'
        df = df.sort_values(by='Price_USD' , ascending = False)
        increasing = df[(df['Price_USD'] > 500) & (df['Change_24h_pct'] > 0)]
        folder = 'Market_reports'
        if not os.path.exists(folder):
            os.mkdir(folder)
        filepath = os.path.join(folder, 'topgainers.xlsx')
        increasing.to_excel(filepath, index=False)
        print('Process is completed! File is downloaded to folder')
    except Exception as e:
        print(f"Error {e} occurred")
market_analysis()
