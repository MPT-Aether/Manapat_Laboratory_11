# Entering of Inputs & Lists
Word_Count = 0
List_of_Words = []
Printed_List = []
Amount_Letter_Input = int(input("Please enter the minimum amount of letter count you want to be classified: "))

while Word_Count < 10:
    Words_Input = input("Please enter a word: ")
    List_of_Words.append(Words_Input)
    Word_Count += 1

for letters in List_of_Words:
    if len(letters) >= Amount_Letter_Input:
        Printed_List.append(letters)     
    
print(Printed_List)


input()