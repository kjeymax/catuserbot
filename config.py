from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 1733305
    API_HASH = "f423cffca6b5b7247b31b5b0df61f48d"
    # the name to display in your alive message
    ALIVE_NAME = "Mr Dani"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://jhuxnzom:jx3U5CUb6f8WpCFFD3ZKcYYiSF0-XjVV@hansken.db.elephantsql.com/jhuxnzom"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOJwBu7UclP-9W2sX4AS-f6ScLTyXHZtryZrLx866qvHhGmntg9Lvf12XCvx9QjzLxMnUmn7eSbkDwcFXdf28XQsIdm49F4tYPQA7MfES0gdtJI3FMPHSVpXbinPGvmkb5a_Thos-BMxmu7Xq0J9MhHJa0qYYCLRpvEq7gBRhfNUD9s_mRmKVgyJetT4rILAt48ezVAaBx6GLm3OtC7YRpEVrHlcHmlpIw1yQuVkskcCX2juOQbn3SDMzDJF0SZnVzker8N8owLMUr0brz0w9Hf0rJsIRhGblbhDTwDcnq4bMRda8_b6XqjSD1eUaaE_6KfEVgdDkqk9qFjo16ZYvdREb0V4=
"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "7067081736:AAE8Q-rCbt6IHDpuxRU5x97G5QKA8DkcIGU"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002077741713
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
