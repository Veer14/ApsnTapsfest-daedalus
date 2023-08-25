import os
import sys
import textwrap
from tabulate import tabulate
from ascii import *

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


architecture_data = {
    "Doric Column": "The Doric order is characterized by its simple, sturdy design...",
    "Ionic Column": "The Ionic order is known for its taller, more slender columns...",
    "Corinthian Column": "The Corinthian order features intricate capitals...",
}

def display_menu_arch():
    clear_screen()
    print("Explore Greek Architecture\n")
    print(tabulate(architecture_data.items(), headers=["Architecture", "Description"], tablefmt="fancy_grid"))
    c = input("\nEnter your choice: ")
    return c

def explore_architecture():
    display_menu_arch()
    choice=display_menu_arch()

    if choice=="1":
        print("""The Doric order is known for its simplicity and sturdy look.
The column shaft is usually thicker and heavier, resting directly on the stylobate (the platform on which the columns stand) without a separate base.
The capital is simple, with a plain, cushion-like molding known as the echinus and a square abacus (a flat slab) on top.
The entablature consists of a plain architrave, a frieze adorned with triglyphs (vertical bands with three vertical grooves) and metopes (spaces between the triglyphs that can be sculpted), and a simple cornice.""")
        print(doric)
        
    if choice=="2":
        print("""Characterized by slender, fluted columns with a base at the bottom.
The capital (top part of the column) features scroll-like ornaments known as volutes.
The entablature consists of an architrave, a frieze with continuous sculpted decorations, and a cornice.""")
        print(ionic)
        
    if choice=="3":
        print("""The Corinthian order is the most ornate and decorative of the three.
The column shaft is slender and fluted, often resting on a decorative base similar to the Ionic order.
The capital is intricately adorned with acanthus leaves, creating a lush and elaborate design. It can also feature small volutes on its corners.
The entablature follows a similar pattern to the Ionic, with an architrave, a frieze, and a more decorative cornice.""")
        print(cornithian)
