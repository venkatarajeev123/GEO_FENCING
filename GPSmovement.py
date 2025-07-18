import time
path = [
    (28.6100, 77.2100),
    (28.6110, 77.2110),
    (28.6120, 77.2120),
]

for lat, lon in path:
    print(f"Current Location -> Latitude: {lat}, Longitude: {lon}")
    time.sleep(2)