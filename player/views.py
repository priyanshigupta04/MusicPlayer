from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Song
from .forms import SongForm

def song_list(request):
    songs = Song.objects.all()
    form = SongForm()

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Song uploaded successfully!')
            return redirect('song_list')

    return render(request, 'player/song_list.html', {'songs': songs, 'form': form})

