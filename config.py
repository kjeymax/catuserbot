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
    STRING_SESSION = "1BVtsOGsBu1_M0UBroSNoN2-Obg9JDq1ACEfBKl3_qVlitacK1BOG5T36MqAu1uxJ9kEl2cMNevZ3wPcWI0N28YSA40px08-UPlbaXxvYw9dxtLnzfodA_3F5gforGMQ6jzd3FvYkz9KeSnlFGms19hbqgqtSDTIKElqbk_m-xSmALGRtcrGZMjzQWjzcjWR856YQ8mIYL8U3lJnWqWRIUTwbvYcUFtIWZUAzq0LhQJdl-7zcR5OkLm4FK77M_g-WakkNwg4tBFHaquytzFiUhjAUhfA4tCilNtczEjSfWIGkKT7blIK-VyRJ9zGtvilZAVexzVYfbmnVFtC1z4k8E-ycYmjFNEM="
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
