# Phone Number Lookup

โปรแกรมตรวจสอบและค้นหาข้อมูลเบื้องต้นของหมายเลขโทรศัพท์ (Phone Number Lookup) โดยใช้ไลบรารี `phonenumbers` ใน Python

## โครงสร้างโฟลเดอร์
- `main.py`: โค้ดโปรแกรม Python สำหรับรับหมายเลขโทรศัพท์และแสดงข้อมูล
- `requirements.txt`: รายการแพ็กเกจที่ติดตั้ง (`phonenumbers`)
- `.venv/`: สภาพแวดล้อมเสมือน (Python Virtual Environment)

## วิธีการรันโปรแกรม

1. เปิด Terminal ในโฟลเดอร์นี้
2. เรียกใช้งาน Virtual Environment:
   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```
   - **Windows:**
     ```cmd
     .venv\Scripts\activate
     ```
3. รันโปรแกรม:
   ```bash
   python main.py
   ```
4. กรอกเบอร์โทรศัพท์ที่ต้องการพร้อมรหัสประเทศ เช่น `+66812345678` หรือ `+3069XXXXXXXX`
   (สามารถพิมพ์ `exit` หรือ `q` เพื่อออกจากโปรแกรมได้)
