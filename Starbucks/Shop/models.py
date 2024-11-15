from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    size = models.CharField(max_length=50)  # Adjust as per your requirement
    created_at = models.DateTimeField(auto_now_add=True)  # Ensure this line exists

    def __str__(self):
        return f"Order by {self.customer_name} for {self.product.name}"
