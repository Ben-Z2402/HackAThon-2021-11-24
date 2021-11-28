
import arcade
import random

###

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Retro Ping Pong"


game_mode = 0  

 

class MyGame(arcade.Window):
    """ Main application class. """
    def Title_Screen():
        global game_mode
        title = arcade.load_texture("Images/hi.png")
        if game_mode == 0:
            arcade.draw_texture_rectangle(title.width, title.height, title.width,title.height, title, 0)

 
    def __init__(self):
        """Creates the Background"""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    def on_draw(self):
        """
        Render the screen.
        """
        global Count_1, Count_2
        global game_mode, new_ball
        # This command has to happen before we start drawing
        arcade.start_render()
        title = arcade.load_texture("Images/hi.png")
        if game_mode == 0:
            arcade.draw_texture_rectangle(title.width//2, title.height, title.width,title.height, title, 0)
def main():
    MyGame()
    arcade.run()



if __name__ == "__main__":
    main()
