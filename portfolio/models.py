from django.db import models

# The class project is inheriting the Model class provided by django. we can add model field references.
# CharField is for storing strings , we can limit the number of characters .
# we can store image using ImageField from Django DB

class Project (models.Model):
    title=models.CharField(max_length=100)
    descriptions=models.CharField(max_length=250)
    image=models.ImageField(upload_to="portfolio/images/")
    url= models.URLField(blank=True)
    # the blank parameter is used to add a class memeber as optional
    def __str__(self):
        return self.title

# the changes in models can be reflected on the database by creating migrations.this will sync-up the database tables with the changes in model classes.
# " python3 manage.py migrate " will do the migrations
