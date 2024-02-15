from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests  # For making HTTP requests to destinations
from ..models import Account, Destination

# views.py

# import logging
# logger = logging.getLogger(__name__)

@api_view(['POST'])
def incoming_data(request):
    if request.method != 'POST' or not request.content_type == 'application/json':
        return JsonResponse({'error': 'Invalid request method or data format'}, status=400)

    secret_token = request.META.get('HTTP_CL_X_TOKEN')

    if not secret_token:
        return JsonResponse({'error': 'Unauthenticated'}, status=401)

    try:
        account = Account.objects.get(app_secret_token=secret_token)
        data = request.data

        for destination in account.destination_set.all():
            try:
                if destination.http_method == 'GET':
                    response = requests.get(destination.url, params=data, headers=destination.headers)
                elif destination.http_method in ('POST', 'PUT'):
                    response = requests.request(destination.http_method, destination.url, json=data, headers=destination.headers)
                else:
                    raise ValueError(f"Unsupported HTTP method: {destination.http_method}")

                response.raise_for_status()  # Raise exception for non-2xx status codes
            except Exception as e:
                print(f"Error sending data to {destination.url}: {e}")
                # Optionally log errors or handle them differently

        return JsonResponse({'success': 'Data sent successfully'})

    except Account.DoesNotExist:
        return JsonResponse({'error': 'Invalid secret token'}, status=401)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
