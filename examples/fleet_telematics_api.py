#!/usr/bin/env python

from herepy import FleetTelematicsApi, RouteMode, MultiplePickupOfferType

fleet_telematics_api = FleetTelematicsApi(api_key="api_key")

# finds time-optimized waypoint sequence route.
start = str.format("{0};{1},{2}", "WiesbadenCentralStation", 50.0715, 8.2434)
intermediate_destinations = [
    str.format("{0};{1},{2}", "FranfurtCentralStation", 50.1073, 8.6647),
    str.format("{0};{1},{2}", "DarmstadtCentralStation", 49.8728, 8.6326),
    str.format("{0};{1},{2}", "FrankfurtAirport", 50.0505, 8.5698),
]
end = str.format("{0};{1},{2}", "MainzCentralStation", 50.0021, 8.259)
modes = [
    RouteMode.fastest,
    RouteMode.car,
    RouteMode.traffic_enabled,
]
response = fleet_telematics_api.find_sequence(
    start=start,
    departure="2014-12-09T09:30:00%2b01:00",
    intermediate_destinations=intermediate_destinations,
    end=end,
    modes=modes,
)
print(response.as_dict())

# finds cheaper route by picking up some additional goods along the route.
modes = [
    RouteMode.fastest,
    RouteMode.car,
    RouteMode.traffic_enabled,
]
start = str.format(
    "{0},{1};{2}:{3},value:{4}",
    50.115620,
    8.631210,
    MultiplePickupOfferType.pickup.__str__(),
    "GRAPEFRUITS",
    1000,
)
departure = "2016-10-14T07:30:00+02:00"
capacity = 10000
vehicle_cost = 0.29
driver_cost = 20
max_detour = 60
rest_times = "disabled"
intermediate_destinations = [
    str.format(
        "{0},{1};{2}:{3},value:{4}",
        50.118578,
        8.636551,
        MultiplePickupOfferType.drop.__str__(),
        "APPLES",
        30,
    ),
    str.format(
        "{0},{1};{2}:{3}",
        50.122540,
        8.631070,
        MultiplePickupOfferType.pickup.__str__(),
        "BANANAS",
    ),
]
end = str.format("{1},{2}", "MainzCentralStation", 50.132540, 8.649280)
response = fleet_telematics_api.find_pickups(
    modes=modes,
    start=start,
    departure=departure,
    capacity=capacity,
    vehicle_cost=vehicle_cost,
    driver_cost=driver_cost,
    max_detour=max_detour,
    rest_times=rest_times,
    intermediate_destinations=intermediate_destinations,
    end=end,
)
