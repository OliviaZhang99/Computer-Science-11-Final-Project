# Olivia Kelli
# Import tkinter for GUI
import tkinter as tk

# Import random to pick words
import random

# Import time to time the test
import time


# -----------------------------
# Constants (easy to change)
# -----------------------------

# Font for most text
FONT = ("Arial", 12)

# Bigger font for the title
FONT_TITLE = ("Arial", 16, "bold")

# Padding values
PAD_Y = 6
PAD_X = 8

# How many words per test
WORDS_PER_TEST = 25


# -----------------------------
# Word lists (no files, no json)
# -----------------------------

# Easy words
WORDS_EASY = [
    "book", "they", "begin", "little", "around", "need", "any",
    "head", "than", "seem", "call", "she", "how",
    "leave", "off", "find", "if", "get", "skill", "learn", "smile", "point", "flash"
    "sea", "see", "house", "hole", "wash", "hand", "each", "baby", "phone", "flask"
    "chord", "food", "game", "jump", "kite", "lamp", "moon", "nest", "owl", "pig", "queen", 
    "rat", "sun", "tree", "van", "wolf", "xray", "yarn", "zebra", "ant", "ball", "cat", "dog", "egg", 
    "fan", "goat", "hat", "ice", "jar", "key", "log", "map", "net", "oak", "pan", "quilt", 
    "red", "sit", "top", "urn", "vase", "wig", "zip", "banana", "apple", "grape", "orange", "peach",
    "pear", "plum", "mango", "melon", "kiwi", "lime", "cherry", "berry", "coconut", "date", "fig", "guava", 
    "hand", "jelly", "lemon", "nut", "olive", "papaya", "quince", "raisin", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten", "red", "blue", "green", "yellow", "purple", "orange", "black", "white", "gray", "pink", 
    "brown", "cyan", "magenta", "silver", "gold", "bronze", "circle", "square", "triangle", "rectangle", "oval", "star", "heart", 
    "diamond", "arrow", "cloud", "rain", "snow", "sun", "wind", "storm", "fog", "hail", "lightning", "thunder", 
    "river", "mountain", "forest", "desert", "ocean", "island", "valley", "canyon", "waterfall", "beach", "cliff", "cave", 
    "field", "meadow", "glacier", "volcano", "jungle", "swamp", "marsh", "lagoon", "reef", "delta", 
    "bay", "gulf", "cape", "peninsula", "isthmus", "plateau", "prairie", "savanna", "tundra", "steppe", 
    "jacket", "shirt", "pants", "shoes", "socks", "hat", "gloves", "scarf", "belt", "tie", "dress", "skirt", "sneakers", "boots", 
    "sandals", "slippers", "suit", "uniform", "apron", "cape", "hood", "pyjamas", "robe", "vest", "watch", "bracelet", "necklace", "ring",
    
]

