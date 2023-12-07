
#Create a Python file named lab_8-7.py

#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Using the nested list rows from the "Nested Data" slide, write a function that prints each person's name 
names = [["Darick", "Eugene", "Kyle", "Azaan"], ["Ryan","Phil", "Eman", "Alex", "Nicholas"],["Christian", "Josh", "Matt", "Francesco"],["Patrick", "Nico", "Trevayne"]]

def sans(rows):
    for row in rows:
        for name in row:
            print (name)
            
def papyrus(rows):
    for row in rows:
        for name in row:
            name += "'s" if name[len(name)-1] != "s" else "'"
            print(name)
            
sans (names)
print("---------------------------------------------------------------------")
papyrus(names)
#BONUS: Make each name be possessive. Remember, if a name ends in s, only add an apostrophe. If the name does not end in s, add, 's.