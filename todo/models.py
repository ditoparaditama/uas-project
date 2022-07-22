from pickle import NONE
from pyexpat import model
from django.forms import IntegerField
from django.utils.translation import gettext_lazy as _
from django.db import models



class Task(models.Model):
    class JenisKelamin(models.TextChoices):
        NONE = 'None',_('?')
        LAKI = 'Laki-laki',_('Laki-laki')
        PEREMPUAN = 'Perempuan',_('Perempuan')

    class TaskStatus(models.TextChoices):
        TODO = 'None', _('?')
        IN_PROGRESS = 'Aktif', _('Aktif')
        CLOSED = 'Transfer', _('Transfer')

    nama = models.CharField(max_length=20)
    nim = models.IntegerField()
    alamat = models.TextField(max_length=100)
    jk = models.CharField(
        max_length=20,
        choices=JenisKelamin.choices,
        default=JenisKelamin.NONE
    )
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'