# Medium words
# Kelli, delete those words just put in random words, dont have to be cs related.
# BUDDY< JUST USE RANDOM WORD GE NERA i like thinking of random words 
# Fuck you thenwhat is fun bro like the words that come to mind or its in front of me
WORDS_MEDIUM = [
    "keyboard", "computer", "potato", "development", "interface", "performance",
    "accuracy", "increase", "challenge", "practice", "improvement", "develop", "learning",
    "volcano", "calculator", "extinguisher", "cylinder", "mathematics", "children", "master", "minimum", 
    "horror", "dramatic", "professional", "sanitizer", "backpack", "participants", "terminal",
    "keyboard", "dramatic", "professional", "sanitizer", "backpack", "participants", "terminal",
    "social", "mountain", "chemistry", "winter", "summer", "alarm", "brother", "exercise", "monopolies", 
    "onomatopoeia", "platinum", "quarantine", "sphinx", "tattoo", "vortex", "waltz", "xylophone", "pronunciation"
    "necessary", "intelligence", "spaghetti", "consciousness", "vacuum", "lightning", "contagious",
    "exaggerate", "fluorescent", "psychology", "restaurant", "basketball", "friendship", "adventure",
    "butterfly", "chocolate", "dinosaur", "elephant", "fireworks", "giraffe", "helicopter",
    "imagination", "jellyfish", "kangaroo", "lighthouse", "motorcycle", "nightmare", "orchestra",
    "pineapple", "quicksand", "rollercoaster", "spaceship", "tornado", "unicorn", "volleyball", 
    "waterfall", "yesterday", "zookeeper", "alligator", "balloon", "caterpillar", "dolphin", "earthquake",
    "fountain", "grasshopper", "hurricane", "jigsaw", "koala", "labrador", "marshmallow", "nectarine",
    "octopus", "popsicle", "quokka", "rhinoceros", "saxophone", "toothbrush", "umbrella", "vegetable",
    "whirlpool", "xenophobia", "yogurt", "zeppelin", "adventure", "bicycle", "carnival", "dandelion", "evergreen",
    "earrings", "crown", "tiara", "glasses", "sunglasses", "backpack", "purse", "wallet", "briefcase", "luggage", "umbrella",
    "camera", "phone", "tablet", "laptop", "desktop", "monitor", "keyboard", "mouse", "printer", "scanner", 
    "speaker", "headphones", "microphone", "charger", "cable", "adapter", "router", "modem", "projector", "television", 
    "radio", "clock", "calendar", "map", "compass", "flashlight", "binoculars", "telescope", "microscope", "thermometer", 
    "barometer", "seismometer", "anemometer", "hygrometer", "altimeter", "speedometer", "odometer", "tachometer", 
    "fuel", "engine", "brake", "steering", "wheel", "tire", "axle", "chassis", "transmission", "radiator",
    "battery", "exhaust", "suspension", "clutch", "differential", "ignition", "carburetor", "catalyst", "muffler", "windshield", "headlight"
    "perservance", "quarantine", "entrepreneur", "camouflage"
]

# Hard words
# This one too, aim around 100 words each if possible
WORDS_HARD = [
    "synchronization", "implementation", "characteristic", "responsibility", "configuration",
    "interpretation", "communication", "approximation", "compatibility", "visualization", "pomegrante", "mangosteen"
    "architecture", "authentication", "specification", "optimization", "determination", 
    "transformation", "representation", "administration", "documentation", "identification",
    "international", "mathematical", "environmental", "organizational", "philosophical",
    "psychological", "technological", "unconstitutional", "extraordinary", "incomprehensible",
    "disproportionate", "misinterpretation", "counterproductive", "overqualification", "hyperventilation",
    "photosynthesis", "neurotransmitter", "electromagnetic", "thermodynamics", "microenvironment",
    "bioluminescence", "cybersecurity", "neuroplasticity", "psychopharmacology", "radiotelemetry", 
    "spectrophotometer", "thermoregulation", "transcendental", "vulnerability", "weatherization",
    "xenotransplantation", "youthfulness", "zoogeographical", "conceptualization", "decontamination",
    "electroencephalogram", "gastroenterological", "heterogeneousness", "immunohistochemistry",
    "jurisprudential", "kaleidoscopically", "lexicographically", "microarchitectural", "neurodegenerative",
    "ophthalmologically", "psychosomatically", "quasiperiodically", "radiocontractility",
    "spectrophotometrically", "thermoelectrically", "ultramicroscopically", "voluntaristically", 
    "weatherproofing", "xerophthalmias", "yesteryear's", "zoophilously", "antidisestablishmentarianism",
    "floccinaucinihilipilification", "pseudopseudohypoparathyroidism", "thyroparathyroidectomized",
    "hepaticocholangiogastrostomy", "spectrophotofluorometrically", "psychoneuroendocrinological", 
    "radioimmunoelectrophoresis", "immunoelectrophoretically", "electroencephalographically",
]


# -----------------------------
# App state (globals)
# -----------------------------

# Current difficulty
difficulty = "easy"

# Current target text the user must type
target_text = ""

# Start time of the typing test (seconds)
start_time = 0.0

# True when a test is running
test_running = False

