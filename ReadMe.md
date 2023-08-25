# Circuit Python Macropad
## What is a Macropad?
If you are familiar with a stream deck, or any other kind of small, customizable keyboard, you are familiar with a macropad. This repository contains the firmware to go with 2004island's hardware design based on the rp2040, and allows its functionality and appearence to be altered using a description language.

## How to use
1. Load the rp2040 in 2004island's macropad design with micropython
2. Copy the required files using the included shell script, changing the path to the location of your rp2040
3. Configure the kdl file to customize your macropad to your liking!

## KDL
KDL stands for Keyboard Description Language and was created to allow those without programming experience to customize their macropad through specific commands without compromising on what could be achieved through a python script.

### KDL Syntax
Each line either starts with a 'State' or 'key' descriptor that defines either a state or a key functionality. Key descriptors also contain attributes of that key and actions taken when it is placed, seperated by commas

### States
A State is similar to a layer, and different States can be switched between by commands from different keys. A state is declared as follows:

`State (statenum)`

where statenum is an integer

### Keys
The functionality of a Key in kdl is described as follows:

`key (row),(col): (attribute/action), (attribute/action), ...`

where row and col are integers corresponding to a valid location on the keypad. As many attributes or actions can be specified, each seperated by commas. One or more attributes or actions are valid.

### Attributes and Actions
Attributes and actions are not treated any different from eachother in KDL, but some keywords (attributes) are used to describe a key and how it works, while others (actions) are executed when the key is pressed. Only attributes or actions for the current state are used

### Attributes:
`color (r) (g) (b)`
Defines the color a key will light up. R G and B are integers from 0 to 255, where 255 is the brightest

`on (condition)`
Defines when a key is lit. Condition can either be
- `pressed` - when the key is held
- `always` - all the time
- `never` - light is permanently off

### Actions
`display (command)`
Makes the display do the specified command. Commands are
- `clear` - clears the display so all pixels are off
- `text (x) (y) (string)` - where x and y are ints for the position on screen, and string is the text to be displayed (Doesnt need to be in quotes)

`press (key) (key) ...` \
Pressed the following keys (seperated by spaces) holding each key until the last one is pressed. Used for sequences like `CTRL C` or `CTRL ALT T`

`type (string)`
Types each letter in the following string one at a time. Used for typing out text. The string doesnt need to be in quotes

### Examples
Examples for kdl syntax and uses can be found in the kdl folder included with the project
