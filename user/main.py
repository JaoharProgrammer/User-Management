from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base

# Import Models
from models.User import User
from models.Car import Car
from models.Pet import Pet
from models.Phone import Phone

# Import Schemas
from schemas.UserCreate import UserCreate, UserResponse
from schemas.CarInfo import Carinfo, CarResponse
from schemas.PetInfo import PetInfo, PetResponse
from schemas.PhoneInfo import PhoneInfo, PhoneResponse

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# ============================================
# USER ROUTES
# ============================================

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    """Get all users"""
    return db.query(User).all()

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get user by ID"""
    return db.query(User).filter(User.id == user_id).first()

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    """Update user by ID"""
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.name = user.name
    db_user.email = user.email
    db_user.age = user.age
    db_user.color = user.color
    db_user.weight = user.weight
    db_user.height = user.height
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete user by ID"""
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}

# ============================================
# CAR ROUTES
# ============================================

@app.post("/cars/", response_model=CarResponse)
def create_car(car: Carinfo, db: Session = Depends(get_db)):
    """Create a new car"""
    db_car = Car(brand=car.brand, model=car.model, color=car.color, year=car.year)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@app.get("/cars/", response_model=list[CarResponse])
def get_cars(db: Session = Depends(get_db)):
    """Get all cars"""
    return db.query(Car).all()

@app.get("/cars/{car_id}", response_model=CarResponse)
def get_car(car_id: int, db: Session = Depends(get_db)):
    """Get car by ID"""
    return db.query(Car).filter(Car.id == car_id).first()

@app.put("/cars/{car_id}", response_model=CarResponse)
def update_car(car_id: int, car: Carinfo, db: Session = Depends(get_db)):
    """Update car by ID"""
    db_car = db.query(Car).filter(Car.id == car_id).first()
    db_car.brand = car.brand
    db_car.model = car.model
    db_car.color = car.color
    db_car.year = car.year
    db.commit()
    db.refresh(db_car)
    return db_car

@app.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    """Delete car by ID"""
    db_car = db.query(Car).filter(Car.id == car_id).first()
    db.delete(db_car)
    db.commit()
    return {"message": "Car deleted successfully"}

# ============================================
# PET ROUTES
# ============================================

@app.post("/pets/", response_model=PetResponse)
def create_pet(pet: PetInfo, db: Session = Depends(get_db)):
    """Create a new pet"""
    db_pet = Pet(name=pet.name, age=pet.age, color=pet.color)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

@app.get("/pets/", response_model=list[PetResponse])
def get_pets(db: Session = Depends(get_db)):
    """Get all pets"""
    return db.query(Pet).all()

@app.put("/pets/{pet_id}", response_model=PetResponse)
def update_pet(pet_id: int, pet: PetInfo, db: Session = Depends(get_db)):
    """Update pet by ID"""
    db_pet = db.query(Pet).filter(Pet.id == pet_id).first()
    db_pet.name = pet.name
    db_pet.age = pet.age
    db_pet.color = pet.color
    db.commit()
    db.refresh(db_pet)
    return db_pet

@app.delete("/pets/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    """Delete pet by ID"""
    db_pet = db.query(Pet).filter(Pet.id == pet_id).first()
    db.delete(db_pet)
    db.commit()
    return {"message": "Pet deleted successfully"}

# ============================================
# PHONE ROUTES
# ============================================

@app.post("/phones/", response_model=PhoneResponse)
def create_phone(phone: PhoneInfo, db: Session = Depends(get_db)):
    """Create a new phone"""
    db_phone = Phone(
        name=phone.name,
        color=phone.color,
        made_in=phone.made_in,
        warranty=phone.warranty
    )
    db.add(db_phone)
    db.commit()
    db.refresh(db_phone)
    return db_phone

@app.get("/phones/{phone_id}", response_model=PhoneResponse)
def get_phone(phone_id: int, db: Session = Depends(get_db)):
    """Get phone by ID"""
    return db.query(Phone).filter(Phone.id == phone_id).first()

@app.get("/phones/", response_model=list[PhoneResponse])
def get_phones(db: Session = Depends(get_db)):
    """Get all phones"""
    return db.query(Phone).all()

@app.put("/phones/{phone_id}", response_model=PhoneResponse)
def update_phone(phone_id: int, phone: PhoneInfo, db: Session = Depends(get_db)):
    """Update phone by ID"""
    db_phone = db.query(Phone).filter(Phone.id == phone_id).first()
    db_phone.name = phone.name
    db_phone.color = phone.color
    db_phone.made_in = phone.made_in
    db_phone.warranty = phone.warranty
    db.commit()
    db.refresh(db_phone)
    return db_phone

@app.delete("/phones/{phone_id}")
def delete_phone(phone_id: int, db: Session = Depends(get_db)):
    """Delete phone by ID"""
    db_phone = db.query(Phone).filter(Phone.id == phone_id).first()
    db.delete(db_phone)
    db.commit()
    return {"message": "Phone deleted successfully"}