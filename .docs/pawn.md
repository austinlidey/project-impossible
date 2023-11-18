# Pawn
A Pawn is the object representation of any and all active characters in the game. It serves as the base class that can be decorated with different components/systems that are necessary for its intended purpose. 

## Important to note:

**Only one pawn object** can have the attribute `is_player` and that is reserved for the human player pawn. This is so that we can discern the player from NPC's.

## Pawn Base Attributes

What can the pawn do?
- ### Move around the world
    - Sprinting
    - **No jumping**
    - Simple swimming
    
- ### Interact with the world directly
    - Acquire resources from:
        - Trees
        - Rocks
        - Object destruction

- ### Interact with objects
    - Use items
        - Drink/eat food
        - Heal
    - Equip from dead pawns (cannot store)
    - Store/equip from containers
    - Store/equip to the world directly

- ### Interact with characters
    - Talk
    - Fight physically
    - Fight via element (fire, water, etc.)
    - Fight via gunfight
    - Loot

- ### Die