from visual import *
#Chester Holtz
#28264729
#Program to study a one-dimensional motion of an electron.

scene = display (autoscale = 0, center = (1500,0,0), range = (2000,2000,2000))
topline = curve(pos=[(0,200,0), (3000,200,0)], color=color.red, radius=10)
botline = curve(pos=[(0,-200,0), (3000,-200,0)], color=color.red, radius=10)

electron = sphere()
c = 3.0e8               # Constant speed of light
electron.mass = 9.0e-31 # Mass of the electron.
electron.radius = 100   # The radius is defined to make the electron
                        # visible on the screen.  The electron is
                        # a point-like particle (it does not have a size).
electron.pos = vector(0.0,0.0,0.0)
electron.p = vector(0.0,0.0,0.0) 
electron.orbit = curve(radius = 25)

# Define the force, the stepsize, etc.
F = vector(2.0e-12,0,0)     # Force in N, directed along the x axis.
time = 0                    # Start time (in s).
dt = 1.0e-10                # Step size (in s).
nstep = 0                   # Step number.
xmax = 3000.0               # Distance travelled by the electron


# print information about the position of the electron
# as it progresses through the accelerator.
print ' '
print 'Properties of the electron before passing the finish line:'
print 'time(s)  x(m)     K(J)     p(kgm/s) v(m/s)   v/c'

while (electron.pos.x < xmax):
  rate(10000)
  time = time + dt
  nstep = nstep + 1
  
  # Calculate the new momentum of the electron.
  # The momentum principle applies in the relativistic regime.
  electron.p = electron.p + F*dt

  # Update the position of the electron and its track.
  # Note: this calculation is ONLY correct in the non-relativistic regime.
# electron.pos = electron.pos + electron.p/electron.mass * dt

  #new position calculated by adding the velocity
  #- computer by solving the relativistic momentum for v - to the old position
  electron.pos = electron.pos + (c*electron.p/math.sqrt((c**2)*(electron.mass**2)+mag(electron.p)**2)) * dt
  electron.orbit.append(pos=electron.pos)

  # Print information about the energy, the momentum, and the speed of the
  # electron to the output.  In addition, add the time of flight.

#new velocity and kinetic energy solved to account for high velocities 
  v = c*mag(electron.p)/math.sqrt((c**2)*(electron.mass**2)+mag(electron.p)**2)
  K = electron.mass*(c**2)*((1/(math.sqrt(1-v**2/c**2)))-1)
  
  if (nstep > 10):
      print '%1.2e %1.2e %1.2e %1.2e %1.2e %1.2e' % (time,electron.pos.x,K,mag(electron.p),v,v/3.0e8)
      nstep = 0

#new velocity and kinetic energy solved to account for high velocities
v = c*mag(electron.p)/math.sqrt((c**2)*(electron.mass**2)+mag(electron.p)**2)
K = electron.mass*(c**2)*((1/(math.sqrt(1-v**2/c**2)))-1)
  
print ' '
print 'Properties of the electron after passing the finish line:'
print 'time(s)  x(m)     K(J)     p(kgm/s) v(m/s)   v/c'
print '%1.2e %1.2e %1.2e %1.2e %1.2e %1.2e' % (time,electron.pos.x,K,mag(electron.p),v,v/3.0e8)