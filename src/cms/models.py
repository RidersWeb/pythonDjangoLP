from django.db import models

class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/', verbose_name='Добавить картинку')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.TextField(verbose_name='Текст к картинке')
    cms_css = models.CharField(max_length=200, null=True, default='-', verbose_name='css класс')

    class Meta:
        verbose_name='Слайдер'
        verbose_name_plural='Слайды'

    def __str__(self):
        return self.cms_title

