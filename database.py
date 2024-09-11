#This NoSQL database implemnentation allows to store, retrieve, update, and delete JSON documents using unique  ID.

import json #working with JSON data
import os #file operations
import uuid #generating unique ids

#Class to handle database operations
class JSONNoSQLDatabase:
    # A simple NoSQL database using JSON files
    def __init__(self, filename='database.json'):
        # Initialize the database with a filename
        self.filename = filename
        # Load the database from the file
        if os.path.exists(self.filename):
            # If the file exists, load the database
            with open(self.filename, 'r') as file:
                self.store = json.load(file)
        else:
            # If the file does not exist, create an empty database
            self.store = {}

    # Save the database to the file
    def save(self):
        # Save the database to the file, overwriting the existing content with the updated content
        with open(self.filename, 'w') as file:
            json.dump(self.store, file, indent=4)

    # Insert a document into the database
    def insert(self, document):
        # Generate a unique document ID, insert the document into the database, and save the database
        doc_id = str(uuid.uuid4())
        self.store[doc_id] = document
        self.save()

        return doc_id

    # Update a document in the database
    def update(self, doc_id, document):
        # Check if the document ID exists, update the document, and save the database, or raise a KeyError 
        # if document ID doesn't exist
        if doc_id not in self.store:
            raise KeyError("Document ID does not exist.")
        self.store[doc_id] = document
        self.save()

    # Get a document from the database
    def get(self, doc_id):
        # Get the document with the specified document ID, or return None if the document ID does not exist
        return self.store.get(doc_id, None)

    # Delete a document from the database
    def delete(self, doc_id):
        # Check if the document ID exists, delete the document, and save the database, or raise a KeyError
        if doc_id in self.store:
            del self.store[doc_id]
            self.save()
        else:
            raise KeyError("Document ID does not exist.")
        
    #Query the database with a condition function
    def query(self, condition):
        results={}
        for doc_id, document in self.store.items():
            if condition(document):
                results[doc_id] = document
        return results
