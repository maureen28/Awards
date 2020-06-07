from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileUpdateForm

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form':form})

def profile(request):
    
    return render(request, 'users/profile.html')

# def update_profile(request):
#     if request.method == 'POST':
#         form=ProfileUpdateForm(request.POST, request.FILES)
#         if profile.is__valid:
#             profile=profile.save(commit=False)
#             profile.user = current_user
#             profile.save()
#             return redirect('update_profile.html')
#     else:
#         form=ProfileUpdateForm()
#     return render(request, 'update_profile.html',{'form':form})

def profile_display(request):
    current_user = request.user
    author = current_user
    projects = Project.get_by_author(author)
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
    else:
        form = ProfileUpdateForm()
    return render(request, 'registration/profile.html', {"form":form, "projects":projects})

