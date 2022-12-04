print("Greetings From the creator!")
print("Now unlike other text adventure games, I will keep the text on the screen as a little log.")

def mygame1():
    print("You think of making money.")
    import time
    time.sleep(1)
    print("But have no idea how.")
    import time
    time.sleep(1)
    print("Then it comes to your head, to make a company.")
    import time
    time.sleep(1)
    print("So you look up on Internet Explorer 'What company types make the most money?'")
    import time
    time.sleep(1)
    print("You have a long look through, And you see nothing that you're good at Except One thing")
    import time
    time.sleep(1)
    print("Hardware.")

    print("You make your company, But haven't given it a name. What is your company called?")
    answer = input()
    print(f"So you make {answer}, But have not chosen the genre. Your company is:")
    print("Custom OS designer [C]")
    print("Computer Components Maker [M]")
    ans2 = input()
    if ans2 == 'C':
        print("What is your OS going to be called?")
        osname = input()
        print(f"So you are currently coding {osname}")
        print("You are going to be coding for 45 IRL seconds (45 days In-Game)")
        for t in range(45):
            import time
            time.sleep(1)
            print(t)
mygame1()
