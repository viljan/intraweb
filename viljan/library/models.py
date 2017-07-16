from hashlib import md5
from datetime import datetime
import os

from django.db import models


def get_filename(instance, filename):
	now = datetime.now()
	base = now.strftime('library_files/%Y/%m/%d')
	hash = md5(str(now).encode('utf-8'))
	return os.path.join(base, '{}_{}'.format(hash.hexdigest(), filename))

class Library(models.Model):
	class Meta:
		verbose_name = 'filbibliotek'
		verbose_name_plural = verbose_name
	
	def __str__(self):
		return self.name or self._meta.verbose_name.title() + ' #' + str(self.id)
		
	name = models.CharField('namn', blank=True, null=True, max_length=100)
	
	documents = models.ManyToManyField('library.Document', verbose_name='dokumentation', blank=True, related_name='library')
	applications = models.ManyToManyField('library.Application', verbose_name='programvaror', blank=True, related_name='library')
	drivers = models.ManyToManyField('library.Driver', verbose_name='drivrutiner', blank=True, related_name='library')
	
class File(models.Model):
	def __str__(self):
		if self.version:
			return self.name + ' (' + self.version + ')'
		else:
			return self.name 
	
	name = models.CharField('namn', max_length=100)
	data = models.FileField('data', upload_to=get_filename)
	uploaded_at = models.DateTimeField('uppladdad', auto_now=True)
	version = models.CharField('version', blank=True, null=True, max_length=20)
	description = models.CharField('beskrivning', blank=True, null=True, max_length=100)
	
class Document(File):
	class Meta:
		verbose_name = 'dokument'
		verbose_name_plural = verbose_name
	
class Software(File):
	class Meta:
		verbose_name = 'dokument'
		verbose_name_plural = verbose_name
		
	update_url = models.URLField('länk till uppdatering', blank=True, null=True)
	documents = models.ManyToManyField(Document, verbose_name='dokument', blank=True)
	
class Application(Software):
	class Meta:
		verbose_name = 'programvara'
		verbose_name_plural = 'programvaror'
		
	developer = models.CharField('utvecklare', blank=True, null=True, max_length=100)

class Driver(Software):
	class Meta:
		verbose_name = 'drivrutin'
		verbose_name_plural = verbose_name + 'er'
		
	used_for = models.CharField('används till', blank=True, null=True, max_length=100)
