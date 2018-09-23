""" Testing swampy """

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
#print bob

# polygon
for i in range(8):
    fd(bob, 20)
    lt(bob, 45)
    fd(bob, 20)

wait_for_user()

