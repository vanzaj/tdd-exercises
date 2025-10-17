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



