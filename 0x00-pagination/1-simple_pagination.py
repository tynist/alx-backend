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
        # Page must be an integer greater than 0
        assert isinstance(page, int) and page > 0,
        # Page size must be an integer greater than 0
        assert isinstance(page_size, int) and page_size > 0,

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []  # Return an empty list if start index is out of range
        return dataset[start_index:end_index]

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
        start_index = (page - 1) * page_size

        # Calculate the end index by adding the start index to the page size
        end_index = start_index + page_size

        return start_index, end_index
