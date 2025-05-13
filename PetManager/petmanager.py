import json


class Pet:
    def __init__(self, name, type, age, weight, health_status):
        self.name = name
        self.type = type
        self.age = age
        self.weight = weight
        self.health_status = health_status
        
    def __str__(self):
        return f"{self.name} ({self.type}), age: {self.age}, weight: {self.weight}, health: {self.health_status}"  
    
class PetManager:
    def __init__(self):
        self.pets = []
        
    def add_pet(self, pet):
        self.pets.append(pet)
        
    def list_pets(self):
        for pet in self.pets:
            print(pet)
            
    def remove_pet_by_name(self, name):
        for pet in self.pets:
            if pet.name.lower() == name.lower():
                self.pets.remove(pet)
                print (f"{name} has been removed.")
                return
        print(f"No pet found with the name {name}.")        
        
    def search_pets(self, keyword):
        found = False
        for pet in self.pets:
            if keyword.lower() in pet.name.lower() or keyword.lower() in pet.type.lower():
                print(pet)
                found = True
        if not found:
            print(f"No pets found matching '{keyword}'.")

    def save_to_file(self, filename="pets.json"):
        with open(filename, "w") as file:
            json.dump([pet.__dict__ for pet in self.pets], file, indent=4)
        print("Pets have been saved.")
        
    def load_from_file(self, filename="pets.json"):
        try:
            with open(filename, "r") as file:
                pet_list = json.load(file)
                self.pets = [Pet(**data) for data in pet_list]
            print("Pets have been loaded.")
        except:
            print("No save data found.")
        
# Make sure to define Pet and PetManager classes before this part

def show_menu():
    print("=== Pet Management System ===")
    print("1. Add a pet")
    print("2. List all pets")
    print("3. Delete a pet")
    print("4. Search pets")
    print("5. Exit")

# Create an instance of PetManager
manager = PetManager()
manager.load_from_file()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter pet's name: ")
        pet_type = input("Enter pet type (e.g. Cat, Dog): ")
        age = int(input("Enter pet age (in years): "))
        weight = float(input("Enter pet weight (in kg): "))
        health_status = input("Enter pet health status: ")
        
        new_pet = Pet(name, pet_type, age, weight, health_status)
        manager.add_pet(new_pet)
        
        print(f"{name} has been added successfully.")
             
    elif choice == "2":
        manager.list_pets()
    elif choice == "3":
        name_to_remove = input("Enter the name of the pet to remove: ")
        manager.remove_pet_by_name(name_to_remove)
    elif choice == "4":
        keyword = input("Enter keyword to search (name or type): ")
        manager.search_pets(keyword)
    elif choice == "5":
        manager.save_to_file()
        break
    else:
        print("Invalid option. Try again.")