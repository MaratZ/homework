import pytest
from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize("number, expected", [
    ('7000792289606361', '7000 79** **** 6361'),
    ('700079228960636', ''),
    ('a00079228960636', ''),
    ('70007922896063612', '')])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected

@pytest.mark.parametrize("account, expected_acc", [
    ('73654108430135874305', '**4305'),
    ('700079228960636', ''),
    ('7365410843013587430a', ''),
    ('736541084301358743051', '')])
def test_get_mask_account(account, expected_acc):
    assert get_mask_account(account) == expected_acc


def test_mask_account_empty():
    assert get_mask_card_number('') == ''
