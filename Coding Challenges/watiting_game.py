"""Challenge Requirements
- When function is run, it should first print a message for them to wait a random number of time, between 2-4 seconds.
- When the player presses enter, that starts a timer.
- The player then must press enter again when they think the given number of seconds has passed.
- The elapsed time is then displayed and a message indicates whether the player was too fast, too slow or right on target."""

import random # For generating a random goal for the player
import time # To gain functionality to measure elapsed time


def waitingGame():
    secondsGoal = random.randrange(2,5)
    
    # Prompt user to start the game
    input(f"Welcome to the waiting game!\nYour goal is to wait {secondsGoal} seconds, press ENTER to start the timer and ENTER again to stop it. Good luck!")
    start = time.perf_counter()

    # Stop the timer with second ENTER press
    input("Timing...")
    end = time.perf_counter()

    # Calculate the elapsed time
    elapsedTime = round(end - start, 2)
    print(elapsedTime)

    # Calculate difference for comparison
    difference = elapsedTime - secondsGoal
    # Analyze the result
    if difference == 0:
        print("Congrats! You got it perfect!")
    elif difference < -2 :
        print("Buddy... way too early!")
    elif difference < 0:
        print("That was close but just a bit too early.")
    elif difference > 2:
        print("Bruh, that was wayyy to late!")
    elif difference > 0:
        print("That was close but a litte too late")


waitingGame()