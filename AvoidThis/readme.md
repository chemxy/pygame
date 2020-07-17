# Python Game: Avoid This!

## Instruction

1. download the folder into your local computer
2. for windows os:

   - start a command prompt 
   - change directory to the game's directory
   - run `python game.py`
      1. **NOTE**: the game requires python package`pygame` to run correctly. if it doesn't run properly, maybe it's because you don't have the complete python package in your computer. try to install `pygame` using the following command: `pip install pygame` 
   - if want to quit the game early, click the `exit` icon at top-right corner
3. for linux os and mac os:
   - to be updated

## Game Spec

character dimensions: 20*20 pixels

bomb dimensions: 20*20 pixels

## Future Work:

1. add character's life. each character has 1 life initially. add 1 life every 400 scores. hitting 1 bomb will lose 1 life. show the number of lives at top-left corner, represented as a red heart.

2. optimize bombs animation in terms of fluency and consistency (or replace bomb image), to reduce damage to eyes. right now my eyes kinda hurt after each game, especially those with scores > 1000.