__author__ = 'Timothy Lam'

import urllib.parse
import requests
import config
import datetime as dt

'''
main_api = "https://api.tfl.gov.uk/"
json_data = requests.get(main_api).json()

print(json_data[0]['lineStatuses'][0]['statusSeverityDescription'])

a = [
    {'$type': 'Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities', 'id': 'victoria', 'name': 'Victoria', 'modeName': 'tube', 'disruptions': [], 'created': '2019-11-12T13:42:45.39Z', 'modified': '2019-11-12T13:42:45.39Z',
     'lineStatuses':
        [{'$type': 'Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities', 'id': 0, 'statusSeverity': 10, 'statusSeverityDescription': 'Good Service', 'created': '0001-01-01T00:00:00', 'validityPeriods': []}],
     'routeSections': [], 'serviceTypes': [{'$type': 'Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities', 'name': 'Regular', 'uri': '/Line/Route?ids=Victoria&serviceTypes=Regular'},
                                           {'$type': 'Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities', 'name': 'Night', 'uri': '/Line/Route?ids=Victoria&serviceTypes=Night'}],
     'crowding': {'$type': 'Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities'}}
]
print(a[0])

'''

b = [
    {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "bakerloo",
        "name": "Bakerloo",
        "modeName": "tube",
        "disruptions": [],
        "created": "2019-11-12T13:42:45.383Z",
        "modified": "2019-11-12T13:42:45.383Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "statusSeverity": 10,
                "statusSeverityDescription": "Good Service",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": []
            }
        ],
        "routeSections": [],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=Bakerloo&serviceTypes=Regular"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    },
    {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "central",
        "name": "Central",
        "modeName": "tube",
        "disruptions": [],
        "created": "2019-11-12T13:42:45.38Z",
        "modified": "2019-11-12T13:42:45.38Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "statusSeverity": 10,
                "statusSeverityDescription": "Good Service",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": []
            }
        ],
        "routeSections": [],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=Central&serviceTypes=Regular"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Night",
                "uri": "/Line/Route?ids=Central&serviceTypes=Night"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    },
    {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "circle",
        "name": "Circle",
        "modeName": "tube",
        "disruptions": [],
        "created": "2019-11-12T13:42:45.38Z",
        "modified": "2019-11-12T13:42:45.38Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "statusSeverity": 10,
                "statusSeverityDescription": "Good Service",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": []
            }
        ],
        "routeSections": [],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=Circle&serviceTypes=Regular"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    },
    {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "district",
        "name": "District",
        "modeName": "tube",
        "disruptions": [],
        "created": "2019-11-12T13:42:45.39Z",
        "modified": "2019-11-12T13:42:45.39Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "statusSeverity": 10,
                "statusSeverityDescription": "Good Service",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": []
            }
        ],
        "routeSections": [],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=District&serviceTypes=Regular"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    },
    {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "hammersmith-city",
        "name": "Hammersmith & City",
        "modeName": "tube",
        "disruptions": [],
        "created": "2019-11-12T13:42:45.403Z",
        "modified": "2019-11-12T13:42:45.403Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "statusSeverity": 10,
                "statusSeverityDescription": "Good Service",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": []
            }
        ],
        "routeSections": [],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=Hammersmith & City&serviceTypes=Regular"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    },
    {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "jubilee",
        "name": "Jubilee",
        "modeName": "tube",
        "disruptions": [],
        "created": "2019-11-12T13:42:45.383Z",
        "modified": "2019-11-12T13:42:45.383Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "statusSeverity": 10,
                "statusSeverityDescription": "Good Service",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": []
            }
        ],
        "routeSections": [],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=Jubilee&serviceTypes=Regular"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Night",
                "uri": "/Line/Route?ids=Jubilee&serviceTypes=Night"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    },
    {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "metropolitan",
        "name": "Metropolitan",
        "modeName": "tube",
        "disruptions": [],
        "created": "2019-11-12T13:42:45.38Z",
        "modified": "2019-11-12T13:42:45.38Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "statusSeverity": 10,
                "statusSeverityDescription": "Good Service",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": []
            }
        ],
        "routeSections": [],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=Metropolitan&serviceTypes=Regular"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    },
    {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "northern",
        "name": "Northern",
        "modeName": "tube",
        "disruptions": [],
        "created": "2019-11-12T13:42:45.38Z",
        "modified": "2019-11-12T13:42:45.38Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "statusSeverity": 10,
                "statusSeverityDescription": "Good Service",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": []
            }
        ],
        "routeSections": [],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=Northern&serviceTypes=Regular"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Night",
                "uri": "/Line/Route?ids=Northern&serviceTypes=Night"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    },
    {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "piccadilly",
        "name": "Piccadilly",
        "modeName": "tube",
        "disruptions": [],
        "created": "2019-11-12T13:42:45.397Z",
        "modified": "2019-11-12T13:42:45.397Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "statusSeverity": 10,
                "statusSeverityDescription": "Good Service",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": []
            }
        ],
        "routeSections": [],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=Piccadilly&serviceTypes=Regular"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Night",
                "uri": "/Line/Route?ids=Piccadilly&serviceTypes=Night"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    },
    {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "victoria",
        "name": "Victoria",
        "modeName": "tube",
        "disruptions": [],
        "created": "2019-11-12T13:42:45.39Z",
        "modified": "2019-11-12T13:42:45.39Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "statusSeverity": 10,
                "statusSeverityDescription": "Good Service",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": []
            }
        ],
        "routeSections": [],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=Victoria&serviceTypes=Regular"
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Night",
                "uri": "/Line/Route?ids=Victoria&serviceTypes=Night"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    },
    {
        "$type": "Tfl.Api.Presentation.Entities.Line, Tfl.Api.Presentation.Entities",
        "id": "waterloo-city",
        "name": "Waterloo & City",
        "modeName": "tube",
        "disruptions": [],
        "created": "2019-11-12T13:42:45.38Z",
        "modified": "2019-11-12T13:42:45.38Z",
        "lineStatuses": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineStatus, Tfl.Api.Presentation.Entities",
                "id": 0,
                "statusSeverity": 10,
                "statusSeverityDescription": "Good Service",
                "created": "0001-01-01T00:00:00",
                "validityPeriods": []
            }
        ],
        "routeSections": [],
        "serviceTypes": [
            {
                "$type": "Tfl.Api.Presentation.Entities.LineServiceTypeInfo, Tfl.Api.Presentation.Entities",
                "name": "Regular",
                "uri": "/Line/Route?ids=Waterloo & City&serviceTypes=Regular"
            }
        ],
        "crowding": {
            "$type": "Tfl.Api.Presentation.Entities.Crowding, Tfl.Api.Presentation.Entities"
        }
    }
]


