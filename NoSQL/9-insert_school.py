#!/usr/bin/env python3
"""insert a docu"""

import sys

def insert_school(mongo_collection, **kwargs):
    """insert a doc in a collection"""
    result = mongo_collection.insert_one(kwargs)

    new_id = result.inserted_id

    return new_id

