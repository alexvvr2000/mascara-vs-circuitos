"""El atajo: `python -m scripts` corre la comprobación, y `python -m scripts --X`, el trabajo X."""
import sys

from . import main


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
