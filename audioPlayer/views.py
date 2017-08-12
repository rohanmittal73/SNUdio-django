from django.shortcuts import render
from .models import AudioFile, Member
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import AudioSerializer


# Create your views here.
def home(request):
    all_audio = AudioFile.objects.all().order_by('-date')
    latest = all_audio[0]
    latest.views += 1
    latest.save()
    trending = all_audio[1:4]
    return render(request, 'audioPlayer/index.html', {'latest': latest, 'trending': trending})


def description(request, audio_id):
    try:
        audio_file = AudioFile.objects.get(pk=audio_id)
        audio_file.views += 1
        audio_file.save()
    except:
        return render(request, 'audioPlayer/error.html')
    return render(request, 'audioPlayer/description.html', {'audio': audio_file})


def team(request):
    members = Member.objects.all()
    return render(request, 'audioPlayer/team.html', {'team': members})


def search(request):
    try:
        search_query = request.POST['search-query']
        matches = AudioFile.objects.filter(title__icontains=search_query)
        return render(request, 'audioPlayer/search.html', {'results': matches[:12]})
    except:
        return render(request, 'audioPlayer/search.html', {'results': AudioFile.objects.all().order_by('-date')[:12]})


class PodcastList(APIView):
    def get(self, request):
        all_audio = AudioFile.objects.all()
        serializer = AudioSerializer(all_audio, many=True)
        return Response(serializer.data)