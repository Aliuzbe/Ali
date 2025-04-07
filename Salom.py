from telethon import TelegramClient, types
import asyncio

# Telegram API credentials
api_id = 25752230
api_hash = '07f3775dfe2c8f2213bd64c87b69e606'
phone_number = '+998951102083'
session_name = 'auto_poster_test'

# Advertisement message
message = """🔥 HARAJATSIZ HARAKAT – 0 TENG! 🔥  
GURUHLARNI KO‘TARAMIZ!  

---  
📱 Telegram obunachilar:  
• 500 ta – 20 000 so‘m  
• 1000 ta – 15 000 so‘m *(noted lower price for larger quantity)*  
• 1000 ta – 30 000 so‘m  

📱 Bez-minus obunachilar:  
• 500 ta – 35 000 so‘m  
• 1000 ta – 65 000 so‘m  

📱 Premium obunachilar:  
• 500 ta – 40 000 so‘m  
• 1000 ta – 80 000 so‘m  

📱 O‘zbek jvoy obunachilar:  
• 500 ta – 55 000 so‘m  
• 1000 ta – 110 000 so‘m  

---  
📸 Instagram obunachi:  
• 500 ta – 25 000 so‘m  
• 1000 ta – 45 000 so‘m  

❤️ Instagram like:  
• 500 ta – 10 000 so‘m  
• 1000 ta – 15 000 so‘m  

👁️ Instagram prasmotr:  
• 500 ta – 10 000 so‘m  
• 1000 ta – 20 000 so‘m  

---  
⭐️ Telegram stars xizmatlari:  
• 15 ta – 5 000 so‘m  
• 25 ta – 8 000 so‘m  
• 50 ta – 16 000 so‘m  
• 75 ta – 23 000 so‘m  
• 100 ta – 29 000 so‘m  

⚡ Telegram premium:  
• 1 oylik – 45 000 so‘m  
• 3 oylik – 168 000 so‘m  
• 6 oylik – 235 000 so‘m  
• Yillik – 315 000 so‘m  

---  
☢️ Guruh kutatarish xizmati  
✅ Telegram akkauntlar  
🎮 PUBG hizmatlari ham mavjud  

---  
ISBOTLAR PROFILDA! TEKSHIRIB YOZING! 💔  
Sifat, tezlik va ishonch — bizda!"""

async def send_to_all_groups():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start(phone_number)
    
    try:
        dialogs = await client.get_dialogs()

        # Filter for groups only
        groups = [
            dialog for dialog in dialogs
            if isinstance(dialog.entity, (types.Chat, types.Channel)) and (
                isinstance(dialog.entity, types.Chat) or
                (isinstance(dialog.entity, types.Channel) and dialog.entity.megagroup)
            )
        ]

        if not groups:
            print("Hech qanday guruh topilmadi.")
            return

        # Send to all groups one by one with a 10-second delay
        for group in groups:
            try:
                await client.send_message(group.entity, message)
                print(f"✅ Xabar yuborildi: {group.name}")
                await asyncio.sleep(10)  # 10 soniya kutish
            except Exception as e:
                print(f"❌ {group.name} guruhiga yuborishda xatolik: {str(e)}")

    except Exception as e:
        print(f"❌ Umumiy xatolik yuz berdi: {str(e)}")
    finally:
        await client.disconnect()

# Run the script
asyncio.run(send_to_all_groups())
