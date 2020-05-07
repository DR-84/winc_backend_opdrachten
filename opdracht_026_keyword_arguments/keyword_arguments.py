# ---------------opdracht 1---------------


def force_needed(mass, gravity=9.798):
    mass_kg = mass
    newton = mass_kg * gravity
    print(f"{newton} N")


force_needed(mass=0.1,)
force_needed(mass=800)
force_needed(mass=0.1, gravity=24.92)
force_needed(mass=0.015, gravity=274)


def force_needed_automatic(mass, gravity=9.798):
    for item in mass:
        for body in gravity:
            newton = item["mass"] * body["gravity"]
            body = body["cel_body"]
            item_name = item["name"]
            newton_round = str(round(newton, 2))
            result = f"Het kost {newton_round} Newton aan kracht"
            result += f" om op {body} een {item_name} vast te houden."
            print(result)


gravity_cel_body = [
    {"cel_body": "earth", "gravity": 9.798},
    {"cel_body": "jupiter", "gravity": 24.92},
    {"cel_body": "sun", "gravity": 274},
]

items = [
    {"name": "appel", "mass": 0.1},
    {"name": "koe", "mass": 800},
    {"name": "reep_chocola", "mass": 0.1},
    {"name": "contactlens", "mass": 0.015},
]

# force_needed_automatic(items, gravity_cel_body)

# ---------------opdracht 2---------------


def gravity_between_objects(object_one, object_two, distance):
    m1_m2 = object_one * object_two
    d2 = distance ** 2
    kg_divided_m = m1_m2 / d2
    G = 6.674 * (10 ** (-11))
    result = G * kg_divided_m
    pretty_result = "{:f}".format(result)
    print(pretty_result)


# gravity_between_objects(object_one=800, object_two=1500, distance=3)
# gravity_between_objects(object_one=800, object_two=1500, distance=3)

# ---------------opdracht 2---------------

# Distance is in AU https://en.wikipedia.org/wiki/Astronomical_unit

distances = [
    {"from": "Mercury", "to": "Venus", "distance": 0.34},
    {"from": "Mercury", "to": "Earth", "distance": 0.61},
    {"from": "Mercury", "to": "Mars", "distance": 1.14},
    {"from": "Mercury", "to": "Jupiter", "distance": 4.82},
    {"from": "Mercury", "to": "Saturn", "distance": 9.14},
    {"from": "Mercury", "to": "Uranus", "distance": 18.82},
    {"from": "Mercury", "to": "Neptune", "distance": 29.70},
    {"from": "Venus", "to": "Earth", "distance": 0.28},
    {"from": "Venus", "to": "Mars", "distance": 0.8},
    {"from": "Venus", "to": "Jupiter", "distance": 4.48},
    {"from": "Venus", "to": "Saturn", "distance": 8.80},
    {"from": "Venus", "to": "Uranus", "distance": 18.49},
    {"from": "Venus", "to": "Neptune", "distance": 29.37},
    {"from": "Earth", "to": "Mars", "distance": 0.52},
    {"from": "Earth", "to": "Jupiter", "distance": 4.2},
    {"from": "Earth", "to": "Saturn", "distance": 8.52},
    {"from": "Earth", "to": "Uranus", "distance": 18.21},
    {"from": "Earth", "to": "Neptune", "distance": 29.09},
    {"from": "Mars", "to": "Jupiter", "distance": 3.68},
    {"from": "Mars", "to": "Saturn", "distance": 7.99},
    {"from": "Mars", "to": "Uranus", "distance": 17.69},
    {"from": "Mars", "to": "Neptune", "distance": 28.56},
    {"from": "Jupiter", "to": "Saturn", "distance": 4.32},
    {"from": "Jupiter", "to": "Uranus", "distance": 14.01},
    {"from": "Jupiter", "to": "Neptune", "distance": 24.89},
    {"from": "Saturn", "to": "Uranus", "distance": 9.7},
    {"from": "Saturn", "to": "Neptune", "distance": 20.57},
    {"from": "Uranus", "to": "Neptune", "distance": 10.88},
]

# Weight is in 10 ** 24 kg
weights = {
    "Mercury": 0.33,
    "Venus": 4.87,
    "Earth": 5.97,
    "Mars": 0.642,
    "Jupiter": 1898,
    "Saturn": 568,
    "Uranus": 86.8,
    "Neptune": 102,
}


def data_for_math(distances, weights):
    for info in distances:
        if info["from"] in weights:
            planet1 = weights[info["from"]]
        if info["to"] in weights:
            planet2 = weights[info["to"]]
        info["from_weight"] = planet1
        info["to_weight"] = planet2
    return distances


def au_to_metres(value):
    meters_from_au = value * 149597870700
    return meters_from_au


def weight_planets_kg(value):
    planets_in_kg = value * 10 ** 24
    return planets_in_kg


def planetary_attraction(planet_distance_weight_names):
    for info in planet_distance_weight_names:
        planet1 = info["from"]
        planet2 = info["to"]
        m1_m2 = weight_planets_kg(info["from_weight"]) * weight_planets_kg(
            info["to_weight"]
        )
        d2 = au_to_metres(info["distance"]) ** 2
        kg_divided_m = m1_m2 / d2
        G = 6.674 * (10 ** (-11))
        result = G * kg_divided_m
        pretty_result = "{:f}".format(result)
        result_string = f"{planet1} en {planet2} attract each other"
        result_string += f" with {pretty_result} Newtons of force."

        print(result_string)
        print(f"Scientific notation: {result} N")


data_for_math(distances, weights)
planetary_attraction(data_for_math(distances, weights))
