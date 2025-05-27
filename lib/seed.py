from models import Session, User, Item, Order, OrderItems
from datetime import datetime, timedelata
import random


def seed_database():
    session = Session()

    session.query(User).delete()
    session.query(Item).delete()
    session.query(Order).delete()
    session.query(OrderItems).delete()
    
    
    
    users_data = []
    
    users = []
    
    for user_data in users_data:
        user = User(**user_data)
        users.append(user)
    session.add_all(users)
    
    
    items_data = []
    
    items = []
    for item_data in items_data:
        item = Item(**item_data)
        items.append(item)
        session.add_all(items)
        
    session.commit()
    
        
        #sample orders to check if code is functional
        
        
        
    session.commit
    session.close()
    print("Database seeded successfully.")
    
if __name__ == "__main__":
    seed_database()    
        
        

    