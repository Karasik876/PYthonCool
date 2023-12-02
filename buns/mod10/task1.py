import copy
import requests
import json

def get_data(url):
    req = requests.get(url)
    data = json.loads(req.text)
    return data

stats = ['name', 'max_atmosphering_speed', 'starship_class', 'pilots']
pilot_stats = ['height', 'mass', 'name', 'homeworld']
pilot_dict = dict()
pilots = []
res_dict = dict()
starship_data = get_data('https://swapi.dev/api/starships/10/')
for i in starship_data:
    if i in stats:
        if i!='pilots':
            res_dict[i] = starship_data[i]
        else:
            for pilot in starship_data[i]:
                pilot_data = get_data(pilot)
                for i in pilot_data:
                    if i in pilot_stats:
                        if i!='homeworld':
                            pilot_dict[i] = pilot_data[i]
                        else:
                            planet_data = get_data(pilot_data[i])
                            pilot_dict[i] = planet_data['name']
                            pilot_dict['homeworld_url'] = pilot_data[i]
                if pilot_dict not in pilots:
                    pilots.append(copy.deepcopy(pilot_dict))
            res_dict['pilots']=pilots

with open('my_swapi_file.json', 'w') as file:
    json.dump(res_dict, file, indent=4)


print(json.dumps(res_dict, indent=4))

