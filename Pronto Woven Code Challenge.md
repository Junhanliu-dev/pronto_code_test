# Pronto Woven Code Challenge
___
### _The terminal robot simulator that takes string of commands as input and prints the minimum path to go to its original point, the robot`s current point and a list of paths to go back._

# How to use
___
#### the project is compiled as a double-click programe.
#### In the _dist/main_ folder, double click the main file, the programme will start automatically.

## Input parameters
___
#### when the programme is running, the terminal will require you enter a string of commands in order to let the robot move.
#### _For example_, F1 means move foward 1 unit, R3 means turn right 3 times.
#### Available commands are:

 - #### F -- move foward 1 unit
 - #### B -- move backward 1 unit
 - #### R -- turn right 90 degrees
 - #### L -- turn left 90 degrees

#### The inputs are case insensitive but thet have to be comma-separated. For example, `F1,R1,B2,L1,B3` is valid, but `F1.R1.B2.L1.B3` is invalid.


## Features
___
- Path finder can be other implementation, as long as it implements the PathFinderBase interface, and pass it into simulator as parameter.
- The simulator returns the minumum number of units required to go back to its original position and paths it will be visited.


