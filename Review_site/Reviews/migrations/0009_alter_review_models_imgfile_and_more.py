# Generated by Django 4.2.2 on 2023-06-26 07:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0008_alter_review_models_objects_clf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_models',
            name='imgfile',
            field=models.ImageField(upload_to='review_images/', validators=[django.core.validators.validate_image_file_extension, django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'], message='다음과 같은 형식의 확장자만 사용 가능합니다[jpg, png, jpeg]')]),
        ),
        migrations.AlterField(
            model_name='review_models',
            name='ratings',
            field=models.IntegerField(choices=[(3, '★★★'), (2, '★★'), (4, '★★★★'), (1, '★'), (5, '★★★★★')]),
        ),
    ]
