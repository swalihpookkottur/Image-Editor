# By @TroJanzHEX


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("1861097491:AAGltLqIzcYm4eLCJY68RUozR9md7Z0y2wA", "")

    APP_ID = int(os.environ.get("1964231", 12345))

    API_HASH = os.environ.get("ec4c7aef178d0f34501bde03c9926da2, "")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("JZwZhXWh6xq9jtMjE27dgSyB", "")
