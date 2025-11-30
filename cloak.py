"""
Invisible Cloak (Harry Potter Style) - OpenCV Python

Supports: red, green, blue, saffron, WHITE
Keys:
- b → capture background
- c → toggle cloak effect
- q → quit
"""

import cv2
import numpy as np
import argparse
import textwrap


# ---------------------------------------------------
# HSV Ranges for Cloak Colors (UPDATED WITH WHITE)
# ---------------------------------------------------
COLOR_RANGES = {
    "red": [
        (np.array([0, 120, 70]), np.array([10, 255, 255])),
        (np.array([170, 120, 70]), np.array([180, 255, 255])),
    ],

    "green": [
        (np.array([35, 40, 40]), np.array([85, 255, 255])),
    ],

    "blue": [
        (np.array([94, 80, 2]), np.array([126, 255, 255])),
    ],

    "saffron": [  # optional
        (np.array([5, 140, 100]), np.array([20, 255, 255])),
    ],

    # 🤍 WHITE cloak detection
    "white": [
        (np.array([0, 0, 200]), np.array([180, 40, 255])),
    ]
}

KERNEL = np.ones((3, 3), np.uint8)


# ---------------------------------------------------
# Argument Handler
# ---------------------------------------------------
def parse_args():
    parser = argparse.ArgumentParser(
        description="Harry Potter Invisible Cloak using OpenCV",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """\
            Controls:
            b - Capture background
            c - Toggle cloak effect
            q - Quit

            Example:
            python cloak.py --color white
            """
        ),
    )

    parser.add_argument(
        "--color",
        type=str,
        default="white",
        choices=["red", "green", "blue", "saffron", "white"],
        help="Cloak color"
    )

    return parser.parse_args()


# ---------------------------------------------------
# Mask Generation
# ---------------------------------------------------
def get_color_mask(hsv, color):
    ranges = COLOR_RANGES[color]
    mask = None

    for lower, upper in ranges:
        current = cv2.inRange(hsv, lower, upper)
        mask = current if mask is None else (mask | current)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, KERNEL, iterations=2)
    mask = cv2.dilate(mask, KERNEL, iterations=1)

    return mask


# ---------------------------------------------------
# Background Capture Function
# ---------------------------------------------------
def capture_background(cap, frames=60):
    print("[INFO] Capturing background… Move out of frame.")
    bg = None

    for i in range(frames):
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)

        if bg is None:
            bg = frame.astype("float")
        else:
            cv2.accumulateWeighted(frame, bg, 0.1)

        cv2.putText(
            frame,
            f"Capturing background… {i+1}/{frames}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            (0, 255, 255), 2
        )
        cv2.imshow("Background", frame)
        cv2.waitKey(1)

    cv2.destroyWindow("Background")
    print("[INFO] Background captured.")
    return cv2.convertScaleAbs(bg)


# ---------------------------------------------------
# Main Function
# ---------------------------------------------------
def main():
    args = parse_args()
    cloak_color = args.color

    print(f"[INFO] Cloak Color Selected: {cloak_color.upper()}")
    print("[INFO] b=background, c=toggle cloak, q=quit")

    cap = cv2.VideoCapture(0)

    background = None
    cloak_enabled = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Webcam not found.")
            break

        frame = cv2.flip(frame, 1)
        output = frame.copy()

        cv2.putText(output, f"Cloak: {'ON' if cloak_enabled else 'OFF'} | {cloak_color.upper()}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(output, "b=background, c=cloak, q=quit",
                    (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        if cloak_enabled and background is not None:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            mask = get_color_mask(hsv, cloak_color)
            mask_inv = cv2.bitwise_not(mask)

            visible = cv2.bitwise_and(frame, frame, mask=mask_inv)
            hidden = cv2.bitwise_and(background, background, mask=mask)

            output = cv2.addWeighted(visible, 1, hidden, 1, 0)

        cv2.imshow("White Cloak Invisible Effect", output)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q") or key == 27:
            break

        elif key == ord("b"):
            background = capture_background(cap)

        elif key == ord("c"):
            if background is None:
                print("[WARN] Please capture background first (press b).")
            else:
                cloak_enabled = not cloak_enabled
                print(f"[INFO] Cloak {'ENABLED' if cloak_enabled else 'DISABLED'}.")

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
