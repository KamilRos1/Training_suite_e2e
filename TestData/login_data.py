from collections import namedtuple
User = namedtuple('User', ['username', 'password'])
correct_user = User('kamil.roslan@globallogic.com', 'Solarium456.')
incorrect_user = User('fake.fake@globallogic.com', 'wrongPassword')
