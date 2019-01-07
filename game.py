import time
def wait():
    wait = input("")
    return
class Grade:
    def __init__(self, grade, stress_points, self_esteem_points, friend_points, intelligence_points, win_points):
        self.grade = grade
        self.stress_points = stress_points
        self.self_esteem_points =self_esteem_points
        self.friend_points = friend_points
        self.intelligence_points = intelligence_points
        self.win_points = win_points
    def stats(self):
        print(f"{self.grade}'s Stats:")
        print(f"-Stress Value: {self.stress_points}")
        print(f"-Self Esteem: {self.self_esteem_points}")
        print(f"-# of Friends: {self.friend_points}")
        print(f"-Intelligence: {self.intelligence_points}")
        print("")
frosh = Grade("Freshman", 2, 3, 1, 2, 0)
soph = Grade("Sophomore", 3, 6, 5, 4, 0)
jun = Grade("Junior", 10, 2, 9, 6, 0)
sen = Grade("Senior", 6, 7, 10, 8, 0)
you = ""
haha = input("Do you want to play a game? ")
print("It literally doesn't matter what you say you're playing.")
frosh.stats()
time.sleep(1)
soph.stats()
time.sleep(1)
jun.stats()
time.sleep(1)
sen.stats()
red = input("What grade do you want to be in? Choose wisely, your stats are actually important and may help or hinder your gaming experience. ").title()
if red == "Freshman":
    you = frosh
elif red == "Sophomore":
    you = soph
elif red == "Junior":
    you = jun
elif red == "Senior":
    you = sen
else:
    print("No. That input wasn't good, so I don't care what you actually want. Now you're a freshman.")
    red = "Freshman"
    you = frosh
print(f"Alright, {red}! Do you think you can survive a day as a Magnet student? I don't either, but let's try anyway.")
print("")
print("The point of the game is to make the right decisions in the situations I present to you. Any time you make the right decision, I reward you with a number of win poits, depending on the situation.")
wait()
print("Make the wrong decision, however, and you lose a number of win points. Trust me, it's a lot easier to lose points that it is to gain them.")
wait()
print("The goal is to end the game with at least 10 win points. Here's a freebie for you. You're probably going to need it. Good luck!")
print("")
you.win_points += 1
wait()
wake = int(input("Pick a number between 1 and 10: "))
if 1<= wake <=4:
    wait()
    print(f"You're wake up at {wake} o'clock! You’re so sleepy by the time you get to school, you fall asleep in class and get in trouble! Minus 2 win points.")
    you.win_points -=2
elif 5<= wake <= 7:
    wait()
    print(f"You woke up at {wake} o'clock! Right on time to get to school! Good job! Plus 3 win points.")
    you.win_points +=3
elif 8<= wake <=10:
    wait()
    print(f"What a disgrace, you woke up at {wake} o'clock. Way too late to get to school on time! Minus 2 win points")
    you.win_points -=2
elif 0>= wake or wake >10:
    wait()
    print("I just said to pick a number between 1 and 10. How hard is it to follow simple instructions? Just for that, you woke up at 10 and were late to school. If you had originally chosen 10, you would still be late but would only lose 2 points.")
    wait()
    print("But you just had to be special. You're incapable of following instructions. So, congrats. You lost 100 win points by being a wise guy. Feel free to keep on playing, but you are incapable of winning.")
    you.win_points -=101
    print("")
    wait()
    print("Sigh.")
    wait()
    failure = input("Do you want to try again? (y/n) ").title()
    wait()
    print("Again, it literally doesn't matter what you say. I worked hard on this game, you're going to play it.")
    wait()
    promise = input("Can you at least promise to actually follow the istructions this time? (y/n) ").title()
    if promise == "Y" or promise == "Yes":
        wait()
        print("Fine. You're on thin ice, but i'm awarding you 95 win points. You're still starting lower than you would have if you had FOLLOWED INSTRUCTIONS, but you still have a chance. Feel free to play on.")
        you.win_points +=95
    elif promise == "N" or promise == "No":
        print("Fine. Coward.")
        wait()
        print(f"Have fun trying to win the game starting with -100 points.")
wait()
print(f"You now have {you.win_points} win points. You will get updates like this after every challenge you complete, so you won't have to track your points yourself.")
print("")
wait()
locker = input("The bell starts belling. You're about to enter your first class when you remember you forgot your binder in your locker. You go up to get it, but do you remember your combination? (y/n) ").title()
wait()
if locker == "Y" or locker == "Yes":
    if you.intelligence_points > 5:
        print("You're right, you do. You get your stuff and head to class, getting there just in time for the announcements to start. Plus 1 win point.")
        you.win_points +=1
    elif you.intelligence_points < 5 and you.friend_points > 5:
        print("Yeah, um, no you don't. Your intelligence isn't high enough for that. Sorry. However, your friends know how forgetful you can be and memorized it for you. What great friends they are!")
        wait()
        print("You cut it close, but you get your bider and get to class on time. However, you don't get any win points. Remember your combo next time.")
    else:
        print("LOL no you don't. Stop lying to yourself, your intelligence isn't high enough for you to remember this kind of stuff. Did you at lease write it down?")
        wait()
        print("Don't bother checking. You didn't. You're not smart enough to remember the combo, you really think you'd be intelligent enough to think to write it down?")
        wait()
        print("What about a friend? Do they kow your combo?")
        wait()
        print("Nope. You don't have many friends, and none of them know your combo. You're screwed. You get to class late. Your binder is still stuck in your locker. Minus 2 win points.")
        you.win_points -=2
