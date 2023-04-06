from pygame import*

class Tile(sprite.Sprite):
    def __init__(self, img, pos, size):
        super().__init__()
        self.image = img
        self.rect = Rect(pos, size)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self, offset):
        self.rect.topleft += offset


tile_sprites={
    'B': 'brick.png' ,
    'L': 'lava.png',
    'G':'glitch.png',
    'O':'orangutan.png'
}
level_1 = [
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BO  G   BOO O O   O   O                                B",
    "B      B                                               B",
    "B     BB   G                                    B      B",
    "B         G   B                B   B        B   O      B",
    "B G     B LLLLLLL B   B   B    O   O       BO          B",
    "B     G BLLLLLLLLLLLLLLLLLLLL            B O           B",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBB       B    O             B",
    "BLLLBBLBBBLLBBBLBBBBBBBBBBBBB       O                  B",
    "BLBBBLBLBLBBLBLBLBBBBBBBBOBBB                          B",
    "BLLLBBLBBLBBLBBLBBBBBBBBBOOBB                          B"
]

def load_tiles(size):
    for image_file in tile_sprites:
        tile_sprites[image_file] = image.load(tile_sprites[image_file])
        tile_sprites[image_file] = transform.scale(tile_sprites[image_file], size)

def create_level(level):
    load_tiles((64,64))
    layer = sprite.Group()
    for y, row in enumerate(level):
        columns = list(row)
        for x, thing in enumerate(columns):
            if thing in tile_sprites:
                tile = Tile(img=tile_sprites[thing], pos=(x*64,y*64), size=(64,64))
                layer.add(tile)
    return layer

plats = create_level(level_1)

if __name__ == '__main__':
    WIDTH, HEIGHT = 950, 960
    window = display.set_mode((WIDTH, HEIGHT))
    clock = time.Clock()

    while not event.peek(QUIT):
        window.fill('black')
        plats.draw(window)

        display.update()
        clock.tick(60)