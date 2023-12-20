# QR ve Nesne Tespiti Uygulaması

Bu uygulama, kamera üzerinden video akışını izleyerek QR kodları ve diğer nesneleri tespit eder. OpenCV ve YOLO (You Only Look Once) modeli kullanılarak geliştirilmiştir.

## Kullanım

1. **Gereksinimler:**
   - Python 3.x
   - OpenCV kütüphanesi (`pip install opencv-python`)
   - Pyzbar kütüphanesi (`pip install pyzbar`)

2. **Çalıştırma:**
   - `python your_script.py` komutunu kullanarak uygulamayı başlatın.

3. **Sonuçları İzleme:**
   - Kamera akışında QR kodları ve diğer nesneleri izleyebilirsiniz.

## Açıklama

Bu uygulama, kamera görüntüsünden QR kodları ve diğer nesneleri tespit ederek ekrana çizgi çizer ve tespit edilen nesnelerin bilgilerini ekrana yazdırır.

```python
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

# Kamera yakalama
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # QR kodları ve nesneleri tespit et
    read_barcodes(frame)

    # Ekrana görüntüyü göster
    cv2.imshow('Barcode/QR Code Scanner', frame)

    # 'ESC' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Kamera yakalamayı serbest bırak
cap.release()
cv2.destroyAllWindows()

