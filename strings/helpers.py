#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅<u>**‹ اوامر المشرفين ›:**</u>

/pause or /cpause • إيقاف تشغيل الموسيقى مؤقتا.

/resume or /cresume • استئناف الموسيقى المتوقفة مؤقتا.

/mute or /cmute • كتم صوت الموسيقى المشغلة.

/unmute or /cunmute • إلغاء كتم صوت الموسيقى الصامتة.

/skip or /cskip • تخطي تشغيل الموسيقى الحالية.

/stop or /cstop- إيقاف تشغيل الموسيقى.

/shuffle or /cshuffle • خلط قائمة التشغيل في قائمة الانتظار عشوائيا.

/seek or /cseek • إعادة توجيه البحث عن الموسيقى إلى المدة الخاصة بك

/seekback or /cseekback • إلى الوراء ابحث عن الموسيقى إلى المدة التي تقضيها

/restart • إعادة تشغيل بوت للدردشة الخاصة بك.

/skip • لتخطي الأغنية الحالية"""


HELP_2 = """✅<u>**‹ اوامر التشغيل ›:**</u>

/play or /vplay or /cplay  • سيبدأ في تشغيل استعلامك المحدد على الدردشة الصوتية أو بث الروابط المباشرة على الدردشات الصوتية.

/playforce or /vplayforce or /cplayforce •  يؤدي فرض التشغيل إلى إيقاف مسار التشغيل الحالي في الدردشة الصوتية وبدء تشغيل المسار الذي تم البحث عنه على الفور دون إزعاج/مسح قائمة الانتظار.

/channelplay [معرف القناه او ايدي القناه] أو [تعطيل] - يمكنك ربط القناة بمجموعة وبث الموسيقى على الدردشة الصوتية للقناة من مجموعتك.

/playlist • تحقق من قائمة التشغيل المحفوظة على الخوادم.

/deleteplaylist • حذف أي موسيقى محفوظة في قائمة التشغيل

/play • ابدء تشغيل قائمة التشغيل المحفوظة من الخوادم.‌‌"""


HELP_3 = """✅<u>**‹ اوامر البوت ›:**</u>

/stats • احصل على أفضل 10 مسارات إحصائيات عالمية ، وأفضل 10 مستخدمين للبوت ، وأفضل 10 دردشات على الروبوت ، وأفضل 10 دردشات تم لعبها في دردشة وما إلى ذلك.

/sudolist • تحقق من قائمه المطورين

/lyrics [اسم الموسيقى] • يبحث في كلمات الأغاني عن موسيقى معينة على الويب.

/song [اسم المسار] أو [رابط YT] • قم بتنزيل أي مسار من youtube بتنسيقات mp3 أو mp4.

/player -  احصل على لوحة تشغيل تفاعلية.

/queue or /cqueue • تحقق من قائمة انتظار الموسيقى."""

HELP_4 = """✅<u>**‹ اوامر اضافية ›:**</u>

/start - بدء تشغيل بوت الموسيقى.

/help  - احصل على قائمة مساعد الاوامــر مع تفسيرات مفصلة للاوامــر.

/ping- بنك بوت والتحقق من ذاكرة الوصول العشوائي، وحدة المعالجة المركزية الخ احصائيات بوت.

/settings • الحصول على إعدادات كاملة للمجموعة باستخدام الأزرار المضمنة"""

HELP_5 = """🔰**<u>‹ اوامر المطور ›:</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖**<u>BOT COMMANDS:</u>**
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

📈**<u>STATS COMMANDS:</u>**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats

⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

👤**<u>BLOCKED FUNCTION:</u>**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot s Blocked List.
/blockedusers - Check blocked Users Lists

👤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot s served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot s gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot s Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""
