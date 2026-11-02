"""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

jerry=Dog(name="jerry",breed="labrador")
print(jerry.name)
print(jerry.breed)

class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000

class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)
gautam=DataValidator()
gautam.validate_email(email="kharagautam24@gmail.com")
gautam.validate_age(age=25)
print(validator.get_errors())
print(gautam.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']

class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(f"{self.name} says Woof!")
jerry=Dog(name="jerry")
print(jerry.name)
jerry.bark()
"""

# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# Child class - specific animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"

# Create a dog - using positional argument
my_dog = Dog("Buddy")
# Or with named argument
my_dog2 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog.eat())    # Buddy is eating
print(my_dog.sleep())  # Buddy is sleeping

# Dog can also do dog things
print(my_dog.bark())   # Buddy says woof!

class Cat(Animal):
    def meow(self):
        return f"{self.name} says meow!"

my_cat = Cat("Whiskers")
print(my_cat.eat())    # Whiskers is eating
