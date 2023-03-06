from django.db import models


class iha_product(models.Model):
    model_code = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        val = self.model_code
        # iha_property olusturulmamissa exception a düs isim ekleme
        try:
            val += "-" + self.iha_property.ad
        except:
            pass
        return val


class iha_property(models.Model):
    IHA_CATEGORY = (
        ('Keşif ve İstihbarat', 'Keşif ve İstihbarat'),
        ('Savunma', 'Savunma')
    )
    iha_Product = models.OneToOneField(iha_product, unique=True, on_delete=models.CASCADE)
    ad = models.CharField(max_length=200)
    marka = models.CharField(default="BAYKAR", max_length=200)
    model = models.CharField(max_length=200)
    agirlik = models.FloatField()
    kategori = models.CharField(max_length=200,choices=IHA_CATEGORY)
    tanim = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.ad + "-" + self.marka + "-" + self.model
