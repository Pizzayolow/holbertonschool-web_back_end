#!/usr/bin/env python3
"""simple helper function"""
from typing import Tuple
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''return a tuple with start and end size'''
    end_index = page * page_size
    start_index = end_index - page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the right data in a list"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """return a dictionnary with all data"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        data_set_page = self.get_page(page, page_size)
        start_index, end_index = index_range(page, page_size)
        if page - 1 > 0:
            previous_page = page - 1
        else:
            previous_page = None
        if end_index >= len(dataset):
            next_page = None
        else:
            next_page = page + 1

        total_page = math.ceil(len(dataset) / page_size)

        new_dict = {
            "page_size": page_size,
            "page": page,
            "data": data_set_page,
            "next_page": next_page,
            "prev_page": previous_page,
            "total_pages": total_page
        }
        return (new_dict)
