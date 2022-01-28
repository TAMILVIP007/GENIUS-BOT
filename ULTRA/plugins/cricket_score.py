import urllib.request
from bs4 import BeautifulSoup
from ULTRA import CMD_HELP
from ULTRA.utils import admin_cmd

@borg.on(admin_cmd(pattern="cs"))
async def _(event):
    score_page = "http://static.cricinfo.com/rss/livescores.xml"
    page = urllib.request.urlopen(score_page)
    soup = BeautifulSoup(page, "html.parser")
    result = soup.find_all("description")
    Sed = "".join(match.get_text() + "\n\n" for match in result)
    await event.edit(
        f"<b><u>Match information gathered successful</b></u>\n\n\n<code>{Sed}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "cricket_score": "**cricket_score**\
\n\n**Syntax : **`.cs`\
\n**Usage :** Gets Live cricket score automatically."
    }
)