# Simple leaderboard list (in memory only)
# Each item: (name, wpm)
leaderboard = []


# -----------------------------
# Bunch of defs
# -----------------------------

# Pick the correct list based on difficulty
def get_word_list():
    # If easy, return easy list
    if difficulty == "easy":
        return WORDS_EASY
    # If medium, return medium list
    if difficulty == "medium":
        return WORDS_MEDIUM
    # Otherwise, return hard list
    return WORDS_HARD


# Make the target text (WORDS_PER_TEST words)
def make_target_text():
    # Get the right list
    words = get_word_list()

    # If list is smaller than WORDS_PER_TEST, just reuse it safely
    if len(words) < WORDS_PER_TEST:
        # Make a copy by building a new list
        temp = []
        for w in words:
            temp.append(w)
        # Keep adding random words until we have enough
        while len(temp) < WORDS_PER_TEST:
            temp.append(random.choice(words))
        # Join them into a string
        return " ".join(temp)

    # Pick WORDS_PER_TEST random words (no repeats if possible)
    picked = random.sample(words, WORDS_PER_TEST)

    # Join list into one string with spaces
    return " ".join(picked)


# Count correct characters compared to target (simple CS11 loop)
def count_correct_chars(typed, target):
    # Start counters
    correct = 0

    # Compare up to the shorter length
    limit = len(typed)
    if len(target) < limit:
        limit = len(target)

    # Loop through each character
    i = 0
    while i < limit:
        # If chars match, add to correct
        if typed[i] == target[i]:
            correct = correct + 1
        i = i + 1

    # Return number correct
    return correct


# Calculate WPM using the common formula: (correct_chars / 5) / minutes
def calculate_wpm(correct_chars, seconds):
    # Avoid dividing by zero
    if seconds <= 0:
        return 0

    # Convert seconds to minutes
    minutes = seconds / 60

    # Calculate words typed (5 chars = 1 word)
    words_typed = correct_chars / 5

    # Calculate WPM
    wpm = words_typed / minutes

    # Return rounded number
    return round(wpm)


# Update the leaderboard display labels
def refresh_leaderboard():
    # Clear the leaderboard text box
    leaderboard_box.config(state="normal")
    leaderboard_box.delete("1.0", tk.END)

    # Copy leaderboard into temp list
    temp = []
    for item in leaderboard:
        temp.append(item)

    # Selection sort by WPM (highest first)
    sorted_list = []
    while len(temp) > 0:
        best_index = 0
        i = 1
        while i < len(temp):
            if temp[i][1] > temp[best_index][1]:
                best_index = i
            i = i + 1

        sorted_list.append(temp[best_index])
        temp.pop(best_index)

    # Only show top 10
    shown = 0
    for item in sorted_list:
        if shown >= 10:
            break
        name = item[0]
        wpm = item[1]
        leaderboard_box.insert(tk.END, name + " - " + str(wpm) + " wpm\n")
        shown = shown + 1

    # Lock the box again
    leaderboard_box.config(state="disabled")


# -----------------------------
# Button commands
# -----------------------------

# Set difficulty to easy
def set_easy():
    global difficulty
    difficulty = "easy"
    difficulty_label.config(text="Difficulty: easy")


# Set difficulty to medium
def set_medium():
    global difficulty
    difficulty = "medium"
    difficulty_label.config(text="Difficulty: medium")


# Set difficulty to hard
def set_hard():
    global difficulty
    difficulty = "hard"
    difficulty_label.config(text="Difficulty: hard")


# Start the typing test
def start_test():
    global target_text, start_time, test_running

    # Make sure test is not already running
    if test_running == True:
        return

    # Create new target text
    target_text = make_target_text()

    # Show target text on screen
    target_display.config(state="normal")
    target_display.delete("1.0", tk.END)
    target_display.insert("1.0", target_text)
    target_display.config(state="disabled")

    # Clear the typing box
    input_box.delete(0, tk.END)

    # Show that Start was clicked
    message_label.config(text="Test started! Type now.")

    # Change Start button text so user sees it worked
    start_btn.config(text="Running...", state="disabled")

    # Set start time
    start_time = time.time()

    # Mark running
    test_running = True

