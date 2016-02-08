class Airport(object):
    """docstring for Airport"""
    def __init__(self):
        self.planes = []

    def land(self, plane):
        self.planes.append(plane)
        return "{} has landed".format(plane)

    def takeoff(self, plane):
        self.planes.remove(plane)
        return "{} has taken off".format(plane)

