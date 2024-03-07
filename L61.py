#Elise Ward and Anastacia Aguirre


def too_long(message):
    length= len(message)
    if length>140:
        print("Your message is too long, please shorten by", length-140, "character(s)")
    else:
        print("Your message can be sent.")


too_long("hello, my day was pretty good today")
too_long("I dont know how much 140 charachters looks like so i'm going to keep typing until I think i reach it. Am I there yet? I feel like it but maybe idk what 140 really looks like?")


#Emojis and unicode

print("Snakes! 🐍🐍🐍")
import unicodedata
unicodedata.lookup("snake")

message1="I have seven cats 🐈🐈🐈🐈🐈🐈🐈"
message2= "I 💕 my cats very much"
message3= "I also have a family dog 🐕"
message4= "I don't like the 🐕 very much 💔"
message5= "Do you have any pets? 🦜🐇🐢🐍"

print(len(message1))
print(len(message2))
print(len(message3))
print(len(message4))
print(len(message5))

unicodedata.name("&")
#'AMPERSAND'
unicodedata.name("[")
#'LEFT SQUARE BRACKET'
unicodedata.name("/")
#'SOLIDUS'
unicodedata.name("~")
#'TILDE'
unicodedata.name("`")
#'GRAVE ACCENT'
