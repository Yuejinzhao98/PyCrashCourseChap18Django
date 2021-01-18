from django.db import models


# Create your models here.

class Topic(models.Model):
	"""用户学习的主题"""

	text = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text


class Entry(models.Model):
	"""学到的有关某个主题的具体知识"""

	topic = models.ForeignKey(Topic,models.deletion.CASCADE)
	text = models.CharField(max_length=9999)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta():
		verbose_name_plural = 'entries'

	def __str__(self):
		return self.text[:50] + "..."
