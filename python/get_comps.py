# get remote files with urls
import urllib.request as libreq
# tool to read in the response as json
import json

# unofficial api, example returns all competitions in a given country
with libreq.urlopen('https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/competitions/DE.json') as file:
    # the file is understood as json
    json_data = json.load(file)

# want to know starting and end times, and want to perform some calls once a week to populate my landing page
import datetime
# when the script runs
now = datetime.datetime.now()
# up until a week from now
d = datetime.timedelta(days=7)
oneweek_from_now = now + d

# formatting into something close to js syntax for UTC time
today = now.strftime("%Y-%m-%d")
oneweek_from_today = oneweek_from_now.strftime("%Y-%m-%d")
print(today)
print(oneweek_from_today)

# assume this script runs, say every Tuesday.
# and this will hold the relevant information per compid
upcoming_comp_info = []
# nested json, get the actual items and loop over them
for k in json_data['items']:
    # only those within one week from now
    if k['date']['from'] >= today and k['date']['from'] < oneweek_from_today:
        print(k)
        compid = k['id']
        # for every compid, there is the wcif with further info,
        # parse this as well (inside the loop for every comp that fulfils the criteria)
        with libreq.urlopen(f'https://worldcubeassociation.org/api/v0/competitions/{compid}/wcif/public') as wcif:
            comp_data = json.load(wcif)

        # walking through the nested json, pick first item wherever possible to not overcomplicate things
        # grab the earliest activity to determine from when to show the corresponding div (UTC)
        starts = min([a['startTime'] for a in comp_data['schedule']['venues'][0]['rooms'][0]['activities']]).split('T')[1][:-1]
        # grab the latest activity to determine until when to show the corresponding div (UTC)
        ends = max([a['endTime'] for a in comp_data['schedule']['venues'][0]['rooms'][0]['activities']]).split('T')[1][:-1]

        # collect everything into a 2d list, one sublist per comp
        upcoming_comp_info.append([compid,
                                   k['date']['from'],
                                   k['date']['till'],
                                   starts,
                                   ends,
                                   k['venue']['coordinates']['latitude'],
                                   k['venue']['coordinates']['longitude']])

# now we know the IDs of comps taking place the upcoming weekend, and relevant info to steer the UI
print(upcoming_comp_info)

if len(upcoming_comp_info) > 1:
    print('Multi-Comp Weekend!')
