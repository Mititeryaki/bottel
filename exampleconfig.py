from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 454554
    API_HASH = "your value"
    # the name to display in your alive message
    ALIVE_NAME = "Your value"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "your value"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill th this
    LEGEND_STRING = "your value"
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = "your value"
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTRA_REPO = "https://github.com/ITS-LEGENDBOT/PLUGINS"
    EXTRA_REPOBRANCH = "main"
    UPSTREAM_REPO = "pro"
    # Your City's TimeZone
    TZ = "Asia/Kolkata"
