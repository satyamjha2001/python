#9. Pet Food Recommendation
#Problem: Recommend a type of pet food based on the pet's species and age.
#Example: Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food.

species = input("Enter pet species (Dog/Cat): ")
age = float(input("Enter pet age in years: "))
if age <=0:   
    print("Invalid age. Please enter a valid age.")
    exit()

if species == "dog" or species == "Dog":
    if age < 2:
        recommendation = "Puppy food"
    elif age <= 5:
        recommendation = "Adult dog food"
    else:
        recommendation = "Senior dog food"
elif species == "cat" or species == "Cat":
    if age < 2:
        recommendation = "Kitten food"
    elif age <= 5:
        recommendation = "Adult cat food"
    else:
        recommendation = "Senior cat food"
else:
    if age < 2:
        recommendation = "Young pet food"
    elif age <= 5:
        recommendation = "Adult pet food"
    else:
        recommendation = "Senior pet food"

print(f"Recommended food: {recommendation}")
