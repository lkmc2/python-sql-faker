from src.random_data.address_random import AddressRandom
from random_data.age_random import AgeRandom
from random_data.email_random import EmailRandom
from random_data.id_random import IdRandom
from random_data.phone_random import PhoneRandom
from random_data.sex_random import SexRandom
from random_data.time_random import TimeRandom
from random_data.username_random import UserNameRandom

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

random = UserNameRandom()
print random.create()

print hasattr(random, 'create')

print type('123') == str