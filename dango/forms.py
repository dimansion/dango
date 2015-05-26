from django import forms
from .models import *

class ConvertForm(forms.ModelForm):
	
	class Meta:
		model = Convert
		fields = ('image_original','ekstensi')

class ResizeForm(forms.ModelForm):
	
	class Meta:
		model = Resize
		fields = ('image_original','persen')

class RotateForm(forms.ModelForm):
	
	class Meta:
		model = Rotate
		fields = ('image_original','direction')

class MemeForm(forms.ModelForm):
	
	class Meta:
		model = Meme
		fields = ('image_original','teksatas','teksbawah')

class WatermarkTxtForm(forms.ModelForm):
	
	class Meta:
		model = WatermarkTxt
		fields = ('image_original','posisi','teks')

class WatermarkImgForm(forms.ModelForm):
	
	class Meta:
		model = WatermarkImg
		fields = ('image_original','image_logo','posisi')


