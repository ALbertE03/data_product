import telebot

token= '7235089424:AAFG69LRNuLCYOFCdnLDuPMQiKxLo7AOj98'
bot = telebot.TeleBot(token)


def recivir_feedback(feedback):
        chat_id = '1883265786'
        try:
            bot.send_message(chat_id=chat_id,text=feedback)
            st.toast("Recibido ✅")
        except Exception as e :
            st.toast('Error al enviar el mensaje',e)
        



@bot.message_handler(commands=['json'])
def  enviar(message):
    with open("track.json",'r') as doc_file:
        bot.reply_to(message,doc_file)


