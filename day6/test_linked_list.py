# coding=utf-8

import pytest

def test_empty_list():
    from linked_list import LinkedList
    LinkedList()
    assert LinkedList().length == 0


#
#
# TEST_POPNODE = {
#     (, )
# }
#
# @pytest.mark.parametrize("fn, result", TEST_NEWNODE)
# def test_pop(fn, result):