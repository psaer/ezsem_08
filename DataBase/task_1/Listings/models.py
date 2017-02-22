from django.db import models

class My_user(models.Model):
    user_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    surname=models.CharField(max_length=200)
    oldname=models.CharField(max_length=200)
    reg_date = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        db_table = "My_user"

class Sells(models.Model):
	sell_id=models.IntegerField(primary_key=True)
	user=models.ForeignKey('My_user')
	sell_date = models.DateField(auto_now=False, auto_now_add=False)

	class Meta:
		db_table = "Sells"
		
class Manufacturer(models.Model):
	manufacturer_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=200)
	country=models.CharField(max_length=200)

	class Meta:
		db_table = "Manufacturer"

class Type(models.Model):
	type_id=models.IntegerField(primary_key=True)
	p=models.ForeignKey('Type', null=True)
	name=models.CharField(max_length=200)
	level=models.IntegerField()

	class Meta:
		db_table = "Type"

class Property(models.Model):
	property_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=200)

	class Meta:
		db_table = "Property"

class Type_prop(models.Model):
	type=models.ForeignKey('Type')
	property=models.ForeignKey('Property')

	class Meta:
		db_table = "Type_prop"

class Product(models.Model):
	product_id=models.IntegerField(primary_key=True)
	manufacturer=models.ForeignKey('Manufacturer')
	name=models.CharField(max_length=200)
	description=models.CharField(max_length=200)
	price=models.FloatField()

	class Meta:
		db_table = "Product"

class Product_types(models.Model):
	product=models.ForeignKey('Product')
	type=models.ForeignKey('Type')

	class Meta:
		db_table = "Product_types"

class Properties(models.Model):
	product=models.ForeignKey('Product')
	property=models.ForeignKey('Property')
	prop_value=models.CharField(max_length=200)

	class Meta:
		db_table = "Properties"

class Review(models.Model):
	product=models.ForeignKey('Product')
	user=models.ForeignKey('My_user')
	rating=models.IntegerField()
	description=models.CharField(max_length=200)

	class Meta:
		db_table = "Review"

class Storage(models.Model):
	storage_id=models.IntegerField(primary_key=True)
	address=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)

	class Meta:
		db_table = "Storage"

class Product_avaliability(models.Model):
	product=models.ForeignKey('Product')
	storage=models.ForeignKey('Storage')
	quantity=models.IntegerField()

	class Meta:
		db_table = "Product_avaliability"

class Supply(models.Model):
	product=models.ForeignKey('Product')
	storage=models.ForeignKey('Storage')
	supply_date = models.DateField(auto_now=False, auto_now_add=True)
	quantity=models.IntegerField()

	class Meta:
		db_table = "Supply"

class Sells_entre(models.Model):
	sell=models.ForeignKey('Sells')
	product=models.ForeignKey('Product')
	storage=models.ForeignKey('Storage')
	product_price=models.FloatField()
	quantity=models.IntegerField()

	class Meta:
		db_table = "Sells_entre"