import pygame, random, time, sys

class Innocent(pygame. sprite . Sprite ) :
    def __init__ ( self ,posX,posY) :
        super(Innocent, self ). __init__ ()
        numImage=random.randint(1,5)
        self .image = pygame.image. load(f"image{numImage}.png")
        self .image = pygame. transform . scale ( self .image, (50 , 50))
        self . rect = self .image. get_rect ()
        self . rect .x=posX
        self . rect .y=posY
    def deplacement(self):
        self.rect.x=self.rect.x+random.randint(-10,10)
        self.rect.y=self.rect.y+random.randint(-10,10)
        if self.rect.x < -10:
            self.rect.x=largeur+10
        elif self.rect.x>largeur-10:
            self.rect.x=-10

        if self.rect.y < -10:
            self.rect.y=hauteur+10
        elif self.rect.y>hauteur-10:
            self.rect.y=-10



class compteur:
    def __init__(self):
        self.value=0
    def increase(self):
        self.value+=1


class Imposteur(pygame.sprite.Sprite):
    def __init__(self,mouseX,mouseY):
        super(Imposteur,self).__init__()
        self.image=pygame.image.load("amogus.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.x=mouseX
        self.rect.y=mouseY
    def deplacement(self):
        x,y = pygame.mouse.get_pos()
        self.rect.x=x-25
        self.rect.y=y-25
        self.miam_miam(innocent_list)
    def miam_miam(self,collidable=pygame.sprite.Group()):
        value=0
        collision_list=pygame.sprite.spritecollide(self,collidable,False)
        for collided_object in collision_list:
            cri.play()
            time.sleep(0.02)
            collidable.remove(collided_object)
            compteur.increase()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.image= pygame.transform.scale(self.image, (1000, 800))

pygame.init()
clock = pygame.time.Clock ()

largeur=1000
hauteur=800
screen = pygame.display.set_mode((largeur , hauteur))

innocent_list = pygame.sprite.Group()

BackGround = Background('cafeteria.png', [0,0])

imposteur_list=pygame.sprite.Group()

done = False

cri=pygame.mixer.Sound("kill.WAV")

compteur=compteur()

myfont=pygame.font.SysFont('Impact', 30)

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

while not done:
    for event in pygame. event . get ():
        if event . type == pygame.QUIT:
            done = True
        if event . type == pygame.KEYDOWN and event .key == pygame.K_SPACE:
            posX=random.randint(0,largeur-50)
            posY=random.randint(0,hauteur-50)
            innocent_list.add(Innocent(posX,posY))
        if event.type == pygame.KEYDOWN and event.key==pygame.K_DOWN:
            x,y = pygame.mouse.get_pos()
            imposteur_list.add(Imposteur(x,y))




    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)

    imposteur_list.draw(screen)
    for imposteur in imposteur_list:
        imposteur.deplacement()



    innocent_list.draw(screen)
    for innocent in innocent_list :
        innocent.deplacement ()

    textsurface=myfont.render(f'Innocents tués: {compteur.value}', False, (220,0,0))

    screen.blit(textsurface,(0,0))

    clock . tick (60)
    pygame. display .update()


pygame.quit ()