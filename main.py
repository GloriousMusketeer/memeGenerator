from typing import List

from lib.argParse import argParse
from lib.textEngine import engine

import cv2 as cv


t_e = engine()


class memeGenerator:
    def meme_engine(self, arg):
        img = cv.imread(arg.image)
        t_e.render_text(img, arg)
        pass


def main(args: List[str]) -> int:
    ap = argParse()
    arg = ap.get_arg_parse()
    meme = memeGenerator()
    meme.meme_engine(arg)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
