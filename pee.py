from peewee import *
database = SqliteDatabase('vocabulary.db')  # Create a database instance.


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = database # this model uses the in-memory database we just created


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = database # use the in-memory database


# Let's create the tables now that the models are defined.
Person.create_table()
Pet.create_table()

# Let's store some people to the database, and then we'll give them some pets.
from datetime import date
uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
uncle_bob.save() # bob is now stored in the database


# We can shorten this by calling `Model.create`.
grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)


# Let's retrieve Grandma's record from the database.
grandma = Person.select().where(Person.name == 'Grandma').get()
print grandma.name
