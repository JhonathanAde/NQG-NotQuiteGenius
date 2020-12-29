from dotenv import load_dotenv
load_dotenv()

from app.models import Employee, Menu, MenuItem, MenuItemType, Table
from app import app, db

with app.app_context():
    db.drop_all()
    db.create_all()

    # employee = Employee(name="Margot", employee_number=1234,
    #                     password="password")
    # db.session.add(employee)
    # db.session.commit()

    # beverages = MenuItemType(name="Beverages")
    # db.session.add(beverages)
    # db.session.commit()

    # entrees = MenuItemType(name="Entrees")
    # db.session.add(entrees)
    # db.session.commit()

    # sides = MenuItemType(name="Sides")
    # db.session.add(sides)
    # db.session.commit()

    # dinner = Menu(name="Dinner")
    # db.session.add(dinner)
    # db.session.commit()

    # fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    # db.session.add(fries)
    # db.session.commit()

    # drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    # db.session.add(drp)
    # db.session.commit()

    # jambalaya = MenuItem(name="Jambalaya", price=21.98,
    #                      type=entrees, menu=dinner)
    # db.session.add(jambalaya)
    # db.session.commit()

    # t1 = Table(number=1, capacity=4)
    # db.session.add(t1)
    # db.session.commit()

    # t2 = Table(number=2, capacity=4)
    # db.session.add(t2)
    # db.session.commit()

    # t3 = Table(number=3, capacity=4)
    # db.session.add(t3)
    # db.session.commit()

    # t4 = Table(number=4, capacity=4)
    # db.session.add(t4)
    # db.session.commit()

    # t5 = Table(number=5, capacity=4)
    # db.session.add(t5)
    # db.session.commit()

    # t6 = Table(number=6, capacity=4)
    # db.session.add(t6)
    # db.session.commit()

    # t7 = Table(number=7, capacity=4)
    # db.session.add(t7)
    # db.session.commit()

    # t8 = Table(number=8, capacity=4)
    # db.session.add(t8)
    # db.session.commit()

    # t9 = Table(number=9, capacity=4)
    # db.session.add(t9)
    # db.session.commit()

    # t10 = Table(number=10, capacity=4)
    # db.session.add(t10)
    # db.session.commit()
