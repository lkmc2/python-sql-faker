from src.random.address_random import AddressRandom
from age_random import AgeRandom
from email_random import EmailRandom
from id_random import IdRandom
from phone_random import PhoneRandom
from sex_random import SexRandom
from src.random.time_random import TimeRandom

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

random = SexRandom()
print random.create()

random = TimeRandom()
print random.create()

