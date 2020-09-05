from telepot import Bot

def get_token() -> str:
    pass # TODO: get tokens from home server

def handle_msg() ->  None: 
    pass

def start_bot() -> None: 
    bot = Bot(get_token())
    bot.message_loop(handle_msg, run_forever=True)
