from django.core.management.base import BaseCommand
from django.db.models import Max, Min
from ulmart.models import *
import random
import datetime

NAMES='Data/names.txt'
SURNAMES='Data/surnames.txt'
OLDNAMES='Data/oldnames.txt'
MANUFACTURERS='Data/manufacturers.txt'
COUNTRY='Data/country.txt'
PROPERTY='Data/property.txt'
PROPERTIES='Data/properties.txt'
TYPE='Data/type.txt'
PRODUCT_NAME='Data/product_name.txt'
PRODUCT_DESCRIPTION='Data/product_description.txt'
REVIEW_DESCRIPTION='Data/review_description.txt'
ADDRESS='Data/address.txt'
PHONE='Data/phone.txt'

MAXIMUM_LEVEL=3

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument('table')
		parser.add_argument('count')

	def getLinesCount(self, filename):
		with open(filename, 'r') as f:
			return(sum(1 for _ in f))

	def getRandomLine(self, filename):
		#Random int between 0 and line's count
		num=random.randint(0,self.getLinesCount(filename)-1)

		#Opening file, and searching for needed line
		f = open(filename, 'r')
		i=0
		for line in f:
			if i==num:
				return(str.strip(line))
			i+=1
		return("null")

	def addUsers(self, count):
		#Check if this table is empty
		if My_user.objects.count()==0:
			max_id=0
		else:
			max_id = My_user.objects.order_by('-user_id')[0].user_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_name=self.getRandomLine(NAMES)
			new_surname=self.getRandomLine(SURNAMES)
			new_oldname=self.getRandomLine(OLDNAMES)
			new_date=datetime.date(random.randint(2006,2016), random.randint(1,12),random.randint(1,28))

			#Creating new object and saving it
			new_user = My_user(user_id=new_id, name=new_name, surname=new_surname, oldname=new_oldname, reg_date=new_date)
			new_user.save()

			i+=1
		print(str(count)+" row(s) successfully added in table my_user.")

	def addSells(self, count):
		#Check if there is no users
		if My_user.objects.count()==0:
			print('No users!')
			return

		#Check if this table is empty
		if Sells.objects.count()==0:
			max_id=0
		else:
			max_id = Sells.objects.order_by('-sell_id')[0].sell_id

		#Variables for generation limits
		min_user_id=My_user.objects.order_by('user_id')[0].user_id
		max_user_id=My_user.objects.order_by('-user_id')[0].user_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_user_id=random.randint(min_user_id, max_user_id)
			new_date=datetime.date(random.randint(2006,2016), random.randint(1,12),random.randint(1,28))

			#Creating new object and saving it
			new_sell = Sells(sell_id=new_id, user_id=new_user_id, sell_date=new_date)
			new_sell.save()

			i+=1
		print(str(count)+" row(s) successfully added in table sells.")

	def addManufacturers(self, count):
		#Check if this table is empty
		if Manufacturer.objects.count()==0:
			max_id=0
		else:
			max_id = Manufacturer.objects.order_by('-manufacturer_id')[0].manufacturer_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_name=self.getRandomLine(MANUFACTURERS)
			new_country=self.getRandomLine(COUNTRY)

			#Creating new object and saving it
			new_manufacturer = Manufacturer(manufacturer_id=new_id, name=new_name, country=new_country)
			new_manufacturer.save()

			i+=1
		print(str(count)+" row(s) successfully added in table manufacturer.")

	def addProperty(self, count):
		#Check if this table is empty
		if Property.objects.count()==0:
			max_id=0
		else:
			max_id = Property.objects.order_by('-property_id')[0].property_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_name=self.getRandomLine(PROPERTY)

			#Creating new object and saving it
			new_property = Property(property_id=new_id, name=new_name)
			new_property.save()

			i+=1
		print(str(count)+" row(s) successfully added in table property.")

	def addType_prop(self, count):
		#Check if there is no data in property or type
		if Property.objects.count()==0 or Type.objects.count()==0:
			print('No data in property or type table!')
			return

		#Check if this table is empty
		if Type_prop.objects.count()==0:
			max_id=0
		else:
			max_id = Type_prop.objects.order_by('-id')[0].id

		#Variables for generation limits
		min_property_id=Property.objects.order_by('property_id')[0].property_id
		max_property_id=Property.objects.order_by('-property_id')[0].property_id

		min_type_id=Type.objects.order_by('type_id')[0].type_id
		max_type_id=Type.objects.order_by('-type_id')[0].type_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_type_id=random.randint(min_type_id, max_type_id)
			new_property_id=random.randint(min_property_id, max_property_id)

			#Creating new object and saving it
			new_type_prop = Type_prop(id=new_id, property_id=new_property_id, type_id=new_type_id)
			new_type_prop.save()

			i+=1
		print(str(count)+" row(s) successfully added in table type_prop.")

	def addSells_entre(self, count):
		#Check if there is no data in storage or product
		if Storage.objects.count()==0 or Product.objects.count()==0 or Sells.objects.count()==0:
			print('No data in storage or product or sells table!')
			return

		#Check if this table is empty
		if Sells_entre.objects.count()==0:
			max_id=0
		else:
			max_id = Sells_entre.objects.order_by('-id')[0].id

		#Variables for generation limits
		min_product_id=Product.objects.order_by('product_id')[0].product_id
		max_product_id=Product.objects.order_by('-product_id')[0].product_id

		min_storage_id=Storage.objects.order_by('storage_id')[0].storage_id
		max_storage_id=Storage.objects.order_by('-storage_id')[0].storage_id

		min_sell_id=Sells.objects.order_by('sell_id')[0].sell_id
		max_sell_id=Sells.objects.order_by('-sell_id')[0].sell_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_sell_id=random.randint(min_sell_id, max_sell_id)
			new_product_id=random.randint(min_product_id, max_product_id)
			new_storage_id=random.randint(min_storage_id, max_storage_id)
			new_product_price=random.uniform(1000, 40000)
			new_quantity=random.randint(1,100)

			#Creating new object and saving it
			new_sells_entre = Sells_entre(id=new_id, sell_id=new_sell_id, product_id=new_product_id, storage_id=new_storage_id, product_price=new_product_price, quantity=new_quantity)
			new_sells_entre.save()

			i+=1
		print(str(count)+" row(s) successfully added in table sells_entre.")

	def addSupply(self, count):
		#Check if there is no data in storage or product
		if Storage.objects.count()==0 or Product.objects.count()==0:
			print('No data in storage or product table!')
			return

		#Check if this table is empty
		if Supply.objects.count()==0:
			max_id=0
		else:
			max_id = Supply.objects.order_by('-id')[0].id

		#Variables for generation limits
		min_product_id=Product.objects.order_by('product_id')[0].product_id
		max_product_id=Product.objects.order_by('-product_id')[0].product_id

		min_storage_id=Storage.objects.order_by('storage_id')[0].storage_id
		max_storage_id=Storage.objects.order_by('-storage_id')[0].storage_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_product_id=random.randint(min_product_id, max_product_id)
			new_storage_id=random.randint(min_storage_id, max_storage_id)
			new_supply_date=datetime.date(random.randint(2006,2016), random.randint(1,12),random.randint(1,28))
			new_quantity=random.randint(1,500)

			#Creating new object and saving it
			new_supply = Supply(id=new_id, product_id=new_product_id, storage_id=new_storage_id, supply_date=new_supply_date, quantity=new_quantity)
			new_supply.save()

			i+=1
		print(str(count)+" row(s) successfully added in table supply.")

	def addProperties(self, count):
		#Check if there is no data in property or product
		if Property.objects.count()==0 or Product.objects.count()==0:
			print('No data in property or product table!')
			return

		#Check if this table is empty
		if Properties.objects.count()==0:
			max_id=0
		else:
			max_id = Properties.objects.order_by('-id')[0].id

		#Variables for generation limits
		min_property_id=Property.objects.order_by('property_id')[0].property_id
		max_property_id=Property.objects.order_by('-property_id')[0].property_id

		min_product_id=Product.objects.order_by('product_id')[0].product_id
		max_product_id=Product.objects.order_by('-product_id')[0].product_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_product_id=random.randint(min_product_id, max_product_id)
			new_property_id=random.randint(min_property_id, max_property_id)
			new_prop_value=self.getRandomLine(PROPERTIES)

			#Creating new object and saving it
			new_properties = Properties(id=new_id, product_id=new_product_id, property_id=new_property_id, prop_value=new_prop_value)
			new_properties.save()

			i+=1
		print(str(count)+" row(s) successfully added in table properties.")

	def addProduct_avaliability(self, count):
		#Check if there is no data in storage or product
		if Storage.objects.count()==0 or Product.objects.count()==0:
			print('No data in storage or product table!')
			return

		#Check if this table is empty
		if Product_avaliability.objects.count()==0:
			max_id=0
		else:
			max_id = Product_avaliability.objects.order_by('-id')[0].id

		#Variables for generation limits
		min_product_id=Product.objects.order_by('product_id')[0].product_id
		max_product_id=Product.objects.order_by('-product_id')[0].product_id

		min_storage_id=Storage.objects.order_by('storage_id')[0].storage_id
		max_storage_id=Storage.objects.order_by('-storage_id')[0].storage_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_product_id=random.randint(min_product_id, max_product_id)
			new_storage_id=random.randint(min_storage_id, max_storage_id)
			new_quantity=random.randint(1,500)

			#Creating new object and saving it
			new_product_avaliability = Product_avaliability(id=new_id, product_id=new_product_id, storage_id=new_storage_id, quantity=new_quantity)
			new_product_avaliability.save()

			i+=1
		print(str(count)+" row(s) successfully added in table product_avaliability.")

	def addProduct_types(self, count):
		#Check if there is no data in product or type
		if Product.objects.count()==0 or Type.objects.count()==0:
			print('No data in product or type table!')
			return

		#Check if this table is empty
		if Product_types.objects.count()==0:
			max_id=0
		else:
			max_id = Product_types.objects.order_by('-id')[0].id

		#Variables for generation limits
		min_product_id=Product.objects.order_by('product_id')[0].product_id
		max_product_id=Product.objects.order_by('-product_id')[0].product_id

		min_type_id=Type.objects.order_by('type_id')[0].type_id
		max_type_id=Type.objects.order_by('-type_id')[0].type_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_type_id=random.randint(min_type_id, max_type_id)
			new_product_id=random.randint(min_product_id, max_product_id)

			#Creating new object and saving it
			new_product_type = Product_types(id=new_id, product_id=new_product_id, type_id=new_type_id)
			new_product_type.save()

			i+=1
		print(str(count)+" row(s) successfully added in table product_types.")

	def addProduct(self, count):
		#Check if there is no data in manufacturer
		if Manufacturer.objects.count()==0:
			print('No data in manufacturer table!')
			return

		#Check if this table is empty
		if Product.objects.count()==0:
			max_id=0
		else:
			max_id = Product.objects.order_by('-product_id')[0].product_id

		#Variables for generation limits
		min_manufacturer_id=Manufacturer.objects.order_by('manufacturer_id')[0].manufacturer_id
		max_manufacturer_id=Manufacturer.objects.order_by('-manufacturer_id')[0].manufacturer_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_manufacturer_id=random.randint(min_manufacturer_id, max_manufacturer_id)
			new_name=self.getRandomLine(PRODUCT_NAME)
			new_description=self.getRandomLine(PRODUCT_DESCRIPTION)
			new_price=random.uniform(1000, 40000)

			#Creating new object and saving it
			new_product = Product(product_id=new_id, manufacturer_id=new_manufacturer_id, name=new_name, description=new_description, price=new_price)
			new_product.save()

			i+=1
		print(str(count)+" row(s) successfully added in table product.")

	def addStorage(self, count):
		#Check if this table is empty
		if Storage.objects.count()==0:
			max_id=0
		else:
			max_id = Storage.objects.order_by('-storage_id')[0].storage_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_address=self.getRandomLine(ADDRESS)
			new_phone=self.getRandomLine(PHONE)

			#Creating new object and saving it
			new_storage = Storage(storage_id=new_id, address=new_address, phone=new_phone)
			new_storage.save()

			i+=1
		print(str(count)+" row(s) successfully added in table storage.")

	def addReview(self, count):
		#Check if there is no data in product or my_user
		if Product.objects.count()==0 or My_user.objects.count()==0:
			print('No data in product or my_user table!')
			return

		#Check if this table is empty
		if Review.objects.count()==0:
			max_id=0
		else:
			max_id = Review.objects.order_by('-id')[0].id

		#Variables for generation limits
		min_product_id=Product.objects.order_by('product_id')[0].product_id
		max_product_id=Product.objects.order_by('-product_id')[0].product_id

		min_my_user_id=My_user.objects.order_by('user_id')[0].user_id
		max_my_user_id=My_user.objects.order_by('-user_id')[0].user_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_product_id=random.randint(min_product_id, max_product_id)
			new_user_id=random.randint(min_my_user_id, max_my_user_id)
			new_rating=random.randint(1,5)
			new_description=self.getRandomLine(REVIEW_DESCRIPTION)

			#Creating new object and saving it
			new_review = Review(id=new_id, product_id=new_product_id, user_id=new_user_id, rating=new_rating, description=new_description)
			new_review.save()

			i+=1
		print(str(count)+" row(s) successfully added in table review.")

	def addType(self, count):
		#Check if this table is empty
		if Type.objects.count()==0:
			max_id=0
		else:
			max_id = Type.objects.order_by('-type_id')[0].type_id

		#Starting of loop
		i=1
		while i<=count:
			new_id=max_id+i
			new_name=self.getRandomLine(TYPE)

			#50 at 50 if new type will have parent, also checking if parent is possible
			if random.randint(0,1)==0 or new_id==1:
				new_p_id=None
				new_level=1
			else:
				#Random parent
				min_p_id=Type.objects.order_by('type_id')[0].type_id
				max_p_id=Type.objects.order_by('-type_id')[0].type_id
				new_p_id=random.randint(min_p_id, max_p_id)
				#Selecting parent level and incrasing it
				new_level=Type.objects.get(pk=new_p_id).level+1
				if new_level>MAXIMUM_LEVEL:
					continue
		
			#Creating new object and saving it	
			new_type = Type(type_id=new_id, p_id=new_p_id, name=new_name, level=new_level)
			new_type.save()
			
			i+=1
		print(str(count)+" row(s) successfully added in table type.")

	def handle(self, *args, **options):
		#Reading input options
		table = options['table']
		count = int(options['count'])

		#Checking of options
		if count<=0:
			print('Wrong count!')
			return
		if table=='my_user':
			self.addUsers(count)
		elif table=='sells':
			self.addSells(count)
		elif table=='manufacturer':
			self.addManufacturers(count)
		elif table=='property':
			self.addProperty(count)
		elif table=='type':
			self.addType(count)
		elif table=='type_prop':
			self.addType_prop(count)
		elif table=='supply':
			self.addSupply(count)
		elif table=='product':
			self.addProduct(count)
		elif table=='product_types':
			self.addProduct_types(count)
		elif table=='review':
			self.addReview(count)
		elif table=='properties':
			self.addProperties(count)
		elif table=='sells_entre':
			self.addSells_entre(count)
		elif table=='storage':
			self.addStorage(count)
		elif table=='product_avaliability':
			self.addProduct_avaliability(count)
		elif table=='all':
			self.addUsers(count)
			self.addManufacturers(count)
			self.addSells(count)
			self.addProperty(count)
			self.addType(count)
			self.addType_prop(count)
			self.addProduct(count)
			self.addProduct_types(count)
			self.addReview(count)
			self.addStorage(count)
			self.addProduct_avaliability(count)
			self.addProperties(count)
			self.addSupply(count)
			self.addSells_entre(count)