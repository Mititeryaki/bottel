import math
import os
import re
import time

import heroku3
import requests
import spamwatch as spam_watch
from validators.url import url

from .. import *
from ..Config import Config
from ..core.logger import logging
from ..core.managers import eod, eor
from ..core.session import legend
from ..helpers import *
from ..helpers.utils import _format, _legendutils, install_pip, reply_id
from ..sql_helper.globals import gvarstatus

# =================== CONSTANT ===================
bot = legend
LOGS = logging.getLogger(__name__)
USERID = legend.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY



thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")

# mention user
mention = f"[{Config.ALIVE_NAME}](tg://user?id={USERID})"
legend_mention = mention
hmention = f"<a href = tg://user?id={USERID}>{Config.ALIVE_NAME}</a>"

#pic
# pic
gban_pic = "./Legendbot/helpers/resources/pics/gban.mp4"
main_pic = "./Legendbot/helpers/resources/pics/main.jpg"
core_pic = "./Legendbot/helpers/resources/pics/core.jpg"
chup_pic = "./Legendbot/helpers/resources/pics/chup.mp4"
bsdk_pic = "./Legendbot/helpers/resources/pics/bsdk.jpg"
bsdkwale_pic = "./Legendbot/helpers/resources/pics/bsdk_wale.jpg"
chutiya_pic = "./Legendbot/helpers/resources/pics/chutiya.jpg"
promote_pic = "./Legendbot/helpers/resources/pics/promote.jpg"
demote_pic = "./Legendbot/helpers/resources/pics/demote.jpg"
mute_pic = "./Legendbot/helpers/resources/pics/mute.jpg"
ban_pic = "./Legendbot/helpers/resources/pics/ban.jpg"


PM_START = []
PMMESSAGE_CACHE = {}
PMMENU = "pmpermit_menu" not in Config.NO_LOAD

# Gdrive
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

# spamwatch support
if Config.SPAMWATCH_API:
    token = Config.SPAMWATCH_API
    spamwatch = spam_watch.Client(token)
else:
    spamwatch = None


# ================================================

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


# thumb image
if Config.THUMB_IMAGE is not None:
    if check := url(Config.THUMB_IMAGE):
        try:
            with open(thumb_image_path, "wb") as f:
                f.write(requests.get(Config.THUMB_IMAGE).content)
        except Exception as e:
            LOGS.info(str(e))


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif isinstance(dictionary[key], list):
        if value in dictionary[key]:
            return
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]
        
      

    
async def make_gif(event, reply, quality=None, fps=None):
    fps = fps or 1
    quality = quality or 256
    result_p = os.path.join("temp", "animation.gif")
    animation = lottie.parsers.tgs.parse_tgs(reply)
    with open(result_p, "wb") as result:
        await _legendutils.run_sync(
            lottie.exporters.gif.export_gif, animation, result, quality, fps
        )
    return result_p
