from day20.particle import Particle

with open('input.txt') as f:
    particles = [Particle(l.rstrip(), i) for i, l in enumerate(f)]

while True:
    min_distance = None
    closest = None
    for i, particle in enumerate(particles):
        particle.tick()
        if not min_distance or particle.distance_to_origin() < min_distance:
            closest = i
            min_distance = particle.distance_to_origin()

    print(closest)
