from src.random.address_random import AddressRandom
from src.random.age_random import AgeRandom
from src.random.email_random import EmailRandom

random = AddressRandom()
print random.create()

random = AgeRandom()
print random.create()

random = EmailRandom()
print random.create()