from bot import toTamilBot
import translator

bot = toTamilBot('config.cfg')

def make_reply(message):
    reply = None
    if message is not None:
        reply = translator.translate(message)
    return reply

update_id = None

while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates['result']
    if updates:
        for item in updates:
            update_id = item['update_id']
            try:
                message = str(item['message']['text'])
            except:
                message = None
            from_person = item['message']['from']['id']
            reply = make_reply(message)
            bot.send_message(reply, from_person)
