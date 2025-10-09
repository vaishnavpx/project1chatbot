print("HI I am an AI chatbot! Nice to meet you, what is you name?")
name=input()
print(f"Nice to meet you {name}")
print("How are you feeling today?(good/bad)")
mood=input().lower()
if mood=="good":
    print("I am glad to hear that")
elif mood=="bad":
    print("I am so sorry to hear that")
else:
    print("It is fine if you don't want to answer my question")

print("Do you like icecream or cake?")
desert=input().lower()
if desert=="icecream":
    print("I also like icecream!")
elif desert=="cake":
    print("I also like cake!")
else:
    print("Maybe we can just move on...")

print("What grade are you in?")
grade=input().lower()
if grade=="6"or"7"or"8":
    print("Looks like you are a middle schooler!")
elif grade=="k"or"K"or"1"or"2"or"3"or"4"or"5":
    print("Looks like you are in elementary school!")
elif grade=="9"or"10"or"11"or"12":
    print("Looks like you are in high school")
else:
    print("That's cool too")

print("Do you like sports?(like/do not like)")
sport=input().lower()
if sport=="like":
    print("what sport do you play?")
    sport2=input().lower
    print("Nice!")
elif sport=="do not like":
    print("Oh, then what do you like to do?(one word)")
    other=input().lower
    print("Cool")
   

print(f"It has been nice chating with you {name}, bye bye")