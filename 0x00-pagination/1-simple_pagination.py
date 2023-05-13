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
        assert page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        dataset = len(self.dataset())
        if start_idx >= dataset:
            # Return an empty list if start index is out of range
            return []
        return dataset[start_idx:end_idx]

    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        Returns a tuple of start & end indexes based on pagination parameters.

        Args:
            page (int): The page number (1-indexed)
            page_size (int): The size of each page

        Returns:
            tuple: A tuple containing the start and end indexes.
        """
        # Calculate the start index based on the page number and page size
        start_idx = (page - 1) * page_size

        # Calculate the end index by adding the start index to the page size
        end_idx = start_idx + page_size

        return start_idx, end_idx
