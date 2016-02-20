from django.db import models

from offices.models import Office


class Client(models.Model):
    office = models.ForeignKey(Office)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "[%s] %s" % (self.office, self.name)

class Contact(models.Model):
    client = models.ForeignKey(Client)
    last_name = models.TextField()
    first_name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    
    def _get_full_name(self):
        return ('%s %s' % (self.first_name, self.last_name)).strip()

    full_name = property(_get_full_name)

    def __str__(self):
        return self.full_name
