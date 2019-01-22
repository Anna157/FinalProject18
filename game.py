#importing time and sys
#time to be used to stutter printing in the game
#sys to be used in delay(string) function and sys.exit()
import time
import sys
#wait() function which will be used after each line of text so player reads line by line
def wait():
    wait = input("")
    return
#delay(string) function, which prints character one by one, to be used for extra credit levels
#whenever delay is called, string within quotes becomes argument used to complete function
def delay(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)
        return
#extra_o() function, the opening of the extra credit level
def extra_o():
    delay("A wild Sanservino appears!*")
    wait()
    delay("He is going to ask you a series of questions.*")
    wait()
    delay("Answer them all correctly, and you may pass.*")
    wait()
#extra1() function, the first question asked for extra credit. (player with 0-9 points at end)
#input uses .title() to compensate for people who may use lowercase for his name instead of caps
#if input is wrong, function returns False, and later on in code (line ~700), the game will not move on to the next question
#it will print a "game over" statement, instead
def extra1():
    delay("Sanservino hisses at you, then asks his first question:")
    print("")
    delay("...")
    delay("~What is my first name?~")
    print("")
    name = input("").title()
    if name == "Jason":
        return True
    else:
        return False
    return win1
#extra2() function, executing the same idea as extra1(), with a different question for a player who ends with 0-9 points
def extra2():
    delay("Sanservino growls. You are getting closer to succeeding.*")
    wait()
    delay("He comes up with a harder question:")
    print("")
    delay("...")
    delay("~What is my birthday?~ (Answer in MM/DD/YYYY form.)")
    print("")
    birth = input("")
    if birth == "12/23/1976":
        return True
    else:
        return False
#extra3() function, executing the same idea as extra1(), with a different question for player who ends with 0-9 points
def extra3():
    delay("You are getting way too close to winning for Sanservino's liking.*")
    wait()
    delay("He decides to ask you a harder question:")
    print("")
    delay("...")
    delay("~Who is Anna's favorite Harry Potter character?~")
    print("")
    fav = input("").title()
    if fav == "Sirius" or fav == "Sirius Black":
        return True
    elif fav == "Hermione" or fav == "Hermione Granger":
        return True
    else:
        return False
#extra_h1() function, executing the same idea as extra1(), with a different question, only for players who end with 0 to 4 points
def extra_h1():
    delay("Sanservino roars. You dare answer all the easy questions? Fine, because you are /such/ a failure...*")
    wait()
    delay("Sanservino decides to give you an EXTRA HARD question now.*")
    wait()
    delay("...")
    delay("~What is the name of the bear in Tiny Headed Kingdom?~")
    print("")
    pip = input("").title()
    if pip == "Pip":
        return True
    else:
        return False
#extra_h2() function, executing the same idea as extra1(), with a different question, only for players who end with 0 to 4 points
def extra_h2():
    delay("Sanservino snarls at you.*")
    wait()
    delay("...")
    delay("~Spell the certain word from Mary Poppins that is very good, wonderful, though it sounds quite atrocious.~")
    print("")
    mary = input("").title()
    if mary == "Supercalifragilisticexpialidocious":
        return True
    else:
        return False
#extra_h3() function, executing the same idea as extra1(), with a different question, only for players who end with 0 to 4 points
def extra_h3():
    delay("What a big shot, you answered all the hard questions, too.*")
    wait()
    delay("Sanservino only has one more question for you, but don't think you're off the hook. This one's a doozy.*")
    wait()
    delay("...")
    delay("...")
    delay("~What is Anna's full name?~")
    print("")
    anna = input("").title()
    if anna == "Anna Maddalena O'Connell":
        return True
    else:
        return False
#class Grade, with arguments of grade, stress_points, self_esteem_points, friend_points, intelligence_points, and win_points to be used for game
#every grade has varying values for stress, self esteem. friends, and intelligence, but starts out wiht 0 win points
#win points gathered thoughout game thorugh successful challenges
class Grade:
    def __init__(self, grade, stress_points, self_esteem_points, friend_points, intelligence_points, win_points):
        self.grade = grade
        self.stress_points = stress_points
        self.self_esteem_points =self_esteem_points
        self.friend_points = friend_points
        self.intelligence_points = intelligence_points
        self.win_points = win_points
    #stats(self) function, used to print out each grade's points at the very start of the game before person chooses grade
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
tec = Grade("Teacher", "?", "?", "?", "?", 0) #a joke
you = "" #an empty variable
#every question with a string input has .title(), which automatically capitalizes whatever input the player uses, to prevent any crashes b/c their input is off by one non-capitalized letter
haha = input("Do you want to play a game? y/n ").title()
#asking if player wants to play my game
#and making sure to mention the * which will be the sign to press enter throughout the game
if haha == "Y" or haha == "Yes":
    print("Oh yay! I'm so happy you said yes, I worked really hard on this game, and I hope you enjoy it!* (Make sure to press enter after line of text when you see this: *)")
    wait()
