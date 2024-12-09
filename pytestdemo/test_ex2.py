import pytest

@pytest.fixture
def fixtureMethod():
    print("This is a Fixture Method")

def test_LoginApplication(fixtureMethod):
    print("Login successful")

def test_SearchingofProducst(fixtureMethod):
    print("Search for Laptops")

def test_AddItemToCart(fixtureMethod):
    print("Add Laptop to the Cart")

def test_CheckingAddItemInCart(fixtureMethod):
    print("Successfully checked Items in Cart")

def test_PaymentDetails():
    print("Successfully checked payment details ")

def test_DeliveryStatus(fixtureMethod):
    print("Verified Delivery status")

def test_RemoveItemFromCart(fixtureMethod):
    print("Removed items from cart")

def test_LogoutCart():
    print("Logout successfully")