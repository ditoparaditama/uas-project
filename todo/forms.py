from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('nama', 'nim', 'alamat', 'jk', 'status')
        labels = {
            'nama': _('Nama'),
            'nim': _('NIM'),
            'alamat': _('Alamat'),
            'jk': _('Jenis Kelamin'),
            'status': _('Status Mahasiswa')
        }
        error_messages = {
            'nama': {
                'required': _("Nama harus diisi."),
            },
            'NIM': {
                'required': _("Nim harus diisi."),
            },
            'alamat': {
                'required': _("alamat harus diisi."),    
            },
        }
