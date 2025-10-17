import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init(autoreset=True)

print(f"{Fore.CYAN}???? Welcome to sentiment spy????{Style.RESET_ALL}")
username=input(f"{Fore.MAGENTA} Please enter your name:{Style.RESET_ALL}").strip()
if not username:
    username="unkown"

conversation_history=[]
print(f"{Fore.CYAN}Hello Agent {username}")
print(f"{Fore.BLUE}Type a sentence and I will analize it for you")
print(f"Type{Fore.YELLOW}'reset'{Fore.CYAN},{Fore.YELLOW}'history'{Fore.CYAN},{Fore.YELLOW}'exit'{Fore.CYAN},{Fore.YELLOW} to quit.{Style.RESET_ALL}\n")
while True:
    user_input=input(f"{Fore.GREEN}>>{Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter some text{Style.RESET_ALL}")
        continue
    if user_input.lower()=="exit":
        print(f"{Fore.BLUE}Exiting the sentiment spy program, Agent {username}{Style.RESET_ALL}")
        break
    elif user_input.lower()=="reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}All conversation is cleared{Style.RESET_ALL}")
        continue
    elif user_input.lower()=="history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation history:{Style.RESET_ALL}")
            for idx,(text,polarity,sentiment_type) in enumerate(conversation_history,start=1):
                if sentiment_type=="Positive":
                    color=Fore.GREEN
                elif sentiment_type=="Negative":
                    color=Fore.RED
                else:
                    color=Fore.YELLOW

                print(f"{idx}.{color}{text}"f"(Polarity:{polarity:.2f},{sentiment_type}){Style.RESET_ALL}")
        continue
    polarity=TextBlob(user_input).sentiment.polarity
    if polarity>0.25:
        sentiment_type="positive"
        color=Fore.GREEN
    elif polarity<-0.25:
        sentiment_type="Negative"
        color=Fore.RED
    else:
        sentiment_type="Neutral"
        color=Fore.YELLOW
    
    conversation_history.append((user_input,polarity,sentiment_type))
    print(f"{color}{sentiment_type} sentiment detected" f"(Polarity:{polarity:.2f}){Style.RESET_ALL}")