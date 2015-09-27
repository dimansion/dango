from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import *
from wand.image import Image
from django.views.generic.base import View
from .models import *

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


from django.core.servers.basehttp import FileWrapper
import mimetypes

def index(request):
    return render(request, 'dango/dango.html')

class ConvertView(View):
	template_name='dango/convert.html'
	def get (self,request):
	 form=ConvertForm()
	 return render(request,self.template_name,{'form':form})
	def post (self,request):
	 form=ConvertForm(request.POST)

	 if form.is_valid():
		konf=form.save(commit=False)
		konf.image_original=request.FILES['image_original']
		konf.save()


		return HttpResponseRedirect(reverse('convert-download',kwargs={'id':konf.id}))
	 return render(request, 'dango/convert.html',{'form':form})



class ConvertDownload(View):
	id=None
	def get (self,request,id):
    		img=Convert.objects.get(id=id)
		filename='/home/dimansion/dango/media/{}'.format(img.image_original.name)
		base=os.path.basename(filename)
		nama=os.path.splitext(base)[0]
		filename='/home/dimansion/dango/media/images/{}.{}'.format(nama,img.ekstensi)
    		wrapper      = FileWrapper(open(filename))  # img.file returns full path to the image
	    	content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
    		response     = HttpResponse(wrapper,content_type=content_type)
    		response['Content-Length']      = os.path.getsize(filename)
    		response['Content-Disposition'] = "attachment; filename=%s" %  filename
    		return response

class RotateView(View):
	template_name='dango/rotate.html'
	def get (self,request):
	 form=RotateForm()
	 return render(request,self.template_name,{'form':form})
	def post (self,request):
	 form=RotateForm(request.POST)
	 if form.is_valid():

	                konf=form.save(commit=False)
			konf.image_original=request.FILES['image_original']
			konf.save()

			return HttpResponseRedirect(reverse('rotate-download',kwargs={'id':konf.id}))
	 return render(request, 'dango/rotate.html',{'form':form})


class RotateDownload(View):
	id=None
	def get (self,request,id):
    		img=Rotate.objects.get(id=id)
		filename='/home/dimansion/dango/media/{}'.format(img.image_original.name)
    		wrapper      = FileWrapper(open(filename))  # img.file returns full path to the image
	    	content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
    		response     = HttpResponse(wrapper,content_type=content_type)
    		response['Content-Length']      = os.path.getsize(filename)
    		response['Content-Disposition'] = "attachment; filename=%s" %  filename
    		return response

class ResizeView(View):
	template_name='dango/resize.html'
	def get (self,request):
	 form=ResizeForm()
	 return render(request,self.template_name,{'form':form})
	def post (self,request):
	 form=ResizeForm(request.POST)

	 if form.is_valid():
		konf=form.save(commit=False)
		konf.image_original=request.FILES['image_original']
		konf.save()


		return HttpResponseRedirect(reverse('resize-download',kwargs={'id':konf.id}))
	 return render(request, 'dango/resize.html',{'form':form})


class ResizeDownload(View):
	id=None
	def get (self,request,id):
    		img=Resize.objects.get(id=id)
		filename='/home/dimansion/dango/media/{}'.format(img.image_original.name)
    		wrapper      = FileWrapper(open(filename))  # img.file returns full path to the image
	    	content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
    		response     = HttpResponse(wrapper,content_type=content_type)
    		response['Content-Length']      = os.path.getsize(filename)
    		response['Content-Disposition'] = "attachment; filename=%s" %  filename
    		return response

class MemeView(View):
	template_name='dango/meme.html'
	def get (self,request):
	 form=MemeForm()
	 return render(request,self.template_name,{'form':form})
	def post (self,request):
	 form=MemeForm(request.POST)

	 if form.is_valid():
		konf=form.save(commit=False)
		konf.image_original=request.FILES['image_original']
		konf.save()


		return HttpResponseRedirect(reverse('meme-download',kwargs={'id':konf.id}))
	 return render(request, 'dango/meme.html',{'form':form})


class MemeDownload(View):
	id=None
	def get (self,request,id):
    		img=Meme.objects.get(id=id)
		filename='/home/dimansion/dango/media/{}'.format(img.image_original.name)
    		wrapper      = FileWrapper(open(filename))  # img.file returns full path to the image
	    	content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
    		response     = HttpResponse(wrapper,content_type=content_type)
    		response['Content-Length']      = os.path.getsize(filename)
    		response['Content-Disposition'] = "attachment; filename=%s" %  filename
    		return response

class WatermarkImgView(View):
	template_name='dango/watermark-img.html'
	def get (self,request):
	 form=WatermarkImgForm()
	 return render(request,self.template_name,{'form':form})
	def post (self,request):
	 form=WatermarkImgForm(request.POST)

	 if form.is_valid():
		konf=form.save(commit=False)
		konf.image_original=request.FILES['image_original']
		konf.image_logo=request.FILES['image_logo']
		konf.save()


		return HttpResponseRedirect(reverse('watermark-img-download',kwargs={'id':konf.id}))
	 return render(request, 'dango/watermark-img.html',{'form':form})



class WatermarkImgDownload(View):
	id=None
	def get (self,request,id):
    		img=WatermarkImg.objects.get(id=id)
		filename='/home/dimansion/dango/media/{}'.format(img.image_original.name)
    		wrapper      = FileWrapper(open(filename))  # img.file returns full path to the image
	    	content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
    		response     = HttpResponse(wrapper,content_type=content_type)
    		response['Content-Length']      = os.path.getsize(filename)
    		response['Content-Disposition'] = "attachment; filename=%s" %  filename
    		return response

class WatermarkTxtView(View):
	template_name='dango/watermark-txt.html'
	def get (self,request):
	 form=WatermarkTxtForm()
	 return render(request,self.template_name,{'form':form})
	def post (self,request):
	 form=WatermarkTxtForm(request.POST)

	 if form.is_valid():
		konf=form.save(commit=False)
		konf.image_original=request.FILES['image_original']
		konf.save()


		return HttpResponseRedirect(reverse('watermark-txt-download',kwargs={'id':konf.id}))
	 return render(request, 'dango/watermark-txt.html',{'form':form})


class WatermarkTxtDownload(View):
	id=None
	def get (self,request,id):
    		img=WatermarkTxt.objects.get(id=id)
		filename='/home/dimansion/dango/media/{}'.format(img.image_original.name)
    		wrapper      = FileWrapper(open(filename))  # img.file returns full path to the image
	    	content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
    		response     = HttpResponse(wrapper,content_type=content_type)
    		response['Content-Length']      = os.path.getsize(filename)
    		response['Content-Disposition'] = "attachment; filename=%s" %  filename
    		return response
