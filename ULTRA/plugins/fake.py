"""Send Chat Actions
Syntax: .fake <option>
        fake options: Options for fake

typing
contact
game
location
voice
round
video
photo
document
cancel"""

import asyncio
from ULTRA.utils import admin_cmd
from ULTRA import CMD_HELP

 
@borg.on(admin_cmd(pattern="fake ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    action = input_str if (input_str := event.pattern_match.group(1)) else "typing"
    async with borg.action(event.chat_id, action):
        await asyncio.sleep(10)  # type for 10 seconds
        
        
        
CMD_HELP.update({
    "fake":
    ".fake (action name)\
    \nUsage: Type .fake (action name) this shows the fake action in the group  the actions are typing contact ,game, location, voice, round, video,photo,document.\
    "
})            
