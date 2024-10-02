# SEM3-3.-Python

Buổi 1:
Python basic:

Tính các phép toán: cộng, trừ, nhân, chia đơn giản với menu

exam: array list và 1 vài thứ liên quan

---------------------------------------------

Buổi 2: 
- List ( "[ ]"), tuple ( "( )")
- dist

Giống:
- lưu dữ liệu
Khác:
- List có thể insert dữ liệu còn tuple không thể


---------------------------------------------

Buổi 4:
 FREE ata grid     (Mất phí): cú pháp: lambda tham_so: bieu_thuc  
 SMMS             (FR EE)
 KSt  nối tới mysql:
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

Buổi 5: Lam bai tap

---------------------------------------------

Buổi 6: Hoàn thiện nốt bài tập buổi 5

join (INNER JOIN, LEFT JOIN, RIGHT JOIN, ... 1 vai kieu nua)

ví dụ: select * from   A   LEFT JOIN    B   ON   A.studentID = B.studentID

LEFT JOIN: Lấy tất cả các bản ghi từ bảng A, cộng với các bản ghi phù hợp từ bảng B. hoặc null trong trường hợp không có giá trị phù hợp

stored procedure (Tạo 1 cái api để clean code, gọi nhiều lần? )

---------------------------------------------

Buổi 7: 
Dạy lại 1 chút về OOP: Object-oriented programming (lập trình hướng đối tượng)


---------------------------------------------
Buổi 8: read file json

lệnh cần thiết: pip install pydantic


---------------------------------------------
B9: Tổng kết, nhìn lại những gì đẫ học:

1. Basic: 
- Loop ( for, while, if else, match - case, ...)
- List, dictionary
- tuple
- Iterator (lấy đc phần tử tiếp theo, gần giống list)
- Lambda ( --- Cú pháp kiểu: ( ) => { }   ---)

2. Database
- MongoDB
- MySQL

3. Lập trình hướng đối tượng ( OOP: Object-oriented programming ) 

4. Bài tập
- Bài 1: 
    + Đọc file student.json
    + Đưa vào list
    + list( filter( lambda() ) )
- Bài 2:
    + Kết nối database
    + Insert, query
- Bài 3.2
    + cách 1:
    + cách 2: case ... when trong sql 
    => Dùng stored procedure

---------------------------------------------
Chuẩn bị cho môn tiếp theo: asp .net core theo mô hình MVC (Môn quan trọng)
+ cài đặt visual studi 
+ SQL server:
    + Azure data studio --------------------- ( FREE )
    + Data grid ------------------------------( Mất phí 💲 )
    + SSMS (SQL Server Management Studio) --- ( FREE )