elif haha == "N" or haha == "No":
    um = input("Wait, seriously? y/n ").title()
    if um == "Y" or um == "Yes":
        print("Fine. It's not like I poured my heart and soul into this or anything.* (Press enter when you see: *)")
        wait()
        guilt = input("Do you feel guilty enough to play my game or are you going to spite me? play/spite ").title()
        if guilt == "Play":
            print("")
            print("I'm glad you came to your senses. Enjoy!*")
            wait()
        elif guilt == "Spite":
            print("")
            print("Wow. That's really rude, you know.*")
            wait()
            print("You're a meanie-face.*")
            wait()
            print("Okay then. Goodbye. I'm sorry you didn't want to play with me.*")
            wait()
            #sys.exit(), used to exit the game by shutting down the code and not allowing the player to continue
            sys.exit()
    elif um == "N" or um == "No":
        print("Wow. okay. You scared me there for a second.* (Press enter when you see: *)")
        wait()
        print("You know, that's a really mean joke to play on someone who just wants to entertain you with their game. You're lucky I'm so forgiving.*")
        wait()
#in case input is not yes or no, i assume they want to play becuase i worked hard on this and they're going to play
else:
    print("That's not a good answer. However, I'm going to assume you meant to say yes. Here we go!* (Press enter when you see: *)")
    wait()
#using a delayed printing method so played can see stats wihtout being overwhelmed by all of it at once
time.sleep(.25)
frosh.stats()
time.sleep(.25)
soph.stats()
time.sleep(.25)
jun.stats()
time.sleep(.25)
sen.stats()
time.sleep(.25)
tec.stats()
time.sleep(.25)
red = input("What grade do you want to be in? Choose wisely, your stats are actually important and may help or hinder your gaming experience. freshman/sophomore/junior/senior/teacher ").title()
#setting the person's choice to their stats, using the empty variable "you"
if red == "Freshman":
    you = frosh
elif red == "Sophomore":
    you = soph
elif red == "Junior":
    you = jun
elif red == "Senior":
    you = sen
elif red == "Teacher": #the end of the joke. not the only joke though, don't worry
    print("")
    print("Bruh.*")
    wait()
    print("This game is about being a Magnet STUDENT. What are you doooing??*") #see it is a joke. i tried my best to make myself laugh ok
    wait()
    print("You just had to be special, huh? Too bad. Game over.*")
    sys.exit()
#security blanket in case ipout is not one of the options i set
else:
    print("No. That input wasn't good, so I don't care what you actually want. Now you're a freshman.")
    red = "Freshman"
    you = frosh
print("")
#finally starting the actual game, 200 lines in
#explaining that the game will be a text based RPG type game, based on the decisions of the player
#aka a lot of if statements
print(f"Alright, {red}! Do you think you can survive a day as a Magnet student? I don't either, but let's try anyway.*")
wait()
print("")
print("The point of the game is to make the right decisions in the situations I present to you. Any time you make the right decision, I reward you with a number of win poits, depending on the situation.*")
wait()
print("Make the wrong decision, however, and you lose a number of win points. Trust me, it's a lot easier to lose points that it is to gain them.*")
wait()
print("The goal is to end the game with at least 10 win points. Here's a freebie for you. You're probably going to need it. Good luck!*")
#player's win points aka you.win_points is increased by 1 b/c i'm generous
you.win_points += 1
wait()
#the first decision of the user, their wake up time
wake = int(input("Pick a number between 1 and 10: "))
if 1<= wake <=4:
    print("")
    print(f"You're wake up at {wake} o'clock! You’re so sleepy by the time you get to school, you fall asleep in class and get in trouble! Minus 2 win points.*")
    #no matter what decision they make, their win points are alerted
    you.win_points -=2
elif 5<= wake <= 7:
    print("")
    print(f"You woke up at {wake} o'clock! Right on time to get to school! Good job! Plus 3 win points.*")
    you.win_points +=3
elif 8<= wake <=10:
    print("")
    print(f"What a disgrace, you woke up at {wake} o'clock. Way too late to get to school on time! Minus 2 win points.*")
    you.win_points -=2
