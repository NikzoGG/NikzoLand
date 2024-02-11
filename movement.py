import pygame
import sys

burzina_na_dvijenie = 8
dibeliq_speed = 5




def left_movement(player_rect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.x -= burzina_na_dvijenie

def right_movement(player_rect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player_rect.x += burzina_na_dvijenie

def dibeliq_movement(dibeliq_rect):
    dibeliq_rect.x += dibeliq_speed
    if dibeliq_rect.x >= 1200:
        dibeliq_rect.x = -1




