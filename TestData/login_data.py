from collections import namedtuple

User = namedtuple('User', ['username', 'password'])
correct_user = User('kamil.roslan@globallogic.com', 'Solarium456.')
incorrect_user = User('fake.fake@globallogic.com', 'wrongPassword')
before_login_url = 'https://training-suite.ppro.dev/login/'
after_login_url = 'https://training-suite.ppro.dev/'
