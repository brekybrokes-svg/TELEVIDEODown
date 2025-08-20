import telegram
print("PTB VERSION:", telegram.__version__)
import os
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Bot token'ı environment variable'dan alıyoruz
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Link algılama regex
URL_RE = re.compile(r'https?://\S+')

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Merhaba! Ben buradayım 🚀\nBana bir link gönder, onu algılayıp cevap vereceğim."
    )

# Mesajları yakala
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    m = URL_RE.search(text)
    if not m:
        await update.message.reply_text("Hmm... link göremedim. Bir link gönderir misin?")
        return

    url = m.group(0)
    # Şimdilik sadece linki geri döndürüyoruz
    await update.message.reply_text(f"🔗 Linki aldım: {url}\n(İleride dosya indirip göndereceğim.)")

def main():
    # Application nesnesi oluştur
    app = Application.builder().token(BOT_TOKEN).build()

    # Komut ve mesaj handler’larını ekle
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    # Botu başlat
    print("✅ Bot çalışıyor... Render üzerinden aktif.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
