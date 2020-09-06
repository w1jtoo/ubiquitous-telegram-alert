from threading import Thread
from telepot import Bot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

WHITE_LIST = [ ]
ADMIN_ID = 0
REMIND_LIST = WHITE_LIST
SERVER_ADDRESS = ""
MESSAGES_TO_TIME  = {}
PLANNED_MESSAGES = []
BOT = None


def get_token() -> str:
	pass # TODO: get tokens from home server

def alert(bot: Bot, msg: dict) -> None:
	chat_id = msg['chat']['id']
	user_name = msg['from']['username']
	msg_text = None
	if msg.get('text') is not None:
		msg_text = msg['text']

	for _id in WHITE_LIST:
		if _id == chat_id: continue
		bot.sendMessage(_id, f'У {user_name} нет вермени объяснять, алерт!')
	bot.sendMessage(chat_id, 'Сообщение было доставлено!')

def get_reply_keyboard() -> ReplyKeyboardMarkup:
	buttons = [ KeyboardButton(text='ALERT!') ]
	return ReplyKeyboardMarkup(keyboard=[buttons])

def update_whitelist() -> None:
	global WHITE_LIST
	pass # TODO: get whitelist

def handle_msg(msg: dict) ->  None:
	chat_id = msg['chat']['id']
	user_name = msg['from']['username']
	msg_text = None
	if msg['text'] is not None:
		msg_text = msg['text']

	if chat_id not in WHITE_LIST:
		warn_to_admin(BOT, msg)
		BOT.sendMessage(chat_id, 'Тебя нет в списке разрешённых пользователей :(')
		BOT.sendSticker(chat_id, 'CAACAgUAAxkBAAMLX1PI2-TOAaXkLvJpyjD3JQzkAAHjAAKfAAPceAwIkmRBx7ks9FgbBA')
		BOT.sendMessage(chat_id, '''Автор бота: @w1jimtoo
Код бота: https://github.com/w1jtoo/ubiquitous-telegram-alert
''')
		return

	if msg_text not in COMMANDS.keys():
		BOT.sendMessage(chat_id, 'Не знаю такой команды', reply_markup=get_reply_keyboard())
		return

	COMMANDS[msg_text](BOT, msg)

COMMANDS = {
	"ALERT!": alert,
}

def warn_to_admin(bot: Bot, msg: str) -> None:
	chat_id = msg['chat']['id']
	user_name = msg['from']['username']
	msg_text = None
	if msg['text'] is not None:
		msg_text = msg['text']

	bot.sendMessage(ADMIN_ID, f'{user_name} пытался поговорить с ботом в чате № {chat_id}')

def start_bot() -> None:
	global BOT
	BOT = Bot('')

	BOT.message_loop(handle_msg, run_forever=True)
