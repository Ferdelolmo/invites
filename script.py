import csv
from pathlib import Path

# Load template
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Translations
translations = {
    "en": "We are thrilled to invite you to our wedding! We can’t wait to celebrate this special moment with you.",
    "es": "¡Estamos encantados de invitarte a nuestra boda! Contamos los días para celebrar este momento especial contigo.",
    "it": "Siamo felicissimi di invitarti al nostro matrimonio! Non vediamo l’ora di festeggiare insieme questo momento speciale."
}

# Create output folder
Path("output").mkdir(exist_ok=True)

# Read guest list
with open("guests.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["name"]
        lang = row["language"]
        invitation_text = translations.get(lang, translations["en"])

        personalized = template.replace("{{name}}", name).replace("{{invitation_text}}", invitation_text)
        filename = f"output/{name.replace(' ', '_').lower()}.html"

        with open(filename, "w", encoding="utf-8") as output_file:
            output_file.write(personalized)

print("✅ Invitations generated!")
