from django.shortcuts import render, redirect

from mymusic.mymusicapp.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from mymusic.mymusicapp.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.last()
    except:
        return None


def add_profile(request):  # Optional
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'add_profile_form': form,
    }

    return render(request, 'core/home-no-profile.html', context=context)


def index(request):
    profile = get_profile()
    # profile = None

    if profile is None:
        return redirect('add profile')

    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'core/home-with-profile.html', context=context)


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'add_album_form': form
    }

    return render(request, 'albums/add-album.html', context=context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    context = {
        'album': album
    }
    return render(request, 'albums/album-details.html', context=context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'edit_album_form': form,
        'album': album
    }

    return render(request, 'albums/edit-album.html', context=context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        album.delete()
        return redirect('index')

    context = {
        'delete_album_form': form,
        'album': album
    }

    return render(request, 'albums/delete-album.html', context=context)


def details_profile(request):
    profile = get_profile()
    if profile is None:
        return render(request, 'core/home-no-profile.html')
    return render(request, 'profiles/profile-details.html')


def delete_profile(request):
    return render(request, 'profiles/profile-delete.html')
