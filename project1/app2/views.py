from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate



def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    template_name = 'app2/register.html'
    context = {'form':form}
    return render(request, template_name, context)


def login_view(request):
    template_name = 'app2/login.html'
    context = {}
    if request.method == 'POST':
         u = request.POST = ['un']
         p = request.POST = ['pw']
         user = authenticate(username=u, password=p)

         if user is not None:
             login(request, user)
             return redirect('show_url')
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('login_url')
