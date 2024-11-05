import pygame
from globals import *
from utils.eventhandler import EventHandler

class Inventory:
    def __init__(self, app) -> None:
        self.app = app
        self.screen = self.app.screen

        self.slot_count = 10
        self.expanded_slot_count = 50
        self.slots = []

        for idx in range(self.expanded_slot_count):
            self.slots.append("")

        self.slot_rects: list[pygame.Rect] = self.gen_slot_positions()
        
        self.active_slot_idx = 0
        self.active_slot = self.slots[self.active_slot_idx]

        self.expanded_inventory = False

        self.font = pygame.font.Font(None, 25)

    def gen_slot_positions(self) -> list:
        slot_rects = []

        x_offset = TILESIZE//4
        y_offset = TILESIZE//4
        column = 0
        row = 0
        for slot in self.slots:
            slot_rects.append(pygame.Rect(x_offset + column*TILESIZE*1.5, y_offset + row*TILESIZE*1.5, TILESIZE, TILESIZE))
            column += 1
            if column == 10:
                column = 0
                row += 1
        return slot_rects

    def input(self):
        if not self.expanded_inventory:
            if EventHandler.scroll_wheel_down():
                self.active_slot_idx += 1
            if EventHandler.scroll_wheel_up():
                self.active_slot_idx -= 1
            if self.active_slot_idx < 0:
                self.active_slot_idx= self.slot_count-1
            if self.active_slot_idx > self.slot_count-1:
                self.active_slot_idx = 0 

        if EventHandler.keydown(pygame.K_e):
            self.expanded_inventory = not self.expanded_inventory

    def update(self):
        self.input()
        self.active_slot = self.slots[self.active_slot_idx]

    def draw(self):
        # transparent surface
        surf = pygame.Surface((TILESIZE*1.5, TILESIZE*1.5))
        surf.fill("gray")
        surf.set_alpha(128)

        # expanded inventory ? 
        visible_slot_count = self.slot_count
        if self.expanded_inventory:
            visible_slot_count = self.expanded_slot_count

        for index in range(visible_slot_count):
            pygame.draw.rect(self.screen, "gray", pygame.Rect(self.slot_rects[index].x-TILESIZE//4, self.slot_rects[index].y-TILESIZE//4, TILESIZE*1.5, TILESIZE*1.5), 2)

            # highlighting
            text_color = "white"
            if index == self.active_slot_idx:
                text_color = "black"
                pygame.draw.rect(self.screen, "white", pygame.Rect(self.slot_rects[index].x-TILESIZE//4, self.slot_rects[index].y-TILESIZE//4, TILESIZE*1.5, TILESIZE*1.5))
            else:
                self.screen.blit(surf, (self.slot_rects[index].x - TILESIZE//4, self.slot_rects[index].y - TILESIZE//4))

            #if self.slots[index].name != "default":
            #    #self.screen.blit(self.textures[self.slots[index].name], self.slot_rects[index])
            #    if self.slots[index].quantity > 1:
            #        self.text = self.font.render(str(self.slots[index].quantity), True, text_color, None)
            #        self.screen.blit(self.text, self.slot_rects[index])
