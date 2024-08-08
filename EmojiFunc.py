message = "Good Morning :)"

emoji_mapper = {

    ":)" : "😀",
    ":("  : "😞",
    ":D"  : "😂"
}


def emojify(message):
    splited_message = message.split()
    output = ""
    for char in splited_message:
        output += emoji_mapper.get(char,char) + " "
    return output


print(emojify(message))
