import requests
import json
import configparser as cfg

class toTamilBot():
    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base_url = 'https://api.telegram.org/bot{}/'.format(self.token)

    def get_updates(self, offset=None):
        url = self.base_url + 'getUpdates?timeout=100'
        if offset:
            url = url + '&offset={}'.format(offset+1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, message, chat_id):
        try:
            url = self.base_url + 'sendMessage?chat_id={}&text={}'.format(chat_id, message.encode('utf-8'))
        except AttributeError:
            url = self.base_url + 'sendMessage?chat_id={}&text={}'.format(chat_id, message)
        if message is not None:
            requests.get(url)

    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')
    
        
