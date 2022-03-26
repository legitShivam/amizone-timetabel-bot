import requests
from datetime import date

def send_image(image_path, credentials):
    time_table = {'photo' : open(image_path, 'rb')}
    token = credentials['telegram_token']
    chat_id = credentials['telegram_chat_id']
    url = f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&caption={date.today()}"
    resp = requests.post(url, files=time_table)
    print("Sent to the telegram!")
