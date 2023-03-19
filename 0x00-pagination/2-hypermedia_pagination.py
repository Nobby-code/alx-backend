#!/usr/bin/env python3
"""
Replicate code from the previous task.
Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing
the following key-value pairs:
page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.
You can use the math module if necessary.
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

    def get_hyper(self, page, page_size) -> dict:
        """
        Returning a dictionary of details
        """
        payload = {}
        # first lets do the easy stuff
        payload['page'] = page
        payload['data'] = self.get_page(page, page_size)
        payload['page_size'] = len(payload['data'])

        # ok now the prev and next if valid
        fullData = self.dataset()
        fullCount = len(fullData)
        pageCount = int(fullCount / page_size)

        payload['total_pages'] = int(pageCount)
        payload['prev_page'] = None
        payload['next_page'] = None

        if pageCount > 1:
            if page > 1:
                payload['prev_page'] = page - 1
            if page < pageCount:
                payload['next_page'] = page + 1

        return payload
