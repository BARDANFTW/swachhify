import csv, os, time
from datetime import datetime
import config
import requests


print("LOADING THE AQI APP")


def local_aqi_input():
    API_KEY = config.secrets['API_KEY']
    location = config.secrets['location']
    url = f"https://api.openaq.org/v3/locations/{location}/latest"
    headers = {
        "X-API-Key": API_KEY
    }

    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            data = response.json()
            measurements = data['results']
            for item in measurements:
                if item['sensorsId'] == 14718801:
                    return round(item['value']), item ['datetime']['local'][11:16]
        else:
            print("Server reached but error")

    except requests.exceptions.RequestException:
        print("Connection failed")
        return None, None


def aqi_ph_input():
    measurements = []
    city_aqi, timestamp = local_aqi_input()
    measurements.append(
        {"pm2.5": city_aqi, "Time": timestamp})
    time.sleep(0.5)
    return measurements


def file_IO():
    measurements = aqi_ph_input()
    file_exists = os.path.isfile("project.csv")
    with open("project.csv", "a", newline="") as outf:
        writer = csv.DictWriter(outf, fieldnames=[
            "Time", "pm2.5"])
        if not file_exists:
            writer.writeheader()
        writer.writerows(measurements)
        time.sleep(1)
        print("THE DATA HAS SUCCESSFULLY BEEN STORED")


def aqi_check(aqi):
    if aqi <= 50:
        return("SAFE")
    elif aqi <= 100:
        return("MODERATE")
    elif aqi <= 150:
        return("UNHEALTHY (SENSITIVE)")
    elif aqi <= 200:
        return("UNHEALTHY")
    elif aqi <= 300:
        return("VERY UNHEALTHY")
    else:
        return ("HAZARDOUS")


def main():
    readings = aqi_ph_input()
    file_IO()
    time.sleep(0.4)
    print("DISPLAYING RESULTS")
    for data in readings:
        print(f"City AQI: {data['pm2.5']}\nTime: {data['Time']}\nResult: {aqi_check(data['pm2.5'])}")
        time.sleep(0.5)
        print("CLOSING THE PROGRAM")



if __name__ == "__main__":
    main()
