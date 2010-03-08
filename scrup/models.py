import datetime

from django.db import models

class Date(models.Model):
    """A date during which a screenshot was uploaded"""
    date = models.DateField(default=datetime.date.today)
    
    def __unicode__(self):
        return self.date.isoformat()
    
class Screenshot(models.Model):
    """A single screenshot uploaded to django-scrup."""
    date = models.ForeignKey(Date, related_name='screenshots')
    name = models.CharField(blank=True, null=True, max_length=255)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        ordering = ('-timestamp',)
        verbose_name, verbose_name_plural = "Screenshot", "Screenshots"

    def __unicode__(self):
        return self.name or self.timestamp.isoformat()
