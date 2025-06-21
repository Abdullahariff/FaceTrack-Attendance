import cv2
import os

save_path="data/images"
os.makedirs(save_path , exist_ok=True)


cap=cv2.VideoCapture(0)
count=1
print("Press 's' to save image, 'q' to quit.")

while(True):
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imshow("Capture Face",frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('s'):
        img_name=f"abdullah{count}.jpg"
        cv2.imwrite(os.path.join(save_path,img_name),frame)
        print(f"[+] Saved {img_name}")
        count+=1
        if count > 5:
            print("✅ Done capturing 5 images.")
            break
    elif key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

