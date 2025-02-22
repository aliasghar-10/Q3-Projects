# Mad Libs Game in Python

def mad_libs():
    print("Welcome to the Mad Libs Game: My Journey!\n")

    # Collect words from the user
    name = input("Enter your name: ")
    institute = input("Enter your institute name: ")
    starting_year = input("Enter the year you started your journey: ")
    field_of_study = input("Enter your field of study: ")
    goal = input("Enter your ultimate goal: ")
    memorable_moment = input("Enter a memorable moment in your journey: ")
    favorite_subject = input("Enter your favorite subject: ")
    inspiration = input("Who or what inspires you the most?: ")

    # Story template
    story = (
        f"My name is {name}, and I am a proud student of {institute}. My journey began in {starting_year} when I decided to pursue "
        f"{field_of_study}. From the very first day, I was determined to achieve my ultimate goal of {goal}.\n\n"
        f"One of the most memorable moments during this journey was {memorable_moment}. It made me realize how much I enjoy learning, "
        f"especially about {favorite_subject}. Through all the ups and downs, I have been consistently inspired by {inspiration}, "
        f"which keeps me motivated to push forward.\n\n"
        f"Looking back, I am grateful for every experience and lesson I have gained, and I look forward to achieving even greater "
        f"milestones in the future."
    )

    print("\nHere is your Mad Libs story:\n")
    print(story)

# Run the game
if __name__ == "__main__":
    mad_libs()