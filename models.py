from sqlalchemy import Column, Integer, String, Text, Date, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)  # Hashed
    email = Column(String(100), unique=True, nullable=False)
    profile_id = Column(Integer, ForeignKey('profile.profile_id'), unique=True)
    balance = Column(DECIMAL(12, 2))

    profile = relationship("Profile", back_populates="user")
    transactions = relationship("FinancialTransaction", back_populates="user")
    budgets = relationship("Budget", back_populates="user")
    goals = relationship("FinancialGoal", back_populates="user")
    investments = relationship("Investment", back_populates="user")


class Profile(Base):
    __tablename__ = 'profile'

    profile_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    date_of_birth = Column(Date)
    gender = Column(String(10))
    address = Column(Text)

    user = relationship("User", uselist=False, back_populates="profile")


class FinancialTransaction(Base):
    __tablename__ = 'financial_transaction'

    transaction_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    amount = Column(DECIMAL(12, 2))
    description = Column(Text)
    timestamp = Column(Date)
    category_id = Column(Integer, ForeignKey('category.category_id'))

    user = relationship("User", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(50), unique=True)

    transactions = relationship("FinancialTransaction", back_populates="category")
    budgets = relationship("Budget", back_populates="category")


class Budget(Base):
    __tablename__ = 'budget'

    budget_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    category_id = Column(Integer, ForeignKey('category.category_id'))
    budget_amount = Column(DECIMAL(12, 2))
    start_date = Column(Date)
    end_date = Column(Date)

    user = relationship("User", back_populates="budgets")
    category = relationship("Category", back_populates="budgets")


class FinancialGoal(Base):
    __tablename__ = 'financial_goal'

    goal_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    goal_description = Column(Text)
    target_amount = Column(DECIMAL(12, 2))
    start_date = Column(Date)
    end_date = Column(Date)

    user = relationship("User", back_populates="goals")


class Investment(Base):
    __tablename__ = 'investment'

    investment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    investment_type = Column(String(50))
    amount = Column(DECIMAL(12, 2))
    description = Column(Text)
    investment_date = Column(Date)

    user = relationship("User", back_populates="investments")
