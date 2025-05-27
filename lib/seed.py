from models import Session, User, Item, Order, OrderItems
from datetime import datetime
import random


def seed_database():
    session = Session()

    session.query(User).delete()
    session.query(Item).delete()
    session.query(Order).delete()
    session.query(OrderItems).delete()
    
    
    
    users_data = [
        {
           "name": "Mercy K",
           "email": "mercy@gmail.com",
           "phone": "1234567890" 
        },
        
        {
            "name": "Anne K",
            "email": "annek@gmail.com",
            "phone": "0987654321"
        }
    ]
    
    users = []
    
    for user_data in users_data:
        user = User(**user_data)
        users.append(user)
    session.add_all(users)
    
    
    items_data = [
        {
          "name": "Jack Daniels",
          "price": 1500.0,
          "availabilty": True,
          "description": "Tennessee Whiskey",
          "volume_ml": 700  
        },
        {
            "name": "Johnnie Walker Black Label",
            "price": 2000.0,
            "availabilty": True,
            "description": "Blended Scotch Whisky",
            "volume_ml": 750  
            },
            {
            "name": "Jameson Irish Whiskey",
            "price": 1800.0,
            "availabilty": True,
            "description": "Irish Whiskey",
            "volume_ml": 750  
            },
            {
            "name": "Chivas Regal 12 Year Old",
            "price": 2200.0,
            "availabilty": True,
            "description": "Blended Scotch Whisky",
            "volume_ml": 700  
            },
            {
            "name": "Glenfiddich 12 Year Old",
            "price": 2500.0,
            "availabilty": True,
            "description": "Single Malt Scotch Whisky",
            "volume_ml": 750
        }
    ]
    
    items = []
    for item_data in items_data:
        item = Item(**item_data)
        items.append(item)
    session.add_all(items)
        
    session.commit()
    
        
        #sample orders to check if code is functional
    #mercy = session.query(User).filter_by(name="Mercy K").first()
    mercy = session.query(User).filter_by(email="mercy@gmail.com").first()
    jack_daniels = session.query(Item).filter_by(name="Jack Daniels").first()  
        
    order = Order(
        date=datetime.utcnow(),
        total=jack_daniels.price * 2,
        user_id=mercy.id,
        status='pending',
        delivery_location='South B, Nairobi',
    )
    
    session.add(order)
    session.commit()
    
    order_item = OrderItems(
        item_id=jack_daniels.id,
        order_id=order.id,
        quantity=2,
        #price=jack_daniels.price
    )
    
    session.add(order_item)
    session.commit()
        
    session.commit
    session.close()
    print("Database seeded successfully.")
    
if __name__ == "__main__":
    seed_database()    
        
        

    