def tfl(message):
    if message[:23] == 'tfl tube service report':
        reply = tfl_tube_status()
        return reply

    elif message[:25] == 'tfl journey duration from':  # e.g tfl journey duration from se1 5hp to se18 3px
        detail = message.strip().lower()[25:].split(' to')
        #print(detail[0].strip(), detail[1].strip())
        reply = journey_duration(detail[0].strip(), detail[1].strip())
        return reply

    elif message[:21] == 'tfl live arrivals for':  # e.g tfl live arrivals for 53 at dunton road
        detail = message.strip().lower()[21:].split(' at')
        reply = get_timetable(detail[0].strip(), detail[1].strip())
        return reply
    else:
        return "Yes I know"


def get_naptan_id(station_id):
    query = f"https://api.tfl.gov.uk/Stoppoint/{station_id}"
    #print(station_id)
    json_data = requests.get(query).json()
    nap_ids = []
    for i in json_data["lineGroup"]:
        try:
            nap_ids.append(i["naptanIdReference"])
        except KeyError:
            continue
    # return json_data["lineGroup"][0]["naptanIdReference"]
    #print("id: ", nap_ids)
    return nap_ids


def get_bus_station_id(station):
    query = "https://api.tfl.gov.uk/StopPoint/Search/"
    query += station
    json_data = requests.get(query).json()
    """
    sample data structure
    {"$type":"Tfl.Api.Presentation.Entities.SearchResponse, Tfl.Api.Presentation.Entities","query":"Green Park Underground Station","total":1,"matches":[{"$type":"Tfl.Api.Presentation.Entities.MatchedStop, Tfl.Api.Presentation.Entities","icsId":"1000093","topMostParentId":"940GZZLUGPK","modes":["tube","bus"],"zone":"1","id":"940GZZLUGPK","name":"Green Park Underground Station","lat":51.506947,"lon":-0.142787}]}
    """
    s_id = json_data['matches'][0]['id']
    return get_naptan_id(s_id)


def get_station_code(station_id, line):
    query = f"https://api.tfl.gov.uk/Stoppoint/{station_id}"
    json_data = requests.get(query).json()

    for i in json_data["lineGroup"]:
        if i["lineIdentifier"][0] == line.lower():
            return i["stationAtcoCode"]
    # return json_data["lineGroup"][0]["naptanIdReference"]