elif 0>= wake or wake >10:
    #hopefully a deterrent for the player to not follow instructions. also, a joke.
    print("")
    print("I just said to pick a number between 1 and 10. How hard is it to follow simple instructions? Just for that, you woke up at 10 and were late to school. If you had originally chosen 10, you would still be late but would only lose 2 points.*")
    wait()
    print("But you just had to be special. You're incapable of following instructions. So, congrats. You now have -100 points. Feel free to keep on playing, but you are incapable of winning.*")
    you.win_points -=101
    wait()
    delay("......Sigh.*")
    wait()
    print("")
    #does the player want to try again and not be a failure?
    failure = input("Do you want to try again? (y/n) ").title()
    print("")
    if failure == "Y" or failure == "Yes":
        promise = input("Okay, but can you promise to actually follow the istructions this time? (y/n) ").title()
        if promise == "Y" or promise == "Yes":
            print("")
            print("Fine. You're on thin ice, but i'm awarding you 95 win points. You're still starting lower than you would have if you had FOLLOWED INSTRUCTIONS, but you still have a chance. Feel free to play on.*")
            you.win_points +=95
        elif promise == "N" or promise == "No":
            print("")
            print("Fine. Coward.*")
            wait()
            sure = input("Are you absolutely positive? y/n ").title()
            #literally this entire if statement is me just trolling the player
            if sure == "Y" or sure == "Yes":
                print("That's sad. Now I'm sad. You happy? I'm crying now. I'm drowning in my tears becuase you won't promise to follow the instructions of my game.*")
                wait()
                print(f"Goodbye. Game over.*")
                wait()
                sys.exit()
            else:
                print("Too bad. You already made your choice. I'm not letting you play my game if you change your mind so easily.*")
                wait()
                print("That's right. Game over.*")
                wait()
                print("Nah, I'm just kidding. I wouldn't be so mean.*")
                wait()
                print("No, I'm not kidding at all. I would be so mean.*")
                wait()
                sys.exit()
    else:
        print("You really don't want to play, huh?*")
        wait()
        print("Fine. Then I don't want you to play, either. Bye bye.*")
        wait()
        sys.exit()
wait()
#the publishing of the player's updated score
print(f"You now have {you.win_points} win points. You will get updates like this after every challenge you complete, so you won't have to track your points yourself.*")
wait()
print("The bell starts belling. You're about to enter your first class when you remember you forgot your binder in your locker.*")
wait()
#next if statement. the results vary based on the player's input
locker = input("You go up to get it, but do you remember your combination? (y/n) ").title()
if locker == "Y" or locker == "Yes":
    #this time, the user's won points come from their stats as well as their decision
    if you.intelligence_points > 5:
        print("")
        print("You're right, you do. You get your stuff and head to class, getting there just in time for the announcements to start. Plus 1 win point.*")
        you.win_points +=1
    #if the player's intelligence is lower than 5, but their number of friends are above or equal to 5
    #(basically if the player chooses to be a sophomore, because they are the only ones who could get this option)
    elif you.intelligence_points < 5 and you.friend_points >= 5:
        print("")
        print("Yeah, um, no you don't. Your intelligence isn't high enough for that. Sorry.*")
        wait()
        print("However, your friends know how forgetful you can be and memorized it for you. What great friends they are!*")
        wait()
        print("You cut it close, but you get your binder and get to class on time. However, you don't get any win points. Remember your combo next time.*")
    else:
        #me being mean if the player's intelligence is less than 5 and their friends are less than 5
        #(me being mean to the freshman in the game basically)
        print("")
        print("LOL no you don't. Stop lying to yourself, your intelligence isn't high enough for you to remember this kind of stuff. Did you at lease write it down?*")
        wait()
        print("Don't bother checking. You didn't. You're not smart enough to remember the combo, you really think you'd be intelligent enough to think to write it down?*")
        wait()
        print("What about a friend? Do they know your combo?*")
        wait()
        print("Nope. You don't have many friends, and none of them know your combo. You're screwed. You get to class late. Your binder is still stuck in your locker. Minus 2 win points.*")
        you.win_points -=2
#if the player says that they don't remember their combo
elif locker == "N" or locker == "No":
    if you.intelligence_points >5:
        print("")
        print("What are you talking about? You're definitely smart enough to remember something as simple as your combo. Get your stuff and stop doubting yourself.*")
        wait()
        print("You don't get any win points for this, even though you succeeded. Be more confident in yourself next time!*")
    elif you.friend_points > 5:
        print("")
        print("You're right, you don't remember it. Luckily, one of your very good friends knows it, and helps you open your locker. You get your binder and get to class on time. The power of friendship! Plus 1 win point.*")
        you.win_points +=1
    else:
        print("")
        print("Yeah, you don't remember your combo, but that's okay. You can just get it from the office later. Trust me, you won't need it for this class. Don't beat yourself up, okay? Here, have a win point, to make yourself feel better.*")
        you.win_points +=1
wait()
print(f"You now have {you.win_points} win points.*")
wait()
#next challenge, not based on any player decision, but their stats alone
print("Guess what? You've got a test! You don't even need that precious binder you spent so much time trying to get! Perfect way to start the day, sucker!*")
wait()
#subtracting or adding a number of points to the player's win points based on their intelligence
#giving them a statement about why they lost/gained points
if you.intelligence_points == 2:
    print("Oh, poor little freshman, you forgot to study last night. You hand in the test knowing you failed. Minus 4 win points.*")
    you.win_points -=4 #i really hate the freshmen, don't i? i promise i don't
elif you.intelligence_points == 4:
    print("Oh, you sophomore, you. You didn’t study last night. Thankfully you paid attention in class, so you kinda knew what you were doing. You still got a C, though. Minus 2 win points.*")
    you.win_points -=2
elif you.intelligence_points == 6:
    #ha like anyone would actually do their timeline instead of studying
    print("Congrats, junior. You actually remembered to study last night. But you were so caught up with Sansi’s timeline you didn’t study that well. You got a B, but you know you could’ve done better. Plus 2 win points.*")
    you.win_points += 2
