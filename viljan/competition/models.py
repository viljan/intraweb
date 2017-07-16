from django.db import models

from viljan.library.models import Library


def get_new_library():
	return Library.objects.create().id

class Competition(models.Model):
	class Meta:
		verbose_name = 'tävling'
		verbose_name_plural = verbose_name + 'ar'
		
	def save(self, *args, **kwargs):
		if self.active:
			Competition.objects.filter(active=True).update(active=False)
		else:
			if not Competition.objects.filter(active=True):
				self.active = True
		super(Competition, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.name
	
	name = models.CharField('namn', max_length=100)
	eventor_id = models.PositiveIntegerField('Eventor-ID')
	active = models.BooleanField('aktiv')
	
	python_utilities = models.ManyToManyField('utility.PythonUtility', verbose_name='pythonverktyg', blank=True)
	command_line_utilities = models.ManyToManyField('utility.CommandLineUtility', verbose_name='kommandoradsverktyg', blank=True)
	library = models.ForeignKey('library.Library', default=get_new_library)
