#!/usr/bin/env python3
"""update with python"""


def update_topics(mongo_collection, name, topics):
    """update the docs in a collection"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}}) 
