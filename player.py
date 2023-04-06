from pygame import *

class PlayerSprite(sprite.Sprite):
    def __init__(self, filename, pos, size, max_speed):
        self.image = image.load(filename)
        self.image = transform.scale(self.image, size)
        self.rect = Rect(pos, size)
        self.max_speed = Vector2(max_speed)
        self.speed = Vector2(0,0)
        self.can_jump = False
        mixer.init()
        self.jump_sound = mixer.Sound('jump.wav')
    def update(self, platforms=None):
        keys = key.get_pressed()
        #horizontal movement
        if keys[K_d]:
            self.speed.x = self.max_speed.x#moves right
        if keys[K_a]:
            self.speed.x = -self.max_speed.x#moves left
        if not keys[K_d] and not keys [K_a]:
            self.speed.x = 0
        self.rect.x += self.speed.x#moving horizontal
        print(len(platforms))
        tiles = sprite.spritecollide(self, platforms, False)
        if self.speed.x > 0:
            for tile in tiles:
                self.rect.right = tile.rect.left
                self.speed.x = 0
        elif self.speed.x < 0:
            for tile in tiles:
                self.rect.left = tile.rect.right
                self.speed.x = 0

        #vertical movement
        if keys[K_w] and self.can_jump:
            self.jump_sound.play()
            self.speed.y = -self.max_speed.y
            self.can_jump = False
        self.speed.y += 1
        self.rect.y += self.speed.y

        tiles = sprite.spritecollide(self, platforms, False)
        if self.speed.y > 0:
            for tile in tiles:
                self.rect.bottom = tile.rect.top
                self.can_jump = True
                self.speed.y = 0
        elif self.speed.y < 0:
            for tile in tiles:
                self.rect.top = tile.rect.bottom
                self.speed.y = 0

        if self.rect.bottom >= 960:
            self.rect.bottom = 960
    def draw(self, surface):
        surface.blit(self.image, self.rect)


if __name__ == '__main__':
    WIDTH, HEIGHT = 800, 640
    window = display.set_mode((WIDTH, HEIGHT))
    clock = time.Clock()

    p1 = PlayerSprite('dude.png', (300,0), (100,100,),(8,10))

    while not event.peek(QUIT):
        window.fill('black')

        p1.update()
        p1.draw(window)

        display.update()
        clock.tick(60)