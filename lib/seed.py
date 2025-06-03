from models import Session, User, Item, Order, OrderItems
from datetime import datetime
import random

def seed_database():
   
    session = Session()
    
    try:
       
        session.query(OrderItems).delete(synchronize_session=False)
        session.query(Order).delete(synchronize_session=False)
        session.query(Item).delete(synchronize_session=False)
        session.query(User).delete(synchronize_session=False)
        session.commit()
        
        print("Existing data cleared successfully.")
        
        # Users data
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
            },
            {
                "name": "Bena k",
                "email": "benak@gmail.com",
                "phone": "1122334455"
            },
            {
                "name": "Joy K",
                "email": "joyk@gmail.com",
                "phone": "5566778899"
            }
        ]
        
        users = []
        for user_data in users_data:
            user = User(**user_data)
            users.append(user)
        session.add_all(users)
        
        # Items data
        items_data = [
            {
              "name": "Jack Daniels",
              "price": 1500.0,
              "availability": True,
              "quantity": 100,
              "description": "Tennessee Whiskey",
              "volume_ml": 700  
            },
            {
                "name": "Johnnie Walker Black Label",
                "price": 2000.0,
                "availability": True,
                "quantity": 50,
                "description": "Blended Scotch Whisky",
                "volume_ml": 750  
            },
            {
                "name": "Jameson Irish Whiskey",
                "price": 1800.0,
                "availability": True,
                "quantity": 75,
                "description": "Irish Whiskey",
                "volume_ml": 750  
            },
            {
                "name": "Chivas Regal 12 Year Old",
                "price": 2200.0,
                "availability": True,
                "quantity": 60,
                "description": "Blended Scotch Whisky",
                "volume_ml": 700  
            },
            {
                "name": "Glenfiddich 12 Year Old",
                "price": 2500.0,
                "availability": True,
                "quantity": 40,
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
        
        # Sample orders to check if code is functional
        mercy = session.query(User).filter_by(email="mercy@gmail.com").first()
        jack_daniels = session.query(Item).filter_by(name="Jack Daniels").first()  
            
        order1 = Order(
            date=datetime.utcnow(),
            total=jack_daniels.price * 2,
            user_id=mercy.id,
            status='pending',
            delivery_location='South B, Nairobi',
        )
        
        session.add(order1)
        session.commit()
        
        order_item1 = OrderItems(
            item_id=jack_daniels.id,
            order_id=order1.id,
            quantity=2,
        )
        
        session.add(order_item1)
        session.commit()
            
        anne = session.query(User).filter_by(email="annek@gmail.com").first() 
        jameson = session.query(Item).filter_by(name="Jameson Irish Whiskey").first()
        
        order2 = Order(
            date=datetime.utcnow(),
            total=jameson.price * 1,
            user_id=anne.id,
            status='completed',
            delivery_location='Westlands, Nairobi',
        )
        
        session.add(order2)
        session.commit()
        
        order_item2 = OrderItems(
            item_id=jameson.id,
            order_id=order2.id,
            quantity=1,
        )
        
        session.add(order_item2)
        session.commit()
        
        print("Database seeded successfully.")
        
    except Exception as e:
        session.rollback()
        print(f"Error seeding database: {e}")
        raise
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()