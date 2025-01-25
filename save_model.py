# Dictionary mapping 100 words to emojis
from model.save_model import predict_emoji

emoji_dict = {
    "happy": "😊", "sad": "😢", "love": "❤️", "angry": "😡",
    "laugh": "😂", "surprised": "😲", "cool": "😎", "sleepy": "😴",
    "thinking": "🤔", "star": "⭐", "fire": "🔥", "clap": "👏",
    "ok": "👌", "party": "🎉", "crying": "😭", "hug": "🤗",
    "sick": "🤒", "heart": "💖", "broken": "💔", "peace": "✌️",
    "coffee": "☕", "book": "📖", "music": "🎵", "phone": "📱",
    "laptop": "💻", "smile": "😁", "praying": "🙏", "wave": "👋",
    "rain": "🌧️", "sun": "☀️", "cloud": "☁️", "snow": "❄️",
    "tree": "🌳", "flower": "🌸", "dog": "🐶", "cat": "🐱",
    "bird": "🐦", "fish": "🐟", "frog": "🐸", "lion": "🦁",
    "tiger": "🐯", "monkey": "🐒", "banana": "🍌", "apple": "🍎",
    "cake": "🍰", "pizza": "🍕", "burger": "🍔", "fries": "🍟",
    "chocolate": "🍫", "icecream": "🍦", "car": "🚗", "bike": "🚴",
    "train": "🚆", "plane": "✈️", "boat": "⛵", "ball": "⚽",
    "basketball": "🏀", "tennis": "🎾", "gym": "🏋️", "medal": "🏅",
    "trophy": "🏆", "rocket": "🚀", "earth": "🌍", "moon": "🌙",
    "star": "🌟", "camera": "📷", "video": "📹", "tv": "📺",
    "clock": "⏰", "money": "💰", "gift": "🎁", "balloon": "🎈",
    "knife": "🔪", "light": "💡", "key": "🔑", "lock": "🔒",
    "crown": "👑", "shirt": "👕", "dress": "👗", "shoe": "👟",
    "bag": "👜", "ring": "💍", "glasses": "👓", "watch": "⌚",
    "medic": "🚑", "police": "🚓", "firetruck": "🚒", "ambulance": "🚑",
    "pencil": "✏️", "paint": "🎨", "robot": "🤖", "alien": "👽",
    "ghost": "👻", "cake": "🎂", "zombie": "🧟", "clown": "🤡",
    "santa": "🎅", "elf": "🧝", "unicorn": "🦄"
}

def predict_emoji(text):
    # Convert text to lowercase for case-insensitive matching
    text = text.lower()
    
    # Check for the keyword in the text and return corresponding emoji
    for word, emoji in emoji_dict.items():
        if word in text:
            return emoji
    return "No emoji found for the given text."

# Test the function
text_input = input("Enter a text to predict an emoji: ")
print("Predicted Emoji:", predict_emoji(text_input))
