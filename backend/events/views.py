from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from events.serializers import EventSerializer,UpdateEventSerializer
from events.models import event
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,UpdateAPIView
from rest_framework.decorators import api_view
from .forms import event_form
from clubs.models import club_detail
from .models import event, eventreg

# Create your views here.
class CreateEvent(CreateAPIView):
    queryset = event.objects.all()
    serializer_class = EventSerializer


class UpdateEvent(UpdateAPIView):

    queryset = event.objects.all()
    serializer_class = UpdateEventSerializer
    # permission_classes = (
    #     IsAuthenticated,
    #     )
# change redirect and render urls
@api_view(['GET'])
def event_list (request):
    events = event.objects.all()
    serializer = EventSerializer(events,many =True)
    return Response(serializer.data)

def register_event(request):
    user = request.user
    event_id = request.session.get("event_id")
    # eventreg = eventreg.filter(user = user).exists()
    events = event.objects.get(id = event_id)

    if eventreg.filter(user = user, event = event).exists():
        eventreg_obj = eventreg.objects.create(user = user, event = event, club = event.club)
    else:
        redirect('/')

@api_view(['GET'])
def event_detail(request,pk):
    events = event.objects.filter(id=pk)
    serializer = EventSerializer(events,many =True)
    return Response(serializer.data)
