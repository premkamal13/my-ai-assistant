import configparser
import sys
import os

sys.path.append(os.getcwd())

from configuration import Configuration

def getConfigs():

    config = configparser.ConfigParser()
    config.read('.config')
    config_sections = config.sections()
    foundAppInfo = 'APP_INFO' in config_sections
    foundCreds = 'APP_CREDS' in config_sections
    
    if foundAppInfo == False :
        print("App information is not present. Please run the config_write with data!")
        exit()

    if foundCreds == False: 
        print("The credentials required are missing. \
        Please generate the app ids and feed in config!")
        exit()

    # Why converting to lower case?
    """ Converting the attributes names to lower case to honor the ConfigParser's \
    default behavior to pass data in optionxform / lower-case
    """
    assistant_name = config['APP_INFO']['ASSISTANT_NAME'.lower()]
    # print(assistant_name)
    user_name = config['APP_INFO']['USER_NAME'.lower()]
    wolfram_app_id = config['APP_CREDS']['WOLFRAM_APP_ID'.lower()]
    # print(wolfram_app_id)
    return Configuration(assistant_name, user_name,  wolfram_app_id)

