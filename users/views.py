from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully. Now you can login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# region UserInformation not in use just for testing
# def user_information(request):
#     if request.method == 'POST':
#         user_info_form = UserInformation(request.POST)
#         if user_info_form.is_valid():
#             user_info_username = user_info_form.cleaned_data.get('name')
#             messages.success(request, f'Details are saved {user_info_username} !')
#             return redirect('home-blog')
#     else:
#         user_info_form = UserInformation()
#     return render(request, 'users/userinfo.html', {'user_info_form': user_info_form})
# endregion

@login_required
def profile(request):
    return render(request, 'users/profile.html')
