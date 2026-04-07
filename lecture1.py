profession = input("choose your profession-")

print ("hello", profession)

print ("if your chosen profession is related to")
print("1. Engineer")
print("2. Doctor")
print("3. Scientist")
print("4. Teacher")
print("5. Entrepreneur")
print("6. PCS Services")
print("7. Any Govt service")

pick = input("Enter your choice-")
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
elif pick == "5":
    print("choose problem of society and try to fix it")
elif pick == "6":
    print("get a graduate degree in any field and prepare for pcs examination and qualify it") 
elif pick == "7":
    print("fulfill the need of the particular exam and prepare for it and qualify all those needs and get into service")


print("If you have further query related to your profession in future")

pick = input("Do you have another question? (yes/no): ")  

if pick == "no":
    print("Thanks to give your valuable time")

elif pick == "yes":
    print("what is your question")

ask = input("Do you want any other profession? (yes/no): ")

if ask == "no":
    print("Thanks to give your valuable time")

elif ask == "yes":
    print("Sorry we will update our system soon")

else: 
    print("invalid choice start choosing with 1,2,3,4,5,6,7")

