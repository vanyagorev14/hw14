from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField()),
                ('description', models.TextField())
            ],
        ),
        migrations.CreateModel(
            name= 'citation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.CASCADE, to='celery_beat.author'))
            ],
        ),
    ]