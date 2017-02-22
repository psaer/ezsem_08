from django.core.management.base import BaseCommand
from ulmart.models import *

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_property(self):
        temp1 = Property(property_id=1, name='prop_1')
        temp1.save()
        temp2 = Property(property_id=2, name='prop_2')
        temp2.save()
        temp3 = Property(property_id=3, name='prop_3')
        temp3.save()

    def _create_type(self):
        temp1 = Type(type_id=1, name='type_1', level=1)
        temp1.save()
        temp2 = Type(type_id=2, p_id=1, name='type_2', level=2)
        temp2.save()
        temp3 = Type(type_id=3, name='type_3', level=1)
        temp3.save()

    def _create_type_prop(self):
    	temp1 = Type_prop(id=1, property_id=1, type_id=1)
    	temp1.save()
    	temp2 = Type_prop(id=2, property_id=2, type_id=2)
    	temp2.save()
    	temp3 = Type_prop(id=3, property_id=3, type_id=3)
    	temp3.save()

    def _create_manufacturer(self):
    	temp1 = Manufacturer(manufacturer_id=1, name='manufac_1', country='China')
    	temp1.save()
    	temp2 = Manufacturer(manufacturer_id=2, name='manufac_2', country='China')
    	temp2.save()
    	temp3 = Manufacturer(manufacturer_id=3, name='manufac_3', country='China')
    	temp3.save()

    def _create_product(self):
    	temp1 = Product(product_id=1, manufacturer_id=1, name='name_1', description='desc_1', price=5000.20)
    	temp1.save()
    	temp2 = Product(product_id=2, manufacturer_id=2, name='name_2', description='desc_2', price=8000.20)
    	temp2.save()
    	temp3 = Product(product_id=3, manufacturer_id=3, name='name_3', description='desc_3', price=9000.20)
    	temp3.save()

    def _create_product_types(self):
    	temp1 = Product_types(id=1, product_id=1, type_id=1)
    	temp1.save()
    	temp2 = Product_types(id=2, product_id=2, type_id=2)
    	temp2.save()
    	temp3 = Product_types(id=3, product_id=3, type_id=3)
    	temp3.save()

    def _create_properties(self):
    	temp1 = Properties(id=1, product_id=1, property_id=1, prop_value='value_1')
    	temp1.save()
    	temp2 = Properties(id=2, product_id=2, property_id=3, prop_value='value_2')
    	temp2.save()
    	temp3 = Properties(id=3, product_id=3, property_id=3, prop_value='value_3')
    	temp3.save()

    def _create_my_user(self):
    	temp1 = My_user(user_id=1, name='name_1', surname='surname_1', oldname='oldname_1', reg_date='2017-10-10')
    	temp1.save()
    	temp2 = My_user(user_id=2, name='name_2', surname='surname_2', oldname='oldname_2', reg_date='2017-10-10')
    	temp2.save()
    	temp3 = My_user(user_id=3, name='name_3', surname='surname_3', oldname='oldname_3', reg_date='2017-10-10')
    	temp3.save()

    def _create_review(self):
    	temp1 = Review(id=1, product_id=1, user_id=1, rating=5, description='desc_1')
    	temp1.save()
    	temp2 = Review(id=2, product_id=2, user_id=2, rating=5, description='desc_2')
    	temp2.save()
    	temp3 = Review(id=3, product_id=3, user_id=3, rating=5, description='desc_3')
    	temp3.save()

    def _create_sells(self):
    	temp1 = Sells(sell_id=1, user_id=1, sell_date='2017-10-10')
    	temp1.save()
    	temp2 = Sells(sell_id=2, user_id=2, sell_date='2017-10-10')
    	temp2.save()
    	temp3 = Sells(sell_id=3, user_id=3, sell_date='2017-10-10')
    	temp3.save()

    def _create_storage(self):
    	temp1 = Storage(storage_id=1, address='addr_1', phone='phone_1')
    	temp1.save()
    	temp2 = Storage(storage_id=2, address='addr_2', phone='phone_2')
    	temp2.save()
    	temp3 = Storage(storage_id=3, address='addr_3', phone='phone_3')
    	temp3.save()

    def _create_product_avaliability(self):
    	temp1 = Product_avaliability(id=1, product_id=1, storage_id=1, quantity=10)
    	temp1.save()
    	temp2 = Product_avaliability(id=2, product_id=2, storage_id=2, quantity=10)
    	temp2.save()
    	temp3 = Product_avaliability(id=3, product_id=3, storage_id=3, quantity=10)
    	temp3.save()

    def _create_supply(self):
    	temp1 = Supply(id=1, product_id=1, storage_id=1, supply_date='2017-10-10', quantity=5)
    	temp1.save()
    	temp2 = Supply(id=2, product_id=2, storage_id=2, supply_date='2017-10-10', quantity=5)
    	temp2.save()
    	temp3 = Supply(id=3, product_id=3, storage_id=3, supply_date='2017-10-10', quantity=5)
    	temp3.save()

    def _create_sells_entre(self):
    	temp1 = Sells_entre(id=1, sell_id=1, product_id=1, storage_id=1, product_price=413.21, quantity=10)
    	temp1.save()
    	temp2 = Sells_entre(id=2, sell_id=2, product_id=3, storage_id=2, product_price=442.21, quantity=10)
    	temp2.save()
    	temp3 = Sells_entre(id=3, sell_id=3, product_id=3, storage_id=3, product_price=5313.21, quantity=10)
    	temp3.save()


    def handle(self, *args, **options):
        self._create_property()
        self._create_type()
        self._create_type_prop()
        self._create_manufacturer()
        self._create_product()
        self._create_product_types()
        self._create_properties()
        self._create_my_user()
        self._create_review()
        self._create_sells()
        self._create_storage()
        self._create_product_avaliability()
        self._create_supply()
        self._create_sells_entre()