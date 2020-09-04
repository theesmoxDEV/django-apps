from django.db import models
import os

# Start with loading all necessary libraries
from wordcloud import WordCloud
from djangoProject.settings import MEDIA_ROOT
from stop_words import get_stop_words


# Create your models here.

class Cloud(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ChatFile(models.Model):
    wordcloud_name = models.CharField(max_length=100, blank=True)
    document = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wordcloud_name

    def create_cloud(self):
        f = open(self.document.path)
        text = f.read()
        f.close()
        stop_words = get_stop_words('spanish')
        words_list = text.split(" ")
        words = [word.lower() for word in words_list if word.lower() not in stop_words]
        words = " ".join(words)

        wordcloud = WordCloud(max_font_size=50, max_words=1000, background_color="white",
                              width=1500, height=900).generate(words)
        try:
            os.mkdir(MEDIA_ROOT)
        except:
            pass

        wordcloud.to_file(os.path.join(MEDIA_ROOT, self.wordcloud_name + '_image.png'))
