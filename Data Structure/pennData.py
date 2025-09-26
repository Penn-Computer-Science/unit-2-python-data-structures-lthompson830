import pandas as pd
import random

fNames = ["Mac", "Danielle", "Aiden", "Ben", "Van", "Kaden", "Lucian", "Andrew", "Benidict", "Keaton", "Joe", "Noah", "Rowman", "Kyan"]
lNames = ["Smith", "Jones", "Johnson", "Brown", "Latson", "White", "Thompson", "Moon", "Anderson", "Watkins", "James", "Watson", "Ronald", "Jacobson"]
years = ["Freshmen", "Sophomore", "Junior", "Senior", "Super Senior"]
pathways = ["Early Collage", "Engineering", "Computer Science", "Buisness", "Bio Med", "Construction"]
names = []

for i in range(20000):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")

print(names)

data = {
    "Name": names,
    "Age": [random.randint(14, 19) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.3),2) for _ in names],
    "Credits Completed": [random.randint(0, 60) for _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathway": [random.choice(pathways) for _ in names]
}

pennData = pd.DataFrame(data)
print(pennData)

students_df = pd.DataFrame(data)
students_df.to_csv('students_dat00.csv', index=False)