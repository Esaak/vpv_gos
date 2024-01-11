class Particle:
    def __init__(self, x, y, vx, vy, v_value, w_number):
        self.coord = [x, y]
        self.velocity = [vx, vy, v_value]
        self.w_number = w_number