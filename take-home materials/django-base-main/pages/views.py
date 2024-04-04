from django.shortcuts import render
import requests
from datetime import datetime, timedelta

def get_wiki_data(params):
    """
    Makes a request to the Wikipedia API.

    Args:
        params (dict): Parameters for the API request.

    Returns:
        dict: JSON response from the API.
    """
    URL = "https://en.wikipedia.org/w/api.php"
    session = requests.Session()
    response = session.get(url=URL, params=params)
    return response.json()

def data_plot(titles, date):

  date_object = datetime.strptime(date, '%Y-%m-%d')
  start_date = date_object + timedelta(days=365)
  end_date = date_object

  revisions_per_month = {}

  for title in titles:
      params = {
          "action": "query",
          "prop": "revisions",
          "titles": title,
          "rvstart": f"{start_date}",
          "rvend": f"{end_date}",
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

def home(request):
    return render(request, 'pages/home.html')


def random_number(request):
    return render(request, 'pages/random_number.html')
