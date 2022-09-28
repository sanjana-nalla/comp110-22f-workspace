"""Examples of importing Python."""

from lessons import helpers

# Alias a module / imported name as another name
from lessons import helpers as hp

# Import names defined globally in a module
from lessons.helpers import powerful, THE_ANSWER

def main() -> None:
    """Entrypoint of program."""
    print(f"The answer: {helpers.THE_ANSWER}")
    print(helpers.powerful(2, 4))
    print(powerful(2,4))
    print(THE_ANSWER)

if __name__ == "__main__":
    main()