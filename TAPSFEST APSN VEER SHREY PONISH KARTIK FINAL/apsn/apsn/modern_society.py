import os
import sys
from tabulate import tabulate
from ascii import *
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Sample modern impact data related to Greek mythology
modern_impact_data = {
    "1. Cultural Impacts": "Greek mythology has greatly influenced culture...",
    "2. Impacts on Linguistics": "Many English words and phrases have roots in Greek...",
    "3. Architectural Impacts": "Ancient Greek buildings have had a profound impact...",
    "4. Philosophical Impacts": "Philosopher's ideas laid groundwork for ethics...",
    "5. Mythological Impacts": "Greek myths explore human nature, morality..."
}

def display_menu_mod():
    clear_screen()
    print("Welcome to Modern Impact of Greek Mythology!")
    print("1. Explore Modern Impacts")
    print("2. Another Option")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def explore_modern_impact():
    clear_screen()
    print("Explore Modern Impact of Greek Mythology\n")
    print(tabulate(modern_impact_data.items(), headers=["Topic", "Description"], tablefmt="fancy_grid"))
    choice2 = input("Select a topic to learn more about (e.g., Arts and Literature): ")
    return choice2
    printOptions()
#    if choice2 in modern_impact_data:
#        display_topic_info(choice2)
#    else:
#        print("Invalid choice.")
#    input("\nPress Enter to continue...")
def printOptions():
    explore_modern_impact()
    temp = explore_modern_impact()
    if temp == "1":
        print("""Movies:

Clash of the Titans (1981, 2010): Both the original and the remake draw heavily from Greek mythology, featuring characters like Perseus, Medusa, and Zeus. The architectural aesthetics, with grand temples and mythical landscapes, help transport viewers into the ancient world.

300 (2006): This film showcases the Battle of Thermopylae between the Greeks and Persians. It's not only known for its stylized visuals but also for its use of Greek architectural elements in creating the Spartan city of Sparta, reinforcing the cultural and historical backdrop.

3)Percy Jackson & the Olympians: The Lightning Thief (2010): Based on the popular book series, the movie follows a modern teenager with ties to Greek mythology. The movie uses Greek architectural designs and mythological creatures to create a visually engaging world.

TV Shows:

1)Class of the Titans (2005-2008): This animated series follows a group of modern-day teenagers who are descendants of Greek heroes and are tasked with preventing mythological villains from escaping the Underworld. The show blends ancient Greek mythology with contemporary settings and challenges.

2)The Iliad (1971): A British TV miniseries adaptation of Homer's epic poem "The Iliad," this show brings the Trojan War to life, showcasing the architecture and landscapes of ancient Greece as a backdrop to the conflict.

3)Atlantis (2013-2015): A fantasy drama series set in the mythical city of Atlantis, drawing inspiration from various Greek myths. The show's architecture and visual design capture the essence of ancient Greece.
Video Games:""")
    elif temp == "2":
        print("""1)Vocabulary Enrichment:
Greek mythology has supplied numerous words and names that are widely used in modern languages. These words often carry nuanced meanings and resonate with cultural significance. For instance, terms such as "narcissism" (derived from the myth of Narcissus) and "chronology" (rooted in the concept of "Chronos," the god of time) have become integral to psychology and historical studies respectively. These borrowed words provide succinct ways to convey complex ideas.

2)Idioms and Metaphors:
Greek myths and symbols are fertile ground for creating idiomatic expressions and metaphors that enrich language. Phrases like "Achilles' heel" (referring to a vulnerability) and "Pandora's box" (alluding to the release of unforeseen troubles) encapsulate broader concepts through mythological references, enhancing linguistic depth and nuance.

3)Symbolism and Allegory:
Greek mythology offers a rich source of symbols and allegories that can be seamlessly integrated into modern linguistic contexts. These symbols often carry universal significance, transcending linguistic and cultural barriers. For instance, the Phoenix, a mythical bird associated with rebirth, continues to symbolize renewal and transformation in various languages and cultures.

4)Influence on Naming Conventions:
Greek mythology has influenced the naming conventions of various entities, from celestial bodies to medical terminology. Planets, constellations, and galaxies often bear the names of mythological figures, reflecting their attributes and stories. In the medical field, terms like "hypnosis" (linked to Hypnos, the god of sleep) and "psychology" (stemming from "psyche," the soul) reveal the pervasive influence of Greek mythology on specialized vocabulary""")
    elif temp == "3":
        print("""ARCHITECTURAL IMPACT

Ionic, Doric, and Corinthian are three distinct architectural styles used in Ancient Greece and later in Roman architecture. These styles pertain to the design of columns and their corresponding entablatures (the horizontal elements supported by the columns) in classical buildings

Ancient Greek buildings like the Parthenon and the Acropolis have had a profound impact on modern architecture. Their emphasis on symmetry, proportion, and the use of columns and entablatures as design elements has influenced the development of neoclassical architecture and continues to inspire contemporary architects seeking timeless and elegant design principles. The harmonious blend of aesthetics and functionality in these ancient structures serves as a foundation for architectural creativity, bridging the gap between the past and present in the world of design.

Greek architectural elements have left an indelible mark on global architecture through their enduring principles of harmony, proportion, and aesthetic balance. From the iconic use of columns in neoclassical buildings in Europe and the United States to the replication of Greek temples in grand government structures and museums worldwide, the legacy of Greek design can be seen in facades, column styles, and decorative motifs. This influence reflects the universal appeal of Greek architecture's timeless elegance and its incorporation into diverse cultural contexts across the globe.""")
        
        print("Parthenon: \n\n\n\n")
        print(parthenon)
        print("Temple of Artemis: \n\n\n\n")
        print(artemis)

    
    elif temp == "4":
        print("""PHILOSIPHICAL IMPACT

Foundation of Ethics: Plato's emphasis on virtue and Aristotle's focus on moral virtues shaped modern ethical theories, influencing discussions on character, values, and the pursuit of the good life.

Concept of Virtue Ethics: Both philosophers' ideas laid the groundwork for virtue ethics, emphasizing personal character over rule-based ethics, resonating in modern discussions on moral excellence and human flourishing.

Teleological Ethics: Aristotle's teleological approach, emphasizing the purpose or end of actions, continues to inspire modern ethical theories centered on consequences, goals, and the ethical evaluation of outcomes.

Freedom of Speech: The ancient Athenian commitment to open dialogue and free expression continues to influence discussions on freedom of speech, censorship, and the importance of diverse perspectives in a democratic society.

Aesthetics and Art: Greek concepts of beauty, harmony, and proportion still shape debates in art, architecture, and design, emphasizing the enduring impact of classical aesthetics on modern creations.""")
    elif temp == "5":
        print("""Greek myths have profoundly shaped modern literature, art, movies, and even everyday language, weaving their timeless themes and archetypal characters into the fabric of contemporary culture. These myths explore human nature, morality, destiny, and the relationships The sculptural idealism of ancient Greek statues continues to influence modern artistic representations of the human form, emphasizing grace, proportion, and ideal beauty.

Movies frequently draw from Greek myths to infuse their stories with depth and resonance. The 1981 film "Clash of the Titans" and its 2010 remake center on Perseus' quest to save Andromeda, bringing gods and monsters to life on the big screen. Marvel's "Thor" comics and films draw inspiration from Norse mythology but incorporate elements of Greek mythology as well, merging the ancient and the contemporary.

Even in everyday language, references to Greek myths are abundant. Phrases like "Pandora's box" (symbolizing unleashing unforeseen troubles) and "Achilles' heel" (signifying a vulnerable point) stem from these tales. Words like "narcissistic" (from Narcissus, who fell in love with his own reflection) and "herculean" (denoting immense strength, after the demigod Hercules) are part of everyday discourse.""")
    else: 
        print("Invalid Choice")
#def display_topic_info(topic):
#    clear_screen()
#    print(f"Modern Impact of Greek Mythology - {topic}\n")
#    # Placeholder text for topic information
#    topic_info = "This is a placeholder text providing detailed information about the topic."
#    print(topic_info)
#    input("\nPress Enter to go back...")

def main2():
    display_menu_mod()
    choice = display_menu_mod()
    if choice == "1":
        printOptions()
    elif choice == "2":
        pass
    elif choice == "3":
        clear_screen()
        print("Thank you for exploring the modern impact of Greek mythology!")
        sys.exit()
    else:
        print("Invalid choice. Please select a valid option.")


if __name__ == "__main2__":
    main2()
