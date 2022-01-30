from django.shortcuts import render
from clubs.serializers import ClublistSerializer
from clubs.models import club_detail
#from django.views.generic.list import ListView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView



'''def club_profile(request):
    clubs_list =club_detail.objects.all()
    context={'club_name':obj.club_name,
    'club_logo':obj.club_logo ,
    'club_description':obj.club_description ,}
    #context={'object' : obj}

    return render(request,"link of the club profile page",context)
    '''

"""class ClubList(ListView):
    model =club_detail"""

class ClubCreation(CreateAPIView):
    queryset = club_detail.objects.all()
    serializer_class = ClublistSerializer

@api_view(['GET'])
def club_list (request):
    clubs = club_detail.objects.all()
    serializer = ClublistSerializer(clubs,many =True)
    return Response(serializer.data)

@api_view(['GET'])
def clubdetail(request,pk):
    clubs = club_detail.objects.filter(id=pk)
    serializer = ClublistSerializer(clubs,many =True)
    return Response(serializer.data)
