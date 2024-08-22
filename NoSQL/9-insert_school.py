#!/usr/bin/env python3
"""import pymongo"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection to insert the document into.
        **kwargs: The key-value pairs representing the fields and values
        of the document to be inserted.

    Returns:
        ObjectId: The ObjectId of the newly inserted document.
    """

    new_doc = mongo_collection.insert(kwargs)

    return new_doc
