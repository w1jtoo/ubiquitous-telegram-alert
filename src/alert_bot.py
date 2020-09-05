from telepot import Bot

WHITE_LIST = [ "w1jimtoo" ]
SERVER_ADDRESS = ""
bot = None

def get_token() -> str:
    pass # TODO: get tokens from home server

def update_whitelist() -> None:
    global WHITE_LIST
    pass # TODO: get whitelist

def handle_msg(msg: dict) ->  None:
    chat_id = msg['chat']['id']
    user_name = msg['from']['username']
    if user_name not in WHITE_LIST:
        bot.sendMessage(chat_id, 'Тебя нет в списке разрешённых пользователей :(')
        bot.sendSticker(chat_id, 'CAACAgUAAxkBAAMLX1PI2-TOAaXkLvJpyjD3JQzkAAHjAAKfAAPceAwIkmRBx7ks9FgbBA')
        bot.sendMessage(chat_id, '''Автор бота: @w1jimtoo
Код бота: https://github.com/w1jtoo/ubiquitous-telegram-alert

''')
        return

def start_bot() -> None:
    global bot
    bot = Bot()
    bot.message_loop(handle_msg, run_forever=True)
