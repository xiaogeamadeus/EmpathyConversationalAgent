import random


class KaomojiManager:

    def __init__(self):
        self.kaomoji_lib = {
            "joy": ["╰(●’◡’●)╮", "♪（＾∀＾●）ﾉｼ （●´∀｀）♪"],
            "sadness": [",,Ծ‸Ծ,,", "π__π", "(→_←)"],
            "anger": ["<(｀^′)>", "ヽ(≧Д≦)ノ "],
            "surprise": ["(*゜ロ゜)ノ", "Σ( ￣д￣；) ！！", "Σ(っ °Д °;)っ"],
            "fear": ["╮(﹀_﹀”)╭", "(｀◕‸◕´+) "],
            "neutral": [":)", ":D"]
        }

    def generate_kaomoji(self, emotion, input_text):
        input_text = input_text + random.choice(self.kaomoji_lib[emotion.emotion])
        return input_text
