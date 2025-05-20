import requests

TOKEN = '7588292084:AAGfNV0yEPovITD6XEfw2saoLki3cg45p08'  # Thay bằng TELEGRAM_TOKEN của bạn

url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
res = requests.get(url)
print(res.json())
