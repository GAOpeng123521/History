# Generated by Django 2.2.7 on 2021-06-25 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0042_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='lali',
            new_name='data1',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='yali',
            new_name='data2',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='zaoyin',
            new_name='data3',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='zhendong',
            new_name='data4',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='lali',
            new_name='data1',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='lalialertstatus',
            new_name='data1alertstatus',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='lalialerttime',
            new_name='data1alerttime',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='laliset',
            new_name='data1set',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='yali',
            new_name='data2',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='yalialertstatus',
            new_name='data2alertstatus',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='yalialerttime',
            new_name='data2alerttime',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='yaliset',
            new_name='data2set',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='zaoyin',
            new_name='data3',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='zaoyinalertstatus',
            new_name='data3alertstatus',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='zaoyinalerttime',
            new_name='data3alerttime',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='zaoyinset',
            new_name='data3set',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='zhendong',
            new_name='data4',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='zhendongalertstatus',
            new_name='data4alertstatus',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='zhendongalerttime',
            new_name='data4alerttime',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='zhendongset',
            new_name='data4set',
        ),
    ]
