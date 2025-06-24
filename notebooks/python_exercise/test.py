

import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
for _ in range(1000):
    p.stepSimulation()
    time.sleep(1./240.)
p.disconnect()