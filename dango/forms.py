from django import forms
from .models import *

class ConvertForm(forms.ModelForm):
	
	class Meta:
		model = Convert
		fields = ('image_original','ekstensi')
		widgets={
			'image_original':forms.FileInput(attrs={'class':'col-md-6 col-sm-6'}),
			'ekstensi':forms.Select(attrs={'class':'col-md-6 col-sm-6','style':'margin-left: 53px'}),
		}

class ResizeForm(forms.ModelForm):
	
	class Meta:
		model = Resize
		fields = ('image_original','persen')
		widgets={
			'image_original':forms.FileInput(attrs={'class':'col-md-6 col-sm-6'}),
			'persen':forms.NumberInput(attrs={'class':'col-md-6 col-sm-6','style':'margin-left: 68px'}),
		}
		
class RotateForm(forms.ModelForm):
	
	class Meta:
		model = Rotate
		fields = ('image_original','direction')
		widgets={
			'image_original':forms.FileInput(attrs={'class':'col-md-6 col-sm-6'}),
			'direction':forms.Select(attrs={'class':'col-md-6 col-sm-6','style':'margin-left: 46px'}),
		}
		
class MemeForm(forms.ModelForm):
	
	class Meta:
		model = Meme
		fields = ('image_original','teksatas','teksbawah')
		widgets={
			'image_original':forms.FileInput(attrs={'class':'col-md-6 col-sm-6'}),
			'teksatas':forms.TextInput(attrs={'class':'col-md-6 col-sm-6','style':'margin-left: 50px'}),
			'teksbawah':forms.TextInput(attrs={'class':'col-md-6 col-sm-6','style':'margin-left: 31px'}),
		}
		
class WatermarkTxtForm(forms.ModelForm):
	
	class Meta:
		model = WatermarkTxt
		fields = ('image_original','posisi','teks')
		widgets={
			'image_original':forms.FileInput(attrs={'class':'col-md-6 col-sm-6'}),
			'posisi':forms.Select(attrs={'class':'col-md-6 col-sm-6','style':'margin-left: 74px'}),
			'teks':forms.TextInput(attrs={'class':'col-md-6 col-sm-6','style':'margin-left: 84px'}),
		}
		
class WatermarkImgForm(forms.ModelForm):
	
	class Meta:
		model = WatermarkImg
		fields = ('image_original','image_logo','posisi')
		widgets={
			'image_original':forms.FileInput(attrs={'class':'col-md-6 col-sm-6'}),
			'image_logo':forms.FileInput(attrs={'class':'col-md-6 col-sm-6','style':'margin-left: 28px'}),
			'posisi':forms.Select(attrs={'class':'col-md-6 col-sm-6','style':'margin-left: 74px'}),
		}

