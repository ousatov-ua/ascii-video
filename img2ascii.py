from cv2 import cv2

if __name__ == "__main__":

    #colorset = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "
    colorset_32 = "ЖWN$@%#&B8жpasenocv?jIli*=-~`. "

    img = cv2.imread("/Users/alus/photo.jpg")
    img = cv2.resize(img, (0, 0), fx=0.18, fy=0.18)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output = ""

    for gray2 in gray:
        output += "\n"
        for dark in gray2:
            output += colorset_32[dark // 8] * 2

    with open("output.txt", mode="w") as f:
        f.write(output)
