#Adam Kimmins
#Final Project
#IT 140

#showing instructions
def show_instructions():
    print("\n---_-_-_--- THE RELICS OF RAGNAROK ---_-_-_---")
    print("Goal: Collect all six relics before facing Jormungandr.")
    print("Move commands- Type: North, South, East, or West")
    print("Add to Inventory- Type: take the 'item name'")
    print("Type 'Exit' at any time to abandon your quest.\n")

#to show current status, made as a def to reference neatly in main loop
def show_status(current_room, inventory, rooms):
    print(f"\nYou are in the {current_room}.")
    print(f"Inventory: {inventory}")
    if 'item' in rooms[current_room]:
        print(f"You see {rooms[current_room]['item']}.")
    else:
        print("There is nothing of value here.")
    print("_---" * 11 + "_")

#Here is my dictionary, using rooms and their matching keys - 'exampleroom': {'South': 'Southroom'} etc
rooms = {
    'Asgard Hall': {'South': 'Midgard Village', 'East': 'Alfheim Glade'},
    'Alfheim Glade': {'West': 'Asgard Hall', 'item': 'the Light of Freyr'},
    'Midgard Village': {'North': 'Asgard Hall', 'South': 'Helheim Depths', 'East': 'Svartalfheim Forge', 'item': 'the Shield of Aesir'},
    'Svartalfheim Forge': {'West': 'Midgard Village', 'item': 'the Dwarven Hammer'},
    'Helheim Depths': {'North': 'Midgard Village', 'East': 'Vanaheim Grove', 'item': "the Spearhead of Odin"},
    'Vanaheim Grove': {'West': 'Helheim Depths', 'South': 'Jotunheim Peaks', 'item': 'the Golden Apple of Idunn'},
    'Jotunheim Peaks': {'North': 'Vanaheim Grove', 'East': 'Midgard Ruins', 'item': "the Frost Giants Helm"},
    'Midgard Ruins': {'West': 'Jotunheim Peaks', 'item': 'Jormungandr'}
}
#I've added in item keys also on top of directions for the next step in my program

# set the current player "info"
current_room = 'Asgard Hall'
inventory = []
game_over = False
required_items = 6

# call def from start to make program more readable, cleaner, etc
show_instructions()

#Start Game Loop
while not game_over:

    # every time the loop starts, it displays your updated information
    show_status(current_room, inventory, rooms)

    # I use direction to make the input line shorter
    # I clarify that I only want to display the possible directions and not "item" aswell
    # I also remove case sensitivity from previous line
    directions = [key for key in rooms[current_room].keys() if key.lower() in ['north', 'south', 'east', 'west']]
    player_input = input(f"Enter a direction ({', '.join(directions)}) or 'Exit' to quit: ").strip().lower()

    # kill switch
    if player_input == 'exit':
        print("You abandon your quest. Odin’s voice fades off into silence...")
        game_over = True

#I start with introducing an exit or kill switch for the game, before moving on to the actual game input

    elif player_input.capitalize() in rooms[current_room]:
        # using rooms[][] I'm able to make the new_room variable
        new_room = rooms[current_room][player_input.capitalize()]
        # Here I use the players input to determine their next room using the dictionary I made
        print(f"You traveled {player_input.lower()} and entered {new_room}.")
        # since my loop uses current_room, I make sure to set its value = to new_room
        current_room = new_room


#Now I add in the ability to "take" the relics

    elif player_input.startswith('take '):
        item_name = player_input[5:].strip().lower()
        # I use .lower and reference my item key after removing characters 0-4 ("take ")
        if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == item_name:
            # add to the inventory variable
            inventory.append(rooms[current_room]['item'])
            # announce adding item successfully to player
            print(f"\nYou took {rooms[current_room]['item']}!")
            # remove the item from the dictionary, as it's been moved to players inventory
            del rooms[current_room]['item']
        else:
            print("\nThere is nothing like that here.\n")

    # for wrong input
    else:
        print("The Norse winds block your path! Choose another direction.\n")

#end scenarios for the final room

    if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Jormungandr':
        # announce finale
        print("\nYou enter the lair of the great serpent Jormungandr!")

        # win
        if len(inventory) == required_items:
            print("\nYou wield all six relics. The great serpent Jormungandr falls before your might!")
            print("Congratulations, warrior, you have restored balance to the realms!")

        # lose
        else:
            print("\nJormungandr rises before you! You are unprepared and swallowed whole.")
            print("CRUNCH CRUNCH ... YOU TASTE LIKE FISH")
        game_over = True

#End Game
print("\nThe game has ended. Farewell, warrior.")
