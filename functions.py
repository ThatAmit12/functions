def display_message():
    print("I am learning about functions in this chapter.")

display_message()

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")

def make_shirt(size, message):
    print(f"Shirt size: {size}, Message: '{message}'")

make_shirt("M", "Keep coding")
make_shirt(message="Hello World", size="L")

def make_shirt(size="L", message="I love Python"):
    print(f"Shirt size: {size}, Message: '{message}'")

make_shirt()

make_shirt("M")

make_shirt("S", "Code is life")

def describe_city(city, country="Bangladesh"):
    print(f"{city} is in {country}.")

describe_city("ctg")
describe_city("rajshahi")
describe_city("Dhaka", "BD")
