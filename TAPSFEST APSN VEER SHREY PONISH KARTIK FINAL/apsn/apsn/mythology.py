import os
import sys
import textwrap
import nltk
from tabulate import tabulate
from nltk.sentiment import SentimentIntensityAnalyzer
from PIL import Image, ImageShow

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)["compound"]
    return sentiment_score

mythology_data = {
    "Zeus": "Zeus, the king of the gods, was known for his lightning bolt...",
    "Athena": "Athena, the goddess of wisdom, emerged fully grown and armored...",
    "Hercules": "Hercules, known for his incredible strength, completed the twelve labors...",
    "Apollo": "Apollo, the god of music and healing, was known for his radiant beauty...",
    "Aphrodite": "Aphrodite, the goddess of love and beauty, was born from the sea foam...",
    "Persephone": "Persephone, the queen of the underworld, was abducted by Hades and became...",
    "Odysseus": "Odysseus, the hero of the Trojan War, embarked on a long journey home...",
    "Medusa": "Medusa, once a beautiful woman, was cursed by Athena and turned into a hideous...",
    "Pandora": "Pandora, the first human woman, opened a forbidden box and released all...",
    "Orpheus and Eurydice": "Orpheus, a gifted musician, journeyed to the underworld to rescue...",
    "Prometheus": "Prometheus, the Titan, stole fire from the gods and gave it to humans...",
    "Theseus and the Minotaur": "Theseus, a hero, ventured into the labyrinth to slay the fearsome...",
    "Helen of Troy": "Helen's beauty sparked the Trojan War after she was abducted by Paris...",
}
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def dive_into_mythology():
    clear_screen()
    print("Dive into Greek Mythology\n")
    print(tabulate(mythology_data.items(), headers=["Mythology", "Description"], tablefmt="fancy_grid"))
    choice = input("Select a mythology to analyze sentiment (e.g., Zeus): ")
    if choice in mythology_data:
        sentiment_score = analyze_sentiment(mythology_data[choice])
        print("\nSentiment Analysis:")
        if sentiment_score >= 0.05:
            print("Positive sentiment")
        elif sentiment_score <= -0.05:
            print("Negative sentiment")
        else:
            print("Neutral sentiment")
    else:
        print("Invalid choice.")
    input("\nPress Enter to continue...")