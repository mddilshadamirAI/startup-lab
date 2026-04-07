#ask name of costumer 

name = input("Enter Your Name-")

print ("Welcome,", name.title())
# ask what his goal 
print("what is your goal")

print("1. Engineer")
print("2. Doctor")
print("3. Scientist")
print("4. Teacher")

pick =input("Enter your choice-")
if pick == "1":
    print("Path 1: The Degree (Standard)")
    print("Graduate: 4-year ABET-accredited Engineering B.S.")
    print("Path 2: No Degree (Alternative)")
    print("Experience: Work 8-12 years in technical roles varies by state/country")
elif pick == "2":
    print("Path 1: The Degree (Standard)")
    print("text for doc")
    print("Path 2: No Degree (Alternative)")
    print("text for doc")
elif pick == "3":
    print("Path 1: The Degree (Standard)")
    print("qualify exam go to r and d ")
    print("Path 2: No Degree (Alternative)")
    print("very difficult next to impossible")
elif pick == "4":
    print("Path 1: The Degree (Standard)")
    print("complete bed or deled and qualify exam")
    print("Path 2: No Degree (Alternative)")
    print("train yourself in teaching and interact with children")
else:
    print("invalid choice lets start with 1 2 3 4")
print("Best of luck for your future")
print(" If you have any question contact us ")
print("                  [BYE]                        ")
print("i will be back")

