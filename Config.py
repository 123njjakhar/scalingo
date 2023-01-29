import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16553400"))
    API_HASH = os.environ.get("API_HASH", "e0ca5f5bf7d59b96c8abd76cc255deb2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5892195204:AAH3f_eu36WA6Ol8VJXybAeA6axZvE5HQxg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQDGZpj24vHX6XaKWrXrWJ-Fiai38n1-Gj91Cs-8HSmzmQNqWRAuWZzstxufScuZsYsTKEVP2nJ_RrbiqfMvLSrvz0j625yMEBd_NMvWnVDDcp1cuoztJ9Jvilm6l6ke4YDAbRcgRU45N5A_zgbJuxL8RM9ygb3zr7c66LCS2LUcwhntdbb3CaAqOvI78vTDzHpLh8Dc4w6pbEM3DOGrgCd1EhNr4F5vEk4RUgs5FcaF57kzkdko5CxVSJ9reTa3W6PM_VY4HcndZfLBFvI8pTyiIZUCHdFN496M2qeaWey9uNPiHYEly0OMt3nJAfUsIBkIMe9FdkUvteU0qmKyIQ0AAAAAAU1JXKIA")#pastw string session 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("TONY_STARK_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "ROMEOBOT_OP") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "ROMEOBOT_OP") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/74607f92f18218ae4d61e.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/261b8f5dc24de55be9bdd.jpg")
    ASSISTANT_ID = int(os.environ.get("5591620770")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
