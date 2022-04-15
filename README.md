# Clash of Clans



I display the village base using ascii chart. The base.render() function is called again and again in game.py in order to display the base (rendering the changes that have taken place).  The timeout for input is set to 0.5 seconds. I have used the OOPS concepts (Polymorphism, Encapsulation, Inheritance and Abstraction) to deliver the required functionalities.

## Village

- Spawning points:
  There are 3 spawing points for the troops(barbarians):
  i - (6,9)
  j - (10,45)
  k - (20,10)

- Town Hall:
  Coordinates: (50,25)
  Height: 4
  Width: 3
  Hitpoints: 300

- Huts:
  Width: 1
  Height:1
  Hitpoints: 40
  There are 5 huts in total around the corners of the village.

- Cannons:
  Coordinates: (20,30), (30,40)
  Width: 1
  Height: 1
  Hitpoints: 60
  Damage: 20
  The cannon attacks troops within a raduis of 5. It targets a single troop until it dies or goes out of range. The time delay for shooting is 0.5 second.

- Walls:
  Width: 1
  Height: 1
  Hitpoints: 30
  Walls are present around the townhall and the two cannons.  

All the buildings change in colour based on their hitpoints. Once the hitpoints become 0, they disappear from the village base. Walls only have one colour and they disappear when destroyed.

## King

Coordinates: (5,6)
Width: 1
Height: 1
Hitpoints: 200
damage=20
The king is spwaned at the beginning of the game at the specified coordinates.
The king's health is displayed by a health bar.

Movement:
The King is controlled with W/A/S/D which correspond to Up/Left/Down/Right.
<SPACE> is used for sword attack. The King attacks a single building with a sword when he is in contact with the building. In case of multiple buildings in contact, the priority order to attack is: Townhall > Cannons > Hut > Wall.
The movement of the King is restricted, i.e. he cannot move through the buildings unless they are destroyed.

'l' is used for leviathan axe attack where the king can attack any building within the radius of 7.



## Barbarians


Width: 1
Height: 1

Hitpoints: 50
Damage: 5


The movement and attack is automated.
Time delay for action: 0.5 seconds


## Spells

1. Rage: 
   Number: 1
   Time: 5 seconds
   Increases the damage of all the troops by two.
   Increases the movement speed of the king by two.
   Decreases the time delay of action for barbarians to 0.25 seconds.
   The village base colour turns light green when the rage spell is in effect.

2. Heal:
   Number: 1
   Increases the health of all the troops(king and barbarians) to 150% of the current health.
   

## Game Endings
Each game can end in either victory or defeat.
1. Victory: All buildings (excluding walls) have been destroyed.
2. Defeat: All troops and the King have died without destroying all buildings.
Once either of these conditions is satisfied, the game ends and appropriate message is displayed.


