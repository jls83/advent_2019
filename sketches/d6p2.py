class Planet:
    def __init__(self, name, orbit_center=None):
        self.name = name
        self.orbit_center = orbit_center

        self._satellites = set()

    def __repr__(self):
        return '<Planet: {}>'.format(self.name)

    def set_orbit_center(self, other):
        self.orbit_center = other
        other._satellites.add(self)

    def get_direct_path_to_planet(self, other):
        if other not in set(self.orbit_path):
            print('No direct path found')
            return []

        if self.orbit_center == other:
            return []
        return [self.orbit_center] + self.orbit_center.get_direct_path_to_planet(other)

    @property
    def orbit_path(self):
        if not self.orbit_center:
            return []
        return [self.orbit_center] + self.orbit_center.orbit_path

    @property
    def total_orbit_count(self):
        return len(self.orbit_path)

def create_or_get_planet(name, planet_dict):
    planet = planet_dict.get(name)
    if not planet:
        planet = Planet(name)
        planet_dict[name] = planet
    return planet

def get_total_orbit_count(object_dict):
    """
    NOTE: I __know__ we can make this more effecient, but f it.
    """
    return sum(l.total_orbit_count for l in object_dict.values())

def get_orbit_path_intersection(planet_1, planet_2):
    planet_2_path_set = set(planet_2.orbit_path)
    for p in planet_1.orbit_path:
        if p in planet_2_path_set:
            return p
    return None

if __name__ == '__main__':
    object_dict = {}

    with open('d6_input.txt', 'r') as f:
        object_name_list = [l.strip() for l in f.readlines()]

    object_name_pairs = [s.split(')') for s in object_name_list]
    # For line in file
    for pair in object_name_pairs:
        l_planet = create_or_get_planet(pair[0], object_dict)
        r_planet = create_or_get_planet(pair[1], object_dict)

        r_planet.set_orbit_center(l_planet)

    YOU = object_dict.get('YOU')
    SAN = object_dict.get('SAN')

    pivot_planet = get_orbit_path_intersection(YOU, SAN)

    path_you = YOU.get_direct_path_to_planet(pivot_planet)
    path_san = SAN.get_direct_path_to_planet(pivot_planet)

    print(len(path_you) + len(path_san))

