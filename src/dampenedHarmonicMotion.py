#Chester Holtz
from __future__ import division
from visual import *
from visual.graph import *

scene.background = color.white
scene.x = scene.y = 0
scene.width = 1000
scene.height = 300

r = 0.05        # Radius of the spring.
L = 2           # Rest length of the spring.
y = 0.5         # Initial displacement of the end of the spring with the block attached.
G = 9.8         # Gravitational acceleration
dt = 0.0005     # Time step size
t = 0           # Start time of the calculation
uvisc = 0.003 # 0.003   # Damping force coefficient of the viscous force (proportional to v).
ukin = 0.05     # Coefficient of kinetic friction (proportional to the normal force).
uair = 0.003    # Damping force coefficient of the friction due to the air (proportional to v^2).

# The spring is defined to have a spring constant Ks = 0.7 N/m:
#   the position of the left-end of the spring is set of (-L,0,0) and the vector that points
#   from the left-end of the spring to the right-end of the spring is (L+y,0,0) where y is
#   the initial displacement of the block.
#
# The block is defined to have 0.02 kg mass:
#   its original position ifs (y,0,0).
#
spring = helix(color=color.red, pos=(-L,0,0), axis=((L+y),0,0), radius = r, Ks = .7)
ball = sphere(color=color.red, pos=(-L,0,0), radius = 0.025)
block = box(length=.5, width=.5, height=.5, pos=(y,0,0), mass=.02, color=color.blue)
ground = box(length=5, width=5, height=.01, pos=(0,-.25,0), color=color.cyan)

WF = math.sqrt(spring.Ks/block.mass)
WD = .9*WF        # Angular frequency of the driving displacement.
D = .005         # Amplitude of the driving displacement.

gravforce = vector(0,0,0)
scene.autoscale=0

# Set the initial momentum, velocity, and friction for to 0 N.
block.p = vector(0,0,0)
block.vel = vector(0,0,0)
ffriction = vector(0,0,0)

# Create a display to show grapgs of the kinetic energy, the potential energy, and the total energy.
gdisplay(x=0, y=300, width=1000, background=color.white,
         title='K:blue, U:red, K+U: magenta')
uplot=gcurve(color=color.red)
kplot=gcurve(color=color.blue)
ukplot=gcurve(color=color.magenta)
posplot=gcurve(color=color.blue)

# Start simulation and continue until time t = 10 s.
print('time(s)   U(J)      K(J)      E(J)')

while (t < 10):
    rate(400)

    # Determine the gravitational force on the block (which in this case is
    # also equal to the normal force exerted on the block (which we need if
    # we want the determine the kinetic friction force).
    gravforce = G*block.mass

    # Determine the viscous friction force.
    ffriction.x = -uvisc*block.vel.x

    # Other friction forces that may be considered:
    # sliding and air resistance
#     if (block.vel.x < 0):
#         #ffriction.x = ukin*gravforce          # sliding
#         ffriction.x = uair*(block.vel.x**2)    # air resistance
#     else:
#         #ffriction.x = -ukin*gravforce         # sliding
#         ffriction.x = -uair*(block.vel.x**2)   # air resistance
#     ## end sliding and air resistance
 
    # Calculate the spring force.
    # Note: the axis of the spring is compared to the vector that specifies the
    #       rest length of the spring in order to determine the spring force.
    fspring = (spring.axis-vector(L,0,0))*(-spring.Ks)


    # Determine the new position and velocity of the block.
    block.p = block.p + (ffriction + fspring)*dt
    block.vel = block.p/block.mass
    block.pos = block.pos + (block.vel*dt)
    y=mag(block.p)

    # Calculate the new position of the spring.  Note: we need to define the
    # position of both ends of the spring. The right-end of the spring is located
    # at the position of the block.
#    spring.pos = (-L,0,0)
    spring.pos = spring.pos+(D*math.sin(WD*dt),0,0)
    ball.pos = ball.pos+(D*math.sin(WD*dt),0,0)
    spring.axis = block.pos - spring.pos

    t = t + dt

    ##Energy Stuff=======================================================
    spring.k = (mag(block.p)**2) / (2 * block.mass)
    spring.u = (.5*(spring.Ks*((mag(block.pos))**2)))
    spring.uk = spring.u + spring.k
   

    ## Graph Stuff=======================================================
    uplot.plot(pos=(t , spring.u))
    kplot.plot(pos=(t, spring.k))
    ukplot.plot(pos=(t, spring.uk))
	
    print('%1.2e, %1.2e, %1.2e, %1.2e' %(t, spring.u, spring.k, spring.uk))  
    
