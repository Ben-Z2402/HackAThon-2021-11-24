import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Finacnce Your Education"

class MyGame(arcade.Window):
    """ Main application class. """
    def Title_Screen():
        title = arcade.load_texture("Images/Welcome_Screen.png")
        arcade.draw_texture_rectangle(title.width, title.height, title.width,title.height, title, 0)

 
    def __init__(self):
        """Creates the Background"""
        global new_ball
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

def main():
    MyGame()
    arcade.run()



if __name__ == "__main__":
    main()