elif you.intelligence_points == 8:
    print("Since you’re a highly intelligent senior, you knew everything on that test. You aced it, good job! Plus 3 win points.*")
    you.win_points +=3
wait()
print(f"You now have {you.win_points} win points. *")
wait()
print("The class goes on, but you're getting really tired. You just took a test, okay. How in the world are you supposed to stay awake?*")
wait()
#if statement with a really weird variable name
seven = input("You're not. So here's the deal, do you want to struggle to keep your eyes open or just go to sleep? awake/sleep ").title()
#if the player decides to stay awake like a good student
if seven == "Awake":
    print("")
    print("But you're so tireddddd. You fight your hardest to keep your eyes open, being a good student and paying attention to your boring teacher.*")
    wait()
    print("Turns out your teacher was just going to review everything you were just tested on for the rest of class. There was absolutely no need for you to stay awake.*")
    wait()
    print("Good job, goody two shoes. Minus 2 win points.*")
    wait()
    #update the score
    you.win_points -=2
#if the user decides to take a nap
elif seven == "Sleep":
    print("")
    print("Good idea. You've dealt with a lot so far. You need a break.*")
    wait()
    print("What a fantastic nap. And the greatest part, your friend tells you that your teacher literally did nothing but review the stuff you just got tested on. You got away scot-free!*")
    wait()
    print("Just for that, plus 3 win points! You deserve it!*")
    #i do not usually promote sleeping in class nor have i ever done it
    #because that is very bad and i would never do it
    wait()
    #updating score
    you.win_points +=3
print(f"You now have {you.win_points} win points.*")
wait()
#me not wanting to come up with a cool new way for them to win points
print(f"Alright, class is over! You're lucky, too. You just watch a movie in your next class. What a perfect little break for you. You deserve it, after that test. Plus 1 win point.*")
#updating the score and the user
you.win_points += 1
wait()
print(f"You now have {you.win_points} win points.*")
wait()
#asking if the player brought or bought their lunch to school that day
lunch = input("Lunch time! Did you bring lunch or are you going to buy it? (bring/buy) ").title()
print("")
#making the user aware that bringing lunch is obviously superior to walking allll the way to the caf and buying lunch every day
if lunch == "Bring":
    print("Your lunch is a little cold, but at least you don't have to walk alllllll the way to the cafeteria. Plus 2 win points.*")
    you.win_points +=2
#or if they do decide to buy lunch
elif lunch == "Buy":
    print("None of your friends want to go to the cafeteria with you. You're going to have to walk there all by yourself. Looking like a loser with no friends. Through the very crowded quad.*")
    wait()
    #their points depend on their self esteem stats
    #if their self esteem is above 5
    if you.self_esteem_points <5:
        print("You're way too self conscious right now to look like a loser. Your self esteem is pretty low. You should get that checked out. Anyway, you don't want to look like a loser, so you go hungry instead. What a smart decision. Minus 1 win point.*")
        you.win_points -=1
    #if their self esteem isn't above 5
    elif you.self_esteem_points >5:
        print("Literally who cares if people think you're a loser. Go get that lunch! Plus 4 win points!*")
        wait()
        #using the delay function to make the situation extra awkward for the user
        delay("...um*")
        wait()
        print("")
        print("Yeah... um... you forgot your money....... Good job.. Minus 3 win points.*")
        you.win_points +=1
wait()
print(f"You now have {you.win_points} win points.*")
wait()
#reminding people of sansi, basically
print("7/8 starts, and right off the bat your teacher announces a pop quiz you're totally unprepared for. Hope your stress doesn't keep you from doing well!*")
wait()
#basically the only time the underclassmen can win based on stats alone
#if the player's grade's stress is below 5
if you.stress_points <5:
    print("You actually were good on the stress. Sure, you were unprepared, but you were calm enough that you could take the quiz wihtout double guessing yourself. Plus 3 win points.*")
    you.win_points += 3
#if they're a normal Magnet student with more stress than humanly possible
else:
    print("Yeah. You stressed out way too much. You needed an A in this class, but it doesn't look like you're going to get it now. Sorry. Minus 3 win points.*")
    #yeah like 1 pop quiz would drop my grade that much. surrrrreee anna that makes total sense.
    you.win_points -= 3
wait()
print(f"You now have {you.win_points} win points.*")
wait()
attention = input("The bell rings, and you go to 9/10. But your teacher is just sooooooooo boring. Do you want to zone out or keep paying attention? zone/pay ").title()
#asking if the player wants to go to sleep in class again, wondering if they'll change their answer based on results given earlier in the game
if attention == "Zone":
    print("")
    print("Yeah, you're right. Who needs to pay attention in class? It sucks, you're bored, so why not take a nap instead?*")
    wait()
    print("Your teacher looks around the room at all the bored faces. Their eyes land on you. You remain unaware as they stalk closer to you.*")
    wait()
    #more sansi vibes
    print("Your teacher asks you a question. You are unable to answer. You fail the class instantly. Minus 2 win points.*")
    wait()
    you.win_points -=2
