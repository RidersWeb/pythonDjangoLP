# Generated by Django 4.0.3 on 2022-04-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_alter_cmsslider_cms_img_alter_cmsslider_cms_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(max_length=200, null=True, verbose_name='css'),
        ),
    ]
