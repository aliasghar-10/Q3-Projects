# Countdown Timer in Python
import time

def countdown_timer():
    print("Welcome to the Countdown Timer!\n")

    # Get user input for the countdown duration
    try:
        total_seconds = int(input("Enter the countdown time in seconds: "))
        if total_seconds <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    print("\nStarting the countdown...\n")

    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        timer_display = f"{minutes:02d}:{seconds:02d}"
        print(timer_display, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("00:00")
    print("Time's up! 🚀")

# Run the timer
if __name__ == "__main__":
    countdown_timer()