def get_train_station_id(station, line):
    query = "https://api.tfl.gov.uk/StopPoint/Search/"
    if "and" in station:
        station = station.replace(" and ", " & ")
    query += station
    json_data = requests.get(query).json()
    """
    sample data structure
    {"$type":"Tfl.Api.Presentation.Entities.SearchResponse, Tfl.Api.Presentation.Entities","query":"Green Park Underground Station","total":1,"matches":[{"$type":"Tfl.Api.Presentation.Entities.MatchedStop, Tfl.Api.Presentation.Entities","icsId":"1000093","topMostParentId":"940GZZLUGPK","modes":["tube","bus"],"zone":"1","id":"940GZZLUGPK","name":"Green Park Underground Station","lat":51.506947,"lon":-0.142787}]}
    """
    s_id = json_data['matches'][0]['id']
    return get_station_code(s_id, line)


def format_time(time):
    # "2019-11-16T15:01:37Z"
    date = time[0].split('-')
    t_time = time[1][:-1].split(':')
    raw_time = date + t_time
    _time = []
    for i in raw_time:
        _time.append(int(i))

    return dt.datetime(_time[0], _time[1], _time[2], _time[3], _time[4], _time[5])


def get_timetable(line, station):
    try:
        if line.strip()[-1].isnumeric():
            station_ids = get_bus_station_id(station)
            #print(station_ids)
            reply = f"Time Table for {station}: "

            for nap_id in station_ids:
                query = f"https://api.tfl.gov.uk/Line/{line}/Arrivals/{nap_id}?app_id={config.tfl_id}&app_key={config.tfl_Keys}"
                json_data = requests.get(query).json()
                if not json_data:
                    continue
                """
                sample data structure
                
                """
                js_data = [
                    {
                        "$type": "Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities",
                        "id": "2114623668",
                        "operationType": 1,
                        "vehicleId": "201",
                        "naptanId": "940GZZLUGPK",
                        "stationName": "Green Park Underground Station",
                        "lineId": "victoria",
                        "lineName": "Victoria",
                        "platformName": "Southbound - Platform 4",
                        "direction": "inbound",
                        "bearing": "",
                        "destinationNaptanId": "940GZZLUBXN",
                        "destinationName": "Brixton Underground Station",
                        "timestamp": "2019-11-16T00:15:39.8032218Z",
                        "timeToStation": 505,
                        "currentLocation": "Between Highbury & Islington and Kings Cross St. P",
                        "towards": "Brixton",
                        "expectedArrival": "2019-11-16T00:24:04Z",
                        "timeToLive": "2019-11-16T00:24:04Z",
                        "modeName": "tube",
                        "timing": {
                            "$type": "Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities",
                            "countdownServerAdjustment": "00:00:00",
                            "source": "0001-01-01T00:00:00",
                            "insert": "0001-01-01T00:00:00",
                            "read": "2019-11-16T00:16:17.922Z",
                            "sent": "2019-11-16T00:15:39Z",
                            "received": "0001-01-01T00:00:00"
                        }
                    },
                    {
                        "$type": "Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities",
                        "id": "-1016541864",
                        "operationType": 1,
                        "vehicleId": "205",
                        "naptanId": "940GZZLUGPK",
                        "stationName": "Green Park Underground Station",
                        "lineId": "victoria",
                        "lineName": "Victoria",
                        "platformName": "Northbound - Platform 3",
                        "direction": "outbound",
                        "bearing": "",
                        "destinationNaptanId": "940GZZLUWWL",
                        "destinationName": "Walthamstow Central Underground Station",
                        "timestamp": "2019-11-16T00:15:39.8032218Z",
                        "timeToStation": 115,
                        "currentLocation": "Between Victoria and Green Park",
                        "towards": "Walthamstow Central",
                        "expectedArrival": "2019-11-16T00:17:34Z",
                        "timeToLive": "2019-11-16T00:17:34Z",
                        "modeName": "tube",
                        "timing": {
                            "$type": "Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities",
                            "countdownServerAdjustment": "00:00:00",
                            "source": "0001-01-01T00:00:00",
                            "insert": "0001-01-01T00:00:00",
                            "read": "2019-11-16T00:16:17.922Z",
                            "sent": "2019-11-16T00:15:39Z",
                            "received": "0001-01-01T00:00:00"
                        }
                    },
                    {
                        "$type": "Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities",
                        "id": "-1596964419",
                        "operationType": 1,
                        "vehicleId": "206",
                        "naptanId": "940GZZLUGPK",
                        "stationName": "Green Park Underground Station",
                        "lineId": "victoria",
                        "lineName": "Victoria",
                        "platformName": "Northbound - Platform 3",
                        "direction": "outbound",
                        "bearing": "",
                        "destinationNaptanId": "940GZZLUWWL",
                        "destinationName": "Walthamstow Central Underground Station",
                        "timestamp": "2019-11-16T00:15:39.8032218Z",
                        "timeToStation": 505,
                        "currentLocation": "At Stockwell",
                        "towards": "Walthamstow Central",
                        "expectedArrival": "2019-11-16T00:24:04Z",
                        "timeToLive": "2019-11-16T00:24:04Z",
                        "modeName": "tube",
                        "timing": {
                            "$type": "Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities",
                            "countdownServerAdjustment": "00:00:00",
                            "source": "0001-01-01T00:00:00",
                            "insert": "0001-01-01T00:00:00",
                            "read": "2019-11-16T00:16:17.922Z",
                            "sent": "2019-11-16T00:15:39Z",
                            "received": "0001-01-01T00:00:00"
                        }
                    },
                    {
                        "$type": "Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities",
                        "id": "238539794",
                        "operationType": 1,
                        "vehicleId": "207",
                        "naptanId": "940GZZLUGPK",
                        "stationName": "Green Park Underground Station",
                        "lineId": "victoria",
                        "lineName": "Victoria",
                        "platformName": "Southbound - Platform 4",
                        "direction": "inbound",
                        "bearing": "",
                        "destinationNaptanId": "940GZZLUBXN",
                        "destinationName": "Brixton Underground Station",
                        "timestamp": "2019-11-16T00:15:39.8032218Z",
                        "timeToStation": 295,
                        "currentLocation": "At Warren Street",
                        "towards": "Brixton",
                        "expectedArrival": "2019-11-16T00:20:34Z",
                        "timeToLive": "2019-11-16T00:20:34Z",
                        "modeName": "tube",
                        "timing": {
                            "$type": "Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities",
                            "countdownServerAdjustment": "00:00:00",
                            "source": "0001-01-01T00:00:00",
                            "insert": "0001-01-01T00:00:00",
                            "read": "2019-11-16T00:16:17.922Z",
                            "sent": "2019-11-16T00:15:39Z",
                            "received": "0001-01-01T00:00:00"
                        }
                    },
                    {
                        "$type": "Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities",
                        "id": "-613543127",
                        "operationType": 1,
                        "vehicleId": "242",
                        "naptanId": "940GZZLUGPK",
                        "stationName": "Green Park Underground Station",
                        "lineId": "victoria",
                        "lineName": "Victoria",
                        "platformName": "Southbound - Platform 4",
                        "direction": "inbound",
                        "bearing": "",
                        "destinationNaptanId": "940GZZLUBXN",
                        "destinationName": "Brixton Underground Station",
                        "timestamp": "2019-11-16T00:15:39.8032218Z",
                        "timeToStation": 985,
                        "currentLocation": "At Seven Sisters Platform 5",
                        "towards": "Brixton",
                        "expectedArrival": "2019-11-16T00:32:04Z",
                        "timeToLive": "2019-11-16T00:32:04Z",
                        "modeName": "tube",
                        "timing": {
                            "$type": "Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities",
                            "countdownServerAdjustment": "00:00:00",
                            "source": "0001-01-01T00:00:00",
                            "insert": "0001-01-01T00:00:00",
                            "read": "2019-11-16T00:16:17.922Z",
                            "sent": "2019-11-16T00:15:39Z",
                            "received": "0001-01-01T00:00:00"
                        }
                    },
                    {
                        "$type": "Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities",
                        "id": "1715108579",
                        "operationType": 1,
                        "vehicleId": "274",
                        "naptanId": "940GZZLUGPK",
                        "stationName": "Green Park Underground Station",
                        "lineId": "victoria",
                        "lineName": "Victoria",
                        "platformName": "Southbound - Platform 4",
                        "direction": "inbound",
                        "bearing": "",
                        "destinationNaptanId": "940GZZLUBXN",
                        "destinationName": "Brixton Underground Station",
                        "timestamp": "2019-11-16T00:15:39.8032218Z",
                        "timeToStation": 175,
                        "currentLocation": "At Oxford Circus",
                        "towards": "Brixton",
                        "expectedArrival": "2019-11-16T00:18:34Z",
                        "timeToLive": "2019-11-16T00:18:34Z",
                        "modeName": "tube",
                        "timing": {
                            "$type": "Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities",
                            "countdownServerAdjustment": "00:00:00",
                            "source": "0001-01-01T00:00:00",
                            "insert": "0001-01-01T00:00:00",
                            "read": "2019-11-16T00:16:17.922Z",
                            "sent": "2019-11-16T00:15:39Z",
                            "received": "0001-01-01T00:00:00"
                        }
                    }
                ]
                dict_time = {}
                for i in json_data:
                    dict_time[json_data.index(i)] = format_time(i["expectedArrival"].split('T'))
                min_time = min(dict_time, key=dict_time.get)

                reply += f" \nThe expected arrival Time for {json_data[min_time]['lineName']} " \
                         f"in bus stop {json_data[min_time]['platformName']} on {json_data[min_time]['stationName']} " \
                         f"travelling towards {json_data[min_time]['destinationName']} " \
                         f"is {json_data[min_time]['expectedArrival'].split('T')[1][:-1]}"

            if reply == f"Time Table for {station}: ":
                return f"{line} does not call at {station}"

            return reply
        else:

            if station.lower().split()[-1] != "station":
                station += " station"

            #print(station)
            station_id = get_train_station_id(station, line)
            reply = f"Time Table for {station}: "
            query = f"https://api.tfl.gov.uk/Line/{line}/Arrivals/{station_id}?app_id={config.tfl_id}&app_key={config.tfl_Keys}"
            json_data = requests.get(query).json()
            #print(json_data)
            outbound_dict_time = {}
            inbound_dict_time = {}

            for i in json_data:
                if i["direction"] == "outbound":
                    outbound_dict_time[json_data.index(i)] = format_time(i["expectedArrival"].split('T'))
                else:
                    inbound_dict_time[json_data.index(i)] = format_time(i["expectedArrival"].split('T'))
            if outbound_dict_time:
                out_min_time = min(outbound_dict_time, key=outbound_dict_time.get)
                reply += f" \nThe expected arrival Time for {json_data[out_min_time]['lineName']} " \
                         f"in {json_data[out_min_time]['platformName']} on {json_data[out_min_time]['stationName']} " \
                         f"travelling towards {json_data[out_min_time]['destinationName']} " \
                         f"is {json_data[out_min_time]['expectedArrival'].split('T')[1][:-1]}"
            if inbound_dict_time:
                in_min_time = min(inbound_dict_time, key=inbound_dict_time.get)
                reply += f" \nThe expected arrival Time for {json_data[in_min_time]['lineName']} " \
                         f"in {json_data[in_min_time]['platformName']} on {json_data[in_min_time]['stationName']} " \
                         f"travelling towards {json_data[in_min_time]['destinationName']} " \
                         f"is {json_data[in_min_time]['expectedArrival'].split('T')[1][:-1]}"

            return reply

    except KeyboardInterrupt:
        #return "Sorry, I can't find the line or station name"
        return 'stopped'


