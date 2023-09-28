from django.db import models

# Create your models here.

class School(models.Model):
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
    
class SchoolSearch(models.Model):
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
    
