from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuwithusers.db?check_same_thread=False')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the lcd .cast commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


# Foods containing Vitamin D
restaurant1 = Restaurant(user_id=1, name="Vitamin D")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Papaya", description="Controls calcium absorption for healthy bones and teeth, healthy immune system, and nervous system, cancer-protective, hormone-balancing",
                     price="ADI: 1-5mg", course="Spring", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Basil", description="Controls calcium absorption for healthy bones and teeth, healthy immune system, and nervous system, cancer-protective, hormone-balancing",
                     price="ADI: 1-5mg", course="Summer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Sweet Potato", description="Controls calcium absorption for healthy bones and teeth, healthy immune system, and nervous system, cancer-protective, hormone-balancing",
                     price="ADI: 1-5mg", course="Fall", restaurant=restaurant1)

session.add(menuItem3)
session.commit()


#Foods containing Vitamin E
restaurant2 = Restaurant(user_id=1, name="Vitamin E")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Oatmeal", description="Antioxidant, healthy immune system, heart and circulation, lipid balance, sex hormone regulator, fertility, gestation, growth", price="ADI: 30mg", course="Summer", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Pecans", description="Antioxidant, healthy immune system, heart and circulation, lipid balance, sex hormone regulator, fertility, gestation, growth", price="ADI: 30mg", course="Fall", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Carrots", description="Antioxidant, healthy immune system, heart and circulation, lipid balance, sex hormone regulator, fertility, gestation, growth", price="ADI: 30mg", course="Summer", restaurant=restaurant2)

session.add(menuItem3)
session.commit()


#Foods containing Magnesium
restaurant1 = Restaurant(user_id=1, name="Magnesium")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Artichoke", description="Synthesis of proteins, carbohydrates, and lipids, DNA repair, energy production, modulation of muscle activity, homeostasis of calcium, heart and circulation health.", price="ADI: 350mg", course="Winter", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Date", description="Synthesis of proteins, carbohydrates, and lipids, DNA repair, energy production, modulation of muscle activity, homeostasis of calcium, heart and circulation health.", price="ADI: 350mg", course="Fall", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Apricot", description="Synthesis of proteins, carbohydrates, and lipids, DNA repair, energy production, modulation of muscle activity, homeostasis of calcium, heart and circulation health.", price="ADI: 350mg", course="Summer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()


#Foods containing Calcium
restaurant1 = Restaurant(user_id=1, name="Calcium")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Spinach", description="Bone and teeth formation, regulates nerve and muscle function, hormones and blood pressure", price="ADI: 800-1400mg", course="Summer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Almonds", description="Bone and teeth formation, regulates nerve and muscle function, hormones and blood pressure", price="ADI: 800-1400mg", course="Summer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Corn", description="Bone and teeth formation, regulates nerve and muscle function, hormones and blood pressure", price="ADI: 800-1400mg", course="Summer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()


#Foods containing Vitamin A
restaurant1 = Restaurant(user_id=1, name="Vitamin A")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Kale", description="Antioxidant, vision and night vision, growth and reproduction, collagen production, moistness of mucosa", price="ADI: 5,000-9,000IU", course="Fall", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Cherry", description="Antioxidant, vision and night vision, growth and reproduction, collagen production, moistness of mucosa", price="ADI: 5,000-9,000IU", course="Spring", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Chard", description="Antioxidant, vision and night vision, growth and reproduction, collagen production, moistness of mucosa", price="ADI: 5,000-9,000IU", course="Summer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()



#Foods containing Vitamin C
restaurant1 = Restaurant(user_id=1, name="Vitamin C")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Broccoli", description="Antioxidant that helps repair tissues, gums and adrenal glands. Enhances immune system function, improves the body's assimilation of iron.", price="ADI: 75-125mg", course="Fall", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Arugula", description="Antioxidant that helps repair tissues, gums and adrenal glands. Enhances immune system function, improves the body's assimilation of iron.", price="ADI: 75-125mg", course="Spring", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Mango", description="Antioxidant that helps repair tissues, gums and adrenal glands. Enhances immune system function, improves the body's assimilation of iron.", price="ADI: 75-125mg", course="Summer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()


print ("Deficiencies have been added!")