def tfl_tube_status():
    main_api = f"https://api.tfl.gov.uk/Line/Mode/tube/Status?app_id={config.tfl_id}&app_key={config.tfl_Keys}"
    json_data = requests.get(main_api).json()
    reply = "TFL Tube Service Report"
    for i in json_data:
        reply += f"\n{i['name']} : {i['lineStatuses'][0]['statusSeverityDescription']}"

    return reply


def journey_duration(start, stop):
    try:
        main_api = f"https://api.tfl.gov.uk/Journey/JourneyResults/{start}/to/{stop}?app_id={config.tfl_id}&app_key={config.tfl_Keys}"
        json_data = requests.get(main_api).json()
        start_time = json_data["journeys"][0]["startDateTime"].split('T')[1][:-1]  # "2019-11-16T16:14:00"
        arrival_time = json_data["journeys"][0]["arrivalDateTime"].split('T')[1][:-1]  # "2019-11-16T16:45:00"
        duration = json_data["journeys"][0]["duration"]
        return f"If you leave by {start_time}, you will arrive at {stop} by {arrival_time}" \
               f"\nTherefore, It will take {duration}mins"
    except Exception as e:
        return "Ask me another question"

# get_station_id("victoria station")
#print(get_timetable("115", "aldgate underground station"))
# print(get_timetable("northern", "elephant & castle underground station"))
#print(get_timetable("northern", "bank underground station"))
# print(format_time("2019-11-16T15:01:37Z".split('T')))
#print(journey_duration(start="se18 3px", stop="se1 5hp"))
