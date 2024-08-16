import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("nums, mask", [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353')])
def test_mask_account_card(nums, mask): # type: ignore
    assert mask_account_card(nums) == mask


@pytest.mark.parametrize("date, expected", [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('', ''),
    ('2022-05-30T15:43:16.25613', '30.05.2022'),
    ('2023-11-03T00:00:00', '03.11.2023'),
    ('2024-03-11', '11.03.2024')])
def test_get_date(date, expected): # type: ignore
    assert get_date(date) == expected