from django.db import models


class Company(models.Model):
    # Basic Information
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)

    # Company Type and Size
    TYPE_CHOICES = [
        ('Private', 'Private'),
        ('Public', 'Public'),
        ('Nonprofit', 'Nonprofit'),
        ('Government', 'Government'),
        ('Other', 'Other'),
    ]
    company_type = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True,
                            null=True)  # You can use CharField or IntegerField based on how you want to store size

    # Logo
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    # Contact Information
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    # Address
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    # Social Media Links
    facebook_profile = models.URLField(blank=True, null=True)
    twitter_profile = models.URLField(blank=True, null=True)
    instagram_profile = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name


