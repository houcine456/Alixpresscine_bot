from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_msg = """
مرحباً بك في بوت alixpresscine

هذا البوت يساعدك في الحصول على تخفيضات عالية على منتجات AliExpress 
✅ من 5%~1% إلى خصومات قد تصل إلى 90% على بعض المنتجات.

‼️ فقط أرسل الروابط التي تحتوي على نقاط AliExpress وسنُظهر لك أفضل الخصومات الممكنة!
    """
    await update.message.reply_text(welcome_msg)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
