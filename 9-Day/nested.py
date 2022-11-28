# capitals = {
#     "France" : "Paris",
#     "Germany" : "Berlin"
# }
#
# travel_log = {
#     "France" : { "cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12},
#     "Germany" :{"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 5} ,
# }

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]

def add_new_country(Country, VisitCount, Cities):
    travel_log.append({"Country" : Country, "cities_visited" : Cities, "total_visits" : VisitCount })
    print(travel_log)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])