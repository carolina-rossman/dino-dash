# Dino Dash 
Dino Dash is an adventurous game where you play as Dino the dinosaur, a dinosaur from a corrupt test lab. 
Your objective is to lead Dino through various obstacles to escape the corrupt test lab. 
We are bringing two beloved games together, the dinosaur game (no-wifi Google game) and Jetpack Joyride, 
to provide our take on the genre of side-scrolling games. Together, we have worked to create a sci-fi 
experience like no other, creating an addictive experience for all. 

## To Run the Game
You will need to install packages, to run this game, refer to requirement.txt for  
those packages, additionally you can try:   
pip install -r requirements.txt  
To run the game first download the src and stimuli folders  
Then in your terminal, put in   
"uv run python main.py"  
Make sure your path is "...\dino-dash\src"  

## Names and Parameters
       1.) Start Screen + Instruction screen                      
       -The instructions                                          
       -The start button                        
       -the quit button
       
       2.) Powers Screen    
       - Background explains each power-up and power-down 
       - Start button    
       - Quit button  
       
      3.) Base Dino 
      - When spacebar is pressed, Dino Jumps
      - Dino legs are animated, when Dino jumps the legs are still, when dino runs the legs move

      4.) Power Ups
       At set distances, a random power-up will appear, by assigned weights
      -Jet Pack: 
      (When jetpack is picked up, switch to jetpack/flying Dino image)
      (Dino doesn't run, Dino flies, legs don't move)
      - Immunity: 
      (when an immunity power up is picked up. switch to Dino with shield image)
      (immmunity continues for set amount of time then returns to normal)

      5.) Power Downs
       At set distances a random power down will appear
      - Speed up:  
      (for a set amount of time, the speed is faster/the background is scrolling the fastest)
      -Tiny Dino: 
       (Dino becomes smaller, making the jumps harder to clear for user)
      
       6.) Score Counters
       - Distance Based Counter 
       - Shows how far from the end the player is
       - Once a certain distance is reached, an end screen
        will appear
        
       7.) End Screen 
       -Dino blows up a wall (to escape the corrupt test lab)
       -Dino runs off screen
       (Background stops Scrolling)
       -A congrats message appears
        
       8.) Game Over Screen
       - When an obstacle is hit, a Game Over screen appears
       - Has a message "You Died."
       - Two Buttons
       (Quit, Restart)
        
       9.) Obstacles
       - Various different images
       - Will randomly appear but we will put a guideline in the code that prevents the obstacles from being too close together.

       
## Why Someone Would Use This
Someone would use this program to pass the time and have fun. This game is meant to be for dinosaur, sci-fi, and side scrolling game lovers.

## Project Details
### 1. A brief (3-5 sentences) description of your planned project
We will be attempting to recreate an advanced version of the no wifi dinosaur game. The game will include various user-input jumps, and various power-ups and power-downs, ranging from jetpacks, rocket blasters, speed up game and midget Dino. The goal of the game is to reach the end, blow up a fence, and escape the test lab. 
### 2. For each of the three functions, a very brief (1-2 sentences) description of what the function will do.
      a) One of the functions needs to collect and activate the power-ups and power-downs.
      b) Another function needs to control the dinosaur, including user-inputted jumps.
      c) The last function needs to control the background and have it scroll, as the dinosaur moves. 
### 3. If you are doing a group project, the list of group members with both their real names and Github usernames.
      Alex Transue: a-tran69
      Patricia Richards: liltrishpzr-glitch
      Carolina Rossman: carolina-rossman
### 4. If you are doing a group project, very brief statements (1-2 sentences each) describing:
      a) How work will be divided (assigned and tracked) among group members.    
      Tracked: Through Git can see when someone makes changes to the repository.      
      Assigned: It has already been decided that Alex will find/draw the graphics. We will   divide the work based on classes. If we have an amount of classes that is not divisible by three, we will discuss what the fairest division of labor will be. If someone feels they have an undeserved amount of work, we will discuss and re-divide the work.   
      b) How (and how often!) team members will communicate with each other about the   project (such as weekly meetings, ongoing group chat, etc.)  
      We already have an ongoing group chat. We will have in-person meetings on Mondays from 4:30 to 6, starting on week 9. If we feel that our Monday meeting is insufficient, we will also meet on Thursdays at a similar time.

## Testing
You can run the test by running pytest in the root directory as a module. Do so by running:  
uv run pytest test_agents.py   

  
When running the game you should expect the following:  
The dino should stay in the far left of the screen while the background scrolls.  
As the background scrolls horizontally, obstacles appear that the users should avoid.  
By pressing spacebar. Users can clear the obstacles as they appear.  
As the user progresses through the game, the tempo gradually speeds up, and the difficulty increases as the background scrolls faster.  

  
Throughout the game there will be a score counter that:  
- Shows how far the users has progressed/the distances the dino has traveled since the start of the game.  
- As well as how close the user is to escaping the corrupt test lab.  
- Then finally, after each attempt, we will gather the users highest distance traveled and display it as the highscore.   

  
To make the game more engaging we added various power-ups and power-downs.  
These abilities automatically engage with no user input.  
The power-ups include:  
- Jetpack (when jetpack is picked up the Dino begins to fly over obstacles, for a set distance to be determined.)  
- Immunity (when an Immunity power-up is picked up the Dino has a shield protecting itself from any obstacles, for a set distance to be determined.)  
- Revival (A rare power-up not guaranteed to spawn in the game, it gives a second chance of life if you hit an obstacle.)  

  
The power-downs include,  
- Speed-up (the game speeds up, reaching the maximum speed for a set amount of time making it harder for users)  
- Tiny Dino (Shrinks the Dino, making the jumps harder.)


Finally if the user hits the desired distance, to be determined, to escape the corrupt test lab the dino would have escaped.  
Presenting a Congratulations screen.  
However if the dino runs into an obstacle before hand a game over screen appears giving the user two options:  
"try again" and "quit".  


