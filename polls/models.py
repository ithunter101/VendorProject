from django.db import models


# Create your models here.
class VendorCategory(models.Model):
    vendorCategory = models.AutoField(primary_key=True)
    vendorCategoryName = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return "%d %s" % (self.vendorCategory, self.vendorCategoryName)

    class Meta:
        db_table = "db_vendor_categories"


class Vendor(models.Model):
    vendorId = models.AutoField(primary_key=True)
    vendorName = models.CharField(max_length=50, blank=False)
    vendorCategory = models.ForeignKey(VendorCategory, on_delete=models.CASCADE)

    def __str__(self):
        return "%d %s" % (self.vendorId, self.vendorName)

    class Meta:
        db_table = "db_vendors"
        ordering = ['vendorId']
