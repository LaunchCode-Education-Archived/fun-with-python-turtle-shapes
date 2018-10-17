# Summary
Demonstration program that uses Python 3, the [Turtle library](https://docs.python.org/3.0/library/turtle.html), Objects, and functions to draw shapes. 
The code is a combination of Object Oriented and functions. The `main()` in `main.py` is the starting point for reading the code. 

# Repl.it Version
A version of this code is availbe to run on repl.it. This only requires a browser to run and edit the code.
- Link to repl.it version: [https://repl.it/@launchcode/fun-with-python-turtle-shapes](https://repl.it/@launchcode/fun-with-python-turtle-shapes)
- After opening the repl.it version be sure to fork it, so that you can save your changes
  - Click the pencil icon next to the name in the top left
  - Click the fork button
- NOTE: repl.it version is not guaranteed to be up to date with repo version.

# Install Instructions
If you want to run the code on your computer using Python, please follow these instructions.
1. Clone the repo to your computer (requires that you have `git` installed)
2. Check if you already have Python 3
   - in terminal run `python -V`
   - if you see anything starting with 3, then **skip to the next section** "Running It" 
3. Install Python 3
   - [Download Miniconda](https://conda.io/miniconda.html) ([read about miniconda here](https://conda.io/miniconda.html))
   - Download the Python 3 installer for your Operating System
   - Special Mac or Linux instructions
     - run `chmod +x Miniconda3-actual-file-name.sh` in your terminal, where you downloaded the install file
     - then run `./Miniconda3-actual-file-name.sh`, but be sure to use the name of the file you downloaded
     - The installer will ask you questions
       - Agree to the license
       - Be sure to say Yes to the question about adding `python` to your `$PATH`
       - When installer is finished, close all terminals (new terinals will reference newly installed python version)

# Running It
- After Python 3 has been installed
- Open a terminal and navigate to the repo folder. Example: `/Users/your-name/repos/fun-with-python-turtle-shapes`
- run program by running this command in terminal: `python main.py`

# What the Program Does
- The user interacts with the program via the console(terminal)
- Has two modes
  - create mode
    - user is asked via console(terminal) what they want to draw
    - options: stars, triangles, a rocket, and planets 
  - demo mode
    - repeatly draws stars, triangles, a rocket, and planets
    - there is no close feature, you have to kill the program manually
    
# Possible Tasks/Assignments
1. Have the program say "Hello, what is your name" and wait for the user to answer.
   - Program should say "Nice to meet you {USER'S NAME HERE}"
2. In the demo program white stars are added to the left part of the screen
   - Change them to be blue
   - Make them show up on the right side instead of the left
3. Make the program draw a square on the scene. It can be in any mode
4. Add a 'draw_square' function
5. Add a "square" option to create mode which will add a square to the scene
   - Use the `draw_square` function you created
6. Add a `Moon` class or `draw_moon()` that draws a moon in the sky
7. Add a `House` class or `draw_house()` that will draw a house on the ground
8. Add a ring around the planet Saturn

# Reference Help
- [Turtle Library Docs](https://docs.python.org/3.0/library/turtle.html)
