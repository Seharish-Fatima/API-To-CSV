import requests
import csv

api_url = ("https://api.open-meteo.com/weather?latitude=37.7749&longitude=-122.4194&hourly=temperature_2m,"
           "relative_humidity_2m,dew_point_2m,apparent_temperature,precipitation,rain,snowfall,snow_depth,"
           "weather_code,pressure_msl,surface_pressure,cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,"
           "wind_speed_10m,wind_direction_10m,is_day,sunshine_duration&daily=")

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    hourly_data = data.get('hourly', [])

    if hourly_data:
        csv_filename = "weather_data.csv"

        # Writing data to CSV
        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Writing header
            header = hourly_data[0].keys()
            csv_writer.writerow(header)

            # Writing data rows
            for entry in hourly_data:
                csv_writer.writerow(entry.values())

        print(f"Data has been successfully written to {csv_filename}")
    else:
        print("No hourly data found in the API response.")
else:
    print(f"Failed to fetch data from the API. Status code: {response.status_code}")
