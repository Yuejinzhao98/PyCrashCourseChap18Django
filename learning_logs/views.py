from django.shortcuts import render

from .models import Topic, Entry

# new_topic所需的模块
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import TopicForm, EntryForm


# Create your views here.

def index(request):
	"""学习笔记的主页"""

	return render(request, 'learning_logs/index.html')


def topics(request):
	topics = Topic.objects.order_by('date')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, "entries": entries}
	return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
	"""添加新主题"""
	if request.method != "POST":
		form = TopicForm()
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)


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


def edit_entry(request, entry_id):
	"""编辑既有条目"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(data=request.POST, instance=entry)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(redirect_to=reverse('learning_logs:topic', args=[topic.id]))

	context = {'form': form, 'entry': entry, 'topic': topic}
	return render(request, "learning_logs/edit_entry.html", context)
