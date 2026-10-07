import json
import random

NUM_APARTMENTS = 20
OUTPUT_FILE = "apartments.json"
LOCATIONS = ["Centru", "Floreasca", "Dristor", "Berceni", "Drumul Taberei", "Titan", "Militari"]
LOCATION_FACTOR = {
    "Centru": 1.35,
    "Floreasca": 1.30,
    "Dristor": 1.0,
    "Berceni": 0.85,
    "Drumul Taberei": 0.9,
    "Titan": 0.95,
    "Militari": 0.8,
}


def generate_apartment():
    location = random.choice(LOCATIONS)
    rooms = random.randint(1, 4)
    surface = round(rooms * random.uniform(18, 26) + random.uniform(5, 15))
    floor = random.randint(0, 10)
    bathrooms = 1 if rooms <= 2 else random.randint(1, 2)
    distance = random.randint(100, 1500)

    price = surface * 1500 * LOCATION_FACTOR[location]
    price -= distance * 5
    price += random.uniform(-5000, 5000)

    return {
        "location": location,
        "rooms": rooms,
        "surface_m2": surface,
        "floor": floor,
        "bathrooms": bathrooms,
        "distance_to_transport_m": distance,
        "price": round(price, -2),
    }


def main():
    random.seed(42)
    apartments = [generate_apartment() for _ in range(NUM_APARTMENTS)]
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(apartments, f, indent=2, ensure_ascii=False)
    print(f"Am generat {NUM_APARTMENTS} apartamente in {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
