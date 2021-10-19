from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from voxel import *

app = Ursina()
for z in range(20):S
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))
player = FirstPersonController()
app.run()
