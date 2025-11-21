Đối với phát triển backend và frontend, việc gửi các truy vấn thủ công đến Gramps Web API có thể rất hữu ích. Sử dụng HTTPie và jq, điều này có thể được thực hiện một cách thuận tiện bao gồm xác thực JWT.

## Cài đặt

HTTPie được cài đặt bằng `pip`:

```bash
python3 -m pip install httpie
```

Bạn sẽ cần phiên bản HTTPie 3.0.0 hoặc mới hơn.

jq có thể được cài đặt trên Ubuntu thông qua

```bash
sudo apt install jq
```

## Lấy mã thông báo truy cập

Để lấy mã thông báo truy cập, hãy truy vấn điểm cuối mã thông báo. Giả sử phiên bản phát triển của bạn đang chạy trên `localhost:5555`, bạn có thể sử dụng lệnh

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Bạn sẽ thấy các mã thông báo JSON dưới dạng đầu ra.

Sử dụng jq, bạn cũng có thể lưu mã thông báo truy cập vào biến môi trường:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Bây giờ bạn có thể sử dụng mã thông báo này trong tất cả các cuộc gọi API yêu cầu xác thực, ví dụ:

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Lưu ý rằng, theo mặc định, các mã thông báo truy cập sẽ hết hạn sau 15 phút.
