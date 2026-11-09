"""
Function to attack enemy
"""
def attack(action):
    if action == "Fire":
        print("-->")
    elif action == "Stay":
        print("Stayed")

"""
Check body condition
"""

def body(condition):
    if condition < 5:
        print("Danger")
    elif condition < 10:
        print("Your health is fine")
    else:
        print("Stay sharp! ")

