class Particle:

    def __init__(self, input_text: str, idx: int):
        self.idx = idx
        pva_str = [prop[3:-1] for prop in input_text.split(', ')]
        p, v, a = tuple([pva.split(',') for pva in pva_str])
        self.position = tuple([int(coord) for coord in p])
        self.velocity = tuple([int(coord) for coord in v])
        self.acceleration = tuple([int(coord) for coord in a])

    def tick(self):
        px, py, pz = self.position
        vx, vy, vz = self.velocity
        ax, ay, az = self.acceleration
        vx += ax
        vy += ay
        vz += az
        px += vx
        py += vy
        pz += vz
        self.position = px, py, pz
        self.velocity = vx, vy, vz
        self.acceleration = ax, ay, az

    def distance_to_origin(self):
        x, y, z = self.position
        return abs(x) + abs(y) + abs(z)
