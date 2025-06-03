from models import Session, User, Item, Order, OrderItems
from sqlalchemy import func
from datetime import datetime
import re


current_user = None
cart = []


def display_welcome():
    print("\n" + "=" * 50)
    print("Welcome to The Liquor Vault!")
    print("="*50)
    print("Explore the finest collection of wines,sprits, and liquors delivered directly to you.")
    print("=" * 50 + "\n")
    
    
def display_collection():
    print("\n" + "=" * 50)
    print("Our Collection:")
    print("1. Login")
    print("2. Browse through our collection")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")
    return input("Please select an option (1-5): ")


def login():
    global current_user
    session = Session()
    
    print("User Authentication")
    print("1. Login")
    print("2. Register New User")
    choice = input("Please select an option (1-2): ")
    
    if choice == '1':
        email = input("Enter your email: ")
        user = session.query(User).filter_by(email=email).first()
        if user:
            current_user = user
            print(f"Welcome back, {user.name}!")
        else:
            print("User not found. Please register first.")
            
    elif choice == '2':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format.")
            session.close()
            return
        
        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            print("Email already registered. Please login.")
            session.close()
            return
        
        new_user = User(name=name, email=email, phone=phone)
        session.add(new_user)
        session.commit()
        current_user = new_user
        print(f"Registration successful! Welcome, {new_user.name}!")
        
    session.close()
    
    
def browse_collection():
    session = Session()
    items = session.query(Item).all()
    
    print("\n" + "=" * 50)
    print("Our Liquor Collection:")
    print("=" * 50)
    print(f"{'ID':<5} {'Name':<30} {'Price':<10} {'Availabilty':<10}")
    print("=" * 50)
    
    for item in items:
        availability = "Available" if item.availability > 0 else "Out of Stock"
        print(f"{item.id:<5} {item.name:<30} Ksh{item.price:<10} {availability}")
    print("=" * 50)
    
    if current_user:
        add_choice = input("Would you like to add an item to your cart? (y/n): ").strip().lower()
        if add_choice == 'y':
            add_to_cart(session)
        else:
            print("Please continue browsing or checkout.")
                
    session.close()
    
def add_to_cart(session):
    global cart
    
    try:
        item_id = int(input("Enter the ID of the item you want to add to your cart: "))
        item = session.query(Item).filter_by(id=item_id).first()
        
        if not item:
            print("Item not found. Please try again.")
            return
        if not item.availability:
            print("Item out of stock!")
            return
        
        quantity = int(input(f"Enter the quantity of {item.name}"))
        if quantity <= 0:
            print("Invalid quantity. Please try again.")
            return
        
        cart.append({
            'item_id': item.id,
            'name': item.name,
            'price': item.price,
            'quantity': quantity
        })
        print(f"{item.name} has been added to your cart.")
        
    except ValueError:
        print("Invalid input. Please enter a valid item ID and quantity.")
        
def view_cart():
    global cart
    
    if not cart:
        print("Your cart is empty.")
        return
    
    print("\n Shopping Cart:")
    print("=" * 50)
    print(f"{'ID':<5} {'Name':<30} {'Price':<10} {'Quantity':<10} {'Total':<10}")
    print("=" * 50)
    
    total = 0
    for item in cart:
        item_total = item['price'] * item['quantity']
        total += item_total
        print(f"{item['item_id']:<5} {item['name']:<30} ${item['price']:<10} {item['quantity']:<10} ${item_total:<10}")
        
    print("=" * 50)
    print(f"Total Amount: ${total}")
    print("=" * 50)
    
    
    print("Cart Options:")
    print("1. Remove an item from the cart")
    print("2. Update item quantity")
    print("3. Clear cart")
    print("4. Proceed to checkout")
    
    choice = input("Please select an option (1-4): ")
    
    if choice == '1':
        remove_from_cart()
    elif choice == '2':
        update_item_quantity()
    elif choice == '3':
        cart.clear()
        print("Your cart has been cleared.")
       
def remove_from_cart():
    global cart
    
    if not cart:
        return
    
    print("\nItems in cart:")
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['name']} (Qty: {item['qty']})")
    
    try:
        choice = int(input("Enter item number to remove: ")) - 1
        if 0 <= choice < len(cart):
            removed_item = cart.pop(choice)
            print(f"Removed {removed_item['name']} from cart!")
        else:
            print("Invalid selection!")
    except ValueError:
        print("Please enter a valid number!")    
        
def update_item_quantity():
    global cart
    
    if not cart:
        return
    
    print("\nItems in cart:")
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['name']} (Current qty: {item['qty']})")
    
    try:
        choice = int(input("Enter item number to update: ")) - 1
        if 0 <= choice < len(cart):
            new_qty = int(input("Enter new quantity: "))
            if new_qty > 0:
                cart[choice]['qty'] = new_qty
                print(f"Updated quantity for {cart[choice]['name']}!")
            else:
                print("Quantity must be positive!")
        else:
            print("Invalid selection!")
    except ValueError:
        print("Please enter valid numbers!")      
        
        
def place_order():
    global cart, current_user
    
    if not current_user:
        print("Please login to place an order.")
        return
    
    if not cart:
        print("Your cart is empty. Please add items to your cart before placing an order.")
        return
    
    session = Session()
    
    total_amount = sum(item['price'] * item['quantity'] for item in cart)
    
    order = Order(
        date=datetime.utcnow(),
        total=total_amount,
        user_id=current_user.id,
        status='pending',
        delivery_location=input("Enter delivery location: ")
    )
    
    session.add(order)
    session.commit()
    
    for item in cart:
        order_item = OrderItems(
            item_id=item['item_id'],
            order_id=order.id,
            quantity=item['quantity']
        )
        session.add(order_item)
        
    session.commit()
    
    print(f"Order placed successfully! Your order ID is {order.id}.")
    
    cart.clear()  # Clear the cart after placing the order
    session.close()
    
def checkout():
    print("\n" + "=" * 50)
    print("Checkout")
    print("=" * 50)
    print("Thank you for shopping with us!")
    print("Drink Responsibly!")
    print("=" * 50 + "\n")
    
    
    ##CHECKING FUNCTINALITY:
    
if __name__ == "__main__":
    display_welcome()
    
    while True:
        choice = display_collection()
        
        if choice == "1":
            login()
        elif choice == "2":
            browse_collection()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            place_order()
        elif choice == "5":
            checkout()
            break
        else:
            print(" Invalid option! Please select 1-5.")     
                           
                
    
     
    
       