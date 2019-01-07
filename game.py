import time
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
haha = input("Do you want to play a game?")
print("It literally doesn't matter what you say you're playing.")
time.sleep(2)
frosh.stats()
time.sleep(2)
soph.stats()
time.sleep(2)
jun.stats()
time.sleep(2)
sen.stats()
time.sleep(1)
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
time.sleep(1)
print("The point of the game is to make the right decisions in the situations I present to you. Any time you make the right decision, I reward you with a number of win poits, depending on the situation.")
time.sleep(1)
print("Make the wrong decision, however, and you lose a number of win points. Trust me, it's a lot easier to lose points that it is to gain them.")
time.sleep(1)
print("The goal is to end the game with at least 10 win points. Here's a freebie for you. You're probably going to need it. Good luck!")
print("")
time.sleep(1)
wake = int(input("Pick a number between 1 and 10: "))
if 1<= wake <=4:
    time.sleep(1)
    print(f"You're wake up at {wake} o'clock! You’re so sleepy by the time you get to school, you fall asleep in class and get in trouble! Minus 2 win points.")
    you.win_points -=2
elif 5<= wake <= 7:
    time.sleep(1)
    print(f"You woke up at {wake} o'clock! Right on time to get to school! Good job! Plus 3 win points.")
    you.win_points +=3
elif 8<= wake <=10:
    time.sleep(1)
    print(f"What a disgrace, you woke up at {wake} o'clock. Way too late to get to school on time! Minus 2 win points")
    you.win_points -=2
elif 0>= wake or wake >10:
    time.sleep(1)
    print("I just said to pick a number between 1 and 10. How hard is it to follow simple instructions? Just for that, you woke up at 10 and were late to school. If you had originally chosen 10, you would still be late but would only lose 2 points.")
    time.sleep(1)
    print("But you just had to be special. You're incapable of following instructions. So, congrats. You lost 100 win points by being a wise guy. Feel free to keep on playing, but you are incapable of winning.")
    you.win_points -=100
    print("")
    time.sleep(1)
    print("Sigh.")
    time.sleep(1)
    failure = input("Do you want to try again? (y/n) ").title()
    if failure == "Y" or failure == "Yes":
        time.sleep(1)
        promise = input("And do you promise to actually follow the istructions this time? (y/n) ").title()
        if promise == "Y" or promise == "Yes":
            time.sleep(1)
            print("Fine. Youre on thin ice, but i'm awarding you 95 win points. You're still starting lower than you would have if you had FOLLOWED INSTRUCTIONS, but you still have a chance. Feel free to play on.")
            you.win_points +=95
        elif promise == "N" or promise == "No":
            time.sleep(1)
            print("Fine. Coward.")
            print(f"You ended the game with {you.win_points} win points. You suck.")
    elif failure == "N" or failure == "No":
        time.sleep(1)
        print("Fine. Coward.")
        time.sleep(1)
        print(f"You ended the game with {you.win_points} win points. You suck.")
time.sleep(1)
print(f"You now have {you.win_points} win points. You will get updates like this after every challenge you complete, so you won't have to track your points yourself.")
print("")
time.sleep(1)
locker = input("The bell starts belling. You're about to enter your first class when you remember you forgot your binder in your locker. You go up to get it, but do you remember your combination? (y/n) ").title()
if locker == "Y" or locker == "Yes":
    if you.intelligence_points > 5:
        time.sleep(1)
        print("You're right, you do. You get your stuff and head to class, getting there just in time for the announcements to start. Plus 1 win point.")
        you.win_points +=1
    elif you.intelligence_points < 5 and you.friend_points > 5:
        time.sleep(1)
        print("Yeah, um, no you don't. Your intelligence isn't high enough for that. Sorry. However, your friends know how forgetful you can be and memorized it for you. What great friends they are!")
        time.sleep(1)
        print("You cut it close, but you get your bider and get to class on time. However, you don't get any win points. Remember your combo next time.")
    else:
        time.sleep(1)
        print("LOL no you don't. Stop lying to yourself, your intelligence isn't high enough for you to remember this kind of stuff. Did you at lease write it down?")
        time.sleep(1)
        print("Don't bother checking. You didn't. You're not smart enough to remember the combo, you really think you'd be intelligent enough to think to write it down?")
        time.sleep(1)
        print("What about a friend? Do they kow your combo?")
        time.sleep(1)
        print("Nope. You don't have many friends, and none of them know your combo. You're screwed. You get to class late. Your binder is still stuck in your locker. Minus 2 win points.")
        you.win_points -=2
