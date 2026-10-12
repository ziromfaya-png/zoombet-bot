import re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '8908450578:AAFsXAJdxUUAhUpXcECsTvcHBcS6SmMU2OI'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "🤖 **Bienvenue sur votre Bot ZOOM BET !**\n\n"
        "Pour analyser un match, envoyez-moi un message sous ce format :\n"
        "`Équipe A vs Équipe B / Cotes : 2.10 - 3.40 - 3.20`"
    )
    await update.message.reply_text(msg, parse_mode='Markdown')

async def analyser_match(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texte = update.message.text
    cotes = re.findall(r'\b\d+[\.,]\d+\b', texte)
    
    if len(cotes) < 3:
        await update.message.reply_text(
            "⚠️ **Format incorrect.**\n"
            "Veuillez indiquer les 3 cotes (Victoire 1 - Nul - Victoire 2).\n"
            "Exemple : `Real Madrid vs FC Barcelone / 2.10 - 3.50 - 3.20`"
        )
        return

    c1 = float(cotes[0].replace(',', '.'))
    cX = float(cotes[1].replace(',', '.'))
    c2 = float(cotes[2].replace(',', '.'))

    p1_brut = (1 / c1) * 100
    pX_brut = (1 / cX) * 100
    p2_brut = (1 / c2) * 100

    total_prob = p1_brut + pX_brut + p2_brut
    marge = total_prob - 100

    p1 = (p1_brut / total_prob) * 100
    pX = (pX_brut / total_prob) * 100
    p2 = (p2_brut / total_prob) * 100

    if p1 > p2 and p1 > pX:
        tendance = "Victoire Équipe Domicile (1)"
        favori_prob = p1
    elif p2 > p1 and p2 > pX:
        tendance = "Victoire Équipe Extérieur (2)"
        favori_prob = p2
    else:
        tendance = "Match Nul (X)"
        favori_
  
