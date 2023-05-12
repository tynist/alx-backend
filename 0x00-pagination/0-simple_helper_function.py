#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
    Returns a tuple of start and end indexes based on pagination parameters.

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

    # Return a tuple containing the start and end indexes
    return start_idx, end_idx
