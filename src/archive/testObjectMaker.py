import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GLU import gluPerspective
from cubeListCreator import CubeListCreator
from frameCalculator import FrameCalculator
from objectMaker import ObjectMaker
import keyboard
import time
from data import Utils, MathUtils
import random

detections = Utils.open_json("sample_output_1.json")

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
gluPerspective(45, (display[0]/display[1]), 0.1, 200.0)
cube_list = CubeListCreator()
frame_calculator = FrameCalculator()
obj_maker = ObjectMaker(cube_list, 0, 0, -100, 0, 0.04)
lastPosition = 0
posIncrement = 0
colorIncrement = 0

for each in range(1):
    # each = Cube(random.randint(0, 5), random.randint(0, 5), random.randint(0, 5))
    # receivedPoints
    obj_maker.add_new_point(0, 1, -10, 5, True)
    obj_maker.add_new_point(0, 1.3, -10, 5, True)
    obj_maker.add_new_point(0, 1.6, -10, 5, True)
    obj_maker.add_new_point(0, 1.9, -10, 5, True)
    obj_maker.add_new_point(0, 2.1, -10, 5, True)
    obj_maker.add_new_point(99, 99, 99, 5, True)

    obj_maker.add_new_point(0, 1, -10, 300, True)
    obj_maker.add_new_point(0, 10, -100, 300, True)
    obj_maker.add_new_point(0, 11, -10, 300, True)
    obj_maker.add_new_point(0, 12, -10, 300, True)
    obj_maker.add_new_point(0, 2.1, -10, 300, True)
    obj_maker.add_new_point(99, 99, 99, 5, True)


start = time.time()
end = time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if keyboard.is_pressed("left"):
        cube_list.rotate_horizontally(0.1)
        cube_list.plotCubes()
    if keyboard.is_pressed("right"):
        cube_list.rotate_horizontally(-0.1)
        cube_list.plotCubes()
    if keyboard.is_pressed("up"):
        cube_list.rotate_vertically(-0.1)
        cube_list.plotCubes()
    if keyboard.is_pressed("down"):
        cube_list.rotate_vertically(0.1)
        cube_list.plotCubes()

    # cubeList.add_new_cube(Cube(random.randint(-50, 50), random.randint(-50, 50), random.randint(-70, -50)))
    cube_list.plotCubes()
    pygame.time.wait(50)

    end = time.time()
    if((end-start) >= 1.0):
        detect = detections.pop()
        obj_maker.add_new_point(detect['x'], detect['z'], -detect['y'], 90.0+MathUtils.get_azimuth(detect['x'], detect['z']), True)
        start = time.time()
