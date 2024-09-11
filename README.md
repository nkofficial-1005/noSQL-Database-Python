# Python NoSQL Database

This project implements a simple NoSQL database in Python, allowing users to store, retrieve, update, delete, and query JSON documents. The database stores data in a JSON file, providing a persistent and lightweight solution.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Inserting Documents](#inserting-documents)
  - [Retrieving Documents](#retrieving-documents)
  - [Updating Documents](#updating-documents)
  - [Deleting Documents](#deleting-documents)
  - [Querying Documents](#querying-documents)
- [Testing](#testing)
- [License](#license)

## Overview

This project demonstrates the creation of a document-based NoSQL database, where each record is stored as a JSON object. The database is file-based, and data is persisted in a JSON file. This project is suitable for learning purposes or small-scale applications where simplicity and flexibility are essential.

The core functionality includes:
- Insert documents (JSON format)
- Retrieve documents by ID
- Update documents by ID
- Delete documents by ID
- Query documents using a custom condition

## Features

- **Flexible Data Storage**: Store documents in JSON format with no predefined schema.
- **Unique IDs**: Each document is assigned a unique identifier.
- **Basic Querying**: Query documents using lambda functions to specify conditions.
- **Persistence**: Data is stored in a file, ensuring it is available across program executions.
- **Basic CRUD Operations**: Support for Create, Read, Update, Delete operations.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/nosql-database.git
    cd nosql-database
    ```

2. Ensure Python 3 is installed:
    ```bash
    python --version
    ```

3. Install any necessary dependencies:
    (No external dependencies are required beyond the standard library.)

## Usage

### Inserting Documents

To insert a new document, use the `insert` method. It will return the unique ID of the inserted document:

```python
from database import JSONNoSQLDatabase

db = JSONNoSQLDatabase()
doc_id = db.insert({"name": "Alice", "age": 30})
print(f"Document ID: {doc_id}")
```

### Retrieving Documents

Retrieve a document by its unique ID:

```python
document = db.get(doc_id)
print(document)  # Output: {"name": "Alice", "age": 30}
```

### Updating Documents

Update an existing document using its ID:

```python
db.update(doc_id, {"name": "Alice", "age": 32})
print(db.get(doc_id))  # Output: {"name": "Alice", "age": 32}
```

### Deleting Documents

Delete a document using its ID:

```python
db.delete(doc_id)
print(db.get(doc_id))  # Output: None
```

### Querying Documents

Query documents using conditions (such as lambda function):

```python
results = db.query(lambda doc: doc["age"] > 25)
print(results)  # Output: Documents where age > 25
```

## Testing

You can run the test script to verify that the database works as expected. The `test_database.py` script includes unit tests for the basic operations.

To run the tests:
```python
python test_database.py
```

You should see All tests passed. if everything works correctly.

## License

This project is licensed under the MIT License.
