def convert_to_uppercase(word):
    return word.upper()

try:
    user_input = input("Bir kelime girin: ")
    converted_word = convert_to_uppercase(user_input)
    print("Orijinal kelime:", user_input)
    print("Büyük harfli kelime:", converted_word)
except Exception as e:
    print("Bir hata oluştu:", e)

