# ⚠️ Landslide Early Detection and Warning System (LEDWS)

> **Dự án Nghiên cứu & Thiết kế Kiến trúc Hệ thống Cảnh báo Sạt lở đất.**

---

## 1. Vấn đề (Problem Statement)
Sạt lở đất tại miền Trung diễn biến phức tạp và gây thiệt hại lớn về người và tài sản do thiếu các giải pháp cảnh báo sớm tự động tại các khu vực rủi ro cao.

---

## 2. Giải pháp (Solutions)
**LEDWS** đề xuất hệ thống cảnh báo sớm sạt lở kết hợp giữa nút cảm biến IoT thu thập dữ liệu tự động và phân tích dữ liệu chuỗi thời gian (Time-Series Data Analytics) để đưa ra các mức độ cảnh báo nguy cơ thiên tai.

---

## 3. Cách triển khai (Implementation)

1. **Thu thập dữ liệu (IoT Edge):** Nút cảm biến đo độ ẩm đất, lượng mưa và độ nghiêng mặt đất truyền dữ liệu về Gateway qua kết nối không dây.
2. **Xử lý & Cảnh báo (Cloud Analytics):** Máy chủ phân tích dữ liệu bất thường và phát cảnh báo tự động khi vượt ngưỡng an toàn.
3. **Tài liệu & Hồ sơ Dự án:** 
   - Báo cáo KHKT: [`docs/LEDWS_Technical_Report.pdf`](docs/LEDWS_Technical_Report.pdf)
   - Slide thuyết trình: [`docs/LEDWS_Presentation_Slide.pdf`](docs/LEDWS_Presentation_Slide.pdf)
   - Trích dẫn mã nguồn phần cứng gốc: [`src/source_reference.py`](src/source_reference.py)

---

## 👤 Tác giả & Đóng góp
- **Đỗ Trần Khánh Vinh** (*Lead System Architect & Researcher*): Thiết kế kiến trúc luồng dữ liệu, phân tích bài toán phát hiện bất thường từ cảm biến, thực hiện báo cáo KHKT, slide bảo vệ và poster truyền thông.