# Finish the typing test and show results
def finish_test():
    global test_running

    # If no test is running, do nothing
    if test_running == False:
        message_label.config(text="Click Start first.")
        return

    # Get what user typed
    typed = input_box.get()

    # End time
    end_time = time.time()

    # Total seconds
    seconds = end_time - start_time

    # Count correct chars
    correct_chars = count_correct_chars(typed, target_text)

    # Calculate wpm
    wpm = calculate_wpm(correct_chars, seconds)

    # Accuracy (based on target length)
    # Avoid dividing by zero
    if len(target_text) == 0:
        accuracy = 0
    else:
        accuracy = round((correct_chars / len(target_text)) * 100)

    # Show results
    message_label.config(
        text="Time: " + str(round(seconds, 1)) + "s | WPM: " + str(wpm) + " | Accuracy: " + str(accuracy) + "%"
    )

    # Add to leaderboard if a name exists
    name = name_entry.get().strip()
    if name != "":
        leaderboard.append((name, wpm))
        refresh_leaderboard()

    # Reset Start button so it can be used again
    start_btn.config(text="Start", state="normal")


    # Stop running
    test_running = False


# -----------------------------
# Build the GUI (tkinter only)
# -----------------------------

# Create the main window
root = tk.Tk()

# Set title
root.title("Typing Test (CS11)")

# Set minimum size
root.minsize(700, 600)


# Title label
title_label = tk.Label(root, text="Typing Test", font=FONT_TITLE)
title_label.pack(pady=PAD_Y)

# Name entry area
name_frame = tk.Frame(root)
name_frame.pack(pady=PAD_Y)

name_label = tk.Label(name_frame, text="Name:", font=FONT)
name_label.pack(side="left", padx=PAD_X)

name_entry = tk.Entry(name_frame, font=FONT, width=18)
name_entry.pack(side="left", padx=PAD_X)


# Difficulty area
diff_frame = tk.Frame(root)
diff_frame.pack(pady=PAD_Y)

difficulty_label = tk.Label(diff_frame, text="Difficulty: easy", font=FONT)
difficulty_label.pack(side="left", padx=PAD_X)

easy_btn = tk.Button(diff_frame, text="Easy", font=FONT, command=set_easy)
easy_btn.pack(side="left", padx=PAD_X)

medium_btn = tk.Button(diff_frame, text="Medium", font=FONT, command=set_medium)
medium_btn.pack(side="left", padx=PAD_X)

hard_btn = tk.Button(diff_frame, text="Hard", font=FONT, command=set_hard)
hard_btn.pack(side="left", padx=PAD_X)


# Target text display (read-only Text widget)
target_display = tk.Text(root, height=6, width=60, font=FONT)
target_display.pack(pady=PAD_Y)

target_display.config(state="disabled")


# Input area
input_label = tk.Label(root, text="Type here:", font=FONT)
input_label.pack(pady=PAD_Y)

input_box = tk.Entry(root, font=FONT, width=60)
input_box.pack(pady=PAD_Y)


# Buttons area
btn_frame = tk.Frame(root)
btn_frame.pack(pady=PAD_Y)

start_btn = tk.Button(btn_frame, text="Start", font=FONT, command=start_test)
start_btn.pack(side="left", padx=PAD_X)

finish_btn = tk.Button(btn_frame, text="Finish", font=FONT, command=finish_test)
finish_btn.pack(side="left", padx=PAD_X)


# Message / results label
message_label = tk.Label(root, text="Click Start to begin.", font=FONT)
message_label.pack(pady=PAD_Y)


# Leaderboard area
leader_label = tk.Label(root, text="Leaderboard (Top 10)", font=FONT_TITLE)
leader_label.pack(pady=PAD_Y)

leaderboard_box = tk.Text(root, height=8, width=40, font=FONT)
leaderboard_box.pack(pady=PAD_Y)

leaderboard_box.config(state="disabled")


# Run the tkinter loop
root.mainloop()
