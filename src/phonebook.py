from peewee import CharField, Model, SqliteDatabase

db = SqliteDatabase('database.db')


class Contact(Model):
    name = CharField(unique=True)
    contact = CharField(max_length=16)
    email = CharField()

    class Meta:
        database = db

    def search_by_name(self):
        query = self


db.connect()
db.create_tables([Contact])
