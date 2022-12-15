import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25954149"))
    API_HASH = os.environ.get("API_HASH", "f7634977b2f47796d6df125bb8408cf5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5534222726:AAGlXXsfp0wiEX1EBrR-1Dis_ozwHrfkyho")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCXyPjton-HtxsTmA55LW8qdmt1tBr03YLjnkKUz5UbEfmR39DhF_4zQpbd55l0v4B9rB2yvNF_fSfA1WxF7zdiGf7mw_yx0UQeeZ8mAwAWKEDOXC7kkpe-Ujll3tsAvqJco0FLagVCTD5zM59AVzGLO5Vbkqbj0jfP1WVfD4v9UTexzpa8JiJhisyKZrKygo5uPAqFrmfqDFRqAkmRrEiB6QRs_FEpWx88_4uTJObo-W7RYd3MyPt_sI_CL7EAqsw1kKS1F7UlzpQfmq5IUjoCcKiHuBDXhViNTU_KbFvYfvmem4Qk88A3a-P4ym0g6NBG1lXfrhNLTyyJMvxIo3fqAAAAAWOmrvAA")#pastw string session 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("itz_star_robot")
    SUPPORT = os.environ.get("SUPPORT", "ROMEOBOT_OP") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "ROMEOBOT_OP") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/74607f92f18218ae4d61e.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/261b8f5dc24de55be9bdd.jpg")
    ASSISTANT_ID = int(os.environ.get("5966835440")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
