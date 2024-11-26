import redis
import uuid
from typing import Union


class Cache:
    def __init__(self, host='localhost', port=6379, db=0):
        """
        Initialize the Cache class.

        Parameters:
        - host: Redis server hostname (default is 'localhost').
        - port: Redis server port (default is 6379).
        - db: Redis database number (default is 0).
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()  # Flush the database during initialization
        
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the cache with a randomly generated key.

        Parameters:
        - data: The data to store. Can be str, bytes, int, or float.

        Returns:
        - str: The key under which the data is stored.
        """
        # Generate a random key
        key = str(uuid.uuid4())

        # Store the data in Redis
        self._redis.set(key, data)

        return key