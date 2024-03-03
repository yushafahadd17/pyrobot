# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import os
from distutils.util import strtobool
from os import getenv
from Uputt.helpers.cmd import cmd

from dotenv import load_dotenv

load_dotenv("config.env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "?¥µ")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://raw.githubusercontent.com/cacacr4ck/mawing/main/Uputt/resources/aw.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")
API_HASH = getenv("API_HASH", "bfd323eb8889f834993c3e30308ca2d2")
API_ID = getenv("API_ID", "25711467")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1002126334237, -1001608701614, -1001675459127, -1001473548283, -1001608701614]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "1.1.5@main"
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HNDLR = cmd
OWNER_ID = getenv("OWNER_ID", "6508228335")
BOT_TOKEN = getenv("BOT_TOKEN", "7029455313:AAFoBZTu1R3oz8r1_20cbaM4ElbMOpVk96U")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "sk-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")
CHANNEL = getenv("CHANNEL", "yushaa17")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "zodiaclights17")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "False"))
REPO_URL = getenv("REPO_URL", "https://github.com/cacacr4ck/mawing")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQDNvmIAbFPKvNAsmgIXGrvKehdf84snQmh7cP2BFjAqGXzMuzTTPA_ForGN7AEnCoo60FC7csuqPuq8JIYBxC91HgDa-lTmTsg31B-67NhqNb1_eWD92P6iyjfiELyrO6piPDwdzn1VhNY-Ariu1_mNfuvEMyVpfNBCGYXZWkicMPr4gusF3-9zIUm5QK-Iuz-iAdNWWd28moColT8f2eg2cZnlAug6D8TrPCEf4Dm_rScyZ-RyC5POrqs83ww7LbR23URobIu47ji1JFc2pnCCi6IYgnHjKwKrLINl_vNcXwST2ocu4YthCcDChqKKjWstegAtiwHD9pWaa223qhVYFlRpCwAAAAGD667vAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
