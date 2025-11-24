import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
    ContextTypes,
)
from engine import choose_card

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Conversation states
CATEGORY, PLATFORM, AMOUNT = range(3)

categories = [
    "grocery", "dining", "online_shopping",
    "fuel", "utilities", "bhima", "jewellery", "others"
]

platforms = [
    "offline", "amazon", "flipkart", "myntra",
    "swiggy", "zomato", "bigbasket"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup([[c] for c in categories], one_time_keyboard=True)
    await update.message.reply_text("Select spend category:", reply_markup=keyboard)
    return CATEGORY

async def get_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["category"] = update.message.text
    keyboard = ReplyKeyboardMarkup([[p] for p in platforms], one_time_keyboard=True)
    await update.message.reply_text("Select platform:", reply_markup=keyboard)
    return PLATFORM

async def get_platform(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["platform"] = update.message.text
    await update.message.reply_text("Enter amount in ₹:")
    return AMOUNT

async def get_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amt = float(update.message.text)
    except:
        await update.message.reply_text("Please enter a valid number:")
        return AMOUNT

    category = context.user_data["category"]
    platform = context.user_data["platform"]

    card, reason = choose_card(category, amt, platform)

    reply = (
        f"💳 *Recommended Card*: *{card}*\n"
        f"📌 *Reason*: {reason}\n"
        f"💰 *Amount*: ₹{amt}"
    )

    await update.message.reply_markdown(reply)
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cancelled.")
    return ConversationHandler.END

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_category)],
            PLATFORM: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_platform)],
            AMOUNT:   [MessageHandler(filters.TEXT & ~filters.COMMAND, get_amount)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv)
    app.run_polling()

if __name__ == "__main__":
    main()
