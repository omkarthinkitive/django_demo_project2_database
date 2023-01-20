from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=2)

    # By using this we can change the columns name of table in admin panel
    def __str__(self):
        return f"{self.name}  {self.code}"
    
    # By using this class we can change the name of table in admin panel
    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.city}  {self.pincode}"
    
    class Meta:
        verbose_name_plural = "Address"



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True) 
    # on_delete=CASCADE : suppose author is deleted but in books model author books also establish relation 
    #  cascade will act as author is deleted then in boks model all the books belongs to that author 
    # also get deleted
    is_bestselling = models.BooleanField(default=False)
    publish_countries = models.ManyToManyField(Country)
            
        
    # This method used for display the data as per our convience
    def __str__(self):
        return f"{self.title} ({self.rating}),{self.author},{self.is_bestselling}"
    

