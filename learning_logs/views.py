from django.shortcuts import render

from .models import Topic, Entry

# new_topic所需的模块
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .form import TopicForm, EntryForm

from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
	"""学习笔记的主页"""
	print()
	return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
	topics = Topic.objects.filter(owner=request.user).order_by('date')
	print(topics.__dict__)
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	# check request topic is whether is the user's.
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, "entries": entries}
	return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
	"""添加新主题"""
	if request.method != "POST":
		form = TopicForm()
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)#注意这里如果没加commit=false会发生NOT NULL constraint failed: learning_logs_topic.owner_id，是因为此时信息不全
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(redirect_to=reverse('learning_logs:topic', args=[topic_id]))
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
	"""编辑既有条目"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(data=request.POST, instance=entry)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(redirect_to=reverse('learning_logs:topic', args=[topic.id]))

	context = {'form': form, 'entry': entry, 'topic': topic}
	return render(request, "learning_logs/edit_entry.html", context)
