import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16553400"))
    API_HASH = os.environ.get("API_HASH", "e0ca5f5bf7d59b96c8abd76cc255deb2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5892195204:AAH3f_eu36WA6Ol8VJXybAeA6axZvE5HQxg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKkBu3AFYmr6qn3UyE5dfQtq7qevO0p9Abp4xKkkXXq7zqdz0vQg3Aws8dPnBD_ZClCrA0njByxWCGGzz_xVB4NGt0kUdHKkb1ffRzeHvlytkaNkk841s6UxfpCpE-QpeHHqoougaS414r95knUwIc0DHnBNYcGLFKHzMRDvYinLDBR1V-VRLF4xh1q5MBz_3YdBZTlWIeq67vfioUvdVMFQyFmxNrO8ZNI9mHoS2Mk8Squm_BxDIIH_ta-dlEs2kS0mGzgla2qISAOohS60lv3kd-ab36fSMN3DEOzdf7_x5Tjori236v58KDhIP4LA_JEATYEeD13o3akVVkCdJCLLg80=")#pastw string session 
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
