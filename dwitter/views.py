from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.
def homeview(request):
    return render(request,'registration/home.html')

def dashboard(request):
    form = forms.CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("Dwitter:dashboard")

    followed_dweets = models.comment.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    return render(
        request,
        "Dwitter/dashboard.html",
        {"form": form, "dweets": followed_dweets},
    )

def profile_list(request):
    profiles = models.Profile.objects.exclude(user=request.user)
    return render(request, 'Dwitter/profile_list.html', {'profiles':profiles})

def profile(request,pk):

    if not hasattr(request.user, 'profile'):
        missing_profile = models.Profile(user=request.user)
        missing_profile.save()

    profile = models.Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request,'Dwitter/profile.html', {'profile': profile})
