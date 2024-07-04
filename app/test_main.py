from app.main import is_isogram
from pytest import mark, param


@mark.parametrize(
    "word,expected_result",
    [
        param("", True,
              id="should return true string is empty"),
        param("playgrounds", True,
              id="should return true if string no has the same letters"),
        param("food", False,
              id="should return false if string has the same letters"),
        param("Adam", False,
              id="should return false if string has the same letters"
                 "in different cases")
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
