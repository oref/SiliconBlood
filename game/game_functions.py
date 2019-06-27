# 3rd party modules
import pygame
# game files
import constants
from drawing.draw_functions import draw_game
from ecs.actor import ObjActor
from ecs.creature import ComCreature
from ecs.ai import ComAi
from map.game_map import GameMap


def game_main_loop():
    game_quit = False

    while not game_quit:
        game_handle_keys()
        draw_game(SURFACE_MAIN, GAME_MAP, GAME_OBJECTS)
    #while not game_quit:

    #    # handle player input
    #    player_action = game_handle_keys()

    #    if player_action == "QUIT":
    #        game_quit = True

    #    if player_action != "no-action":
    #        for obj in GAME_OBJECTS:
    #            if obj.ai:
    #                obj.ai.take_turn()

    #    # draw the game
    #    draw_game(SURFACE_MAIN, GAME_MAP, GAME_OBJECTS)

    ## quit the game
    #pygame.quit()
    #exit()


def game_initialize():

    global SURFACE_MAIN, GAME_MAP, PLAYER, ENEMY, GAME_OBJECTS

    # initialize pygame
    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))

    GAME_MAP = GameMap(constants.MAP_HEIGHT, constants.MAP_WIDTH)

    creature_com1 = ComCreature("greg")
    PLAYER = ObjActor(0, 0, "python", constants.S_PLAYER, creature=creature_com1)

    creature_com2 = ComCreature("WigWig")
    ai_com = ComAi()
    ENEMY = ObjActor(15, 15, "WigWig", constants.S_WIGWIG, ai=ai_com)

    GAME_OBJECTS = [PLAYER, ENEMY]


def game_handle_keys():
    # get player input
    events_list = pygame.event.get()

    # process input
    for event in events_list:
        if event.type == pygame.QUIT:
            return "QUIT"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PLAYER.move((0, -1))
                return "player-moved"

            if event.key == pygame.K_DOWN:
                PLAYER.move((0, 1))
                return "player-moved"

            if event.key == pygame.K_LEFT:
                PLAYER.move((-1, 0))
                return "player-moved"

            if event.key == pygame.K_RIGHT:
                PLAYER.move((1, 0))
                return "player-moved"

    return "no-action"
