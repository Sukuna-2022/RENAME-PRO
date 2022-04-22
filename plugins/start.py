from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	𝐇𝐞𝐥𝐥𝐨 👋 {message.from_user.first_name }
	
➡️ 𝐈'𝐦 𝐚 𝐓𝐆 𝐑𝐞𝐧𝐚𝐦𝐞𝐫 𝐁𝐨𝐭

➡️ 𝐈 𝐜𝐚𝐧 𝐑𝐞𝐧𝐚𝐦𝐞 𝐚𝐧𝐲 𝐅𝐢𝐥𝐞 ✍️ 𝐰𝐢𝐭𝐡 𝐂𝐮𝐬𝐭𝐨𝐦 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐚𝐧𝐝 𝐑𝐞𝐮𝐩𝐥𝐨𝐚𝐝 𝐢𝐭 𝐭𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐚𝐬 𝐅𝐢𝐥𝐞 𝐨𝐫 𝐕𝐢𝐝𝐞𝐨
       

	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup(
	 ))
	



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename")
       ,InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))
