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
sen = Grade("Senior", 5, 7, 10, 8, 0)
you = ""
frosh.stats()
soph.stats()
jun.stats()
sen.stats()
red = input("What grade do you want to be in? ").title()
if red == "Freshman":
    you == frosh
elif red == "Sophomore":
    you = soph
elif red == "Junior":
    you == jun
elif red == "Senior":
    you == sen
else:
    print("No.")
print("Do you think you can survive a day at Magnet? I don't either, but let's try anyway.")