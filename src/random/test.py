from src.random.address_random import AddressRandom
from src.random.age_random import AgeRandom
from src.random.email_random import EmailRandom
from src.random.id_random import IdRandom
from src.random.phone_random import PhoneRandom

random = AddressRandom()
print random.create()

random = AgeRandom()
print random.create()

random = EmailRandom()
print random.create()

random = IdRandom()
print random.create()

random = PhoneRandom()
print random.create()