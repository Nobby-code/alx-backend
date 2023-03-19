#!/usr/bin/env python3
"""
    Write a function named index_range that
    takes two integer arguments page and
    page_size.
    The function should return a tuple of size
    two containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters.
    Page numbers are 1-indexed, i.e. the first page
    is page 1.
"""
import csv
import math
from typing import List


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
        """
        check that page and page_size are valid
        and then return the proper data in a list
        """
        # make an empty list and gather all baby names
        results = []
        fullData = self.dataset()
        # check vars are valid
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # get our range from page and page size
        location = self.index_range(page, page_size)

        # If range is greater than data length, out of range
        if len(fullData) < location[1]:
            return results

        # append the rsults and return
        for i in range(location[0], location[1]):
            results.append(fullData[i])
        return results

    def index_range(self, page, page_size) -> tuple:
        """
        Getting the starting and ending position for
        pagination.
        """
        if page == 1:
            start = 0
            end = page_size
        elif page < 1 or page_size < 1:
            exit(1)
        else:
            start = ((page - 1) * page_size)
            end = (start + page_size)
        payload = (start, end)
        return payload
