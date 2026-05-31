import pytest
from app.logic import is_eligible_for_loan


def test_eligible_user():

    assert is_eligible_for_loan(60000, 25, "Employed") == True


def test_undrage_user():
    assert is_eligible_for_loan(60000, 14, "Employed") == False


def test_low_income():

    assert is_eligible_for_loan(30000, 25, "Employed") == False


def test_unemployed_user():

    assert is_eligible_for_loan(30000, 25, "unEmployed") == False


def test_boundary():

    assert is_eligible_for_loan(50000, 21, "Employed") == True


def boundary_bb():

    assert is_eligible_for_loan(50000, 21, "Employed") == True
