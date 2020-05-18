from connectionDB import db, Production, Sales

# Brands
new_brand = Brand(1, 'Electra')
db.session.add(new_brand)
db.session.commit()

new_brand = Brand(2,'Haro')
db.session.add(new_brand)
db.session.commit()

new_brand = Brand(3,'Heller')
db.session.add(new_brand)
db.session.commit()

new_brand = Brand(4,'Pure Cycles')
db.session.add(new_brand)
db.session.commit()

new_brand = Brand(5,'Ritchey')
db.session.add(new_brand)
db.session.commit()

new_brand = Brand(6,'Strider')
db.session.add(new_brand)
db.session.commit()

new_brand = Brand(7,'Sun Bicycles')
db.session.add(new_brand)
db.session.commit()

new_brand = Brand(8,'Surly')
db.session.add(new_brand)
db.session.commit()

new_brand = Brand(9,'Trek')
db.session.add(new_brand)
db.session.commit()


# Categories
new_category = Categories(1, 'Children Bicycles')
db.session.add(new_category)
db.session.commit()

new_category = Categories(2,'Comfort Bicycles')
db.session.add(new_category)
db.session.commit()

new_category = Categories(3,'Cruisers Bicycles')
db.session.add(new_category)
db.session.commit()

new_category = Categories(4,'Cyclocross Bicycles')
db.session.add(new_category)
db.session.commit()

new_category = Categories(5,'Electric Bikes')
db.session.add(new_category)
db.session.commit()

new_category = Categories(6,'Mountain Bikes')
db.session.add(new_category)
db.session.commit()

new_category = Categories(7,'Road Bikes')
db.session.add(new_category)
db.session.commit()


# Products
new_product = Products(1,'Trek 820 - 2016',9,6,2016,379.99)
db.session.add(new_product)
db.session.commit()

new_product = Products(2,'Ritchey Timberwolf Frameset - 2016',5,6,2016,749.99)
db.session.add(new_product)
db.session.commit()

new_product = Products(3,'Surly Wednesday Frameset - 2016',8,6,2016,999.99)
db.session.add(new_product)
db.session.commit()

new_product = Products(4,'Trek Fuel EX 8 29 - 2016',9,6,2016,2899.99)
db.session.add(new_product)
db.session.commit()

new_product = Products(5,'Heller Shagamaw Frame - 2016',3,6,2016,1320.99)
db.session.add(new_product)
db.session.commit()

new_product = Products(6,'Surly Ice Cream Truck Frameset - 2016',8,6,2016,469.99)
db.session.add(new_product)
db.session.commit()

new_product = Products(7,'Trek Slash 8 27.5 - 2016',9,6,2016,3999.99)
db.session.add(new_product)
db.session.commit()


# Customers
new_customer = Customers('Debra','Burks',NULL,'debra.burks@yahoo.com', '9273 Thorne Ave. ','Orchard Park','NY',14127)
db.session.add(new_customer)
db.session.commit()

new_customer = Customers('Kasha','Todd',NULL,'kasha.todd@yahoo.com','910 Vine Street ','Campbell','CA',95008)
db.session.add(new_customer)
db.session.commit()

new_customer = Customers('Tameka','Fisher',NULL,'tameka.fisher@aol.com','769C Honey Creek St. ','Redondo Beach','CA',90278)
db.session.add(new_customer)
db.session.commit()

new_customer = Customers('Daryl','Spence',NULL,'daryl.spence@aol.com','988 Pearl Lane ','Uniondale','NY',11553)
db.session.add(new_customer)
db.session.commit()

new_customer = Customers('Charolette','Rice','(916) 381-6003','charolette.rice@msn.com','107 River Dr. ','Sacramento','CA',95820)
db.session.add(new_customer)
db.session.commit()

new_customer = Customers('Lyndsey','Bean',NULL,'lyndsey.bean@hotmail.com','769 West Road ','Fairport','NY',14450)
db.session.add(new_customer)
db.session.commit()

new_customer = Customers('Latasha','Hays','(716) 986-3359','latasha.hays@hotmail.com','7014 Manor Station Rd. ','Buffalo','NY',14215)
db.session.add(new_customer)
db.session.commit()


