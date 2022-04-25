from django.db import models


STATUS = (
	(0, "Draft"),
	(1, "Publish")
)

class Post(models.Model):
	icon = models.ImageField(upload_to='icon/', blank=True)
	title = models.CharField(max_length=300, unique=True)
	slug = models.SlugField(max_length=300, unique=True)
	content = models.TextField()
	status = models.IntegerField(choices=STATUS, default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.title