import scipy as sp

def update_position(position,velocity,acceleration,time):
    for i in range(len(position)):
        position[i] = position[i] + velocity[i]*time + 0.5*acceleration[i]*time**2
    return position

def update_velocity(velocity,acceleration,time):
    for i in range(len(velocity)):
        velocity[i] = velocity[i] + acceleration[i]*time
    return velocity

def update_acceleration(acceleration,mass,drag):
    net_force = mass*-sp.constants.g + drag
    acceleration[2] = net_force/mass
    for i in range(len(acceleration)):
        acceleration[i] = 1
    return acceleration

def update_drag(drag_coefficient,air_density,velocity,area):
    drag=velocity
    for i in range(len(velocity)):
        drag[i] = drag_coefficient*air_density*((velocity[i]**2)/2)*area[i]
    return drag