from database import JSONNoSQLDatabase

db = JSONNoSQLDatabase()

#Insert some documents
doc1_id = db.insert({"name": "Alice", "age": 30})
doc2_id = db.insert({"name": "Bob", "age": 24})

#Retrieve a document
print(db.get(doc1_id)) # Output will be in Json format

#Update a document
db.update(doc1_id, document ={"name": "Alice", "age": 32 })

#Query documents
results = db.query(lambda doc:doc["age"]>25)
print(results)