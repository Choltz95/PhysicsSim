#Chester Holtz
from visual import *

G = 6.673E-11              #Gravitational Constant: units m^3/(kg*s^2)
earth = sphere(pos=(0,0,0), radius = 6.3E6, color=color.blue)
earth.mass=2.0E30            #Units: kg

#ship1 - initial velocity which leads to elliptical orbit
ship1 = sphere(pos=(6.3E7,0,0), radius = 6.3E5, color=color.green)    #Units for both position and raidus: m
ship1.mass = 6.0E24        #Units: kg
ship1.velocity = vector(0,9.8E5,0)    #Units: m/s
ship1.acceleration = vector(0,0,0)    #Units: m/s^2
ship1.orbit = curve(color=color.green)     #Curve used to show path of orbit

#ship2 - initial velocity of 0 which results acceleration towards earth
ship2 = sphere(pos=(-6.3E7,0,0), radius = 6.3E5, color=color.red)
ship2.mass = 6.0E24      
ship2.velocity = vector(0,0,0)   
ship2.acceleration = vector(0,0,0)    
ship2.orbit = curve(color=color.red)

#ship3 - initial velocity to orbit...minimum initial velocity to escape gravitational pull is approx -8E6 based on escape velocity equation ((2GM)/r)^.5.
ship3 = sphere(pos=(-6.3E6,0,0), radius = 6.3E5, color=color.yellow)    
ship3.mass = 6.0E24       
ship3.velocity = vector(-8E6,0,0) 
ship3.acceleration = vector(0,0,0)    
ship3.orbit = curve(color=color.yellow)    

#time variables
t = 0            #Units: s
dt = .50
#Force variables
force_gravity = vector(0,0,0)   #Units: kg
force_ship = vector(0,0,0)     #Units: kg

force_gravity2 = vector(0,0,0)  
force_ship2 = vector(0,0,0)     

force_gravity3 = vector(0,0,0)  
force_ship3 = vector(0,0,0)    

while 1 and abs(ship1.pos) > earth.radius:      #while greater then one radius
    rate(20)
    scene.autoscale = 0
    print ship1.pos

    #Calculate the force of gravity from the earth on the ship.
    force_gravity = -G*earth.mass*ship1.mass/(mag(ship1.pos-earth.pos)**2)*norm(ship1.pos-earth.pos)
    force_gravity2 = -G*earth.mass*ship2.mass/(mag(ship2.pos-earth.pos)**2)*norm(ship2.pos-earth.pos)
    force_gravity3 = -G*earth.mass*ship3.mass/(mag(ship3.pos-earth.pos)**2)*norm(ship3.pos-earth.pos)

    #Update the acceleration, velocity, and position of ship1
    ship1.acceleration = force_gravity/ship1.mass
    ship1.velocity=ship1.velocity+ship1.acceleration*dt
    ship1.pos=ship1.pos+ship1.velocity*dt

    #Update the acceleration, velocity, and position of ship2
    ship2.acceleration = force_gravity2/ship2.mass
    ship2.velocity=ship2.velocity+ship2.acceleration*dt
    ship2.pos=ship2.pos+ship2.velocity*dt

    #Update the acceleration, velocity, and position of ship3
    ship3.acceleration = force_gravity3/ship3.mass
    ship3.velocity=ship3.velocity+ship3.acceleration*dt
    ship3.pos=ship3.pos+ship3.velocity*dt

    #Update orbit tail
    ship1.orbit.append(pos=ship1.pos)
    ship2.orbit.append(pos=ship2.pos)
    ship3.orbit.append(pos=ship3.pos)

    t=t+dt
