from day20.particle import Particle

with open('input.txt') as f:
    particles = [Particle(l.rstrip(), i) for i, l in enumerate(f)]

while True:
    positions = {}
    collisions = set()
    for particle in particles:
        particle.tick()
        if particle.position not in positions:
            positions[particle.position] = particle
        else:
            collisions.add(particle)
            collisions.add(positions[particle.position])

    for collided in collisions:
        particles.remove(collided)

    print(len(particles))
