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

    @property
    def total_orbit_count(self):
        if not self.orbit_center:
            return 0
        return 1 + self.orbit_center.total_orbit_count

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

    print(get_total_orbit_count(object_dict))

