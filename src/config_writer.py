import configparser

config = configparser.ConfigParser()
config['APP_INFO'] = {'ASSISTANT_NAME': 'Agamya','USER_NAME': 'Kamal'}
# replace the DEMO keyword with actual wolfram app id
# Note to @self: Use the gitignored version of this file to find id 
config['APP_CREDS'] = {'WOLFRAM_APP_ID' : 'DEMO'}

with open('.config', 'w+') as configfile:
    config.write(configfile)
