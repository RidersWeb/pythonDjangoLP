import requests, re, datetime
from .models import TeleSettings

def write_debug(debug_text):
    with open('./debug.txt', 'a', encoding='1251') as file:
        file.write('\n' + debug_text)



def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        setting_db = TeleSettings.objects.get(pk=1)
        token = str(setting_db.tg_token)
        chat_id = str(setting_db.tg_chat)
        text = str(setting_db.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        now = datetime.datetime.now()
        time_dt = now.strftime("%d-%m-%Y %H:%M")
        time_dt = str(time_dt)
        text_list = re.split(r'{\s\w*\s}', text)

        text = f'{text_list[0]}  {time_dt}  {text_list[1]}  {tg_name}  {text_list[2]} {tg_phone}'


    try:
        req = requests.post(method, data={
            'chat_id': chat_id,
            'text': text
        })
    except:
        pass
    finally:
        if req.status_code != 200:
            write_debug(time_dt + 'Проверьте Токен и Чат ID')
        elif req.status_code == 500:
            write_debug(time_dt + 'Ошибка 500')
        else:
            write_debug(time_dt + ' Всё хорошо, сообщение отправлено!')
