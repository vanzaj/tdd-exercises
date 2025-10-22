## Maze Model

Design a data structure to represent a **maze** using dictionaries and lists.
  - Each **room** in the maze has a name, which is a string.
  - Each place in the maze has one or more **people** currently standing at it, by name.
  - Each place in the maze has a maximum capacity of people that can fit in it.
  - From each place in the maze, you can go from that place to a few other places, using a direction like ‘up’, ‘north’, or ‘sideways’

Create an example instance, in a notebook, of a simple structure for your maze:
  - The front room can hold 2 people. James is currently there. You can go outside to the garden, or upstairs to the bedroom, or north to the kitchen.
  - From the kitchen, you can go south to the front room. It fits 1 person.
  - From the garden you can go inside to front room. It fits 3 people. Sue is currently there.
  - From the bedroom, you can go downstairs to the front room. You can also jump out of the window to the garden. It fits 2 people.

Make sure that your model:
  - Allows empty rooms
  - Allows you to jump out of the upstairs window, but not to fly back up.
  - Allows rooms which people can’t fit in.


Convert this to classes with necessairy properties and methods.

## Examples:

Given an initial maze with following rooms and people

livingrroom: James 
garden: Sue, Clare
bedroom: Bob

When

James goes north to the kitchen
Sue goes inside to the livingroom
Clare goes inside to the livingroom
Bob goes jump to the garden

Then

livingroom: Sue, Clare
kitchen: James
garden: Bob

When

Sue goes upstairs to the bedroom
Clare goes outside to the garden
James goes south to the livingroom
Bob goes inside to the livingrroom

livingroom: James, Bob
garden: Clare
bedroom: Sue

# Troll Treasure


A *dungeon* is a network of connected *rooms* on a square grid. One or more rooms contain *treasure*. Your character, the *adventurer*, moves between rooms, looking for the treasure. A *troll* is also in the dungeon and moves between rooms. If the troll catches the adventurer, you lose. If you find treasure before being eaten, you win. (In this simple version, we do not consider the need to leave the dungeon.)

The starting rooms for the adventurer and troll are given in the definition of the dungeon.

The way the adventurer and troll move is called a *strategy*. Different strategies are more or less likely to succeed. There are two strategies in the provided code - random movement, and movement controlled by human input.


Source: [Troll treasure exercise](https://alan-turing-institute.github.io/rse-course/html/module06_software_projects/06_09_exercise.html).

Original game: [Hunt the Wumpus](https://en.wikipedia.org/wiki/Hunt_the_Wumpus)).
