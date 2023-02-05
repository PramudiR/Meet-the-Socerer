import pygame, sys
from pygame.locals import QUIT

# initializing
pygame.init()
flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
screen = pygame.display.set_mode((0, 0), flags, 16)
pygame.display.set_caption("Magical Adventure")
screen_w, screen_h = screen.get_size()
screen.set_alpha(None)
bg = pygame.image.load("bg1.png")
bg = pygame.transform.scale(bg, (screen_w, screen_h))
screen.blit(bg, (0, 0))
objects = []
font = pygame.font.Font('pacifico.ttf', 20)


# game buttions
class Button():

    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 buttonText='Button',
                 onclickFunction=None,
                 onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#bc6c25',
            'hover': '#606c38',
            'pressed': '#283618'
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, '#fefae0')
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


# frequent fucntions
def blit_text(surface, text, pos, font, color):
    words = [word.split(' ') for word in text.splitlines()
             ]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    max_width = int(max_width * 0.85)
    max_height = int(max_height * 0.85)
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def next():
    screen.blit(bg, (0, 0))


#-  -  - score sheme  -  -  #
curious = 0
thoughtful = 0
lovely = 0
brave = 0


def score():
    scoretxt = 'Your score, \n' + f'Curious: {curious} \n' + f'Thoughtful: {thoughtful} \n' + f'Lovely: {lovely} \n' + f'Brave: {brave} \n'
    text = font.render(scoretxt, True, '#fefae0')
    screen.blit(text, (screen_w * 0.1, screen_h * 0.75))
    pygame.display.flip()


def rank():
    rank = thoughtful + curious + lovely + brave
    rnktxt = "You don't have any game ranking yet"
    if (rank == 4):
        rnktxt = 'Your Rank, \n \t Newbie Explorer !'
    if (rank > 4 and rank < 8):
        rnktxt = 'Your Rank, \n \t Explorer !'
    if (rank == 8):
        rnktxt = 'Your Rank, \n \t Adventurer !'
    if (rank > 8 and rank < 12):
        rnktxt = 'Your Rank, \n \t Young Wizard !'
    if (rank == 12):
        rnktxt = 'Your Rank, \n \t Wizrd !'
    text = font.render(rnktxt, True, '#fcd5ce')
    screen.blit(text, (screen_w * 0.1, screen_h * 0.7))
    pygame.display.flip()


# Start page
welcm = 'Greetings Seeker ! \n Before going further be warned your journey is greately affected by your choices. Yet magic can do changes too.\n \n Each choice may or may not add scores about 4 aspects of your personality. \n At the end you will know more about yourself.'
blit_text(screen, welcm, (screen_w * 0.1, screen_h * 0.1), font, '#ccd5ae')

score()
rank()
Button(screen_w * 0.83, screen_h * 0.83, 70, 36, 'Next', next)

#main game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for object in objects:
        object.process()

    pygame.display.update()