else:
    if you.intelligence_points >5:
        print("What are you talking about? You're definitely smart enough to remember something as simple as your combo. Get your stuff and stop doubting yourself.")
        wait()
        print("You don't get any win points for this, even though you suceeded. Be more confident in yourself next time!")
    elif you.friend_points > 5:
        print("You're right, you don't remember it. Luckily, one of your very good friends knows it, and helps you open your locker. You get your binder and get to class on time. The power of friendship! Plus 1 win point.")
        you.win_points +=1
    else:
        print("Yeah, you don't remember your combo, but that's okay. You can just get it from the office later. Trust me, you won't need it for this class. Don't beat yourself up, okay? Here, have a win point, to make yourself feel better.")
        you.win_points +=1
wait()
print(f"You now have {you.win_points} win points.")
print("")
wait()
print("Guess what? You've got a test! You don't even need that precious binder you spent so much time trying to get! Perfect way to start the day, sucker!")
wait()
if you.intelligence_points == 2:
    print("Oh, poor little freshman, you forgot to study last night. You hand in the test knowing you failed. Minus 4 win points.")
    you.win_points -=4
elif you.intelligence_points == 4:
    print("Oh, you sophomore, you. You didn’t study last night. Thankfully you paid attention in class, so you kinda knew what you were doing. You still got a C, though. Minus 2 win points.")
    you.win_points -=2
elif you.intelligence_points == 6:
    print("Congrats, junior. You actually remembered to study last night. But you were so caught up with Sansi’s timeline you didn’t study that well. You got a B, but you know you could’ve done better. Plus 2 win points.")
    you.win_points += 2
elif you.intelligence_points == 8:
    print("Since you’re a highly intelligent senior, you knew everything on that test. You aced it, good job! Plus 3 win points.")
    you.win_points +=3
wait()
print(f"You now have {you.win_points} win points.")
print("")
wait()
print("The class goes on, but you're getting really tired. You just took a test, okay. How in the world are you supposed to stay awake?")
seven = input("You're not. So here's the deal, do you want to struggle to keep your eyes open or just go to sleep? awake/sleep ").title()
if seven == "Awake":
    print("But you're so tireddddd. You fight your hardest to keep your eyes open, being a good student and paying attention to your boring teacher.")
    wait()
    print("Turns out your teacher was just going to review everything you were just tested on for the rest of class. There was absolutely no need for you to stay awake.")
    wait()
    print("Good job, goody two shoes. Minus 2 win points.")
    you.win_points -=2
if seven == "Sleep":
    print("Good idea. You've dealt with a lot so far. You need a break.")
    wait()
    print("What a fantastic nap. And the greatest part, your friend tells you that your teacher literally did nothing but review the stuff you just got tested on. You got away scot-free!")
    wait()
    print("Just for that, plus 3 win points! You deserve it!")
    you.win_points +=3
print(f"You now have {you.win_points} win points.")
wait()
print("")
print(f"Alright, class is over! You're lucky, too. You just watch a movie in your next class. What a perfect little break for you. You deserve it, after that test. Plus 1 win point.")
you.win_points += 1
wait()
print(f"You now have {you.win_points} win points.")
print("")
wait()
lunch = input("Lunch time! Did you bring lunch or are you going to buy it? (bring/buy) ").title()
wait()
if lunch == "Bring":
    print("Your lunch is a little cold, but at least you don't have to walk alllllll the way to the cafeteria. Plus 2 win points.")
    you.win_points +=2
elif lunch == "Buy":
    print("None of your friends want to go to the cafeteria with you. You're going to have to walk there all by yourself. Looking like a loser with no friends. Through the very crowded quad.")
    wait()
    if you.self_esteem <5:
        print("You're way too self conscious right now to look like a loser. Your self esteem is pretty low. You should get that checked out. Anyway, you don't want to look like a loser, so you go hungry instead. What a smart decision. Minus 1 win point.")
        you.win_point -=1
    elif you.self_esteem >5:
        print("Literally who cares if people think you're a loser. Go get that lunch! Plus 4 win points!")
        wait()
        print("Yeah... um... you forgot your money....... Good job.. Minus 3 win points.")
        you.win_points +=1
wait()
print(f"You now have {you.win_points} win points.")
print("")
wait()
print("7/8 starts, and right off the bat your teacher announces a pop quiz you're totally unprepared for. Hope your stress doesn't keep you from doing well!")
wait()
if you.stress_points <5:
    print("You actually were good on the stress. Sure, you were unprepared, but you were calm enough that you could take the quiz wihtout double guessing yourself. Plus 3 win points.")
    you.win_points += 3
else:
    print("Yeah. You stressed out way too much. You needed an A in this class, but it doesn't look like you're going to get it now. Sorry. Minus 3 win points.")
    you.win_points -= 3
wait()
print(f"You now have {you.win_points} win points.")
wait()
print("")
attention = input("The bell rings, and you go to 9/10. But your teacher is just sooooooooo boring. Do you want to zone out or keep paying attention? zone/pay ").title()
if attention == "Zone":
    print("Yeah, you're right. Who needs to pay attention in class? It sucks, you're bored, so why not take a nap instead?")
    wait()
    print("Your teacher looks around the room at all the bored faces. Their eyes land on you. You remain unaware as they stalk closer to you.")
    wait()
    print("Your teacher asks you a question. You are unable to answer. You fail the class instantly. Minus 2 win points.")
    you.win_points -=2
elif attention == "Pay":
    print("You struggle to stay awake, but you do in the end. Good perseverance.")
    wait()
    print("Your teacher looks around the room at all the bored faces. Their eyes land on you. You become slightly frightened as they stalk towards you.")
    wait()
    print("They stop in front of you. They ask a question. Hesitantly, you answer, and though shaky, you get it correct. Good job. If you hadn't paid attention, your teacher would totally hate you.")
    wait()
    print("Your teacher smiles at you. They're so grateful you were paying attention. Plus 2 win points.")
    you.win_points +=2


