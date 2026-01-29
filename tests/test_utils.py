from src.utils import is_even, normalize_text


def test_is_even_true():
    assert is_even(4) is True


def test_is_even_false():
    assert is_even(5) is False


def test_normalize_text():
    assert normalize_text("  HeLLo ") == "hello"
