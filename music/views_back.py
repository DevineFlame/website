from django.shortcuts import render
from  django.shortcuts import Http404,get_object_or_404 #this is shortcut for using in place of this as we use this many times

from .models import Album,song



def index(request):
    all_albums=Album.objects.all()
    return  render(request,'music/index.html',{'all_albums':all_albums})

def detail(request,album_id):
        #try:
        #album=Album.objects.get(pk=album_id)
        #except Album.DoesNotExist:
        #raise Http404("Album does not exit ")      // in place of this
        album=get_object_or_404(Album,pk=album_id)
        return  render(request,'music/details.html',{'album':album})


def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except(KeyError,song.DoesNotExist):
        return render(request,'music/details.html',
                      {
                          'album':album,
                          'error_message':"you did'nt selected right one",
                      }
                      )
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})