elif attention == "Pay":
    print("")
    print("You struggle to stay awake, but you do in the end. Good perseverance.*")
    wait()
    print("Your teacher looks around the room at all the bored faces. Their eyes land on you. You become slightly frightened as they stalk towards you.*")
    wait()
    print("They stop in front of you. They ask a question. Hesitantly, you answer, and though shaky, you get it correct. Good job. If you hadn't paid attention, your teacher would totally hate you.*")
    #this enitre game just shows how traumatized i am from sansi. except i don't think i'm that traumatized
    wait()
    print("Your teacher smiles at you. They're so grateful you were paying attention. Plus 2 win points.*")
    wait()
    you.win_points +=2
print(f"You now have {you.win_points} win points.*")
wait()
#finishing the school day, but not releasing the player from the torture that is this game
print("School is over! Yay! But the game's not done!*")
wait()
#asking how the player wants to get home
home = input("Do you take the bus home, drive, or walk? bus/drive/walk ").title()
if home == "Drive":
    print("")
    #if they said they drive home, asking if they carpool with others or not
    car = input("Okay,but do you carpool with friends or just go straight home? carpool/home ").title()
    #if they go straight home
    if car == "Home":
        print("")
        print("You go straight home. There's an accident on the road and it take you 15 extra minutes to get home because of it.*")
        wait()
        print("That's a little inconvenient, sure, but you deal with it.*")
        wait()
        print("Minus 1 win point, though.*")
        wait()
        you.win_points -=1
    #if they carpool
    elif car == "Carpool":
        print("")
        print("You have to wait an extra 10 minutes for your friends to get ready to go.*")
        wait()
        print("Which makes you so late to get to your car, you get stuck behind all the buses leaving the parkig lot.*")
        wait()
        print("Plus, once you do get on the road, there's an accident that causes you to have to go 30 minutes out of your way to drop your friends off.*")
        wait()
        print("And then another 15 minutes to get home. Minus 2 win points.*")
        wait()
        you.win_points -=2
#if they decide to take the bus
elif home == "Bus":
    print("")
    print("Your bus leaves on time, but there's an accident on the road near the school, which makes your driver a little impatient.*")
    wait()
    print("Though you have to go 15 minutes out of your way to get home, your bus driver is so impatient that they speed.*")
    wait()
    print("You end up getting home 5 minutes earlier than usual! Yay speeding! Plus 1 win point.*")
    wait()
    #an important message to the easily influenced youth
    print("Make sure to actually follow the rules of the road, though.")
    wait()
    you.win_points +=1
#if the player decides to walk home
elif home == "Walk":
    print("")
    print("You walk home. As you get out of campus, you notice an accident on the road near school.*")
    wait()
    print("Good thing you walked home, or you would have been stuck behind that accident for a while!*")
    wait()
    print("Plus 2 win points.*")
    wait()
    you.win_points += 2
#updating the player on their score
print(f"You now have {you.win_points} win points.*")
wait()
print("As you walk into your house, you feel your phone buzz.*")
wait()
#ooh, powerschool update! asking if the player wants to check their phone
grades = input("Oh look, an update from PowerSchool! Do you want to check it? y/n ").title()
if grades == "Y" or grades == "Yes":
    print("")
    print("You open up PowerSchool and wait for it to load.*")
    wait()
    print("")
    delay("...Oof.*")
    wait()
    #their points earned/lost depend on their self esteem
    if 5 <= you.self_esteem_points:
        #if ther self esteem is high, I'm much nicer
        print("Your grades weren’t the best, but your self esteem is high enough that you can take this hit and still survive.*")
        wait()
        print("Don’t worry, it’ll get better! Plus 1 win point.*")
        wait()
        you.win_points +=1
    #if not, then i'm the meanest person on the planet
    elif 5 >= you.self_esteem_points:
        print("Your grades were awful, as to be expected from you.*")
        wait()
        print("Your self esteem is so low and this was just the final push to realizing you suck. Minus 3 win points.*")
        wait()
        you.win_points -=3
#if they don't want to check they get off the hook and win the most points out of the other choices
else:
    print("")
    print("That’s fine, it was probably a good idea not to anyway. Your grades would just depress you, and you know it. Plus 2 win points.*")
    wait()
    you.win_points +=2
print(f"You now have {you.win_points} win points.*")
wait()
print("The day's almost done!*")
wait()
#i wish it was friday every day and the player definitely does, too
print("T.G.I.F, am I right?*")
wait()
#the message as to why they have to study changes based on whether or not they have a lot of friends
if you.friend_points >=5:
    print("Here’s the thing, though. Because you have so many friends, your weekend is packed with plans, and you won’t have much time to do any work, even though you have a test on Monday.*")
    wait()
    study = input("Well? Do you want to study now? y/n ").title()
    #asking if the player wants to be responsible
    #if they decide to be responsible
    if study == "Yes" or study == "Y":
        print("")
        print("Wow, how responsible of you! You’re really the epitome of good, hardworking Magnet students. Plus 2 win points.*")
        wait()
        you.win_points +=2
    #if they want to procrastinate
    else:
        print("")
        print("Yeah, you’re right. Fridays are for laying around doing nothing.*")
        wait()
        #luring them into a false sense of security so i can slam them later on at the very end
        print("Besides, this game is about surviving a day at Magnet, and ends before Monday, it’s not like this means anything.*")
        wait()
