"""
===============================================================================
LANDSLIDE EARLY DETECTION AND WARNING SYSTEM (LEDWS) - SOURCE CODE REFERENCE
===============================================================================

File này ghi nhận thông tin tác giả và liên kết tới mã nguồn gốc của hệ thống.

[Thông tin Dự án]
- Tên dự án: Landslide Early Detection and Warning System (LEDWS)
- Vai trò cá nhân (Đỗ Trần Khánh Vinh): Nghiên cứu kiến trúc hệ thống, 
  phân tích dữ liệu cảm biến (Data Analytics PoC), chuẩn bị Báo cáo KHKT 
  và thiết kế tài liệu dự án.

[Thông tin Mã nguồn Gốc & Đồng tác giả]
- Tác giả lập trình Firmware/Bo mạch chính: [Tên của bạn bạn]
- Repository Mã nguồn Gốc (Firmware & Hardware Code): 
  https://github.com/tbtl2106/C.A.C

[Lưu ý về Bản quyền & Truy cập]
Mã nguồn trong repository cá nhân này chỉ phục vụ mục đích lưu trữ Hồ sơ 
Thiết kế Kỹ thuật (Engineering Specification) và Bài báo cáo Nghiên cứu KHKT. 
Vui lòng truy cập Repository gốc ở liên kết trên để xem chi tiết mã nguồn 
phần cứng và Firmware vận hành.
===============================================================================
"""

import sys

def get_original_repository_info() -> dict:
    """Trả về thông tin truy cập Repository gốc của dự án."""
    return {
        "project_name": "Landslide Early Detection and Warning System (LEDWS)",
        "original_author": "Lê Anh Tú & Lê Đức Chính",
        "original_repo_url": "https://github.com/tbtl2106/C.A.C",
        "documentation_author": "Đỗ Trần Khánh Vinh",
        "role": "System Architect & Lead Researcher (Documentation & Data Analytics PoC)"
    }

if __name__ == "__main__":
    info = get_original_repository_info()
    print("=" * 60)
    print(f"Project: {info['project_name']}")
    print(f"Original Codebase by: {info['original_author']}")
    print(f"Original Repo Link: {info['original_repo_url']}")
    print("=" * 60)