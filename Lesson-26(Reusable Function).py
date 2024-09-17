def emoji_converted(message):
    separate_words = message.split(' ')
    emoji = {
        ":)": "🙂",
        ":(": "☹️"
    }
    output = " "

    for word in separate_words:
        output += emoji.get(word, word) + " "
    return output

message = input("Type your message: ")
result = emoji_converted(message)

print(result)
