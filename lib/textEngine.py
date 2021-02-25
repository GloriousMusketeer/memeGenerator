import cv2 as cv


class engine:
    def render_text(self, img, arg):
        font = cv.FONT_HERSHEY_SIMPLEX
        (width, height) = (img.shape[0], img.shape[1])
        cv.putText(
            img,
            arg.top,
            (int((width / 2) + 100), int((height / 4))),
            font,
            2,
            (0, 0, 0),
            2
        )
        cv.putText(
            img,
            arg.bottom,
            (int((width / 2) + 100), int(height / 2) + 100),
            font,
            2,
            (0, 0, 0),
            2
        )
        cv.imshow('Meme Generator 0.1 alpha', img)
        cv.waitKey(0)
        cv.destroyAllWindows()