else:
    if you.intelligence_points >5:
        time.sleep(1)
        print("What are you talking about? You're definitely smart enough to remember something as simple as your combo. Get your stuff and stop doubting yourself.")
        time.sleep(1)
        print("You don't get any win points for this, even though you suceeded. Be more confident in yourself next time!")
    elif you.friend_points > 5:
        time.sleep(1)
        print("You're right, you don't remember it. Luckily, one of your very good friends knows it, and helps you open your locker. You get your binder and get to class on time. The power of friendship! Plus 1 win point.")
        you.win_points +=1
    else:
        time.sleep(1)
        print("Yeah, you don't remember your combo, but that's okay. You can just get it from the office later. Trust me, you won't need it for this class. Don't beat yourself up, okay? Here, have a win point, to make yourself feel better.")
        you.win_points +=1
time.sleep(1)
print(f"You now have {you.win_points} win points.")
print("")
time.sleep(1)
print("Guess what? You've got a test! You don't even need that precious binder you spent so much time trying to get! Perfect way to start the day, sucker!")
if you.intelligence_points == 2:
    time.sleep(1)
    print("Oh, poor little freshman, you forgot to study last night. You hand in the test knowing you failed. Minus 4 win points.")
    you.win_points -=4
elif you.intelligence_points == 4:
    time.sleep(1)
    print("Oh, you sophomore, you. You didn’t study last night. Thankfully you paid attention in class, so you kinda knew what you were doing. You still got a C, though. Minus 2 win points.")
    you.win_points -=2
elif you.intelligence_points == 6:
    time.sleep(1)
    print("Congrats, junior. You actually remembered to study last night. But you were so caught up with Sansi’s timeline you didn’t study that well. You got a B, but you know you could’ve done better. Plus 2 win points.")
    you.win_points += 2
elif you.intelligence_points == 8:
    time.sleep(1)
    print("Since you’re a highly intelligent senior, you knew everything on that test. You aced it, good job! Plus 3 win points.")
    you.win_points +=3
time.sleep(1)
print(f"You now have {you.win_points} win points.")
print("")
time.sleep(1)
print(f"Alright, class is over! You're lucky, too. You just watch a movie in your next class. What a perfect little naptime for you. Not that you, a responsible {red} would sleep in class, even if it was just a movie. Plus 1 win point.")
you.win_points += 1
time.sleep(1)
print(f"You now have {you.win_points} win points.")
print("")
time.sleep(1)
lunch = input("Lunch time! Did you bring lunch or are you going to buy it? (bring/buy) ").title()
if lunch == "Bring":
    time.sleep(1)
    print("Your lunch is a little cold, but at least you don't have to walk alllllll the way to the cafeteria. Plus 2 win points.")
    you.win_points +=2
elif lunch == "Buy":
    time.sleep(1)
    print("None of your friends want to go to the cafeteria with you. You're going to have to walk there all by yourself. Looking like a loser with no friends. Through the very crowded quad.")
    if you.self_esteem <5:
        time.sleep(1)
        print("You're way too self conscious right now to look like a loser. Your self esteem is pretty low. You should get that checked out. Anyway, you don't want to look like a loser, so you go hungry instead. What a smart decision. Minus 1 win point.")
        you.win_point -=1
    elif you.self_esteem >5:
        time.sleep(1)
        print("Literally who cares if people think you're a loser. Go get that lunch! Plus 4 win points!")
        time.sleep(1)
        print("Yeah... um... you forgot your money....... Good job.. Minus 3 win points.")
        you.win_points +=1
time.sleep(1)
print(f"You now have {you.win_points} win points.")
print("")
time.sleep(1)
print("7/8 starts and passes without incident. But then 9/10 starts. And your teacher announces a pop quiz you're totally unprepared for. Hope your stress doesn't keep you from doing well!")
if you.stress_points <5:
    time.sleep(1)
    print("You actually were good on the stress. Sure, you were unprepared, but you were calm enough that you could take the quiz wihtout double guessing yourself. Plus 3 win points.")
    you.win_points += 3
else:
    time.sleep(1)
    print("Yeah. You stressed out way too much. You needed an A in this class, but it doesn't look like you're going to get it now. Sorry. Minus 3 win points.")
    you.win_points -= 3
time.sleep(1)
print(f"You now have {you.win_points} win points.")
print("")



