'''
Shortener Forms qrcode/forms.py
'''

from django import forms

from config.qrcod.models import Qrcode


class QrcodeForm(forms.ModelForm):
    document = forms.URLField(widget=forms.URLInput(
        attrs={
            "class": "shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md",
            "placeholder": "upload website or text"}))

    class Meta:
        model = Qrcode
        fields = ('document',)
