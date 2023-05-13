#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List
from typing import Tuple


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
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0

        dataset = self.dataset()
        csv_size = len(dataset())
        start_idx, end_idx = index_range(page, page_size)
        end_idx = min(end_idx, csv_size)
        if start_idx >= len(dataset):
            # Return an empty list if start index is out of range
            return []
        return dataset[start_idx:end_idx]

    def index_range(page, page_size):
        """
        Returns a tuple of start & end indexes based on pagination parameters.
        """
        return ((page - 1) * page_size, page * page_size)
