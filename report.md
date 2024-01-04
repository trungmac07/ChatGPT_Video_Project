# Báo cáo đồ án Video

## Thành Viên

|MSSV|Họ Tên|
|----|------|
|21127403 | Nguyễn Minh Quân|
|21127367 | Đỗ Thế Nghĩa|
|21127384 | Dương Hạnh Nhi|
|21127461 | Lê Thành Trung|
|21127462 | Mạc Tuấn Trung|

## Mô Hình Ngôn Ngữ

Mô hình ngôn ngữ là mô hình xác suất của ngôn ngữ tự nhiên. Đây là một mô hình trí tuệ nhân tạo hoàn thành một câu bằng cách dự đoán từ tiếp theo sẽ xuất hiện sau các từ đã có trước. 


Mô hình ngôn ngữ học từ sự phân bố xác suất trên các từ hoặc chuỗi từ. Trong thực tế, nó đưa ra xác suất để một chuỗi từ nhất định là “hợp lệ”. Sự hợp lệ này không đề cập đến giá trị ngữ pháp mà thay vào đó, câu hợp lệ số giống với cách mọi người viết, đó là những gì mô hình ngôn ngữ học được.

Giả sử chúng ta có một câu chưa hoàn chỉnh sau:

<center><b>Hôm nay tôi ...</b></center>

Từ những từ trước đó và dựa trên những gì mà mô hình học được trong quá trình huấn luyện, mô hình có thể sẽ dự đoán từ tiếp theo trong câu này. Một số ví dụ như:

<center><b>Hôm nay tôi<span style="color:red"> học</span></b></center>

<center><b>Hôm nay tôi<span style="color:red"> đi</span></b></center>

<center><b>Hôm nay tôi<span style="color:red"> làm</span></b></center>

Thực tế có 2 loại mô hình ngôn ngữ phổ biến

### Mô hình ngôn ngữ dựa trên xác suất thống kê

Mô hình ngôn ngữ thống kê học xác suất xuất hiện của từ dựa trên các ví dụ về văn bản. Dựa trên những thống kê và tần suất xuất hiện của các từ, mô hình ngôn ngữ dựa trên xác suất sẽ dự đoán từ tiếp theo trong câu dựa trên những từ trước đó trong câu.

#### Mô hình ngôn ngữ Unigram

Mô hình ngôn ngữ Unigram là một trong những mô hình đơn giản trong lĩnh vực xử lý ngôn ngữ tự nhiên (NLP). Được sử dụng để đánh giá và mô tả xác suất xuất hiện của mỗi từ đơn trong một ngôn ngữ, mô hình Unigram giúp hiểu rất tốt về cấu trúc ngôn ngữ và sự phụ thuộc giữa các từ.

Giả sử ta có một câu cấu thành từ các từ:
$$t_1,t_2,...t_n$$

Xác suất của câu này sẽ là:
$$P(t_1,t_2,t_3,…,t_𝑛 )=P(t_1 )  P(t_2 )  P(t_3 )…P(t_𝑛)$$


Một ví dụ thực tế như sau:
<center>Hôm nay là một ngày đẹp trời bạn muốn đi dã ngoại hay bạn muốn ở nhà?</center>

Một vài dòng code Python sau đây sẽ giúp ví dụ dễ hiểu hơn

Đầu tiên ta chuẩn bị đoạn dữ liệu trên


```python
# Dữ liệu văn bản
text = "Hôm nay là một ngày đẹp trời bạn muốn đi dã ngoại hay bạn muốn ở nhà?"

# Chuyển đổi thành danh sách các từ
words = text.split()
```

Bước tính xác suất


```python
# Tính xác suất cho mỗi từ sử dụng mô hình Unigram
unigram_probabilities = {}
total_words = len(words)

for word in set(words):
    word_count = words.count(word)
    probability = word_count / total_words
    unigram_probabilities[word] = probability

# In kết quả
print("Xác suất của các từ: ")
for key,value in unigram_probabilities.items():
    print(key,":",value)
```

    trời : 0.058823529411764705
    bạn : 0.11764705882352941
    Hôm : 0.058823529411764705
    một : 0.058823529411764705
    ngày : 0.058823529411764705
    muốn : 0.11764705882352941
    ngoại : 0.058823529411764705
    hay : 0.058823529411764705
    ở : 0.058823529411764705
    nhà? : 0.058823529411764705
    nay : 0.058823529411764705
    đi : 0.058823529411764705
    dã : 0.058823529411764705
    là : 0.058823529411764705
    đẹp : 0.058823529411764705
    
