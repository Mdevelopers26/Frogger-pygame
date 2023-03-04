import turtle
import math
import random
import time


####----------------------Set up the Screen

wn = turtle.Screen()
wn.title("Frogger by @mihir")
wn.setup(600, 800)
wn.tracer(0)
wn.cv._rootwindow.resizable(False,False)
wn.bgpic("background.gif")
wn.bgcolor("green")


####----------------------Register shape

# Register shape
shapes = ["frog.gif", "car_left.gif", "car_right.gif", "log_full.gif", "turtle_left.gif", "turtle_right.gif", "turtle_right_half.gif", 
    "turtle_left_half.gif", "turtle_submerged.gif", "home.gif", "frog_home.gif", "frog_small.gif"]

for shape in shapes:
    wn.register_shape(shape)



pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()



####-----------------------Create Classes

class Sprite():

    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def render (self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

    def is_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

    def update(self):
        pass

        


#Player class

class Player(Sprite):
    def __init__(self, x, y, width, height, image):
       Sprite. __init__(self, x, y, width, height, image)
       self.dx = 0
       self.collision = False
       self.frog_home = 0
       self.max_time = 60
       self.time_remaining = 60
       self.start_time = time.time()
       self.lives = 3
    pass

    def up(self):
        self.y +=50

    def down(self):
        self.y -=50

    def right(self):
        self.x +=50

    def left(self):
        self.x -=50

    def update(self):
        self.x += self.dx

        if self.x <-300 or self.x >300:
            self.x = 0
            self.y = -300

        if self.y < -325:
            self.y = -325
            
        


class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx): 
            Sprite.__init__(self, x, y, width, height, image)
            self.dx = dx
    
    def update(self):

        self.x += self.dx

        if self.x < -400:
            self.x = 400

        if self.x > 400:
            self.x = -400


class Log(Sprite):
    def __init__(self, x, y, width, height, image, dx): 
            Sprite.__init__(self, x, y, width, height, image)
            self.dx = dx

    def update(self):
        self.x += self.dx

        if self.x < -400:
            self.x = 400

        if self.x > 400:
            self.x = -400


class Home(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx=0

class Turtle(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        self.state = "full" # half, submerged
        self.full_time = random.randint(8, 12)
        self.half_time = random.randint(4, 6)
        self.submerged_time = random.randint(4, 6)
        self.start_time = time.time()
        
    def update(self):
        self.x += self.dx
        
        # Border checking
        if self.x < -400:
            self.x = 400
            
        if self.x > 400:
            self.x = -400
                        
        # Update image based on state
        if self.state == "full":
            if self.dx > 0:
                self.image = "turtle_right.gif"
            else:
                self.image = "turtle_left.gif"
        elif self.state == "half_up" or self.state == "half_down":
            if self.dx > 0:
                self.image = "turtle_right_half.gif"
            else:
                self.image = "turtle_left_half.gif"
        elif self.state == "submerged":
            self.image = "turtle_submerged.gif"

                
        # Timer stuff
        if self.state == "full" and time.time() - self.start_time > self.full_time:
            self.state = "half_down"
            self.start_time = time.time()
        elif self.state == "half_down" and time.time() - self.start_time > self.half_time:
            self.state = "submerged"
            self.start_time = time.time()
        elif self.state == "submerged" and time.time() - self.start_time > self.submerged_time:
            self.state = "half_up"
            self.start_time = time.time()
        elif self.state == "half_up" and time.time() - self.start_time > self.half_time:
            self.state = "full"
            self.start_time = time.time()          
    
        
        

   

class Timer():
    def __init__(self, max_time):
        self.x = 200
        self.y = -375
        self.max_time = max_time
        self.width = 200

    def render(self, time, pen):
        pass

  
###########----------------------Creating Objects

#Create the Player Object

player = Player (0, -325, 40, 40, "frog.gif")
level_1 = [
    Car(0, -275, 121, 40, "car_left.gif", -1),
    Car(221, -275, 121, 40, "car_left.gif", -1),
    
    Car(0, -225, 121, 40, "car_right.gif", 0.5),
    Car(221, -225, 121, 40, "car_right.gif", 2),
    
    Car(0, -175, 121, 40, "car_left.gif", -0.1),
    Car(221, -175, 121, 40, "car_left.gif", -0.1),
    
    Car(0, -125, 121, 40, "car_right.gif", 0.1),
    Car(221, -125, 121, 40, "car_right.gif", 0.1),
    
    Car(0, -75, 121, 40, "car_left.gif", -0.1),
    Car(221, -75, 121, 40, "car_left.gif", -0.1),
    
    Log(0, 25, 161, 40, "log_full.gif", 0.2),
    Log(261, 25, 161, 40, "log_full.gif", 0.2),
    
    Log(0, 75, 161, 40, "log_full.gif", -0.2),
    Log(261, 75, 161, 40, "log_full.gif", -0.2),
    
    Turtle(0, 125, 155, 40, "turtle_right.gif", 0.15),
    Turtle(255, 125, 155, 40, "turtle_right.gif", 0.15),
    
    Turtle(0, 175, 155, 40, "turtle_left.gif", -0.15),
    Turtle(255, 175, 155, 40, "turtle_left.gif", -0.15),
    
    Log(0, 225, 161, 40, "log_full.gif", 0.2),
    Log(261, 225, 161, 40, "log_full.gif", 0.2)
    ]


homes = [
    Home(0, 275, 50, 50, "home.gif"), 
    Home(-100, 275, 50, 50, "home.gif"),
    Home(-200, 275, 50, 50, "home.gif"),
    Home(100, 275, 50, 50, "home.gif"),
    Home(200, 275, 50, 50, "home.gif")
    ]

#Create list of sprites

sprites = level_1 + homes
sprites.append(player)
# 


###-----------------------------Keyboard bindings

wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.right, "Right")
wn.onkeypress(player.left, "Left")



#The Main game loop

while True:
    for sprite in sprites:
        sprite.render(pen)
        sprite.update()
    
    #Render lives
    pen.shape("frog_small.gif")
    for life in range(player.lives):
        pen.goto(-280 + (life * 30), -375)
        pen.stamp()

    #Check for collisions
    player.dx = 0
    player.collision = False

    for sprite in sprites:
        if player.is_collision (sprite):
            if isinstance(sprite, Car):
                player.lives -= 1
                player.x = 0
                player.y = -300
                break

            elif isinstance (sprite, Log):
                player.dx = sprite.dx
                player.collision = True
                break

            elif isinstance (sprite, Turtle) and sprite.state != "submerged":
                player.dx = sprite.dx
                player.collision = True
                break

    if player.y >0 and player.collision != True:
        player.lives -= 1
        player.x = 0
        player.y = -325

            
  
    
    #Update the screen
    wn.update()

    #Clear the screen
    pen.clear()
    


    
    


















    

