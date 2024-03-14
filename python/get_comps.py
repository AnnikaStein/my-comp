# tool to write html in a pythonic way
import dominate
from dominate.util import raw, text
from dominate.tags import *

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
                                   k['name'],
                                   k['date']['from'],
                                   k['date']['till'],
                                   starts,
                                   ends,
                                   k['venue']['coordinates']['latitude'],
                                   k['venue']['coordinates']['longitude']])


def generate_html(comp_info, multi = False):
    doc = dominate.document(title='My Comp')

    with doc.head:
        meta(charset='utf-8')
        meta(name='viewport', content='width=device-width, initial-scale=1')
        link(rel='stylesheet', href='https://www.w3schools.com/w3css/4/w3.css')
        link(rel='stylesheet', href='https://www.w3schools.com/lib/w3-theme-light-blue.css')
        link(rel='stylesheet', href='css/style.css')
        link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css')

    with doc:
        comment(' Content container ')
        # one div per comp and language
        for ic, info in enumerate(comp_info):
            # german
            with div():
                if ic == 0:
                    attr(cls='container navi', id=f'main-de-{ic}')
                else:
                    attr(cls='container', id=f'main-de-{ic}', style='display:none;')
                with div():
                    attr(cls='icons w3-padding')
                    a(raw('🇬🇧'), onclick='toggleLang()', cls='w3-button w3-round link flag')
                    if (multi):
                        a(raw('🌐'), onclick='openManualLocModal()', cls='w3-button w3-round link globe')
                comment(' Name container ')
                with div():
                    attr(cls='', style='text-align: center')
                    p(span('Willkommen!', cls='w3-padding w3-theme-l1 w3-round', style='font-weight: bolder; font-size: large;'), cls='name')
                    p(span(info[1], cls='w3-padding w3-theme-d5 w3-round', style='font-weight: bolder;'))
                    br()
                comment(' Links section ')
                with div():
                    # individual per comp
                    attr(cls='links-container')
                    a_ = a(href=f'https://live.worldcubeassociation.org/link/competitions/{info[0]}')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-solid fa-ranking-star')
                        text(' WCA Live')
                    br()
                    a_ = a(href=f'https://www.competitiongroups.com/competitions/{info[0]}')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-solid fa-users')
                        text(' Einteilungen')
                    br()
                    a_ = a(href=f'https://www.worldcubeassociation.org/competitions/{info[0]}#competition-schedule')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-regular fa-clock')
                        text(' Zeitplan')
                    br()
                    a_ = a(href=f'https://www.worldcubeassociation.org/competitions/{info[0]}#general-info')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-solid fa-circle-info')
                        text(' Alle Infos')
                    br()
                    # standard
                    a_ = a(href=f'https://www.germancubeassociation.de/anleitungen/#competitor-tutorial')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-regular fa-lightbulb')
                        text(' Teilnehmer Crash-Kurs')
                    br()
                    a_ = a(href=f'https://www.germancubeassociation.de/anleitungen/#judging-tutorial')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-solid fa-scale-balanced')
                        text(' Judging Crash-Kurs')
                    br()
                    a_ = a(href=f'https://www.germancubeassociation.de/verein/')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-solid fa-crown')
                        text(' Werde GCA Mitglied')
                    br()
                    a_ = a(href=f'https://www.worldcubeassociation.org/competitions?region=Germany&search=&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank', title='Grünes Symbol in der Liste zeigt, dass die Anmeldung geöffnet ist und noch Plätze da sind.')
                        i('', cls='fa-solid fa-thumbs-up')
                        text(' Mehr Comps!')
                    br()
                    comment(' Icons section ')
                    with div():
                        attr(cls='icons w3-padding')
                        a(i(cls='fa-brands fa-instagram', aria_hidden='true', style='color: #c7dfee; font-size: xx-large;'), href='https://www.instagram.com/germancubeassociation/', target='_blank')
                        a(i(cls='fa-brands fa-discord', aria_hidden='true', style='color: #c7dfee; font-size: xx-large;'), href='https://discord.gg/vUaxGnYGP2', target='_blank')
                        a(i(cls='fa-solid fa-envelope', aria_hidden='true', style='color: #c7dfee; font-size: xx-large;'), href='https://www.germancubeassociation.de/kontakt/', target='_blank')

            # english
            with div():
                if ic == 0:
                    attr(cls='container navi hidden', id=f'main-en-{ic}', style='display:none;')
                else:
                    attr(cls='container hidden', id=f'main-en-{ic}', style='display:none;')
                with div():
                    attr(cls='icons w3-padding')
                    a(raw('🇩🇪'), onclick='toggleLang()', cls='w3-button w3-round link flag')
                    if (multi):
                        a(raw('🌐'), onclick='openManualLocModal()', cls='w3-button w3-round link globe')
                comment(' Name container ')
                with div():
                    attr(cls='', style='text-align: center')
                    p(span('Welcome!', cls='w3-padding w3-theme-l1 w3-round', style='font-weight: bolder; font-size: large;'), cls='name')
                    p(span(info[1], cls='w3-padding w3-theme-d5 w3-round', style='font-weight: bolder;'))
                    br()
                comment(' Links section ')
                with div():
                    # individual per comp
                    attr(cls='links-container')
                    a_ = a(href=f'https://live.worldcubeassociation.org/link/competitions/{info[0]}')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-solid fa-ranking-star')
                        text(' WCA Live')
                    br()
                    a_ = a(href=f'https://www.competitiongroups.com/competitions/{info[0]}')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-solid fa-users')
                        text(' Assignments')
                    br()
                    a_ = a(href=f'https://www.worldcubeassociation.org/competitions/{info[0]}#competition-schedule')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-regular fa-clock')
                        text(' Schedule')
                    br()
                    a_ = a(href=f'https://www.worldcubeassociation.org/competitions/{info[0]}#general-info')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-solid fa-circle-info')
                        text(' All info')
                    br()
                    # standard
                    a_ = a(href=f'https://documents.worldcubeassociation.org/edudoc/competitor-tutorial/tutorial.pdf')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-regular fa-lightbulb')
                        text(' Competitor tutorial')
                    br()
                    a_ = a(href=f'https://documents.worldcubeassociation.org/edudoc/judge-tutorial/judge-tutorial.pdf')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-solid fa-scale-balanced')
                        text(' Judging tutorial')
                    br()
                    a_ = a(href=f'https://www.germancubeassociation.de/verein/')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank')
                        i('', cls='fa-solid fa-crown')
                        text(' Become GCA member')
                    br()
                    a_ = a(href=f'https://www.worldcubeassociation.org/competitions?region=Germany&search=&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list')
                    with a_:
                        attr(cls='w3-button w3-round w3-theme-d3 w3-border link', target='_blank', title='Green symbol in list signalizes registration is open and not yet full.')
                        i('', cls='fa-solid fa-thumbs-up')
                        text(' More comps!')
                    br()
                    comment(' Icons section ')
                    with div():
                        attr(cls='icons w3-padding')
                        a(i(cls='fa-brands fa-instagram', aria_hidden='true', style='color: #c7dfee; font-size: xx-large;'), href='https://www.instagram.com/germancubeassociation/', target='_blank')
                        a(i(cls='fa-brands fa-discord', aria_hidden='true', style='color: #c7dfee; font-size: xx-large;'), href='https://discord.gg/vUaxGnYGP2', target='_blank')
                        a(i(cls='fa-solid fa-envelope', aria_hidden='true', style='color: #c7dfee; font-size: xx-large;'), href='https://www.germancubeassociation.de/kontakt/', target='_blank')


        script(src='js/script-Copy1.js')
        script(data_id='101446349', _async=True, src='//static.getclicky.com/js')

    print(doc.render())
    with open("../Output.html", "w") as text_file:
        print(doc, file=text_file)


# now we know the IDs of comps taking place the upcoming weekend, and relevant info to steer the UI
print(upcoming_comp_info)

some_new = True
if len(upcoming_comp_info) == 0:
    print('No new upcoming comps, exiting.')
    some_new = False

if some_new:
    multi_comp_weekend = False
    if len(upcoming_comp_info) > 1:
        print('Multi-Comp Weekend!')
        multi_comp_weekend = True
        generate_html(comp_info = upcoming_comp_info, multi = multi_comp_weekend)
