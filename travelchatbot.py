import random,re
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

destinations={"beaches":["Maldives","Bali"],"mountains":["Mt. St. Helens","Mount Denali"],"cities":["New York City","Tokyo"]}
jokes=["What do you call an ocean of orange juice? A Fanta sea.","I was going to tell a joke about sodium, but then I thought, Na"]
def normalize_input(text):
    return re.sub (r"\s+"," ",...)
def recomend():
    print(f"{Fore.BLUE}Travel Bot: Beaches, Mountains or Cities?")
    preference=input({Fore.YELLOW}+"You:")
    #preference=normalize_input(preference)
    if preference in destinations:
        suggestion=random.choice(destinations[preference])
        print(f"Travel Bot: How about a {suggestion}?")
        print("Travel Bot: Do you like my suggestion or not?(yes/no)")
        answer=input(f"{Fore.YELLOW}You:").lower()
        if answer=="yes":
            print(f"Travel Bot: Awsome, enjoy {suggestion}")
        elif answer=="no":
            print("Travel Bot: That is fine, let's try another one.")
            recomend()
        else:
            print("Travel Bot: I will suggest again")
    else:
        print("Travel Bot: Sorry, but I don't have that type of destination.")
    show_help()
def tell_joke():
    print(f"Travel Bot: {random.choice(jokes)}")
def show_help():
    print("Travel Bot: I can suggest travel spots(say 'recomend')")
    print("Travel Bot: I can suggest jokes as well(say'jokes')")
    print("Travel Bot: Type exit or bye to end the conversation.")
def chat():
    print("Travel Bot: Hi, I am you Travel Bot.")
    name=input("Travel Bot: What is your name?:")
    print(f"Travel Bot: Nice to meet you {name}.")
    show_help()
    while True:
        user_input=input(f"enter something:")
        #user_input=normalize_input(user_input)
        if user_input=="recomend":
            recomend()
        elif user_input=="jokes":
            tell_joke()
        elif user_input=="exit"or"bye":
            print("Travel Bot: Safe travels! Goodbye!")
            break
        else:
            print("Travel Bot: Could you please repeat that again.")
if __name__=="__main__":
    chat()