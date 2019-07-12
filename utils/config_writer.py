import configparser

config = configparser.ConfigParser()
config['APP_INFO'] = {'ASSISTANT_NAME': 'Psy'}
config['APP_CREDS'] = {'WOLFRAM_APP_ID' : 'DEMO'}

with open('.config', 'w+') as configfile:
    config.write(configfile)
