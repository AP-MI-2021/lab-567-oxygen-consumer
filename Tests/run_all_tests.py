from Tests.test_domain import test_cheltuiala
from Tests.test_crud import test_crud
from Tests.test_functionalitati import test_functionalitati


def run_all_tests():
    test_cheltuiala()
    test_crud()
    test_functionalitati()
