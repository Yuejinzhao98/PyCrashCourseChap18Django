from django.shortcuts import render
# import module by myself
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import logout

# modules used by register
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(redirect_to=reverse('learning_logs:index'))


def register(request):
	"""create a new user"""

	if not request.method == 'POST':
		form = UserCreationForm()
	else:
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()

			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context = {'form': form}
	return render(request, "users/register.html", context)
