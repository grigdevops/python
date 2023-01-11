import yaml


# dict object
members = [{'User': 'Zoey', 'Password': 'Xavier@123', 'Phone': 345464, 'Skills': ['Python', 'SQL', 'Django', 'Rest Framework', 'JavaScript']},
           {'name': 'Zaara', 'occupation': 'Dentist'}]



with open("grigor.yaml", "w") as f:
    data = yaml.dump(members,f, sort_keys=False, default_flow_style=False)