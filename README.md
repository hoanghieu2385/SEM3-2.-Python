# SEM3-3.-Python

B1:
Python basic:

Tính các phép toán: cộng, trừ, nhân, chia đơn giản với menu

exam: array list và 1 vài thứ liên quan

---------------------------------------------

B2: 
- List ( "[ ]"), tuple ( "( )")
- dist

Giống:
- lưu dữ liệu
Khác:
- List có thể insert dữ liệu còn tuple không thể


---------------------------------------------

B4:
Lambda: cú pháp: lambda tham_so: bieu_thuc

Kết nối tới mysql:
- add thêm thư viện: => pip install mysql-connector-python

Cách phần cần tìm hiểu thêm:
- SELECT, INSERT, UPDATE, DELETE
- JOIN (LEFT JOIN, RIGHT JOIN, INNER JOIN, OUTER JOIN)
- UNION / UNION ALL (Union all không xoá các bản ghi bị trùng lặp. Union all nhanh hơn do không cần phải check trùng lặp)
- WHERE 
- HAVING condition (thường được sử dụng thay thế cho mệnh đề WHERE khi điều kiện chọn lọc dữ liệu có nhắc đến các hàm tính toán tổng hợp như: COUNT, SUM, MIN, MAX, AVG)
- GROUP BY ( sử dụng để nhóm các hàng có cùng một bản ghi thuộc một trường nhất định nào đó)
- 1nf 2nf 3nf 

Transactions

Ví dụ: 

- START TRANSACTION;
- SELECT balance FROM checking WHERE customer_id = 10233276;
- UPDATE checking SET balance = balance - 200.00 WHERE customer_id = 10233276;
- UPDATE savings  SET balance = balance + 200.00 WHERE customer_id = 10233276;
- COMMIT;

nếu chẳng may đang chuyển tiền ở dòng 4 thì lỗi. Thì có thể user sẽ nhận đc 200$ mà lại không được ghi vào trong hệ thống 

Deadlock

========= ADD INFO ============ !!!!!!!!!!!


---------------------------------------------

B5: 