
# testing Fibonacci number function
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1)+fib(n-2)

def test_fibonacci():
    assert fib(10) == 55

from plywood_gallery import ChapterManager


def test_chaptermanager():
    ChapterManager.cell_counter = 12
    ChapterManager.reset_counter()
    assert ChapterManager.cell_counter == 0, "Chapter manager did not reset"
