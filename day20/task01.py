from day20.particle import Particle

with open('input.txt') as f:
    particles = [Particle(l.rstrip(), i) for i, l in enumerate(f)]

while True:
    min_distance = None
    closest = None
    for particle in particles:
        particle.tick()
        distance = particle.distance_to_origin()
        if not min_distance or distance < min_distance:
            closest = particle.idx
            min_distance = distance

    print(closest)
