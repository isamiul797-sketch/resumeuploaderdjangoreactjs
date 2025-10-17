from django.db import models

STATE_CHOICES = [
        ('DHAKA', 'Dhaka'),
        ('CHATTOGRAM', 'Chattogram'),
        ('RAJSHAHI', 'Rajshahi'),
        ('KHULNA', 'Khulna'),
        ('BARISHAL', 'Barishal'),
        ('SYLHET', 'Sylhet'),
        ('RANGPUR', 'Rangpur'),
        ('MYMENSINGH', 'Mymensingh'),
    ]

class Profile(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices= STATE_CHOICES, max_length=55)
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    pimg = models.ImageField(upload_to='pimgs',blank=True)
    rdoc = models.FileField(upload_to='rdocs',blank=True)
