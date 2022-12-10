from django.shortcuts import render, redirect

from mymusic.mymusicapp.forms import ProfileCreateForm
from mymusic.mymusicapp.models import Profile


def get_profile():
    try:
        Profile.objects.get()
    except:
        return None


def add_profile(request):  # Optional
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
    return render(request, 'core/home-no-profile.html')


def index(request):
    profile = get_profile()
    if profile is None:
        return render(request, 'core/home-no-profile.html')
        # return redirect('add profile') # Optional
    return render(request, 'core/home-with-profile.html')


def add_album(request):
    return render(request, 'albums/add-album.html')


def details_album(request, pk):
    return render(request, 'albums/album-details.html')


def edit_album(request, pk):
    return render(request, 'albums/edit-album.html')


def delete_album(request, pk):
    return render(request, 'albums/delete-album.html')


def details_profile(request):
    profile = get_profile()
    if profile is None:
        return render(request, 'core/home-no-profile.html')
    return render(request, 'profiles/profile-details.html')


def delete_profile(request):
    return render(request, 'profiles/profile-delete.html')
