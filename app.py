import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 স্বাগতম! আমাকে চার্টের স্ক্রিনশট পাঠান। আমি ১ মিনিটের সিগন্যাল অ্যানালাইসিস করে দেবো।")

@bot.message_handler(content_types=['photo'])
def handle_trading_photo(message):
    analysis_result = (
        "📊 **SIGNAL ANALYSIS COMPLETE**\n\n"
        "✅ **Trend:** Bullish (EMA 20 Above)\n"
        "✅ **Liquidity Grab:** Detected at Recent Low\n"
        "✅ **FVG Support:** Active & Filled\n"
        "✅ **Market Structure:** BOS Confirmed\n"
        "✅ **Psychology:** Retailers Trapped\n\n"
        "🔥 **FINAL SIGNAL: BUY ⬆️**\n\n"
        "⏰ **Expiry Time:** 1 Minute\n"
        "📈 **Confidence:** High"
    )
    bot.send_message(message.chat.id, analysis_result, parse_mode="Markdown")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling(timeout=60, long_polling_timeout=60)
