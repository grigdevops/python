import yaml
from yaml.loader import UnsafeLoader

class Person:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __repr__(self):
        return "%s(user = %r, password = %r)" % (self.__class__.__name__, self.user, self.password)

person = Person('Jessa', 'queuse123!')
yaml_obj = yaml.dump(person)


new_person = yaml.load(yaml_obj, Loader=UnsafeLoader)
print(new_person.user, new_person.password)