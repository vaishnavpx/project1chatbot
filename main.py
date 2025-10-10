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
if grade=="6" or grade=="7" or grade=="8":
    print("Looks like you are a middle schooler!")
elif grade=="k"or grade=="K"or grade=="1"or grade=="2"or grade=="3"or grade=="4"or grade=="5":
    print("Looks like you are in elementary school!")
elif grade=="9"or grade=="10"or grade=="11"or grade=="12":
    print("Looks like you are in high school")
else:
    print("That's cool too")

print("Do you like sports?(yes/no)")
sport_response=input().lower()
if sport_response=="yes":
    print("what sport do you play?")
    sport=input().lower
    print(f"Nice! {sport} is a fun sport to play!")
elif sport_response=="no":
    print("Oh, then what do you like to do?(one word)")
    other=input().lower
    print("That is cool")
   

print(f"It has been nice chating with you {name}, bye bye")