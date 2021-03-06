# Generated by Django 3.1.7 on 2021-02-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
                ('img_url', models.TextField()),
                ('list_ingredient', models.ManyToManyField(to='ingredient.ingredientItem')),
            ],
        ),
    ]
