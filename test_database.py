from database import JSONNoSQLDatabase

def test_database():
    db = JSONNoSQLDatabase()

    #Test Insertion
    doc_id =  db.insert({"name": "Alice", "age": 30})
    assert db.get(doc_id) == {"name": "Alice", "age": 30}

    #Test update
    db.update(doc_id, document={"name": "Alice", "age": 32})
    assert db.get(doc_id) == {"name": "Alice", "age": 32}

    #Test deletion
    db.delete(doc_id)
    assert db.get(doc_id) is None

    #Test query
    doc_id1 = db.insert({"name": "Alice", "age": 30})
    doc_id2 = db.insert({"name": "Bob", "age": 24})
    results = db.query(lambda doc:doc["age"]>25)
    assert doc_id1 in results
    assert doc_id2 not in results

    print("All tests passed.")

if __name__ == "__main__":
    test_database()