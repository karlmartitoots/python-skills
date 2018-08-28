'''
Encapsulate a request as an object, thereby letting users parameterize clients with different requests, queue or log requests, and support undoable operations.

or

A command is a reified method call.
'''
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RECT_WIDTH = 50
RECT_HEIGHT = 50

MOVEMENT_SPEED = 5
AI_MOVE_INTERVAL = 10
NUMBER_OF_AIS = 10

class Command:
    def execute():
        raise NotImplementedError

class MoveRightCommand(Command):
    def execute(player):
        player.addSpeedRight()
        
class MoveLeftCommand(Command):
    def execute(player):
        player.addSpeedLeft()

class MoveUpCommand(Command):
    def execute(player):
        player.addSpeedUp()

class MoveDownCommand(Command):
    def execute(player):
        player.addSpeedDown()

class StopHorizontalCommand(Command):
    def execute(player):
        player.stopHorizontalMovement()
        
class StopVerticalCommand(Command):
    def execute(player):
        player.stopVerticalMovement()
        


class Rectangle:
    """ Class to represent a rectangle on the screen """

    def __init__(self, x, y, width, height, angle, color):
        """ Initialize our rectangle variables """

        # Position
        self.x = x
        self.y = y

        # Vector
        self.delta_x = 0
        self.delta_y = 0

        # Commands
        self.upPress = MoveUpCommand.execute
        self.downPress = MoveDownCommand.execute
        self.leftPress = MoveLeftCommand.execute
        self.rightPress = MoveRightCommand.execute
        self.upDownRelease = StopVerticalCommand.execute
        self.leftRightRelease = StopHorizontalCommand.execute

        # Size and rotation
        self.width = width
        self.height = height
        self.angle = angle

        # Color
        self.color = color

    def draw(self):
        """ Draw our rectangle """
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height,
                                     self.color, self.angle)

    def move(self):
        """ Move our rectangle """

        # Move left/right
        self.x += self.delta_x

        # See if we've gone beyond the border. If so, reset our position
        # back to the border.
        if self.x < RECT_WIDTH // 2:
            self.x = RECT_WIDTH // 2
        if self.x > SCREEN_WIDTH - (RECT_WIDTH // 2):
            self.x = SCREEN_WIDTH - (RECT_WIDTH // 2)

        # Move up/down
        self.y += self.delta_y

        # Check top and bottom boundaries
        if self.y < RECT_HEIGHT // 2:
            self.y = RECT_HEIGHT // 2
        if self.y > SCREEN_HEIGHT - (RECT_HEIGHT // 2):
            self.y = SCREEN_HEIGHT - (RECT_HEIGHT // 2)
    
    def stopHorizontalMovement(self):
        self.delta_x = 0

    def stopVerticalMovement(self):
        self.delta_y = 0

    def addSpeedRight(self):
        self.delta_x = MOVEMENT_SPEED
    
    def addSpeedLeft(self):
        self.delta_x = -MOVEMENT_SPEED
    
    def addSpeedUp(self):
        self.delta_y = MOVEMENT_SPEED
    
    def addSpeedDown(self):
        self.delta_y = -MOVEMENT_SPEED
    
    def randomCommand(self):
        random.choice([self.upPress, self.downPress,self.leftPress,self.rightPress,self.upDownRelease,self.leftRightRelease])(self)

class MyGame(arcade.Window):
    """
    Main application class.
    """
    def __init__(self, width, height):
        super().__init__(width, height, title="Command pattern")
        self.player = None
        self.AI_list = []
        self.AI = None
        self.left_down = False

    def setup(self):
        """ Set up the game and initialize the variables. """
        width = RECT_WIDTH
        height = RECT_HEIGHT
        x = SCREEN_WIDTH // 2
        y = SCREEN_HEIGHT // 2
        angle = 0
        color = arcade.color.WHITE
        self.player = Rectangle(x, y, width, height, angle, color)
        for _ in range(NUMBER_OF_AIS):
            self.AI_list.append(Rectangle(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT), width, height, angle, arcade.color.RED))
        self.left_down = False

    def update(self, dt):
        """ Move everything """
        self.player.move()
        for AI in self.AI_list:
            AI.move()
            if random.randrange(AI_MOVE_INTERVAL) == 0:
                AI.randomCommand()

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        self.player.draw()
        for AI in self.AI_list:
            AI.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            self.player.upPress(self.player)
        elif key == arcade.key.DOWN:
            self.player.downPress(self.player)
        elif key == arcade.key.LEFT:
            self.player.leftPress(self.player)
        elif key == arcade.key.RIGHT:
            self.player.rightPress(self.player)

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.upDownRelease(self.player)
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.leftRightRelease(self.player)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()