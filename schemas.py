from typing import List, Optional
from pydantic import BaseModel
from datetime import date


class ProfileBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    date_of_birth: Optional[date]
    gender: Optional[str]
    address: Optional[str]


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    profile_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    balance: Optional[float]
    profile: Optional[Profile]

    class Config:
        orm_mode = True


class FinancialTransactionBase(BaseModel):
    amount: float
    description: Optional[str]
    timestamp: Optional[date]


class FinancialTransactionCreate(FinancialTransactionBase):
    user_id: int
    category_id: int


class FinancialTransaction(FinancialTransactionBase):
    transaction_id: int
    user_id: int
    category_id: int

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    category_name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    category_id: int

    class Config:
        orm_mode = True


class BudgetBase(BaseModel):
    budget_amount: float
    start_date: date
    end_date: date


class BudgetCreate(BudgetBase):
    user_id: int
    category_id: int


class Budget(BudgetBase):
    budget_id: int
    user_id: int
    category_id: int

    class Config:
        orm_mode = True


class FinancialGoalBase(BaseModel):
    goal_description: Optional[str]
    target_amount: float
    start_date: date
    end_date: date


class FinancialGoalCreate(FinancialGoalBase):
    user_id: int


class FinancialGoal(FinancialGoalBase):
    goal_id: int
    user_id: int

    class Config:
        orm_mode = True


class InvestmentBase(BaseModel):
    investment_type: str
    amount: float
    description: Optional[str]
    investment_date: date


class InvestmentCreate(InvestmentBase):
    user_id: int


class Investment(InvestmentBase):
    investment_id: int
    user_id: int

    class Config:
        orm_mode = True
