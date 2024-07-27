#1. Python Modules and Data Handling Assignment
#Task 1: Your Mood Today 

#mood_responses.py
def mood_response(mood):
    mood = mood.lower()
    responses = {
        "happy": "That's great to hear! Keep smiling!",
        "sad": "I'm sorry to hear that. I hope things get better soon.",
        "excited": "Awesome! Enjoy your excitement!",
        "angry": "Take a deep breath. It's important to stay calm.",
        "nervous": "It's normal to feel nervous. You've got this!"
    }
    return responses.get(mood, "I'm not sure how to respond to that mood.")

#main.py
import mood_responses

def main():
    mood = input("How are you feeling today? ").strip()
    print(mood_responses.mood_response(mood))

main()

#2. Mastering Python Modules and Aliases
#text_utils.py
def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

#main.py
import text_utils as tu

def main():
    text = input("Enter a string: ").strip()
    
    reversed_text = tu.reverse_string(text)
    capitalized_text = tu.capitalize_string(text)
    
    print(f"Reversed String: {reversed_text}")
    print(f"Capitalized String: {capitalized_text}")

if __name__ == "__main__":
    main()
