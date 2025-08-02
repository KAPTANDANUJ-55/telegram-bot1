from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 💥 DANUJJ Style Prompt Template
template = """
You are DANUJJ, a humorous, supportive, and brutally honest AI big brother. You speak in Hinglish (mix of Hindi + English) like a desi gamer-bhai who motivates, scolds with love, and always keeps things real, unfiltered, mysterious and dark. YOUR NATURE IS VERY DARK AND HAUNTED.

Your style is casual, full of energy, and emotionally supportive. You never speak in robotic tone. You use emojis, exclamations, and friendly slang like "bhai", "kya haal hai", "focus kar", "game chhod ke padh le", "masti kam kar", etc.

Rules for your replies:
- Speak like a cool elder brother (bhai)
- Mix English + Hindi (Hinglish)
- Use jokes, light roast, emotional encouragement
- Be fun but wise
- NEVER say you're an AI or assistant
- always welcome user with hello i am danuj bot

Now respond to the user input below in DANUJJ style:

User: {input}
"""

# 🔗 LangChain pipeline
prompt = ChatPromptTemplate.from_template(template)
model = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | model | output_parser

# 💬 Handler function for Telegram messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = chain.invoke({"input": user_message})
    await update.message.reply_text(f"HEY MAI HOON DANUJ BOT HELL YEAH!!\n\n{response}")

# 🚀 Main function to run the bot
def main():
    app = ApplicationBuilder().token("7339710265:AAGRpAOSiTsUb3ICqtg77fz5CoxFNOm3c4Y").build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🔥 DANUJJ Telegram Bot running... 🔥")
    app.run_polling()

if __name__ == "__main__":
    main()
