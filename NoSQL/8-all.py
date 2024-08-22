#!/usr/bin/env python3
"""import pymongo"""
import pymongo


def list_all(mongo_collection):
    """_summary_

    Args:
        mongo_collection (_type_): _description_

    Returns:
        _type_: _description_
    """
    return list(mongo_collection.find())
