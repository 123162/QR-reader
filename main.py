import cv2
from pyzbar.pyzbar import decode

def read_barcodes(frame):
    barcodes = decode(frame)
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print(f'Type: {barcode_type}, Data: {barcode_data}')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    read_barcodes(frame)

    cv2.imshow('Barcode/QR Code Scanner', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # 'ESC' tuşuna basıldığında döngüyü sonlandır.
        break

cap.release()
cv2.destroyAllWindows()

