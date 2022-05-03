from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата обращения')
    order_name = models.CharField(max_length=100, verbose_name='Имя')
    order_phone = models.CharField(max_length=11, verbose_name='№ телефона')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, default=1, blank=True, verbose_name='Статус')
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        # return self.order_dt.strftime('%d-%m-%Y'), self.order_phone, self.order_name
        return self.order_name

class ComentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    coment_text = models.TextField(verbose_name='Текст комента')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.coment_text
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'
