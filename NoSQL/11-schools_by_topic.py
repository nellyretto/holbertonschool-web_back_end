#!/usr/bin/env python3

"""module for bang"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve schools from the given MongoDB collection that
    match the specified topic.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection to query.
        topic (str): The topic to search for.

    Returns:
        pymongo.cursor.Cursor: A cursor object containing
        the matching schools.
    """
    """"""
    return mongo_collection.find({"topics": topic})
