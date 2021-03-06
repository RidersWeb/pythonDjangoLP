# Generated by Django 4.0.3 on 2022-04-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cms_img', models.ImageField(upload_to='sliderimg', verbose_name='Картинка')),
                ('cms_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('cms_text', models.TextField(verbose_name='Текс')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
