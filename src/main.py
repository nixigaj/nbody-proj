import struct


class CelestialBody:
    def __init__(self, position_x, position_y, mass, velocity_x, velocity_y, brightness):
        self.position_x = position_x
        self.position_y = position_y
        self.mass = mass
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.brightness = brightness

    def pack(self):
        # Packing the attributes into a binary structure of 8-byte doubles
        return struct.pack(
            '6d', self.position_x, self.position_y, self.mass, self.velocity_x, self.velocity_y, self.brightness)

    def unpack(self, packed_data: bytes):
        # Unpacking the binary structure back into the attributes
        self.position_x, self.position_y, self.mass, self.velocity_x, self.velocity_y, self.brightness = struct.unpack(
            '6d', packed_data)

    def __str__(self):
        return (f"Celestial Body:\n"
                f"  Position X: {self.position_x}\n"
                f"  Position Y: {self.position_y}"
                f"  Mass:       {self.mass}\n"
                f"  Velocity X: {self.velocity_x}\n"
                f"  Velocity Y: {self.velocity_y}\n"
                f"  Brightness: {self.brightness}\n")
