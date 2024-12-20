from random import choice

def game():
    answers = [
        "Well, of course, yes, what else is there to guess?",
        "It's decided from above, go and rejoice.",
        "Even a hedgehog could see that.",
        "The default 'yes', just like you wanted.",
        "You can relax — it's definitely a yes.",
        "Well, probably yes... although, not sure.",
        "More yes than no, but don't get too comfortable.",
        "Everything is heading for success, don't mess it up.",
        "The universe hints — everything's fine.",
        "Yes, period.",
        "It's blurry now, try asking sober.",
        "Ask later, I'm not in the mood right now.",
        "It's... better if you don't know.",
        "Well, it's unpredictable, think about it yourself.",
        "Pull yourself together and ask properly.",
        "Don't even start, okay?",
        "No, period. Deal with it.",
        "All signs point to no, no matter how hard you try.",
        "The prospects are as foggy as your attempts.",
        "So doubtful it's actually funny."
    ]
    
    print("Hello World, I am a magic ball, and I know the answer to any of your questions")
    name = input(f"What's your name?")
    print(f"Hey {name}")
    
    while True:
        print(f"\n{name}, ask your question (yes or no): ")
        input()
        print(choice(answers))
        
        while True:
            user_input = input("Do you wanna ask a new question? (Y/n): ").strip()
            if user_input == 'n':
                print(f"See ya next time, {name}")
                return
            elif user_input == 'Y':
                break
            else:
                print("Please try again (Yes - Y, No - n): ")

game()