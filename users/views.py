from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileUpdateForm
from  .models import Profile

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
    user_details = Profile.objects.get(user=request.user)
    return render(request, 'users/profile.html', {'user_details': user_details})

def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form=ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            print(current_user)
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('users/update_profile.html')
    else:
        form=ProfileUpdateForm()
    return render(request, 'users/update_profile.html',{'form':form})

# def profile_display(request):
#     current_user = request.user
#     author = current_user
#     projects = Project.get_by_author(author)
#     try:
#         profile = request.user.profile
#     except Profile.DoesNotExist:
#         profile = Profile(user=request.user)
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.save()
#         return redirect('profile')
#     else:
#         form = ProfileUpdateForm()
#     return render(request, 'registration/profile.html', {"form":form, "projects":projects})

