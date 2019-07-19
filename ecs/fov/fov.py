from constants import *
from ecs.fov.fov_component import FovComponent
from ecs.display.display_component import DisplayComponent
from ecs.movement.movement_component import MovementComponent
import tcod
import pysnooper


class FovSystem:
    def __init__(self, game_map=None):
        self.game_map = game_map
        self.fov_map = tcod.map_new(CAM_WIDTH, CAM_HEIGHT)
        for y in range(CAM_WIDTH):
            for x in range(CAM_WIDTH):
                tcod.map_set_properties(self.fov_map, x, y,
                                        not game_map[x][y].block_path,
                                        not game_map[x][y].block_path)

    def update(self, entities):
        for e in entities:
            if e.get(FovComponent).fov_recalculate:
                tcod.map_compute_fov(
                    self.fov_map,
                    e.get(MovementComponent).cur_x,
                    e.get(MovementComponent).cur_y,
                    FOV_RADIUS,
                    FOV_LIGHT_WALLS,
                    tcod.FOV_PERMISSIVE_0)
                e.get(FovComponent).fov_map = self.fov_map

