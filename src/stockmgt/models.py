from django.db import models

# Create your models here

category_choices=(
    ('Funitiure' , 'Furniture'),
    ('IT Equiment' , 'IT Equiment'),
    ('Phone' , 'Phone'),
    ('Electronic' , 'Electronic'),
)

class Category(models.Model):
    name=models.CharField(max_length=50 , blank=True , null=True)
    def __str__(self):
        return self.name


class Stock(models.Model):
    category=models.ForeignKey(Category , on_delete=models.CASCADE, blank=True)
    item_name=models.CharField(max_length=50 , blank=True , null=True)
    quantity=models.IntegerField(default=0 , blank=True , null=True)
    recieve_quantity=models.IntegerField(default=0, blank=True , null=True)
    recieve_by=models.CharField(max_length=50 , blank=True , null=True)
    recieve_to=models.CharField(max_length=50 , blank=True , null=True)
    issue_quantity=models.IntegerField(default=0 , blank=True , null=True)
    issue_by=models.CharField(max_length=50, blank=True , null=True)
    issue_to=models.CharField(max_length=50 , blank=True , null=True)
    phone_number=models.CharField(max_length=50, blank=True, null=True)
    created_by=models.CharField(max_length=50, blank=True, null=True)
    reorder_level=models.CharField(max_length=50, blank=True, null=True)
    last_updated=models.DateTimeField(auto_now_add=False,auto_now=True )
    timestamp=models.DateTimeField(auto_now_add=True ,auto_now=False)

    def __str__(self):
        return self.item_name 


class StockHistory(models.Model):
    category=models.ForeignKey(Category , on_delete=models.CASCADE, blank=True)
    item_name=models.CharField(max_length=50 , blank=True , null=True)
    quantity=models.IntegerField(default=0 , blank=True , null=True)
    recieve_quantity=models.IntegerField(default=0, blank=True , null=True)
    recieve_by=models.CharField(max_length=50 , blank=True , null=True)
    recieve_to=models.CharField(max_length=50 , blank=True , null=True)
    issue_quantity=models.IntegerField(default=0 , blank=True , null=True)
    issue_by=models.CharField(max_length=50, blank=True , null=True)
    issue_to=models.CharField(max_length=50 , blank=True , null=True)
    phone_number=models.CharField(max_length=50, blank=True, null=True)
    created_by=models.CharField(max_length=50, blank=True, null=True)
    reorder_level=models.CharField(max_length=50, blank=True, null=True)
    last_updated=models.DateTimeField(auto_now_add=False,auto_now=True )
    timestamp=models.DateTimeField(auto_now_add=True ,auto_now=False)

    def __str__(self):
        return self.item_name 