# Ryan-s-Final-Space-Trip
Final Project Freshman year 2024 | Craton

Ryan's Final Space Trip - Game README

"Ryan's Final Space Trip" is an exciting space-themed action game built using Python and the Pygame library. The game takes the player on an intergalactic adventure where they control a rocket ship, dodge meteors, collect power-ups, and compete for high scores.

Features:

Main Menu with a Start Game button.

Game Loop with an increasing difficulty as the player progresses.

Pause/Unpause Functionality.

High Score tracking and saving/loading of the player's highest score.

Leveling System that increases enemy speed and spawns more enemies as the score increases.

Collision Detection between the player's rocket and incoming meteors.

Sound Effects for collisions and background music.

Starfield Animation to simulate space travel.

Installation
To run the game, ensure you have Python 3.x and Pygame installed on your system.

Download or Clone the Repository:
If you haven’t already, download or clone this repository to your local machine.
Install Pygame: If Pygame is not installed, open a terminal/command prompt and run:

Copy code
pip install pygame
Download Game Assets: The game requires the following asset files to run properly:

rocket.png (Player's rocket ship image)
meteor.png (Meteor image)
background_music.mp3 (Background music for the game)
collision.mp3 (Sound for player-enemy collision)
Make sure these files are placed in the same directory as your Python script or update the file paths accordingly.

Game Controls

Left Arrow Key: Move the player’s rocket left.

Right Arrow Key: Move the player’s rocket right.

P Key: Pause/Unpause the game.

Escape Key: Quit the game at any time.

Game Features

1. Main Menu
When you start the game, you’ll be greeted with a main menu. From there, you can start the game by clicking the "Start Game" button. You can also adjust volume or settings if applicable (though in this version, volume control is not implemented yet).

2. Gameplay
The player controls a rocket ship at the bottom of the screen. Meteors fall from the top of the screen, and the goal is to avoid collisions with them.
The score increases as meteors are dodged and enemies reach the bottom of the screen.
The game features a leveling system where the speed of the meteors increases as the score gets higher, making the game progressively harder.

3. Pause Functionality
Press the P key during gameplay to pause the game. A "PAUSED" screen will appear, and no gameplay actions will be processed until the game is unpaused by pressing P again.

4. Game Over
If the player’s rocket collides with a meteor, the game ends and the Game Over screen is shown.
The final score is displayed, and the high score is saved.
The game will automatically exit after a short delay.

5. High Score
The highest score achieved in the game is tracked and saved automatically.

When you start the game, your highest score will be loaded and displayed.

How to Play
Launch the game by running the Final Project.py file.
On the main menu, click the Start Game button to begin playing.
Use the left and right arrow keys to control the rocket and avoid meteors.
Try to achieve the highest score possible while dodging meteors.
The game will automatically increase in difficulty as you progress by speeding up the meteors.
When you die (collide with a meteor), the Game Over screen will show, and the final score will be displayed.

File Structure
Final Project.py: The main Python script containing the game logic.
rocket.png: Image file for the player’s rocket.
meteor.png: Image file for the meteors.
background_music.mp3: Background music that plays throughout the game.
collision.mp3: Sound effect played when a collision occurs.

Future Enhancements
Volume Control: Implement a volume control slider for both background music and sound effects in the main menu.
Multiple Levels: Add more levels with unique challenges and backgrounds.
Power-ups: Include power-ups that give the player temporary invincibility or slow down the meteors.
Leaderboard: Store and display the top scores in the main menu for competitive play.

Credits
Game Design & Code: Ryan (Your Name)
Graphics & Sound: (Credit any sources or creators for the assets used)
Rocket and meteor graphics from (mention source if applicable).
Background music and sound effects from (mention source if applicable).