#basically the same options as before but with slight tweaks to the text so it is never the exact same experience
else:
    print("")
    print("Here’s the thing, though. You don’t have a lot of friends, so you have nothing to do.*")
    wait()
    #does anyone ever really want to be responsible though? i sure don't
    study = input("However, you do have a test on Monday. Do you want to study now? y/n ").title()
    print("")
    if study == "No" or study == "N":
        print("You’re right! That’s what weekends are for, after all! Procrastinate now.*")
        wait()
        print("Besides, this game ends is about surviving a day at Magnet, and ends before Monday, it’s not like this means anything.*")
        wait()
    else:
        print("Bruh you're so responsible you're making me look bad.*")
        wait()
        print("But it's fine. Good for you, really. You're the epitome of good, hardworking Magnet students. Plus 2 win points.*")
        wait()
        you.win_points +=2
print(f"You now have {you.win_points} win points.*")
wait()
print("It's almost time for you to go to sleep! You've got an early morning tomorrow, so you've got to choose a time to go to sleep!*")
wait()
#asking when the player wants to go to sleep
tired = int(input("Choose a number between 1 and 12. "))
#they get between 1 and 3 hours of sleep
if 1<= tired <=3:
    print("")
    print(f"You only got {tired} hours of sleep!*")
    wait()
    print("You know that teens are supposed to get between 8 to 10 hours of sleep a night, right?*")
    wait()
    print("This really isn't healthy. You should change your habits. As an incentive to get more sleep at night, I'm subtracting 5 win points.*")
    wait()
    print("And yes, I know, if you're going for the authentic Magnet experience, choosing to get less than 3 hours of sleep was the right decision.*")
    wait()
    print("It's still not healthy, but I'll add back 2 win points for accuracy.*")
    you.win_points -=3
#or they get between 4 and 6 hours of sleep
elif 4<= tired <= 6:
    print("")
    print(f"You got {tired} hours of sleep.*")
    wait()
    print("You do realize it's the weekend, right? You should be trying to catch up on all the sleep you lost during the week.*")
    wait()
    print("Plus, you know you're supposed to get between 8 to 10 hours as a teenager, right?*")
    wait()
    print("You're a couple hours short of that. Minus 1 win point.*")
    wait()
    you.win_points -=1
#or between 7 and 9 hours of sleep
elif 7<= tired <=9:
    print("")
    print(f"You got {tired} hours of sleep, good for you! (I haven't gotten that much sleep in months)*")
    wait()
    print("Good job, you, with your healthy habits. Plus 3 win points.*")
    wait()
    you.win_points +=3
    envy = input("I'm jealous. Tell me, in real life, do you actually get that much sleep on the regular? y/n ").title()
    #me being a troll because it doesn't matter what they say they still lose points
    #but if they say yes
    if envy == "Y" or envy == "Yes":
        print("")
        print("Seriously, good for you.*")
        wait()
        print("Minus one point because of my jealousy.*")
        wait()
        you.win_points -=1
    #or if they say no, or any other input
    else:
        print("")
        print("Oh, okay. So you lied to the game, huh?*")
        wait()
        print("Lying isn't a good character trait. You should change that. Minus 1 win point.*")
        you.win_points -=1
#if they get between 10 and 12 hours of sleep
elif 10<= tired <= 12:
    print("")
    print(f"Dang, you got {tired} hours of sleep. Impressive. I haven't gotten that much sleep since I was born.*")
    wait()
    print("Congrats. I'm jealous of your healthy habits. Plus 5 win points.*")
    wait()
    jealous = input("Though, tell me, in real life, do you actually get that much sleep on the regular? y/n ").title()
    #more of me trolling the player
    #again, if they say yes
    if jealous == "Y" or jealous == "Yes":
        print("")
        print("Wow. Really? Good for you.*")
        wait()
        print("Minus two points because you made me jealous.*")
        wait()
        you.win_points -=2
    #if they say no, they lose the same amount of points
    else:
        print("")
        print("Oh, okay. So you lied to the game, huh?*")
        wait()
        print("Lying isn't a good character trait. You should change that. Minus 2 win points.*")
        wait()
        you.win_points -=2
#if they went outside the recommended input of 1 to 12
else:
    #i love being a troll
    #so if they answered outside of the recommended inputs for when they wanted to wake up
    #i yell at them
    if 0>= wake or wake >10:
        print("")
        print("Again?? You didn't learn from the first time? You know how annoyed I got the first time, so you decided to test me again?*")
        wait()
        print("You buttmunch. Minus 10 win points.*")
        wait()
        you.win_points -=10
    #if this was their first offense
    else:
        print("")
        print("Okay, you were supposed to pick a number between 1 and 12. You decided to defy the rules that I clearly expressed to you.*")
        wait()
        print("Minus 5 win points. Follow the rules next time.*")
        wait()
        you.win_points -=5
