from django.db import models

class IPO(models.Model):
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    price_band = models.CharField(max_length=50)
    open_date = models.CharField(max_length=50)
    close_date = models.CharField(max_length=50)
    issue_size = models.CharField(max_length=50)
    issue_type = models.CharField(max_length=50)
    listing_date = models.CharField(max_length=50)
    rhp_pdf = models.URLField(blank=True, null=True)
    drhp_pdf = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name