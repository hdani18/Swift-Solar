from django.shortcuts import render, get_object_or_404
from pages import models
import requests
from django.conf import settings
from datetime import datetime, timedelta

def get_wiki_data(params):
    
    URL = "https://en.wikipedia.org/w/api.php"
    session = requests.Session()
    response = session.get(url=URL, params=params)
    return response.json()

def data_plot(titles, date):

    end_date = date.strftime('%Y-%m-%d')
    start_date = (date + timedelta(days=365)).strftime('%Y-%m-%d')

    revisions_per_month = {}

    for title in titles:
        params = {
            "action": "query",
            "prop": "revisions",
            "titles": title,
            "rvstart": f"{start_date}T23:59:59Z",
            "rvend": f"{end_date}T00:00:00Z",
            "rvlimit": "max",
            "rvprop": "timestamp",
            "formatversion": "2",
            "format": "json"
        }

        data = get_wiki_data(params)
        pages = data["query"]["pages"]
        for page in pages:
            for revision in page.get("revisions", []):
                timestamp = datetime.strptime(revision.get("timestamp"), '%Y-%m-%dT%H:%M:%SZ')
                year_month = timestamp.strftime('%Y-%m')  
                revisions_per_month[year_month] = revisions_per_month.get(year_month, 0) + 1

    return revisions_per_month

def get_events():
   
    events = models.Event.objects.all()
    event_dicts = []
    for event in events:
        event_dict = {
            'date': event.event_date.strftime('%Y-%m-%d'),
            'name': event.event_name,
        }
        event_dicts.append(event_dict)
    return event_dicts

def generate_histogram(request):
    
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        titles = request.POST.get('titles')
        if not titles:
            events = get_events()
            return render(request, 'pages/form.html', {'events': events, 'error_message': 'Please enter at least one title.'})
        
        title_list = titles.split(",")
        try:
            event = models.Event.objects.get(event_name=event_name)
        except models.Event.DoesNotExist:
            event = None

        if event:
            event_data = {
                'name': event.event_name,
                'date': event.event_date.strftime('%Y-%m-%d')
            }
            date = event.event_date

            histogram_data = data_plot(title_list, date)
            
            return render(request, 'pages/histogram.html', {
                'event_data': event_data,
                'revisions_per_month': histogram_data
            })
  
    events = get_events()  
    return render(request, 'pages/form.html', {'events': events})