print(f"You now have {you.win_points} win points.*")
wait()
print("Before you go to sleep, you feel a bunch of buzzes from your phone.*")
wait()
print("You scroll down, and at the bottom, oh look, another notification from PowerSchool! You open your phone.*")
wait()
#delaying the text to make it extra Dramatic™
delay("...This is your phone screen: *")
wait()
#i don't give them a choice. they automatically lose 5 points because i hate them
#not really but the powerschool took a while to get correct so they have to watch it
print("""
 _______________________________________________
|   __________                                  |
|  |  _ ___   |                                 |
|  | | |   \  |                                 |
|  | | | |) ) |                                 |
|  | | |___/  |                                 |
|  | | |      |                                 |
|  | |_|      |                                 |
|  |__________|                                 |
|                                               |
|       PowerSchool is temporarily shut down.   |
|       Please check back in 2 weeks,           |
|       even though it’ll actually              |
|       only open a month later.                |
|                                               |
|                                               |
|       (Sucker.)                               |
|                                               |
|                                               |
|                                               |
|                                               |
|                                               |
|       (Minus 5 win points.)                   |
|_______________________________________________|
""")
you.win_points -=5
print(f"You now have {you.win_points} win points.*")
wait()
print("Oh, and before you get your final score, do you remember that test you've got on Monday?*")
wait()
#if they decided not to study i yell at them again
if study == "No" or study == "N":
    print("Remember how I said the game ended before Monday and therefore whether or not you studied didn’t matter?*")
    wait()
    print("I lied.*")
    wait()
    print("You failed it. Good job.*")
    wait()
    #haha here i hate them. and i deter them from not being responsible
    print("Minus another 4 win points. Hope you didn't need them to win the game.*")
    wait()
    you.win_points -=4
#if they decided to study i am merciful
else:
    print("Congrats, you studied hard and didn’t have to cram on Sunday, making it easier and less stressful to study.*")
    wait()
    print("You’re going to do so well on that test!*")
    wait()
    print("Plus another win point, just because you deserve it.*")
    wait()
    you.win_points +=1
#finishing the game and telling them how many points they ended with
print(f"You finished the game with {you.win_points} win points.*")
wait()
print("")
#if they ended with more than 10 points, they won!
if you.win_points >=10:
    if red == "Freshman":
        #if they chose to be a freshman, they extra won because it was definitely the hardest level
        print("Congratulations, I'm so proud of you for beating my game!*")
        wait()
        print("Why don't you try beating it again, but on a harder level?*")
        wait()
        #Suspense™
        delay("...Slight problem*")
        wait()
        print("So it kinda appears like being a freshman is the hardest level you can choose.*")
        wait()
        print("So now I'm even more proud of you! WHy don't you try again, but on an easier level? Or you can experiment more with your answers and see if you can still win.*")
        wait()
        print("Either way, I hope you have a good day. Bye!*")
        wait()
        sys.exit()
    #if they originally chose an easier level but still won
    else:
        print("Congratulations, I'm so proud of you for beating my game!*")
        wait()
        print("You can choose to play on a harder level, if you want. It's not exact, but it is definitely harder to win as a younger grade.*")
        wait()
        print("Well, hope you have a good day! Bye!*")
        wait()
        sys.exit()
#if they lost, but not by a lot
elif 5<= you.win_points >=9:
    print("You were so close!*")
    wait()
    print("Well then, I know that I'm pretty competitive, and I would be super pissed to play this entire game and then lose because of Powerschool.*")
    wait()
    bonus = input("Well then, do you want to play a bonus level for some extra credit? y/n ").title()
    print("")
    #asking if the player wants to play the bonus round to get the points they need to win
    #if they don't want the points and are okay with failing
    if bonus == "No" or bonus == "n":
        print("Oh, so I guess you're fine with being a failure.*")
        wait()
        print("That's not very Magnet of you. In fact, it's so unlike a Magnet student, you don't deserve to win it.*")
        wait()
        print("Get out of my game. Now.*")
        wait()
        sys.exit()
    #if they are willing to try the bonus level
    elif bonus == "Y" or bonus == "Yes":
        print("Good luck, okay?*")
        wait()
        print("The bonus level is going to be hard. It might even be a litle scary. But you're sure you want this?*")
        wait()
        scared = input("You can back out right now if you want. Do you want to? I won't judge. y/n ").title()
        print("")
        #i give them a way out in case they get scared
        if scared == "Y" or scared == "Yes":
            #again, i am a troll
            print("I lied. I'm judging you really hard.*")
            wait()
            print("Goodbye, coward. Hope you like living your cowardly life. As long as it's far away from me, I'll be happy.*")
            wait()
            sys.exit()
        #if they are brave enough to take the challenge
        else:
            print("Okay, if you're absolutely sure.*")
            wait()
            print(f"Good luck, brave {red}. You will need copious amounts of it.*")
            print("")
            #running the opening fuction
            extra_o()
            #since each function returns True when the player's answer is correct
            #if the 1 question is ansered correctly,
            if extra1() is True:
                #then it goes into the second function
                #if that is answered correctly,
                if extra2() is True:
                    #then it goes into the third and final function for the player
                    if extra3() is True:
                        #if the player was correct, they get 5 extra points and win the game
                        print("")
                        you.win_points += 5
                        delay(f"Congratulations. You earned 5 extra win points from that excursion. You now have {you.win_points}, enough to win the game!*")
                        wait()
                        delay("Feel free to play the game again on a harder level, if you feel up to it. Have a good day!*")
                        wait()
                        sys.exit()
                    #if they got the 3rd question wrong, i express my disappointment
                    else:
                        delay("You lost. You were so close to the end, too. Guess you should learn more about my reading tastes.*")
                        wait()
                        delay("Goodbye, loser.*")
                        wait()
                        sys.exit()
                #if they got the 2nd quesiton wrong, i tell them the answer after expressing my disappoingment in them
                else:
                    delay("You lost. How dare you not know Sanservino's birthday? Disappointing.*")
                    wait()
                    delay("It's December 23, 1976, by the way.*")
                    wait()
                    delay("Goodbye, you disgrace.*")
                    wait()
                    sys.exit()
            #if they get the 1st question, they are a failure
            else:
                delay("You lost. And on such a simple question, too? Obviously his name is Jason. Disappointing.*")
                wait()
                delay("Goodbye.*")
                wait()
                sys.exit()
