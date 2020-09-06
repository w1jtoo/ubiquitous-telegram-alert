import time
from telepot import Bot

UPDATE_TIME = 100

def update_loop(bot:Bot, reminder_list:list, planned_messages: list) -> None:
	while 1:
		time.sleep(UPDATE_TIME)
		for user_id in reminder_list:
			for msg in planned_messages:
				bot.sendMessage(chat_id, f"{planned_messages}")
