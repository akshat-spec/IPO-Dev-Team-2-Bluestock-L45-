from django.db import models

class IPO(models.Model):
    company_name = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='logos/')
    price_band_min = models.DecimalField(max_digits=10, decimal_places=2)
    price_band_max = models.DecimalField(max_digits=10, decimal_places=2)
    opening_date = models.DateField()
    closing_date = models.DateField()
    issue_size = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=100)
    listing_date = models.DateField()
    status = models.CharField(max_length=50)
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_gain = models.DecimalField(max_digits=10, decimal_places=2)
    cmp = models.DecimalField(max_digits=10, decimal_places=2)
    current_return = models.DecimalField(max_digits=10, decimal_places=2)
    rhp_pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)
    drhp_pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)

    def __str__(self):
        return self.company_name
