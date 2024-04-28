from pygame import*

window = display.set_mode((1500, 800))

fps = time.Clock()
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, size_x, size_y, player_x, player_y,  player_speed, player_hp):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.hp = player_hp
        self.napr = "vverh"

    def ris(self):
        self.tanku = transform.scale(self.image, (70,100))
        self.tankr = transform.rotate(self.image, 90)
        self.tankd = transform.rotate(self.image, 180)
        self.tanka = transform.rotate(self.image, 270)
        if player.napr == "vverh":
            window.blit(self.tanku, (self.rect.x, self.rect.y))
        elif player.napr =="vniz":
            window.blit(self.tankd, (self.rect.x, self.rect.y))
        elif player.napr =="levo":
            window.blit(self.tankr, (self.rect.x, self.rect.y))
        elif player.napr =="pravo":
            window.blit(self.tanka, (self.rect.x, self.rect.y))

class gameobj(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = GameSprite('tanku.png', 70, 100, 0, 0, 5, 100)

with open('map.txt') as file:
    karta = file.readlines()

x1 = 0
y1 = 0
map = []

for y in karta:
    line = y.split(' ')
    for x in line:
        if "1" in x:
            w = gameobj('wall.png', x1, y1, 50,50)
            map.append(w)
        x1 += 40
    x1 = 0
    y1+=50

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type==KEYDOWN:
            if e.key==K_e:
                player.image=transform.rotate(player.image, -90)
    keys = key.get_pressed()
    if keys[K_d]:
        player.napr = "pravo"
        player.rect.x += player.speed
    elif keys[K_a]:
        player.napr = "levo"
        player.rect.x -= player.speed
    if keys[K_w]:
        player.napr = "vverh"
        player.rect.y -= player.speed
    elif keys[K_s]:
        player.napr = "vniz"
        player.rect.y += player.speed

    window.fill((40, 80, 60))
    player.ris()
    for w in map:
        w.ris()
    fps.tick(60)
    display.update()
        
