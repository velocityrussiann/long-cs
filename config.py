"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY CZECH"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "CZECH"
HANDLE = "@velocityczech"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'cs',
 'name': 'Czech',
 'native_name': 'Čeština',
 'history_key': 'czech',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'cs-CZ-AntoninNeural',
 'native_fallback_voice': 'cs-CZ-VlastaNeural',
 'native_engine': 'edge',
 'native_lang_code': 'cs',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'ČEŠTINA',
 'translit_label': 'SAY IT LIKE',
 'flag': 'cz',
 'greeting': 'Ahoj!',
 'encouragement': 'Výborně!',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Motivace',
 'Love': 'Láska',
 'Success': 'Úspěch',
 'Wisdom': 'Moudrost',
 'Happiness': 'Štěstí',
 'Self Improvement': 'Seberozvoj',
 'Gratitude': 'Vděčnost',
 'Friendship': 'Přátelství',
 'Hope': 'Naděje',
 'Creativity': 'Kreativita',
 'Inner Peace': 'Vnitřní Klid',
 'Confidence': 'Sebevědomí',
 'Perseverance': 'Vytrvalost',
 'Inspiration': 'Inspirace',
 'Positive Life': 'Pozitivní Život',
 'Courage': 'Odvaha',
 'Kindness': 'Laskavost',
 'Patience': 'Trpělivost',
 'Forgiveness': 'Odpuštění',
 'Strength': 'Síla',
 'Joy': 'Radost',
 'Balance': 'Rovnováha',
 'Growth': 'Růst',
 'Purpose': 'Smysl Života',
 'Mindfulness': 'Všímavost',
 'Travel & Airport': 'Cestování a Letiště',
 'Ordering Food & Dining': 'Objednávání Jídla a Restaurace',
 'Shopping & Prices': 'Nakupování a Ceny',
 'Asking for Directions': 'Ptaní se na Cestu',
 'Hotel & Accommodation': 'Hotel a Ubytování',
 'Daily Routine': 'Denní Rutina',
 'Meeting People & Greetings': 'Seznamování a Pozdravy',
 'Emergency & Health': 'Nouzové Situace a Zdraví',
 'Public Transportation': 'Veřejná Doprava',
 'Work & Office': 'Práce a Kancelář',
 'Weather & Small Talk': 'Počasí a Nezávazná Konverzace',
 'Coffee Shop & Bakery': 'Kavárna a Pekárna',
 'Family & Home': 'Rodina a Domov',
 'Hobbies & Free Time': 'Koníčky a Volný Čas',
 'Dating & Romance': 'Rande a Romantika',
 'Phone Calls & Messages': 'Telefonování a Zprávy',
 'Banking & Money': 'Bankovnictví a Peníze',
 'Doctor & Pharmacy': 'Lékař a Lékárna',
 'Sports & Fitness': 'Sport a Fitness',
 'Celebrations & Parties': 'Oslavy a Párty',
 'Feelings & Emotions': 'Pocity a Emoce',
 'Agreeing & Disagreeing': 'Souhlas a Nesouhlas',
 'Making Plans': 'Plánování',
 'Common Native Slang': 'Běžný Hovorový Jazyk',
 'Cultural Traditions': 'Kulturní Tradice'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnczech',
 '#czechlessons',
 '#czechforbeginners',
 '#languagelearning',
 '#czechvocabulary',
 '#velocityczech',
 '#dailyczech',
 '#czech',
 '#learnlanguages',
 '#speakczech']
# ==== HASHTAGS END ====
