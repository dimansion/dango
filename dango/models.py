from django.db import models
from wand.image import Image
from wand.color import Color
from wand.font import Font
from wand.compat import nested
import os

class Convert(models.Model):
	FORMAT=(('png','png'),('jpg','jpg'),('tiff','tiff'),('pdf','pdf'))
	ekstensi=models.CharField(max_length=9,choices=FORMAT)
	image_original = models.ImageField(upload_to="images/",null=True,blank=True)
	image_converted = models.ImageField(upload_to="images/",null=True,blank=True)
	def save(self):
		super(Convert,self).save()
		fotoname="/home/dimansuardi/dango/media/{}".format(self.image_original.name)
		nama="/home/dimansion/dango/media/{}".format(self.image_original.name)
		with Image(filename=nama) as original:
			with original.convert(str(self.ekstensi)) as converted:
				base=os.path.basename(fotoname)

				nama=os.path.splitext(base)[0]

				converted.save(filename='/home/dimansion/dango/media/images/{}.{}'.format(nama,self.ekstensi))
		super(Convert,self).save()

class Resize(models.Model):
	image_original = models.ImageField (upload_to="images/",null=True,blank=True)
	image_converted = models.ImageField(upload_to="images/",null=True,blank=True)
	persen=models.IntegerField(null=True,blank=True)
	def save(self):
		super(Resize,self).save()
		fotoname="/home/dimansion/dango/media/{}".format(self.image_original.name)

		with Image(filename=fotoname) as img:
    		 width = img.width * self.persen/100
		 height = img.height * self.persen/100

     		 img.resize(width,height)

     		 img.save(filename=fotoname.format(self.image_original.name))
		super(Resize,self).save()

class Rotate(models.Model):
	Arah=(('kanan','kanan'),('kiri','kiri'))
	image_original = models.ImageField (upload_to="images/",null=True,blank=True)
	image_converted = models.ImageField(upload_to="images/")
	direction=models.CharField(max_length=7,null=True,blank=True,choices=Arah)
	def save(self):
		super(Rotate,self).save()
		fotoname="/home/dimansion/dango/media/{}".format(self.image_original.name)

       	 	with Image(filename=fotoname) as img:

			if str(self.direction) == 'kanan' :
                 	 img.rotate(90)
                 	 img.save(filename=fotoname.format(self.image_original.name))
			elif str(self.direction) == 'kiri' :
                 	 img.rotate(270)
                 	 img.save(filename=fotoname.format(self.image_original.name))
			else :
				print 'ga ada om'
		super(Rotate,self).save()

class Meme(models.Model):
	image_original = models.ImageField (upload_to="images/",null=True,blank=True)
	image_converted = models.ImageField(upload_to="images/")
	teksatas=models.CharField(max_length=20,null=True,blank=True)
	teksbawah=models.CharField(max_length=20,null=True,blank=True)
	url_image=models.CharField(max_length=250,null=True,blank=True)
	def save(self):
		super(Meme,self).save()
		fotoname="/home/dimansion/dango/media/{}".format(self.image_original.name)

		with Image(filename = fotoname) as source_img:
			warna= Color('#ffffff')
			font_title = Font(path='Quicksand-Regular.otf', size=70,color=warna)

			source_img.caption(self.teksatas,font=font_title,gravity='north')
			source_img.caption(self.teksbawah,top=source_img.height-80,font=font_title,gravity='north')
			source_img.save(filename=fotoname.format(self.teksatas,self.teksbawah,self.image_original.name))

class WatermarkTxt(models.Model):
	place=(('kanan atas','kanan atas'),('kanan bawah','kanan bawah'),('kiri atas','kiri atas'),('kiri bawah','kiri bawah'))
	image_original = models.ImageField (upload_to="images/",null=True,blank=True)
	image_converted = models.ImageField(upload_to="images/")
	url_image=models.CharField(max_length=250,null=True,blank=True)
	posisi=models.CharField(max_length=20,null=True,blank=True,choices=place)
	teks=models.CharField(max_length=20,null=True,blank=True)

	def save(self):
		super(WatermarkTxt,self).save()
		fotoname="/home/dimansion/dango/media/{}".format(self.image_original.name)

		with Image(filename = fotoname) as source_img:
		 	warna= Color('#ffffff')
			font_title = Font(path='AlexBrush-Regular.ttf', size=70,color=warna)

		 	if self.posisi == 'kanan atas':
				source_img.caption(self.teks,font=font_title,gravity='north_east')
				savename='result-kananatas.png'
			if self.posisi == 'kiri atas':
				source_img.caption(self.teks,font=font_title,gravity='north_west')
				savename='result-kiriatas.png'
			if self.posisi == 'kiri bawah':
				source_img.caption(self.teks,top=source_img.height-80,font=font_title,gravity='south_west')
				savename='result-kiribawah.png'
			if self.posisi == 'kanan bawah':
				source_img.caption(self.teks,top=source_img.height-80,font=font_title,gravity='south_east')
				savename='result-kananbawah.png'
			source_img.save(filename=fotoname.format(self.image_original.name))


class WatermarkImg(models.Model):
	place=(('kanan atas','kanan atas'),('kanan bawah','kanan bawah'),('kiri atas','kiri atas'),('kiri bawah','kiri bawah'))
	image_logo=models.ImageField (upload_to="images/",null=True,blank=True)
	image_original = models.ImageField (upload_to="images/",null=True,blank=True)
	image_converted = models.ImageField(upload_to="images/")
	url_image=models.CharField(max_length=250,null=True,blank=True)
	posisi=models.CharField(max_length=20,null=True,blank=True,choices=place)
	def save(self):
		super(WatermarkImg,self).save()
		fotonamelogo="/home/dimansion/dango/media/{}".format(self.image_logo.name)
		fotonamebase="/home/dimansion/dango/media/{}".format(self.image_original.name)
		images = (fotonamelogo,fotonamebase)
		with nested(Image(filename=images[0]),
 	           Image(filename=images[1])) as (rose, wizard):
       		   rose.transparentize(0.33)
		   x=0
                   y=0
		   savename=''
		   if self.posisi == 'kanan atas' :
	  	   	amex=wizard.width - rose.width
			y=0

 	       	   elif self.posisi == 'kanan bawah' :
    		        x=wizard.width - rose.width
			y=wizard.height - rose.height

  		   elif self.posisi == 'kiri bawah' :
    		        x=0
			y=wizard.height - rose.height

  		   elif self.posisi == 'kiri atas':
    		        x=0
                        y=0


  		   wizard.composite_channel("all_channels",rose,"dissolve",x,y)

                   wizard.save(filename=fotonamebase.format(self.image_original.name))
