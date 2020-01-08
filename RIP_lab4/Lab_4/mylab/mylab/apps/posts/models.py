from django.db import models


class Post(models.Model):
    post_name = models.CharField('Заголовок поста', max_length=255)
    post_text = models.CharField('Текст поста', max_length=500)
    pub_data = models.DateTimeField('Дата публикации')
    post_image = models.URLField('Изображение', max_length=255)

    def __str__(self):
        return 'Post {}'.format(self.post_name)

