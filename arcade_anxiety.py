import arcade
import random
screen_width=600
screen_height=600
screen_title="Avoid Anxiety"
class Person(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x
        if self.left<50:
            self.left=50
        if self.right>screen_width-50:
            self.right=screen_width-50
    
    # def update(self):
    #     # self.center_x =300
    #     # self.center_y = 100
    #     self.center_x+=self.change_x
class Wall(arcade.Sprite):
    # def update(self):
    #     self.center_x +=self.change_x
    # def __init__(self):
    #     super().__init__(random.random(["wall.png", "wall - Copy.png", "wall - Copy (2).png", "wall - Copy (3).png", "wall - Copy (4).png","wall - Copy (5).png","wall - Copy (6).png","wall - Copy (7).png","wall - Copy (8).png","wall - Copy (9).png"]))
     def update(self):
        if self.center_y<0:
            self.center_y=screen_height
            self.center_x=random.randint(130,screen_width-130)
        self.center_y-=self.change_y

# class Shield(arcade.Sprite):
#     def update(self):
#         if self.center_y<0:
#             self.center_y = screen_height
#             self.center_x= random.randint(130, screen_width-130)
#         self.center_y-=self.change_y

class OurGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.background=arcade.load_texture("ckground.png")
        self.person=Person("45de2c7a0f8014ad38a189edc6f97a91.jpg", 0.4)
        textures = ["wall.png", "wall - Copy.png", "wall - Copy (2).png", "wall - Copy (3).png", "wall - Copy (4).png","wall - Copy (5).png","wall - Copy (6).png","wall - Copy (7).png","wall - Copy (8).png","wall - Copy (9).png"]
        for texture in range(len(textures)):
            self.wall=Wall(random.choice(textures), 0.6)
        # self.wall = Wall("wall.png", 0.6)
        # self.shield = Shield("6232.png_300.png", 0.15)
        self.score=0
        self.attempts=1
        self.speed = 3
        self.level = 1

    def setup(self):
        self.person.center_x=300
        self.person.center_y=100
        # wall = Wall()
        # for wall in self.walls:
        self.wall.center_x = 300
        self.wall.center_y = 500
        # self.shield.center_x = 300
        # self.shield.center_y = 500
        self.speed = 3
        self.wall.center_y = self.speed
        # self.shield.center_y = self.speed2
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        arcade.draw_texture_rectangle(screen_width/2,screen_height/2,screen_width,screen_height,self.background)
        arcade.draw_text(f"Score: {self.score-1}",100,550,arcade.color.BLACK)
        # arcade.draw_text(f"Bar speed: {self.speed}",200,550,arcade.color.BLACK)
        arcade.draw_text(f"Level: {self.level}",250,550,arcade.color.BLACK)
        arcade.draw_text(f"Anxiety Level Counter: {self.attempts}",355,550,arcade.color.BLACK)
        self.person.draw()
        self.wall.draw()
        # self.shield.draw()
        if(self.score == 10):
            arcade.draw_text("YOU BEAT ANXIETY!",75,300,arcade.color.RED_DEVIL,35)
            self.person.stop()
            self.wall.stop()

    def update(self, delta_time):
        self.person.update()
        self.wall.update()
        # self.shield.update()
        self.wall.change_y = self.speed
        # self.shield.change_y = self.speed2
        if(self.attempts > 0):
            if arcade.check_for_collision(self.person,self.wall):
                self.attempts += 1
                self.score = 0
                self.speed = 0
                self.level = 1
                self.setup()
            # if arcade.check_for_collision(self.car, self.shield):
            #     None
        if self.wall.center_y<0:
            self.score+=1
            # textures = ["wall.png", "wall - Copy.png", "wall - Copy (2).png", "wall - Copy (3).png", "wall - Copy (4).png","wall - Copy (5).png","wall - Copy (6).png","wall - Copy (7).png","wall - Copy (8).png","wall - Copy (9).png"]
            # self.wall.
            if self.score==1-1:
                self.level += 1
                self.speed += 0.5
            elif self.score==2:
                self.level += 1
                self.speed += 0.5
            elif self.score==3:
                self.level += 1
                self.speed += 0.5
            elif self.score==4:
                self.level += 1
                self.speed += 0.5
            elif self.score==5:
                self.level += 1
                self.speed += 0.5
            elif self.score==6:
                self.level += 1
                self.speed += 0.5
            elif self.score==7:
                self.level += 1
                self.speed += 0.5
            elif self.score==8:
                self.level += 1
                self.speed += 0.5
            elif self.score==9:
                self.level += 1
                self.speed += 0.5
        # if self.wall.center_y<0:
            textures = ["wall.png", "wall - Copy.png", "wall - Copy (2).png", "wall - Copy (3).png", "wall - Copy (4).png","wall - Copy (5).png","wall - Copy (6).png","wall - Copy (7).png","wall - Copy (8).png","wall - Copy (9).png"]
            new_textures = textures[:]
            random.shuffle(new_textures)
            self.wall=Wall(new_textures.pop(), 0.6)
            # self.wall.center_y=500
            self.wall.center_y=screen_height
            self.wall.center_x=random.randint(130,screen_width-130)
            self.wall.center_y-=self.wall.change_y
    def on_key_press(self, key, modifiers):
        if (key == arcade.key.RIGHT):
            self.person.change_x=5
            self.person.angle=-10
        if (key == arcade.key.LEFT):
            self.person.change_x=-5
            self.person.angle=10
    def on_key_release(self, key , modifiers):
        if (key==arcade.key.RIGHT or key==arcade.key.LEFT):
            self.person.change_x=0
            self.person.angle=0


game=OurGame(screen_width,screen_height,screen_title)
game.setup()
arcade.run()      