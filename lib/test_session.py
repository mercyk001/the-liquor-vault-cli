from models import Session, User, Item, Order, OrderItems

def test_session():
    session = Session()
    
    try:
        
        user_count = session.query(User).count()
        print(f"Current users in database: {user_count}")
        
        item_count = session.query(Item).count()
        print(f"Current items in database: {item_count}")
        
        print("Session is working correctly!")
        
    except Exception as e:
        print(f"Session error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    test_session()