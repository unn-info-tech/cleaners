from django.http import JsonResponse
from django.shortcuts import render
from .models import Service, ExtraService
from django.http import JsonResponse
import json


def index(request):
    services = Service.objects.all()
    extra_services = ExtraService.objects.all()  # Fetch extra services
    return render(request, 'services/index.html', {'services': services, 'extra_services': extra_services})



import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, Service, ExtraService
from django.shortcuts import get_object_or_404

import logging

# Get a logger for the view
logger = logging.getLogger(__name__)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, Service, ExtraService
from django.shortcuts import get_object_or_404

@csrf_exempt
def submit_total(request):
    print("submit_total view is called", flush=True)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            total = data.get('total')
            services = data.get('services')
            extra_services_data = data.get('extra_services', [])

            if total is not None and services:
                selected_services = []
                selected_extra_services = []

                # Get Service objects
                for service in services:
                    service_name = service.get('serviceName')
                    service_object = Service.objects.filter(name=service_name).first()
                    if service_object:
                        selected_services.append(service_object)

                # Get ExtraService objects
                for extra_service in extra_services_data:
                    extra_name = extra_service.get('name')
                    extra_object = ExtraService.objects.filter(name=extra_name).first()
                    if extra_object:
                        selected_extra_services.append(extra_object)

                # Create order
                order = Order.objects.create(total_price=total)

                # Set ManyToMany relations
                order.service.set([s.id for s in selected_services])
                order.extra_service.set([e.id for e in selected_extra_services])
                order.save()

                # Print results
                print(f"Order #{order.id} created successfully.", flush=True)
                print(f"Total: ${order.total_price}", flush=True)
                print("Selected services:", flush=True)
                for service in selected_services:
                    print(f"- {service.name}: ${service.individual_price}", flush=True)
                print("Selected extra services:", flush=True)
                for extra in selected_extra_services:
                    print(f"- {extra.name}: ${extra.price}", flush=True)

                return JsonResponse({
                    'message': 'Order created successfully',
                    'status': 'success',
                    'order_id': order.id
                }, status=200)

            return JsonResponse({'message': 'Total or services not provided'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            print(f"Exception occurred: {e}", flush=True)
            return JsonResponse({'message': f'Error occurred: {str(e)}'}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=405)