#if the player ended between 0 and 4 points
elif 0<= you.win_points >=4:
    #i am mean
    print(f"Ha, you suck. You only got {you.win_points}?*")
    wait()
    print(f"You do realize I gave you like 20 chances to score points, right? And you still only got {you.win_points}.*")
    wait()
    credit = input("Do you want some extra credit? y/n ").title()
    print("")
    #i ask if they want to play the extra credit
    if credit == "Y" or credit == "Yes":
        print(f"Good luck, {red}. You will need copious amounts of it.*")
        wait()
        #same thing as earlier in the code
        #it plays the opening, then, if they answer correctlly to all the questions, they win
        #if not, they lose and get a message displaying the answer and insulting them
        extra_o()
        if extra1() is True:
            if extra2() is True:
                if extra3() is True:
                    if extra_h1() is True:
                        if extra_h2() is True:
                            if extra_h3() is True:
                                #they won! even with 3 more extra hard questions
                                print("")
                                you.win_points +=10
                                delay(f"Congratulations. You earned 10 extra win points from that excursion. You now have {you.win_points}, enough to win the game!*")
                                wait()
                                delay("Feel free to play the game again on a harder level, if you feel up to it. Have a good day!*")
                                wait()
                                sys.exit()
                            else:
                                delay("Congratulations!*")
                                #me = troll
                                wait()
                                delay("You lost. On the very last question. My name is Anna Maddalena O'Connell, by the way.*")
                                wait()
                                delay("You're a disappointment. Goodbye.*")
                                wait()
                                sys.exit()
                        else:
                            delay("It is supercalifragilisticexpialidocious. Good job, learn how to spell.*")
                            wait()
                            delay("Buy a dictionary, and get out of my game.*")
                            wait()
                            sys.exit()
                    else:
                        delay("Stop what you're doing right this instant.*")
                        wait()
                        delay("You don't know Pip??*")
                        wait()
                        delay("Get off my game right this second. Google Tiny Headed Kingdom. You won't be disappointed.*")
                        wait()
                        sys.exit()
                else:
                    delay("You lost. You were so close to the end, too. Guess you should learn more about my reading tastes.*")
                    wait()
                    delay("Goodbye, loser.*")
                    wait()
                    sys.exit()
            else:
                delay("You lost. How dare you not know Sanservino's birthday? Disappointing.*")
                wait()
                delay("It's December 23, 1976, by the way.")
                wait()
                delay("Goodbye.")
                wait()
                sys.exit()
        else:
            delay("You lost. And on such a simple question, too? HIs name is Jason, obviously. Disappointing.*")
            wait()
            delay("Goodbye.*")
            wait()
            sys.exit()
    else:
        print("Wow. You're comfortable with failing, then?*")
        wait()
        ("That's not very Magnet of you. goodbye, coward.*")
        wait()
        sys.exit()
#lastly, if they lose the game so compltely that they end with negative points
elif you.win_points < 0:
    print("You absolute disgrace.*")
    wait()
    print("I am so ashamed of you right now.*")
    wait()
    print("Everyone else who played either won or was offered enough extra credit to win.*")
    wait()
    print("You, on the other hand? You don't get that option.*")
    wait()
    print("Failures don't get to pass my game. Suffer.*")
    you.win_points -=100
    print("Also, because I felt like it, I subtracted 100 more points. To make you an extra failure.*")
    wait()
    print(f"You now have {you.win_points}. Loser. Bye.*")
    wait()
    sys.exit()