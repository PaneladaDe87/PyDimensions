class Camera:
    def __init__(self, id, coord, angle):
        super().__init__()

        self.id = id
        self.coord = coord
        self.angle = angle

    def move(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
