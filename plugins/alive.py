from telethon import events, buttons

from System import ALIVE_NAME
from System.utils import admin_cmd, sudo_cmd
from System.zypherConfig import Config, Var

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ᴢʏᴘʜᴇʀ ᴜsᴇʀ"

@borg.on(lightning_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def omkvai(event):
  omk_caption = f"**{CUSTOM_ALIVE}**\n\n"
  omk_caption += f"**Mʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɢ**\n\n"
  omk_caption += "Aʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ ✗\n\n"
  omk_caption += f"**Zʏᴘʜᴇʀ ᴜsᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={fuk})\n"
  omk_caption += f"**Zʏᴘʜᴇʀ ᴠᴇʀ**: `{lionver}`\n"
  omk_caption += f"**Tᴇʟᴇᴛʜᴏɴ ᴠᴇʀ** ☞ {version.__version__}\n"
  omk_caption += f"**Zʏᴘʜᴇʀ sᴜᴘᴘᴏʀᴛ** ☞ [ᴊᴏɪɴ](https://t.me/ZypherSupport)\n"
  omk_caption += f"**LiCense**  ☞ [𝚃𝙴𝙰𝙼 𝚉𝚈𝙿𝙷𝙴𝚁](https://github.com/Mdnoor786/Zypher-X)\n"
  omk_caption += (
        f"**©️ CopyRight By** ☞ [𝚉𝚈𝙿𝙷𝙴𝚁 𝚇](https://github.com/Mdnoor786/Zypher-X)\n\n"
    )
  omk_button = [[Button.url("Zypher User", f"https://t.me/{bot.me.username}")]]
  omk_button += [[Button.url("Zypher Support", "t.me/ZypherSupport"), Button.url("Zypher Updates", "t.me/teamzypher")]]
  omk_button += [[custom.Button.inline("Deploy Zypher", data="omkd")]]
  await tgbot.send_file(event.chat_id, captions=omk_caption) 

  #OR BAAD ME KARUNGA 
