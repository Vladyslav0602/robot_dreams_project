import requests
from time import perf_counter
from threading import Thread
import multiprocessing
from statistics import mean

# Exercise 1 variant a
result = []

def request_weather(latitude, longitude):
    response = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m",
        }
    )
    temperature_list = response.json()["hourly"]["temperature_2m"]
    result.append(temperature_list)

start_time = perf_counter()

t1 = Thread(target=request_weather, args=(47.91, 33.39))  # Kryvyj Rih
t2 = Thread(target=request_weather, args=(34.05, -118.24))  # Los Angeles
t3 = Thread(target=request_weather, args=(50.45, 30.52))  # Kyiv
t4 = Thread(target=request_weather, args=(47.85, 35.12))  # Zaporizhzhya
t5 = Thread(target=request_weather, args=(50.21, 15.83))  # Hradec Králové

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

end_time = perf_counter()
print(f'It took {end_time - start_time:0.2f} second(s) to complete.')

# Exercise 1 variant b
def request_process_weather(latitude, longitude, result_queue):
    response = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m",
        }
    )
    temperature_list = response.json()["hourly"]["temperature_2m"]
    result_queue.put(temperature_list)

def multiproc():
    result_queue = multiprocessing.Queue()
    processes = []

    coordinates = [
        ((47.91, 33.39)),
        ((34.05, -118.24)),
        ((50.45, 30.52)),
        ((47.85, 35.12)),
        ((50.21, 15.83))
    ]

    for coordinate in coordinates:
        p = multiprocessing.Process(target=request_process_weather, args=(coordinate[0], coordinate[1], result_queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Отримуємо результати з черги
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    return results

if __name__ == "__main__":
    result_2 = multiproc()

    # Exercise 2
    average_temperatures = [mean(city_temperatures) for city_temperatures in result_2]
    hottest_city_index = average_temperatures.index(max(average_temperatures))

    cities = ["Kryvyj Rih", "Los Angeles", "Kyiv", "Zaporizhzhya", "Hradec Králové"]
    hottest_city = cities[hottest_city_index]

    print("Average Temperatures:", average_temperatures)
    print("Hottest City:", hottest_city)

    # Exercise 3
    print("Time Difference:", abs(end_time - start_time))
