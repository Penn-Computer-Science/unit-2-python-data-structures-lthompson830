import pandas as pd
bnames = ["Noah", "Liam", "Jacob", "Willism", "Mason", "Ethan", "Michael", "Alexander", "James", "Elijah"]

gnames = ["Emma", "Olivia", "Sophia", "Isabella", "Ava" "Mia", "Abigail", "Emily", "Charlotte", "Madison"]

bFreq = [183330, 173981, 163266, 159945, 157875, 149082, 145171, 142142, 139652, 137093]

gFreq = [195028, 184528, 181132, 170559, 155884, 129088, 118712, 119626, 102470, 98419]

df = pd.DataFrame({'Boys Names': bnames, 'bFreq': bFreq, 'Girls names': gnames, 'gFreq': gFreq}) 

print(df)