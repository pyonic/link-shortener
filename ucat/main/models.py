from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Link(models.Model):
	author  = models.ForeignKey(User, on_delete = models.CASCADE)
	link    = models.TextField()
	short   = models.CharField(max_length=250)
	publish = models.DateTimeField(default=timezone.now)
	crated_at  = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.link 

	class Meta:
		verbose_name = 'Ссылка'
		verbose_name_plural = 'Ссылки'
