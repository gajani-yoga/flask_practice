from application import db
from application.countries.models import Country 

db.drop_all()
print('Dropping Database')

db.create_all()
print('Creating Database')

print('Seeding Database')

entry1 = Country(name="France", population=64756584, capital_city="Paris") 

entry2 = Country(name="Netherlands", population=17938053, capital_city="Amsterdam") 

entry3 = Country(name="Germany", population=83273144, capital_city="Berlin")

db.session.add(entry1) # add one entry

db.session.add_all([entry2, entry3]) # add multiple

db.session.commit()