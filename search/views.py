import requests
from django.shortcuts import render
from .forms import FlightSearchForm

def search_flights(request):
    response_data = None
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            cabin = form.cleaned_data['cabin']
            
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            }

            json_data = {
                'origin': origin,
                'destination': destination,
                'partnerPrograms': [
                    'Air Canada',
                    'United Airlines',
                    'KLM',
                    'Qantas',
                    'American Airlines',
                    'Etihad Airways',
                    'Alaska Airlines',
                    'Qatar Airways',
                    'LifeMiles',
                ],
                'stops': 2,
                'departureTimeFrom': '2024-07-09T00:00:00Z',
                'departureTimeTo': '2024-10-07T00:00:00Z',
                'isOldData': False,
                'limit': 302,
                'offset': 0,
                'cabinSelection': [
                    cabin,
                ],
                'date': '2024-07-09T12:00:17.796Z',
            }

            response = requests.post('https://cardgpt.in/apitest', headers=headers, json=json_data)
            response_data = response.json()
            for item in response_data.get('data', []):
                item['origin'] = origin
                item['destination'] = destination
    else:
        form = FlightSearchForm()

    return render(request, 'search/search.html', {'form': form, 'response_data': response_data})
