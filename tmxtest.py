import pygame as pg
from pytmx import load_pygame


class Tile(pg.sprite.Sprite):

    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

pg.init()
screen = pg.display.set_mode((800, 600))
tmx_data = load_pygame("imgs/MMtestmap.tmx")
sprite_group = pg.sprite.Group()


# cycle through all layers
for layer in tmx_data.visible_layers:
    if hasattr(layer, "data"):
        for x, y, surf in layer.tiles():
            pos = (x * tmx_data.tilewidth, y * tmx_data.tileheight)
            Tile(pos = pos, surf = surf, groups = sprite_group)









# for layer in tmx_data.visible_layers:
#     print(layer)

#get tiles
# layer = tmx_data.get_layer_by_name('Background')
# print(dir(layer))

# get objects
# object_layer = tmx_data.get_layer_by_name('Objects')

# for obj in object_layer:
#     print(obj)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit

    screen.fill((0, 0, 0))

    sprite_group.draw(screen)


    pg.display.flip()
    pg.time.wait(10)