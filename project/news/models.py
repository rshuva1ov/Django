from django.db import models


class Article(models.Model):
    title = models.CharField("Название", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    full_text = models.TextField("Статья")
    date = models.DateTimeField(
        "Дата публикации", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
