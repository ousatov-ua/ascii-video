from cv2 import cv2

# colorset_64 = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "
colorset_32 = "MWN$@%#&B8gpasenocv?jIli*=-~^`. "

if __name__ == "__main__":

    # Define a video capture object
    vid = cv2.VideoCapture(0)

    while True:

        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        if not ret:
            break

        frame = cv2.resize(frame, (0, 0), fx=0.08, fy=0.08)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        output = ""

        for gray2 in gray:
            output += "\n"
            for dark in gray2:
                # output += colorset_64[dark // 4] * 2
                output += colorset_32[dark // 8] * 2

        print('\r' + output)

    # After the loop release the cap object
    vid.release()

    # Destroy all the windows
    cv2.destroyAllWindows()
