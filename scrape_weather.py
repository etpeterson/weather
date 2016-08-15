#grab current weather data

import urllib.request as ur #urllib2 in python2
import json

def scrape_wunderground(features=(),state='CA',city='Mountain_View',api_key='',api_key_filename='wunderground_api_key'):
    #https://www.wunderground.com/weather/api/d/docs?d=data/index&MR=1
    #the format is 'http://api.wunderground.com/api/_api_key_/_features_1_/_features_2_/q/_state_/_city_.json'
    base_url='http://api.wunderground.com/api/'
    #print(base_url,state,city,api_key)
    #print(features)

    if api_key_filename:
        with open(api_key_filename, 'r') as myfile:
            api_key=myfile.read().replace('\n','')
        print(api_key)

    #make sure we have all the info we need
    if not api_key or not state or not city or not features:
        raise ValueError('missing vital inputs, where and what do you want to scrape?')
    
    url=base_url+api_key
    for item in features:
        print(item)
        url+='/'+item
    url+='/q/'+state+'/'+city+'.json'
    print(url)
    f = ur.urlopen(url)
    #parsed_current = json.loads(f.read())  #python2
    parsed = json.loads(f.readall().decode('utf-8'))  #python3
    f.close()
    return parsed


parsed_current = scrape_wunderground(features=('conditions','geolookup'))

#print(parsed_current)
location = parsed_current['location']['city']

#for key, value in parsed_current['current_observation'].items():
#    print(key)


#print(location)
temp_f = parsed_current['current_observation']['temp_f']
temp_c = parsed_current['current_observation']['temp_c']

print("Current temperature in %s is: %s F and %s C" % (location, temp_f, temp_c))




