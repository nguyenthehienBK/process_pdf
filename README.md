# Xử lý tách file PDF theo số trang
## Cấu trúc thư mục đầu vào
```shell
cac_folder_scan
├───scan1
│       file_chua_tach.pdf
│
└───scan2
        file_chua_tach.pdf
```
## Thực hiện tách file PDF
Sao chép lệnh bên dưới vào `cmd` để chạy:
```sh
python .\main.py `
--src D:\Work_Hien\support_uncle_chien\process_pdf\test_data\cac_folder_scan `
--dest D:\Work_Hien\support_uncle_chien\process_pdf\test_data\results `
--split_end_page 2 `
--name GCN `
--delete_org 0
```
Ý nghĩa các thông số tùy chọn:
- `--src D:\Work_Hien\support_uncle_chien\process_pdf\test_data\cac_folder_scan`: Chỉ định đường dẫn đến folder chứa
các folder scan
- `--split_end_page 2`: Thực hiện tách `2` trang đầu tiên khỏi phần còn lại
- `--name GCN`: Tên của file PDF đầu tiên sẽ là `GCN.pdf`, lưu ý không chứa dầu cách hay khoảng trắng khác khi đặt tên
- `--delete_org 0`: Chọn có xóa file PDF gốc sau khi tách không. `0` là không xóa, `1` là xóa
## Cấu trúc thư mục sau khi tách file PDF
```shell
cac_folder_scan
    ├───scan1
    │       file_chua_tach.pdf
    │       GCN.pdf
    │       other.pdf
    │
    └───scan2
            file_chua_tach.pdf
            GCN.pdf
            other.pdf
```
## Chạy lệnh dưới đây tại `cmd` để cài đặt công cụ
```shell
cd .\process_pdf
python3 -m venv venv
\venv\Scripts\activate
pip3 install -r requirements.txt
```