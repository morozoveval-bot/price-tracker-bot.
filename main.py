import requests
from bs4 import BeautifulSoup

# Замените на ваши данные
BOT_TOKEN = 'ВАШ_ТОКЕН_БОТА'
CHAT_ID = 'ВАШ_CHAT_ID'
URL = 'ССЫЛКА_НА_ТОVAR'

def get_price():
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    price_element = soup.select_one('.price-selector') 
    if price_element:
        return price_element.text.strip()
    return None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, json=payload)

def main():
    price = get_price()
    if price:
        send_telegram_message(f"Текущая цена: {price}")

if __name__ == '__main__':
    main()
