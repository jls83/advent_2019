from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def reader(lines):
    res = set()

    for r, row in enumerate(lines):
        for c, cell in enumerate(row):
            if cell == '#':
                res.add(Asteroid(r, c))

    return res

def file_stripper(filename):
    with open(filename, 'r') as f:
        lines = (line.strip() for line in f.readlines())
    return lines

class Asteroid:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __repr__(self):
        return '<Asteroid ({}, {})>'.format(self.r, self.c)

    def distance(self, other):
        r_distance = self.r - other.r
        c_distance = self.c - other.c

        point_gcd = abs(gcd(r_distance, c_distance))

        r_distance_base = int(r_distance / point_gcd)
        c_distance_base = int(c_distance / point_gcd)

        return (r_distance_base, c_distance_base), point_gcd

def generate_distance_mapping(asteroid_list):
    distance_mapping = defaultdict(lambda: defaultdict(set))

    for i, asteroid in enumerate(asteroid_list):
        for inner_asteroid in asteroid_list[i+1:]:
            s1, m1 = asteroid.distance(inner_asteroid)
            s2, m2 = inner_asteroid.distance(asteroid)
            distance_mapping[asteroid][s1].add(m1)
            distance_mapping[inner_asteroid][s2].add(m2)

    return distance_mapping

if __name__ == '__main__':
    lines = file_stripper('d10_input.txt')
    asteroid_list = list(reader(lines))
    distance_mapping = generate_distance_mapping(asteroid_list)

    foo = sorted(((k, len(v.keys()))
                 for k, v in distance_mapping.items()),
                 key=lambda i: i[1],
                 reverse=True)

    print(foo[0][1])
