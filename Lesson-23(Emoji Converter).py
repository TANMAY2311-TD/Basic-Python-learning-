message = input("Type your message: ")
separated_words = message.split(' ')

print(separated_words)

emoji = {
    ":)": "🙂",
    ":(": "☹️",
    ":|": "😐",
    ";)": "😉",
    "red heart": "❤️"
}
output = ""

for word in separated_words:
    output += emoji.get(word, word) + ' '

print(output)
