from mythology import dive_into_mythology
import os
import sys
import textwrap
import nltk
from tabulate import tabulate
from nltk.sentiment import SentimentIntensityAnalyzer
from architecture import explore_architecture
from modern_society import explore_modern_impact, display_menu_mod, main2


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_menu():
    clear_screen()
    print("Welcome to Greek Odyssey!")
    print("1. Explore Greek Architecture")
    print("2. Dive into Greek Mythology")
    print("3. Impact on Modern Society")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice



def main():
    display_menu()
    choice = display_menu()
    if choice == "1":
        explore_architecture()
    elif choice == "2":
        dive_into_mythology()

    elif choice == "3":
        main2()

    elif choice == "4":
        clear_screen()
        print("Thank you for exploring Greek Odyssey!")
        sys.exit()
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
