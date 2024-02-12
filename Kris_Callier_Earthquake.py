import requests
import json


def load_data(url):
    web = requests.get(url)
    earthquake_dict = None
    if web.satus_code == 200:
        earthquake_dict = json.loads(web.content)
    else:
        print('There was an HTTP error with the request')
        return earthquake_dict


def count_events(info):
    """
    Counts the total number of events in the earthquake data.

    Parameters:
    data (dict): A dictionary containing earthquake data in JSON format.

    Returns:
    int: The total number of events in the earthquake data.
    """
    return info["metadata"]["count"]


def count_felt_reports(info):
    """
    Counts the number of events where at least 1 person reported feeling something.

    Parameters:
    data (dict): A dictionary containing earthquake data in JSON format.

    Returns:
    int: The number of events where at least 1 person reported feeling something.
    """
    events_with_felt_reports = 0
    for event in info["features"]:
        if event["properties"]["felt"] is not None:
            events_with_felt_reports += 1
    return events_with_felt_reports


def count_events_with_mag_greater_than_4(info):
    """
    Counts the number of events with a magnitude greater than 4.

    Parameters:
    data (dict): A dictionary containing earthquake data in JSON format.

    Returns:
    int: The number of events with a magnitude greater than 4.
    """
    mag_greater_than_4 = 0
    for event in info["features"]:
        if event["properties"]["mag"] > 4:
            mag_greater_than_4 += 1
    return mag_greater_than_4


if __name__ == "__main__":
    # Make a request to the USGS API to retrieve earthquake data
    response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")

    # Convert the response to JSON format
    data = json.loads(response.text)

    # Call the functions to process the data
    total_events = count_events(data)
    events_with_felt_reports = count_felt_reports(data)
    events_with_mag_greater_than_4 = count_events_with_mag_greater_than_4(data)

    # Display the results
    print("Total number of events: " + str(total_events))
    print("Number of events with at least 1 felt report: " + str(events_with_felt_reports))
    print("Number of events with magnitude greater than 4: " + str(events_with_mag_greater_than_4))
