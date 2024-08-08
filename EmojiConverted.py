message = input(">")
splitted_messages= message.split(" ")

emoji_dictionary = {
    ":)" : "😀",
    ":(" : "☹️",
    ":D"  : "😂"

}

output =""
for emoji in splitted_messages:
    output +=emoji_dictionary.get(emoji,emoji) + " "
print(output)