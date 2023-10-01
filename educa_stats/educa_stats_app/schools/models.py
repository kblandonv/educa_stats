from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Nombre del colegio')
    address = models.CharField(max_length=100, help_text='Dirección del colegio')
    phone_number = models.CharField(max_length=20, null=True, blank=True, help_text='Número de teléfono del colegio')
    email = models.EmailField(null=True, blank=True, help_text='Correo electrónico del colegio')
    website = models.URLField(null=True, blank=True, help_text='Sitio web del colegio')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, help_text='Latitud del colegio')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, help_text='Longitud del colegio')

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('schools:school_detail', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse('schools:school_update', kwargs={'pk': self.pk})
    
    def get_delete_url(self):
        return reverse('schools:school_delete', kwargs={'pk': self.pk})
    def get_add_url(self):
        return reverse('schools:school_add', kwargs={'pk': self.pk})
    
    def get_search_url(self):
        return reverse('schools:school_search', kwargs={'pk': self.pk})
    
class SchoolSearch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone_number = models.PhoneNumerField()
    email = models.EmailField()
    website = models.URLField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('schools:school_detail', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse('schools:school_update', kwargs={'pk': self.pk})
    
    def get_delete_url(self):
        return reverse('schools:school_delete', kwargs={'pk': self.pk})
    
    def get_add_url(self):
        return reverse('schools:school_add', kwargs={'pk': self.pk})
    
    def get_search_url(self):
        return reverse('schools:school_search', kwargs={'pk': self.pk})
    
class SchoolAdd(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('schools:school_detail', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse('schools:school_update', kwargs={'pk': self.pk})
    
    def get_delete_url(self):
        return reverse('schools:school_delete', kwargs={'pk': self.pk})
    
    def get_add_url(self):
        return reverse('schools:school_add', kwargs={'pk': self.pk})
    
    def get_search_url(self):
        return reverse('schools:school_search', kwargs={'pk': self.pk})
    
class SchoolUpdate(models.Model):
    class SchoolUpdate(models.Model):
        name = models.CharField(max_length=100, unique=True)
        address = models.CharField(max_length=100)
        phone_number = models.PhoneNumberField()
        email = models.EmailField()
        website = models.URLField()
        coordinates = models.PointField()

        def __str__(self):
            return self.name
    
        def get_url(self, action):
            if action == 'absolute':
                return reverse('schools:school_detail', kwargs={'pk': self.pk})
            elif action == 'update':
                return reverse('schools:school_update', kwargs={'pk': self.pk})
            elif action == 'delete':
                return reverse('schools:school_delete', kwargs={'pk': self.pk})
            elif action == 'add':
                return reverse('schools:school_add', kwargs={'pk': self.pk})
            elif action == 'search':
                return reverse('schools:school_search', kwargs={'pk': self.pk})
            else:
                return reverse('schools:school_detail', kwargs={'pk': self.pk})
            
class SchoolDelete(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('schools:school_detail', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse('schools:school_update', kwargs={'pk': self.pk})
    
    def get_delete_url(self):
        return reverse('schools:school_delete', kwargs={'pk': self.pk})
    
    def get_add_url(self):
        return reverse('schools:school_add', kwargs={'pk': self.pk})
    
    def get_search_url(self):
        return reverse('schools:school_search', kwargs={'pk': self.pk})
    
class SchoolSearchResults(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('schools:school_detail', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse('schools:school_update', kwargs={'pk': self.pk})
    
    def get_delete_url(self):
        return reverse('schools:school_delete', kwargs={'pk': self.pk})
    
    def get_add_url(self):
        return reverse('schools:school_add', kwargs={'pk': self.pk})
    
    def get_search_url(self):
        return reverse('schools:school_search', kwargs={'pk': self.pk})
    
