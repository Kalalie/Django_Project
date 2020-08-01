from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.title + str(self.pub_date)
