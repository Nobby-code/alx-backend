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


def index_range(page: int, page_size: int) -> tuple:
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
