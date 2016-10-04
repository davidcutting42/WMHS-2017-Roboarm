#setup section

#3D Mouse Libraries/Setup
from spnav import *
spnav_open()
import Arm

#Cartesian Space to Joint Space Libraries
import math
import numpy as np
import scipy.optimize

#=================================================================

#3D Mouse Input loop
try:
    while True:
        event = spnav_poll_event()
        if (event != None):
            if (event.ev_type == SPNAV_EVENT_MOTION):
                tran = event.translation
                rot = event.rotation
                x = tran[0]
                y = tran[1]
                z = tran[2]
                a = rot[0]
                b = rot[1]
                c = rot[2]
        arm = Arm.Arm3Link(L = np.array([255,255,1]))
        angles = inv_kin(xy = (y, z))
        print angles
        
        
except KeyboardInterrupt:
    print "Whoa there"




#=================================================================

#teardown
spnav_close() 
