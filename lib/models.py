from sqlalchemy import create_engine,Column, Integer, String, DateTime, Float, Boolean, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    #pass
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    
    orders = relationship("Orders", back_populates="user")
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"





class Order(Base):
    #pass
    
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=datetime.utcnow)
    total = Column(Numeric, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(String, default='pending')
    delivery_location = Column(String, nullable=False)
    
    user = relationship("User", back_populates="orders")
    order_items = relationship("Order_Items", back_populates="order")
    
    def __repr__(self):
        return f"<Order(id={self.id}, date={self.date}, total={self.total}, user_id={self.user_id}, status='{self.status}')>"






class Item(Base):
    #pass
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    availabilty = Column(Boolean, default=True)
    description = Column(String)
    volume_ml = Column(Integer)
    
    order_items = relationship("Order_Items", back_populates="item")
    
    def __repr__(self):
        return f"<Item(id={self.id}, name='{self.name}', price={self.price}, available={self.availabilty})>"





class OrderItems(Base):
    #pass
    
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    
    item = relationship("Item", back_populates="order_items")
    order = relationship("Order", back_populates="order_items")
    
    def __repr__(self):
        return f"<OrderItems(id={self.id}, item_id={self.item_id}, order_id={self.order_id}, quantity={self.quantity})>"
    
    
    
    
    
    
    

engine = create_engine('sqlite:///liquor_vault.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
