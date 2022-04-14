import cv2

cap = cv2.VideoCapture('movie.mp4')

ret, frame = cap.read()
scale = frame.shape[0] / frame.shape[1]
w = 640
h = int(scale * w)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (w, h))

frame_num = 0
while (cap.isOpened()):
    if ret:
        vidout = cv2.resize(frame, (w, h))
        if frame_num < 24:
            cv2.rectangle(vidout, (140, h - 40), (215, h - 70), (0, 0, 0), cv2.FILLED)
            cv2.putText(vidout, 'Slushai', (150, h - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        elif frame_num < 54:
            cv2.rectangle(vidout, (140, h - 40), (303, h - 70), (0, 0, 0), cv2.FILLED)
            cv2.putText(vidout, 'Slushai, a lovko ti', (150, h - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 0, 255), 2)
        elif frame_num < 80:
            cv2.rectangle(vidout, (140, h - 40), (410, h - 70), (0, 0, 0), cv2.FILLED)
            cv2.putText(vidout, 'Slushai, a lovko ti eto pridumal', (150, h - 50), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2)
        elif frame_num < 110:
            cv2.rectangle(vidout, (190, h - 40), (353, h - 70), (0, 0, 0), cv2.FILLED)
            cv2.putText(vidout, 'Ya daje v nachale', (200, h - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        elif frame_num < 135:
            cv2.rectangle(vidout, (190, h - 40), (440, h - 70), (0, 0, 0), cv2.FILLED)
            cv2.putText(vidout, 'Ya daje v nachale ne ponyal', (200, h - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        else:
            cv2.rectangle(vidout, (270, h - 40), (350, h - 70), (0, 0, 0), cv2.FILLED)
            cv2.putText(vidout, 'Molodec', (280, h - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.imshow('frame', vidout)

        out.write(vidout)

        frame_num += 1
    else:
        break
    ret, frame = cap.read()

cap.release()
out.release()

cv2.waitKey(0)

cv2.destroyAllWindows()
