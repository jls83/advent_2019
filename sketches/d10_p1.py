def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Asteroid:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def distance(self, other):
        r_distance = self.r - other.r
        c_distance = self.c - other.c

        point_gcd = abs(gcd(r_distance, c_distance))

        r_distance_base = int(r_distance / point_gcd)
        c_distance_base = int(c_distance / point_gcd)

        return (r_distance_base, c_distance_base), point_gcd
