import cv2
import keyboard
def validarLetras(dedos):
    if dedos == [1, 1, 0, 0, 0, 0]:
        return 'A'
    if dedos == [0, 0, 1, 1, 1, 1]:
        return 'B'
    if dedos == [0, 1, 0, 0, 0, 0]:
        return 'C'
    if dedos == [0, 0, 0, 0, 0, 1]:
        keyboard.press("w")
        return 'D'
    if dedos == [0, 0, 0, 0, 0, 0]:
        keyboard.press("s")
        return 'E'
    if dedos == [1, 0, 1, 1, 1, 0]:
        return 'F'
    if dedos == [0, 1, 0, 0, 0, 1]:
        return 'G'
    if dedos == [0, 0, 0, 0, 1, 1]:
        return 'H'
    if dedos == [0, 0, 1, 0, 0, 0]:
        keyboard.press("a")
        return 'I'
    if dedos == [1, 1, 0, 0, 1, 1]:
        return 'K'
    if dedos == [1, 1, 0, 0, 0, 1]:
        keyboard.press("d")
        return 'L'
    if dedos == [0, 1, 0, 0, 1, 1]:
        return 'N'
    "if dedos == [1, 0, 0, 0, 0, 0]:"
    "return 'O'"
    "if dedos == [1, 1, 0, 0, 0, 1]:"
    "return 'P'"
    if dedos == [0, 1, 1, 1, 1, 0]:
        return 'T'
    if dedos == [0, 0, 0, 0, 1, 1]:
        return 'U'
    if dedos == [0, 1, 0, 0, 1, 1]:
        return 'V'
    if dedos == [0, 1, 0, 1, 1, 1]:
        return 'W'
    if dedos == [1, 1, 1, 0, 0, 0]:
        return 'Y'
    if dedos == [0, 1, 0, 1, 1, 0]:
        return 'X'



def condicionalesLetras(dedos, frame):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if dedos == [1, 1, 0, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'A', (20, 80), font, 3, (0, 0, 0), 5, cv2.LINE_AA)
        print("A")

    if dedos == [0, 0, 1, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'B', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("B")

    if dedos == [0, 1, 0, 0, 0, 0]:
         cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
         cv2.putText(frame,'C', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
         print("C")

    if dedos == [0, 0, 0, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'D', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("D")

    # (angulo pulgar 1, angulo pulgar 2, angulo menique, angulo anular, angulo medio, angulo indice)
    if dedos == [0, 0, 0, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'E', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("E")
    if dedos == [1, 0, 1, 1, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'F', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("F")

    if dedos == [0, 1, 0, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'G', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("G")

    if dedos == [0, 0, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'H', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("H")

    if dedos == [0, 0, 1, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'I', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("I")

    if dedos == [1, 1, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'K', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("K")

    if dedos == [1, 1, 0, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'L', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("L")

    if dedos == [0, 1, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'N', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("N")
    if dedos == [1, 0, 0, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'O', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("O")

    if dedos == [1, 1, 0, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'P', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("P")

    #if dedos == [1, 1, 0, 0, 0, 1]: se repite con la L
      #  cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
     #   cv2.putText(frame, 'Q', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
     #   print("Q")

    if dedos == [0, 1, 1, 1, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'T', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("T")

    if dedos == [0, 0, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'U', (20, 80), font, 3, (0, 0, 0), 2,cv2.LINE_AA)
        print("U")

    if dedos == [0, 1, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'V', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("V")
    if dedos == [0, 1, 0, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'W', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("W")
    if dedos == [1, 1, 1, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'Y', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("Y")
    if dedos == [0, 1, 0, 1, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'X', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("X")
    return dedos