import cv2
import os
from deepface import DeepFace
from datetime import datetime, time

# Step 1: Dynamic attendance filename based on date
today_date = datetime.now().strftime("%Y-%m-%d")
attendance_log = f'attendance_{today_date}.csv'

# Step 2: Setup known faces directory
known_faces_dir = "data/images"

# Step 3: Create today's CSV if not already there
if not os.path.exists(attendance_log):
    with open(attendance_log, "w") as f:
        f.write("Name,Timestamp,Status\n")

# Step 4: Time threshold
class_start_time = time(9, 0, 0)
late_threshold = time(9, 15, 0)

# Step 5: Mark attendance
marked_names = set()
def mark_attendance(name):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    arrival_time = now.time()

    status = "On Time" if arrival_time <= late_threshold else "Late"
    with open(attendance_log, "a") as f:
        f.write(f"{name},{timestamp},{status}\n")
    print(f"[+] {name} marked as {status} at {timestamp}")

# Step 6: Start webcam with SFace model
cap = cv2.VideoCapture(0)
cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Face Recognition", 800, 600)

print("📷 Starting face recognition... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        for filename in os.listdir(known_faces_dir):
            image_path = os.path.join(known_faces_dir, filename)
            result = DeepFace.verify(frame, image_path, model_name="SFace", enforce_detection=False)

            if result["verified"]:
                name = os.path.splitext(filename)[0]
                if name not in marked_names:
                    mark_attendance(name)
                    marked_names.add(name)
                    cv2.putText(frame, f"Welcome {name}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                break

    except Exception as e:
        print(f"[!] Error: {e}")

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
