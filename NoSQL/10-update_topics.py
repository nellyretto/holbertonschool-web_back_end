#!/usr/bin/env python3

"""import pymongo"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update the topics field for documents in the given mongo_collection
    that match the specified name.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection to update.
        name (str): The name to match documents against.
        topics (list): The new list of topics to set for matching documents.

    Returns:
        None
    """
    mongo_collection.update_many(
        {name: "name"},
        {"$set": {"topics": topics}},
    )
