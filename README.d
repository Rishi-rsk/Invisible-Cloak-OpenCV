🧙‍♂️ Invisible Cloak Using OpenCV (Python)
Harry Potter–style Real-Time Invisibility Effect Powered by Computer Vision

This project creates a magical “invisible cloak” effect using Python + OpenCV by detecting a colored cloth (red / green / blue / saffron / white) and replacing it with the background in real time.

Inspired by the Harry Potter cloak, but written cleanly and professionally with modular code, background capture, cloak toggle, and multiple color support.

⭐ Features

🎥 Real-time invisibility effect using webcam

🎨 Supports 5 cloak colors:

🔴 Red

🟢 Green

🔵 Blue

🟧 Saffron (Bhagwa)

🤍 White

🖥️ Interactive controls

b → Capture background

c → Toggle cloak ON/OFF

q → Quit

🧹 Noise removal using morphological operations

🧩 Clean, modular code with reusable functions

📦 Ready for GitHub, LinkedIn, and portfolio

📂 Project Structure
Invisible-Cloak/
│── cloak.py
│── requirements.txt
│── README.md
└── (optional) demo.mp4 / images

🛠️ Tech Stack

Python 3.8–3.12

OpenCV

NumPy

📦 Installation

Install required dependencies:
pip install -r requirements.txt
or manually:

pip install opencv-python numpy

🚀 Usage
Run with default color (white):
python cloak.py --color white

Run with specific cloak color:
python cloak.py --color red
python cloak.py --color blue
python cloak.py --color green
python cloak.py --color saffron
python cloak.py --color white

⌨️ Controls
Key	Action
b	Capture background (important!)
c	Enable/disable cloak invisibility
q / ESC	Quit program
🎨 Supported Cloak Colors (HSV Ranges)
Color	HSV Range
Red	[0–10] & [170–180]
Green	[35–85]
Blue	[94–126]
Saffron (Bhagwa)	[5–20, S:140–255]
White	Low Saturation (S:0–40) & High Value (V:200–255)

Saffron & White are challenging colors — this project uses optimized, tested ranges.

🧠 How It Works (Step-by-Step)

1️⃣ Capture Background
User presses b, camera saves a clean background without the person.

2️⃣ Frame Processing
Each frame is converted from BGR → HSV color space.

3️⃣ Color Masking
The cloak color (red/blue/green/saffron/white) is detected using HSV thresholds.

4️⃣ Mask Cleanup
Noise removed using:

Morphological opening

Dilation

5️⃣ Invisibility Effect
Cloak region is replaced with the background:

final_frame = visible_area + background_cloak_area


6️⃣ Result: Cloth disappears in real-time!

⭐ Author

👨‍💻 Rishi Kulshresth
B.Tech CSE (AI)
Shoolini University
AI, ML, Computer Vision, GenAI Projects