from models import Session, User, Item, Order, OrderItems
from datetime import datetime, timedelata
import random


def seed_database():
    session = Session()

    session.query(User).delete()
    session.query(Item).delete()
    session.query(Order).delete()
    session.query(Order_Items).delete()

    