# Stores
new_store = Stores('Santa Cruz Bikes','(831) 476-4321','santacruz@bikes.shop','3700 Portola Drive', 'Santa Cruz','CA',95060),
      ('Baldwin Bikes','(516) 379-8888','baldwin@bikes.shop','4200 Chestnut Lane', 'Baldwin','NY',11432),
      ('Rowlett Bikes','(972) 530-5555','rowlett@bikes.shop','8000 Fairway Avenue', 'Rowlett','TX',75088)
db.session.add(new_store)
db.session.commit()

# Stocks
new_stock = Stocks(1,1,27)
db.session.add(new_stock)
db.session.commit()

new_stock = Stocks(1,2,5)
db.session.add(new_stock)
db.session.commit()

new_stock = Stocks(1,3,6)
db.session.add(new_stock)
db.session.commit()

new_stock = Stocks(1,4,23)
db.session.add(new_stock)
db.session.commit()

new_stock = Stocks(1,5,22)
db.session.add(new_stock)
db.session.commit()

new_stock = Stocks(1,6,0)
db.session.add(new_stock)
db.session.commit()

new_stock = Stocks(1,7,8)
db.session.add(new_stock)
db.session.commit()


# Staffs
new_staff = Staffs(1,'Fabiola','Jackson','fabiola.jackson@bikes.shop','(831) 555-5554',1,1,NULL)
db.session.add(new_staff)
db.session.commit()

new_staff = Staffs(2,'Mireya','Copeland','mireya.copeland@bikes.shop','(831) 555-5555',1,1,1)
db.session.add(new_staff)
db.session.commit()

new_staff = Staffs(3,'Genna','Serrano','genna.serrano@bikes.shop','(831) 555-5556',1,1,2)
db.session.add(new_staff)
db.session.commit()

new_staff = Staffs(4,'Virgie','Wiggins','virgie.wiggins@bikes.shop','(831) 555-5557',1,1,2)
db.session.add(new_staff)
db.session.commit()

new_staff = Staffs(5,'Jannette','David','jannette.david@bikes.shop','(516) 379-4444',1,2,1)
db.session.add(new_staff)
db.session.commit()

new_staff = Staffs(6,'Marcelene','Boyer','marcelene.boyer@bikes.shop','(516) 379-4445',1,2,5)
db.session.add(new_staff)
db.session.commit()

new_staff = Staffs(7,'Venita','Daniel','venita.daniel@bikes.shop','(516) 379-4446',1,2,5)
db.session.add(new_staff)
db.session.commit()


# Orders
new_order = Orders(1,259,4,'20160101','20160103','20160103',1,2)
db.session.add(new_order)
db.session.commit()

new_order = Orders(2,1212,4,'20160101','20160104','20160103',2,6)
db.session.add(new_order)
db.session.commit()

new_order = Orders(3,523,4,'20160102','20160105','20160103',2,7)
db.session.add(new_order)
db.session.commit()

new_order = Orders(4,175,4,'20160103','20160104','20160105',1,3)
db.session.add(new_order)
db.session.commit()

new_order = Orders(5,1324,4,'20160103','20160106','20160106',2,6)
db.session.add(new_order)
db.session.commit()

new_order = Orders(6,94,4,'20160104','20160107','20160105',2,6)
db.session.add(new_order)
db.session.commit()

new_order = Orders(7,324,4,'20160104','20160107','20160105',2,6)
db.session.add(new_order)
db.session.commit()


# Order_items
new_order_item = Order_items(1,1,20,1,599.99,0.2)
db.session.add(new_order_item)
db.session.commit()

new_order_item = Order_items(1,2,8,2,1799.99,0.07)
db.session.add(new_order_item)
db.session.commit()

new_order_item = Order_items(1,3,10,2,1549.00,0.05)
db.session.add(new_order_item)
db.session.commit()

new_order_item = Order_items(1,4,16,2,599.99,0.05)
db.session.add(new_order_item)
db.session.commit()

new_order_item = Order_items(1,5,4,1,2899.99,0.2)
db.session.add(new_order_item)
db.session.commit()

new_order_item = Order_items(2,1,20,1,599.99,0.07)
db.session.add(new_order_item)
db.session.commit()

new_order_item = Order_items(2,2,16,2,599.99,0.05)
db.session.add(new_order_item)
db.session.commit()

