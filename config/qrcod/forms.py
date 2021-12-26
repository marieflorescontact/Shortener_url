'''
Shortener Forms qrcode/forms.py
'''

from django import forms

from config.qrcod.models import Qrcod


class QrcodeForm(forms.ModelForm):
    text = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "class": "shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md",
            "placeholder": "Paste Website'URL or text",
            "name": "qr_text"}))

    class Meta:
        model = Qrcod
        fields = ('text',)
