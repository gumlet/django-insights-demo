from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from insight_data.models import Event
from insight_data.serializers import EventSerializer

@csrf_exempt
def event_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def get_views(request):
    event_count = Event.objects.filter(name="played").count()
    return JsonResponse({"views": event_count}, status=200)