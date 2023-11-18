## Current Systems
### Definition:
`system` is any object that is responsible for: 
* Facilitating a single action (i.e. Combat, Trade, Diplomacy, etc.) 
* Processing interactions between objects implementing a given system.

### Planned Systems
* Pawn stats
    * This system would be an interface to all other components/systems for a given pawn.
    * The following components will live here:
        * Health
        * Offense
        * Defense
        * Modifiers

* Pawn Combat
    * System responsible for managing pawn level engagements.
* Civilization
    * System responsible for:
        * Managing/tracking **all Civilizations**.
        * Manages relationships between Civilizations.
        * Facilitates combat between Civilizations.
        * 

* Movement
    * System responsible for handling movement, and keeping track of pawn positions.
* Reputation
    * System responsible for managing Player pawn reputation and facilitating the getting/setting of reputation.
    * Civilizations will use this systems information to decide how to treat the Player pawn.

## Current Components

### Health
### Offense
### Defense
### Modifiers