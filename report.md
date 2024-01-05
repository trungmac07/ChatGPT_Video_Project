# **Báo cáo đồ án Video**

## **Thành Viên**

|MSSV|Họ Tên|
|----|------|
|21127367 | Đỗ Thế Nghĩa|
|21127384 | Dương Hạnh Nhi|
|21127403 | Nguyễn Minh Quân|
|21127461 | Lê Thành Trung|
|21127462 | Mạc Tuấn Trung|

## **Mô Hình Ngôn Ngữ**

Mô hình ngôn ngữ là mô hình xác suất của ngôn ngữ tự nhiên. Đây là một mô hình trí tuệ nhân tạo hoàn thành một câu bằng cách dự đoán từ tiếp theo sẽ xuất hiện sau các từ đã có trước. 


Mô hình ngôn ngữ học từ sự phân bố xác suất trên các từ hoặc chuỗi từ. Trong thực tế, nó đưa ra xác suất để một chuỗi từ nhất định là “hợp lệ”. Sự hợp lệ này không đề cập đến giá trị ngữ pháp mà thay vào đó, câu hợp lệ số giống với cách mọi người viết, đó là những gì mô hình ngôn ngữ học được.

Giả sử chúng ta có một câu chưa hoàn chỉnh sau:

<center><b>Hôm nay tôi ...</b></center>

Từ những từ trước đó và dựa trên những gì mà mô hình học được trong quá trình huấn luyện, mô hình có thể sẽ dự đoán từ tiếp theo trong câu này. Một số ví dụ như:

<center><b>Hôm nay tôi<span style="color:red"> học</span></b></center>

<center><b>Hôm nay tôi<span style="color:red"> đi</span></b></center>

<center><b>Hôm nay tôi<span style="color:red"> làm</span></b></center>

Thực tế có 2 loại mô hình ngôn ngữ phổ biến

### **Mô hình ngôn ngữ dựa trên xác suất thống kê**

Mô hình ngôn ngữ thống kê học xác suất xuất hiện của từ dựa trên các ví dụ về văn bản. Dựa trên những thống kê và tần suất xuất hiện của các từ, mô hình ngôn ngữ dựa trên xác suất sẽ dự đoán từ tiếp theo trong câu dựa trên những từ trước đó trong câu.

#### **Mô hình ngôn ngữ Unigram**

Mô hình ngôn ngữ Unigram là một trong những mô hình đơn giản trong lĩnh vực xử lý ngôn ngữ tự nhiên (NLP). Được sử dụng để đánh giá và mô tả xác suất xuất hiện của mỗi từ đơn trong một ngôn ngữ, mô hình Unigram giúp hiểu rất tốt về cấu trúc ngôn ngữ và sự phụ thuộc giữa các từ.

Giả sử ta có một câu cấu thành từ các từ:
$$t_1,t_2,t_3,...t_n$$

Xác suất của câu này sẽ là:
$$P(t_1,t_2,t_3,…,t_𝑛 )=P(t_1 )  P(t_2 )  P(t_3 )…P(t_n)$$


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

    Xác suất của các từ: 
    trời : 0.058823529411764705
    là : 0.058823529411764705
    nhà? : 0.058823529411764705
    ngày : 0.058823529411764705
    một : 0.058823529411764705
    đẹp : 0.058823529411764705
    bạn : 0.11764705882352941
    hay : 0.058823529411764705
    nay : 0.058823529411764705
    đi : 0.058823529411764705
    dã : 0.058823529411764705
    ở : 0.058823529411764705
    muốn : 0.11764705882352941
    Hôm : 0.058823529411764705
    ngoại : 0.058823529411764705
    

Với rất nhiều văn bản dữ liệu có thể được mô tả thành bảng như sau:

|Từ |Văn bản 1| Văn bản 2|...|
|---|---------|----------|---|
|Tôi| 0.051   |0.039     |...|
|Là | 0.031   |0.011     |...|
|Anh| 0.012   |0.007     |...|
|Đi | 0.001   |0.002     |...|

#### **Mô hình ngôn ngữ Bigram**

Dựa trên cách tiếp cận tương tự như Unigram, mô hình ngôn ngữ Bigram được mở rộng ý tưởng từ mô hình Unigram bằng cách thay vì tính xác suất các từ riêng lẻ, Bigram sẽ xem xét sự phụ thuộc giữa các từ theo cặp liên tiếp. 

Trong mô hình Bigram, giả định rằng xác suất xuất hiện của một từ phụ thuộc vào từ liền trước nó. Điều này giúp mô hình hiểu được mối quan hệ giữa các từ theo cặp liên tiếp, tăng cường khả năng dự đoán từ tiếp theo trong một chuỗi văn bản.

Giả sử ta có một câu cấu thành từ các từ:
$$t_1,t_2,t_3,...t_n$$

Xác suất của câu này sẽ là:
$$P(t_1,t_2,t_3,…,t_𝑛 )=P(t_1 )  P(t_2|t_1 )  P(t_3|t_2 )…P(t_n|t_{n-1})$$

Tiếp tục với câu ví dụ trên

<center>Hôm nay là một ngày đẹp trời bạn muốn đi dã ngoại hay bạn muốn ở nhà?</center>

Ta lập bảng cho mô hình Bigram như sau:

|       |Hôm|nay|là|một|ngày|đẹp|trời|bạn|muốn|đi|dã|ngoại|hay |ở |nhà?|
|-------|---|---|--|---|----|---|----|---|----|--|--|-----|---|--|----|
|<b> Hôm  </b>  | 0 | 0 | 0| 0 | 0  | 0 | 0  | 0 | 0  |0 | 0| 0   | 0 | 0| 0  |
|<b> nay  </b> | 1 | 0 | 0| 0 | 0  | 0 | 0  | 0 | 0  |0 | 0| 0   | 0 | 0| 0  |
|<b> là   </b> | 0 | 1 | 0| 0 | 0  | 0 | 0  | 0 | 0  |0 | 0| 0   | 0 | 0| 0  |
|<b> một  </b> | 0 | 0 |1 | 0 | 0  | 0 | 0  | 0 | 0  |0 | 0| 0   | 0 | 0| 0  |
|<b> ngày </b> | 0 | 0 | 0| 1 | 0  | 0 | 0  | 0 | 0  |0 | 0| 0   | 0 | 0| 0  |
|<b> đẹp  </b> | 0 | 0 | 0| 0 | 1  | 0 | 0  | 0 | 0  |0 | 0| 0   | 0 | 0| 0  |
|<b> trời </b> | 0 | 0 | 0| 0 | 0  |1  | 0  | 0 | 0  |0 | 0| 0   | 0 | 0| 0  |
|<b> bạn  </b> | 0 | 0 | 0| 0 | 0  | 0 | 1  | 0 | 0  |0 | 0| 0   | 0 | 0| 0  |
|<b> muốn </b> | 0 | 0 | 0| 0 | 0  | 0 | 0  | 1 | 0  |0 | 0| 0   | 0 | 0| 0  |
|<b> đi   </b> | 0 | 0 | 0| 0 | 0  | 0 | 0  | 0 |0.5 |0 | 0| 0   | 0 | 0| 0  |
|<b> dã   </b> | 0 | 0 | 0| 0 | 0  | 0 | 0  | 0 | 0  |1 | 0| 0   | 0 | 0| 0  |
|<b> ngoại</b> | 0 | 0 | 0| 0 | 0  | 0 | 0  | 0 | 0  |0 |1 | 0   | 0 | 0| 0  |
|<b> hay  </b> | 0 | 0 | 0| 0 | 0  | 0 | 0  | 0 | 0  |0 | 0| 1   | 0 | 0| 0  |
|<b> ở    </b> | 0 | 0 | 0| 0 | 0  | 0 | 0  | 0 |0.5 |0 | 0| 0   | 0 | 0| 0  |
|<b> nhà? </b> | 0 | 0 | 0| 0 | 0  | 0 | 0  | 0 | 0  |0 | 0| 0   | 0 | 1| 0  |

#### **Mô hình ngôn ngữ N-grams**

Với Unigram là xác suất các từ đơn lẻ
Với Bigram là xác suất các cặp từ xuất hiện
Còn với N-grams, đây là một phương pháp thống kê sử dụng trong xử lý ngôn ngữ để mô tả xác suất xuất hiện của một chuỗi các từ (nhiều từ với N là số từ trong một chuỗi) dựa trên một lịch sử cụ thể của các từ trước đó (thường được học từ các văn bản có sẵn).

Trong N-grams, "N" thường được sử dụng để chỉ số lượng các từ được xem xét cùng một lúc. Ví dụ:

Trong mô hình bigram (N=2), xác suất xuất hiện của từng từ phụ thuộc vào từ trước nó.\
Trong mô hình trigram (N=3), xác suất xuất hiện của từng từ phụ thuộc vào cả hai từ trước nó.

Giả sử ta có một câu cấu thành từ các từ:
$$t_1,t_2,t_3,...t_n$$

Lúc này Mô hình N-grams tập trung vào xác suất điều kiện của một từ dựa trên N-1 từ trước đó. Điều này được biểu diễn bằng công thức:
$$P(t_n|t_1,t_2,...,t_{n-1})$$

### **Mô hình ngôn ngữ dựa trên mạng nơ ron**

#### **Vấn đề ở mô hình ngôn ngữ xác suất**

Giả sử câu sau:

<center> Tôi nghĩ là chú chó ăn xong bữa ăn rồi </center>

Với mô hình xác suất ta có 
$$P(\text{ăn}|\text{chú chó})$$
Điều này sẽ giúp mô hình dự đoán được từ "ăn" sau "chú chó"

Tuy nhiên nếu ta thay đổi "chú chó" thành "chú mèo". 
<center>Tôi nghĩ là chú mèo ăn xong bữa ăn rồi</center>

Điều này gây khó khăn cho mô hình ngôn ngữ dựa trên xác suất bởi vì trong dữ liệu học nếu như thiếu đi cụm "chú mèo ăn" đồng nghĩa với việc

$$P(\text{ăn}|\text{chú mèo}) = 0$$

Mô hình sẽ không thể nào dự đoán được từ "ăn" nếu trước đó là "chú mèo"

#### **Words Embedding**

Với kỹ thuật nhúng (embedding), tức là chuyển các từ về dạng vector đặc trưng tương ứng với từ đó, ta sẽ nhận được 2 vector đặc trưng từ 2 từ khác nhau là "chó" và "mèo"

Và với mô hình mạng nơ ron sẽ tìm thấy điểm tương đồng giữa 2 vector đặc trưng này. Điều này giúp ích rất nhiều cho mô hình ngôn ngữ của chúng ta dự đoán chính xác từ "ăn" dù cho "chú mèo ăn" xuất hiện ít hoặc chưa từng xuất hiện trong bộ dữ liệu huấn luyện

<center><image src="https://i.imgur.com/bLvLuTq.png" height=50% width=50%}/></center>

#### **Cách hoạt động**

<center><image alt="Sơ đồ mô hình ngôn ngữ mạng nơ rơn đơn giản" src="https://i.imgur.com/iqE2JgN.png" width = 50% height=50%/></center>

**Lớp đầu vào (Input layer)**

Ta sẽ có một từ điển là một tập hợp chứa toàn bộ các từ mà mô hình đã học được. Ở đây ta ký hiệu nó là $V$\
Dựa trên loại mô hình ta sẽ có một cửa sổ trượt trên $N$ từ đã được tạo ra trước đó để xác định xác suất cho từ tiếp theo.\
Với mỗi từ được chọn như vậy, ta sẽ tạo một one-hot vector (vector chỉ toàn 0 và chỉ bằng 1 tại vị trí của từ đó trong từ điển $V$)\
Ví dụ với từ "ăn" nằm ở vị trí thứ 97 trong từ điển $V$ và $x$ là one-hot vector của "ăn":
$$ x = \begin{bmatrix}
x_1 \\
x_2 \\
... \\
x_{|V|}
\end{bmatrix}\\ $$

$$x_{97} = 1 \>\> \text{và} \>\> x_i = 0 \>\>\>\> \forall i \neq 97$$


**Lớp nhúng (Embedding layer)**

Đây là lớp thực hiện chức năng chuyển đổi một từ thành một vector đặc trưng của chúng.\
Tại đây, một ma trận mã hóa $E$ có kích thước $n \times |V|$ sẽ được nhân với các one-hot vector được xây dựng từ lớp đầu vào.\
Do one-hot vector là một vector toàn 0 và chỉ bằng 1 tại vị trí từ đó xuất hiện trong từ điển, phép nhân ma trận trên đồng nghĩa với việc ta rút trích ra cột tương ứng chứa vector mã hóa cho từ 
<center><image src="https://i.imgur.com/3u3jvKt.png" width=50% height=50%/></center>

**Các lớp ẩn (Hidden layers)**

Mô hình ngôn ngữ dựa trên mạng nơ-ron thường có cấu trúc với nhiều hidden layer. Hidden layer đóng một vai trò quan trọng trong quá trình học và hiểu ngôn ngữ. Có thể nói các mạng nơ ron ẩn này là thành phần chính để mô hình thực hiện xác định trọng số cho các từ có thể xuất hiện tiếp theo.\
Trong quá trình huấn luyện các lớp này đã được học các đặc trưng ngôn ngữ ẩn. Các trọng số của hidden layer được điều chỉnh thông qua quá trình lan truyền ngược (backpropagation) để cực tiểu hóa sai số giữa dự đoán và thực tế.\

Mạng nơ ron ẩn giúp mô hình học và hiểu ngữ cảnh, tạo ra dự đoán từ tiếp theo có ý nghĩa chứ không còn là các câu vô nghĩa lắp ghép từ những từ xuất hiện với tấn suât lớn. 
Mạng nơ-ron có thể học các biểu diễn phức tạp của ngôn ngữ.
Càng nhiều tham số cho các hidden layer, mô hình càng trở nên phức tạp và cần nhiều dữ liệu hơn để huấn luyện. Điều này sẽ khiến mô hình rất gần với ngôn ngữ con người sử dụng và ý nghĩa của văn bản được diễn đạt rõ ràng.

**Lớp đầu ra (Output layer)**
Các giá trị ẩn từ hidden layers sau khi hoàn tất sẽ được truyền qua output layer để tạo ra dự đoán cho từ tiếp theo.\
Một hàm kích hoạt sẽ được sử dụng để chuyển đổi giá trị ẩn thành một phạm vi chấp nhận được cho dự đoán. Một cách đơn giản nhất đó là hàm `Softmax`. `Softmax` sẽ chuyển các giá trị ẩn thành một dãy các tỷ lệ các từ tiếp theo có thể xuất hiện.\
Và tất nhiên từ có xác suất xuất hiện cao nhât sẽ được chọn làm từ tiếp theo trong câu\
Đến đây quá trình dự đoán một từ đã hoàn thành. Cửa sổ sẽ tiếp tục trượt xuống một từ và bắt đầu lại quá trình dữ đoán cho từ thứ ${n+1} tiếp theo

## **Mô hình ngôn ngữ lớn (Large Language Models)**

Mô hình ngôn ngữ lớn là một dạng mô hình máy học được huấn luyện trên một lượng lớn dữ liệu ngôn ngữ tự nhiên để hiểu và tạo ra văn bản ngôn ngữ. Những mô hình này thường có kích thước và độ phức tạp lớn, thậm chí có thể chứa hàng tỷ tham số. Dưới đây là một giải thích rõ ràng về mô hình ngôn ngữ lớn.

### **Đặc Điểm Chính**
- Mô hình ngôn ngữ lớn thường được huấn luyện dữ liệu văn bản từ internet, sách, báo, và các nguồn ngôn ngữ tự nhiên khác. Từ đó hiểu được quy luật, cách cấu trúc câu, ý nghĩa của các từ. 
- Những dữ liệu văn bản này là vô cùng lớn, lên đến hàng tetrabytes dữ liệu chữ.
- Đồng thời với dữ liệu lớn thường thời gian huấn luyện sẽ kéo dài từ hàng tuần cho đến hàng tháng với hàng trăm hàng ngàn giờ huấn luyện.
- Các mô hình này thường là các kiến trúc mạng nơ-ron sâu, chẳng hạn như Transformer.
- Một số lớp (layer) có thể kể đến như:
    - *Embedding layer* chuyển đổi từng từ trong văn bản đầu vào thành biểu diễn vectơ nhiều chiều (high-dimensional). Những vec-tơ này nắm bắt thông tin ngữ nghĩa và cú pháp của từng đơn vị cấu tạo nên câu (từ hoặc token) và giúp mô hình hiểu được ngữ cảnh của văn bản.
    - *Attention layers* là một phần quan trọng của LLM, cho phép mô hình tập trung có chọn lọc vào các phần khác nhau của văn bản đầu vào. Cơ chế này giúp mô hình chú ý đến các phần có liên quan nhất của văn bản đầu vào và tạo ra các dự đoán chính xác hơn.
    - *Feedforward layers* gồm nhiều lớp được kết nối đầy đủ áp dụng các phép biến đổi phi tuyến tính cho các embedding vector đầu vào. Các lớp này giúp mô hình học các thông tin trừu tượng hơn từ văn bản đầu vào.
    - *Recurrent layers* của LLM được thiết kế để diễn giải thông tin từ văn bản đầu vào theo trình tự. Các lớp này duy trì trạng thái ẩn được cập nhật ở mỗi bước thời gian, cho phép mô hình nắm bắt được sự phụ thuộc giữa các từ trong câu.


### **Kích Thước và Số Lượng Tham Số**
- Mô hình ngôn ngữ lớn thường có kích thước lớn, có thể chứa hàng triệu hay hàng tỷ tham số.
- Số lượng tham số lớn giúp mô hình học được biểu diễn phức tạp của ngôn ngữ và ngữ cảnh.

### **Pre-training và Fine-tunning**
**Pre-training**
- Mô hình ngôn ngữ lớn được huấn luyện trước (pre-training) trên lượng lớn dữ liệu ngôn ngữ tự nhiên.
- Quá trình này giúp mô hình học được các đặc trưng ngôn ngữ tự nhiên mà không cần thông tin ngữ cảnh cụ thể.

**Fine-tunning**
- Fine-tuning là quá trình điều chỉnh và cập nhật các trọng số của một mô hình đã được huấn luyện trước đó (pre-trained model) để phù hợp với một tập dữ liệu mới hoặc nhiệm vụ cụ thể.
- Thay vì huấn luyện mô hình từ đầu, chúng ta sử dụng kiến thức đã được học từ một mô hình ngôn ngữ có sẵn để nhanh chóng và hiệu quả hóa quá trình học cho tập dữ liệu mới.
- Sau quá trình pre-training, mô hình có thể được fine-tuned trên một tập dữ liệu nhỏ hoặc tác vụ cụ thể để tối ưu hóa cho nhiệm vụ cụ thể nào đó.
- Các tác vụ cụ thể có thể kể đến như: mô hình phiên dịch, mô hình trả lời câu hỏi (chatbot), gợi ý cho người soạn thảo văn bản, soạn thảo code.

## **OpenAI và ChatGPT**

### **Generative Pre-training Transformer - GPT**

GPT là viết tắt cho Generative Pre-training Transformer, là một mô hình ngôn ngữ tự nhiên do chính công ty OpenAI phát triển.\
GPT là mô hình ngôn ngữ dựa trên mạng nơ ron với kiến trúc phức tạp và số lượng tham số khổng lồ

Với GPT-3, số lượng tham số lên đến 175 tỷ và dữ liệu huấn luyện khổng lồ: từ hơn 570GB đến khoảng 45TB

Với lượng tham số khổng lồ và mã hóa các từ thành các vector đặc trưng, GPT-3 có thể hiểu được mối quan hệ cũng như ý nghĩa của các từ và xây dựng một câu có cấu trúc đầy đủ ý nghĩa.
<center><image src="https://i.imgur.com/zp9RQPR.png" width=30% height=30% /></center>

### **ChatGPT**

ChatGPT là ứng dụng do OpenAI phát triển dựa trên mô hình ngôn ngữ GPT\
ChatGPT có thể đơn giản được sử dụng thông qua web hoặc áp dụng vào các ứng dụng thông qua API của OpenAI

ChatGPT được tinh chỉnh (fine-tuning) từ mô hình pre-trained GPT trên những bộ dữ liệu tập trung vào giao tiếp cũng như là hội thoại (tuy nhiên hiện này OpenAI cũng chưa cung cấp đầy đủ các nội dung được sử dụng để tinh chỉnh ChatGPT). Điều này giúp ChatGPT hoạt động như một người trợ lý và có thể trả lời câu hỏi cũng như trò chuyện với người dùng.

#### **Một số chức năng**



- **Hỗ Trợ và Trả Lời Câu Hỏi:**\
ChatGPT có thể được sử dụng để trả lời các câu hỏi của người dùng về nhiều chủ đề khác nhau.

- **Tạo Nội Dung Văn Bản:**\
Có thể sử dụng để tạo văn bản sáng tạo, viết bài, hoặc tạo nội dung cho các ứng dụng khác.

- **Hỗ Trợ Việc Học:**\
Dùng để giải bài toán, giải đáp thắc mắc, hoặc hỗ trợ trong quá trình học tập.

- **Giao Tiếp và Trò Chuyện:**\
Có thể sử dụng để tương tác và trò chuyện với người dùng, giả lập vai trò của một đối tác trò chuyện.

- **Phân Loại Văn Bản:**\
Áp dụng để phân loại văn bản, nhận biết cảm xúc, hoặc phân loại nội dung văn bản theo các đặc điểm nhất định.

- **Tạo Ảnh Hóa Nội Dung:**\
Dùng để biểu diễn thông tin văn bản dưới dạng hình ảnh, tạo visualizations cho dữ liệu văn bản.

- **Hỗ Trợ Sáng Tạo và Tìm Kiếm Ý Tưởng:**\
Giúp người dùng tìm kiếm ý tưởng sáng tạo, tạo ra câu chuyện, hay khám phá các khía cạnh mới trong một chủ đề nào đó.

#### **Cách hoạt động**

<center><image src="https://i.imgur.com/hoRTVVx.png" height=70% width=70%/></center>


ChatGPT là một mạng nơ ron hết sức phức tạp, hình minh họa trên cũng chỉ là tóm tắt rút gọn còn một phần quá trình. Trong thực tế, ChatGPT có rất nhiều khối (blocks) xử lý như vậy trước khi cho ra output thực sự.
Một cách đơn giản dựa trên mô hình tóm tắt trên, quá trình tiếp nhận câu hỏi, xử lý, tính toán và đưa ra câu trả lời có thể tóm tắt như sau:

**Chuyển hóa thành các vector đặc trưng**

Câu đầu vào sẽ được tách thành các từ hoặc chuỗi từ nhỏ hơn và được chuyển hóa thành một vector đặc trưng.\
Vector đặc trưng này sẽ mang đặc trưng của từ ngữ và ý nghĩa sẽ được tầng self attention phân tích mối quan hệ từ đó hiểu rõ ý nghĩa nội dung của câu.

**Self Attention Layer**

Trong mô hình ngôn ngữ như ChatGPT, "self-attention layer" là một thành phần quan trọng trong kiến trúc Transformer. Cụ thể, nó được sử dụng để xử lý thông tin từ tất cả các từ trong câu đầu vào đồng thời, giúp mô hình hiểu được mối quan hệ giữa các từ và tạo ra biểu diễn ngữ cảnh cho mỗi từ dựa trên ngữ cảnh xung quanh nó.

Tính năng chính của self-attention layer bao gồm:

- *Chú ý đồng thời đến tất cả các vị trí:* Mỗi từ trong câu có thể tương tác với tất cả các từ khác thông qua trọng số chú ý. Điều này giúp mô hình hiểu được cách mỗi từ ảnh hưởng đến các từ khác và cũng giúp xử lý các mối quan hệ không cố định giữa các từ.

- *Biểu diễn ngữ cảnh:* Self-attention layer giúp tạo ra một biểu diễn ngữ cảnh cho mỗi từ dựa trên thông tin từ tất cả các từ khác trong câu. Điều này cung cấp một cách hiệu quả để mô hình "hiểu" ngữ cảnh của câu và dự đoán từ tiếp theo trong chuỗi.

- *Khả năng xử lý chuỗi dài:* Do self-attention layer có khả năng xử lý toàn bộ chuỗi đầu vào đồng thời, nó giúp mô hình giải quyết vấn đề vanishing gradient (gradient biến mất) khi xử lý chuỗi dài, là một vấn đề phổ biến trong các mô hình sử dụng kiến trúc RNN (Recurrent Neural Network) truyền thống.

**Feedforward Neural Network**

Feedforward layer trong kiến trúc của mô hình như ChatGPT thường được sử dụng sau các lớp tự chú ý (self-attention layers) trong các mô hình Transformer. Feedforward layer chủ yếu thực hiện các phép biến đổi phi tuyến tính đơn giản cho các biểu diễn đầu vào từ các lớp tự chú ý. Dưới đây là một số điểm quan trọng về tác dụng của feedforward layer:

- *Biến đổi phi tuyến tính:* Feedforward layer thường thực hiện các phép biến đổi phi tuyến tính cho từng vị trí đầu vào độc lập. Điều này giúp mô hình học được các mối quan hệ phức tạp và biểu diễn các đặc trưng phức tạp của dữ liệu đầu vào.

- *Mở rộng không gian đặc trưng:* Bằng cách sử dụng các hàm kích thích phi tuyến tính, feedforward layer giúp mô hình tạo ra các biểu diễn có chiều sâu hơn, mở rộng không gian đặc trưng của dữ liệu. Điều này có thể giúp mô hình học được các biểu diễn phức tạp hơn và thích ứng tốt hơn với dữ liệu đa dạng.

- *Giảm chiều của biểu diễn:* Thông thường, sau khi thực hiện phép biến đổi phi tuyến tính, mô hình có thể sử dụng các kỹ thuật như hàm kích thích (activation function) và dropout để tinh chỉnh và giảm chiều của biểu diễn đầu ra. Điều này giúp kiểm soát số lượng tham số của mô hình và tránh tình trạng overfitting.

- *Tăng tính tương tác không gian:* Feedforward layer tạo ra các tương tác không gian giữa các thành phần của biểu diễn đầu vào, giúp mô hình học được các mối quan hệ phức tạp và tương tác giữa các đặc trưng.

**Final Transform Layer**

Thực tế ChatGPT không có lớp Final Transform Layer chuyên biệt mà thay vào đó ở cuối mỗi block sẽ có một lớp Normalization và một lớp Feedforward Layer

**Lớp Normalization (Layer Normalization):**

- *Tác dụng:* Lớp normalization giúp chuẩn hóa giá trị đầu ra từ lớp tự chú ý để giữ cho các đặc trưng có giá trị gần bằng nhau và dễ quản lý hơn trong quá trình học.
- *Ưu điểm:* Giúp kiểm soát gradient, giảm hiện tượng vanishing/exploding gradient, và cải thiện sự hội tụ của mô hình.
- *Cơ chế hoạt động:* Chuẩn hóa được thực hiện bằng cách trừ đi giá trị trung bình của đầu ra và chia cho độ lệch chuẩn. Điều này giúp đầu ra của lớp có mean bằng 0 và độ lệch chuẩn bằng 1.

**Lớp Feedforward:**

- *Tác dụng:* Lớp feedforward thực hiện các phép biến đổi phi tuyến tính đơn giản cho mỗi vị trí đầu vào độc lập, giúp mô hình học được các mối quan hệ phức tạp giữa các đặc trưng.
- *Cơ chế hoạt động:* Mỗi đầu vào tại mỗi vị trí được đưa qua một lớp kết nối đầy đủ với các trọng số tuyến tính và hàm kích thích phi tuyến tính. Điều này tạo ra đầu ra mới tại mỗi vị trí.

**Dự đoán từ tiếp theo**

Mô hình GPT là một mô hình ngôn ngữ tự động sinh (autoregressive), có nghĩa là nó tạo ra câu trả lời từng từ một theo thứ tự tuần tự.\
Mô hình sử dụng kết quả từ lớp feedforward để dự đoán từ tiếp theo trong chuỗi.\
Quá trình này được lặp lại cho đến khi câu trả lời đủ dài hoặc điều kiện dừng được đạt đến.

**Output**
Nội dung văn bản trả lời sẽ được trả về cho người dùng

#### **Ưu và nhược điểm**

**Ưu điểm**

- *Sự Linh Hoạt:* ChatGPT là một mô hình ngôn ngữ mạnh mẽ có khả năng xử lý nhiều loại nhiệm vụ. Nó có thể được sử dụng cho việc tạo văn bản, tư vấn thông tin, giải bài toán, và nhiều ứng dụng khác.

- *Tính Sáng tạo:* Mô hình có khả năng tạo ra nội dung sáng tạo và độc đáo, giúp người dùng thực hiện công việc sáng tạo và phát triển ý tưởng mới.

- *Hỗ trợ Nhanh chóng:* ChatGPT có thể cung cấp câu trả lời nhanh chóng cho nhiều câu hỏi và vấn đề khác nhau, giúp tăng cường hiệu suất và tiết kiệm thời gian.

- *Dễ sử dụng:* Với giao diện web thân thiện và dễ dùng, người dùng có thể sử dụng ChatGPT ở bất kì đâu, đồng thời cũng có thể áp dụng API của OpenAI vào các ứng dụng phát triển bởi lập trình viên

**Nhược điểm**
- *Hiểu biết hạn chế:* ChatGPT có thể không hiểu rõ ngữ cảnh hoặc yêu cầu thông tin thêm để đưa ra câu trả lời chính xác. Điều này có thể dẫn đến thông tin không chính xác hoặc hiểu lầm.

- *Rủi ro độ chính xác:* Mặc dù có thể sáng tạo, nhưng ChatGPT cũng có khả năng tạo ra thông tin không chính xác, không phù hợp hoặc thiếu tính phân biệt.

- *Bảo mật và Quyền Riêng tư:* Các vấn đề liên quan đến bảo mật và quyền riêng tư có thể nảy sinh khi sử dụng ChatGPT, đặc biệt là khi xử lý thông tin nhạy cảm.

- *Phụ thuộc vào Dữ liệu Đào tạo:* Hiệu suất của ChatGPT phụ thuộc nhiều vào dữ liệu đào tạo, có thể dẫn đến sự thiên lệch hoặc hạn chế trong quy mô và đa dạng của thông tin mà mô hình có thể hiểu và tạo ra.

Tóm lại, tuy ChatGPT mang lại nhiều lợi ích, nhưng việc nhận biết và quản lý nhược điểm của nó là quan trọng để đảm bảo sử dụng có hiệu quả và an toàn.

## **Giới thiệu về JoyImage**

JoyImage là một website được xây dựng đơn giản bằng Streamlit và ngôn ngữ lập trình Python.

Thông qua JoyImage, mọi người có thể tự do sáng tạo ra những bức ảnh ưng ý, bằng nhiều công cụ khác nhau với sự hỗ trợ mạnh mẽ từ ChatGPT 

Các công cụ có thể sử dụng để tạo ảnh là:
- **Tạo ảnh từ những đề tài và mục đã chọn (categories and selections):** Người dùng có thể lựa chọn đề tài cho bức tranh, lựa chọn những nội dung, vật thể, quang cảnh có trong đề tài đó hoặc sáng tạo hơn là kết hợp nhiều đề tài khác nhau để tạo ra những bức ảnh tuyệt đẹp. Các lựa chọn sau khi được chọn sẽ được đưa cho ChatGPT để sinh ra một đoạn văn bản (prompt) để cho AI sáng tạo ảnh.
- **Tạo ảnh từ giọng nói:** Người dùng có thể thu âm trực tiếp trên website và giọng nói tiếng Việt sẽ được chuyển thành văn bản. Với văn bản này người dùng có thể dùng để sáng tạo ảnh trực tiếp hoặc nhờ sự trợ giúp của ChatGPT được tích hợp sẵn trên website để làm câu văn mượt mà hơn và hình ảnh sẽ đẹp hơn.
- **Tạo ảnh từ văn bản:** Một cách đơn giản, người dùng nhập những gì mình muốn có trong bức ảnh vào và yêu cầu AI sáng tạo cho mình bức ảnh tương tự. Tuy nhiên một chức năng được tích hợp đó là sự hỗ trợ từ ChatGPT có thể giúp câu văn dễ hiểu, đầy đủ nội dung và bức ảnh sẽ đẹp hơn, đúng ý người dùng hơn.

### **Công nghệ sử dụng**
Những công nghệ mà JoyImage sử dụng là:
- **Python 3.11.4:** Python là một ngôn ngữ lập trình động mạnh mẽ và đa năng, đặc biệt được ưa chuộng trong lĩnh vực trí tuệ nhân tạo (AI). Với cộng đồng lớn, thư viện phong phú như NumPy, Pandas, và scikit-learn, Python là sự lựa chọn hàng đầu cho việc phát triển mô hình máy học và xử lý dữ liệu trong lĩnh vực AI.
- **Streamlit:** Streamlit là một thư viện Python mã nguồn mở được thiết kế để tạo ứng dụng web được import vào Python để hỗ trợ xây dựng một trang website đẹp, đơn giản và dễ dùng bằng ngôn ngữ lập trình Python.
- **CSS:** CSS được sử dụng chủ yếu để định dạng và trình bày trang web được viết bằng HTML. Do đơn giản, các thiết kế giao diện web của Streamlit sinh ra khá cơ bản và nhàm chán. Do đó cần một vài thay đổi dựa trên một vài đoạn mã CSS để thay đổi giao diện, làm chúng trở nên bắt mắt và thú vị hơn.
- **Stable Diffusion - Openjourney:** Stable Diffusion là một mô hình trí tuệ nhân tạo tạo sinh (là một pre-trained model) có khả năng tạo ra hình ảnh tả thực độc đáo từ lời nhắc bằng văn bản và hình ảnh. Điều đặc biệt là Stable Diffusion hoàn toàn mở cả về mã nguồn và trọng số của mô hình. Do đó mọi người có thể tinh chỉnh (fine-tunning) trên mô hình này và tạo ra những mô hình mong muốn. Openjourney là một mô hình được công bố trên HuggingFace được tinh chỉnh trên Stable Diffusion trên những bức ảnh từ MidJourney. Đây là công nghệ chính của trang web để sáng tạo ra những bức ảnh mà người dùng mong muốn. Ở đây website gọi thông qua API từ HuggingFace.
- **Google Speech Recognition:** Được gọi thông qua thư viện SpeechRecognition sử dụng Google Cloud Speech API. Công nghệ này được sử dụng để nhận diện lời nói của người dùng và chuyển đổi thành văn bản.
- **Google Translate:** Được gọi thông qua thư viện googletrans sử dụng Google Translate API để dịch văn bản tiếng Việt của người dùng sang tiếng Anh. Việc dịch sang tiếng Anh giúp các tác vụ sau có thể xử lí hiệu quả hơn.
- **ChatGPT-3.5:** Được gọi thông qua API của OpenAI ChatGPT hỗ trợ người dùng xây dựng một đoạn prompt hoàn chỉnh, nội dung rõ ràng để Stable Diffusion dễ dàng sáng tạo ra một bức ảnh đẹp ưng ý với người dùng.

<center><image alt="Giao diện chính" src="https://i.imgur.com/lSTa9aC.png" width = 50% height = 50%/></center>

### **Tạo ảnh từ những đề tài và mục đã chọn**

#### **Chọn chủ đề**



Ở giao diện chính của trang web:
- Một dropdown có thể sử dụng để chọn chủ đề cho bức ảnh.

<center><image alt="dropdown" src="https://i.imgur.com/ivGmfKD.png" width=50% height=50% /> </center>

#### **Chọn mục lựa chọn**


- Các mục thuộc vào chủ đề đã chọn sẽ xuất hiện và bạn có thể lựa chọn cho bức ảnh
<center><image alt="Giao diện chính" src="https://i.imgur.com/lSTa9aC.png" width = 50% height = 50%/></center>

- Ở đây ta thử lựa chọn Ao cá, Ngồi làng và Cánh đồng hoa


#### **Sáng tạo ảnh**


- Lướt phía dưới có một lựa chọn để sáng tạo ảnh ngay

<center><image alt="Giao diện chính" src="https://i.imgur.com/vKUtomN.png" width = 50% height = 50%/></center>

- Nhấn vào nút nhấn này và đợi một chút

<center><image alt="Giao diện chính" src="https://i.imgur.com/KvKYlhD.png" width = 50% height = 50%/></center>

- Vậy là một bức ảnh tuyệt vời đã được sáng tạo chỉ trong vài giây


### **Tạo ảnh từ giọng nói**

#### **Thu âm**

- Chọn mục Giọng Nói từ menu bên trái màn hình.
- Chọn thu âm và bắt đầu nói vào micro của mình.
- Giọng nói sẽ được chuyển thành văn bản và cho phép người dùng chỉnh sửa.

<center><image src="https://i.imgur.com/hy3g9kF.png" width = 50% height = 50%></center>

#### **Lựa chọn phương thức sáng tạo**

Người dùng có thể chọn giữa sáng tạo ngay hoặc hỗ trợ của AI:
- Lựa chọn sáng tạo ngay sẽ tạo ảnh từ chính văn bản sinh ra từ văn bản có được từ mô hình chuyển tiếng Việt thành văn bản.
- Văn bản tiếng Việt sau đó thông qua một mô hình phiên dịch sang tiếng Anh cho mô hình sáng tạo ảnh hiểu và tạo ảnh theo yêu cầu.
- Với lựa chọn hỗ trợ bằng AI, văn bản này sẽ được cung cấp cho ChatGPT chỉnh sửa lại nhầm tạo ra một đoạn văn hay hơn giúp hình ảnh sinh ra bắt mắt hơn.

<center><image alt ="Lựa chọn với AI" src = "https://i.imgur.com/5H4efBb.png" height = 50% width = 50%/></center>

- Rất đơn giản bạn đã có cho mình một bức ảnh tuyệt vời chỉ từ giọng nói.

### **Các mô hình pretrained được sử dụng**

#### **ChatGPT (phiên bản 3.5)**

- Dựa trên mô hình ngôn ngữ pre-trained GPT, ChatGPT được tinh chỉnh lại cho phù hợp và tối ưu cho việc trả lời và sáng tạo nội dung hỗ trợ người dùng.
- ChatGPT được sử dụng trong web để tạo ra những đoạn văn bản (prompt) để mô hình sáng tạo ảnh sử dụng làm thông tin để tạo ra ảnh đúng với yêu cầu người dùng.

#### **Stable Diffusion OpenJourney**

- Stable Diffusion là một mô hình Generative AI mã nguồn mở được phát triển bởi công ty Stability AI và ra mắt công khai vào năm 2022, có khả năng tạo ra bất kỳ hình ảnh chi tiết theo ý muốn dựa trên prompt văn bản 
- Mô hình này dựa trên công nghệ Diffusion (khuếch tán) và sử dụng Latent space (không gian ngầm).

**Huấn luyện**

Giả sử ta có bức ảnh "chó" và "mèo"
- Quá trình forward diffusion thêm nhiễu vào ảnh huấn luyện, dần dần biến nó thành ảnh nhiễu không đặc trưng. Các bức ảnh này sẽ trở thành ảnh với mật đỗ nhiễu rất cao đến nổi ta không còn nhận diện được ảnh là chó hay là mèo.
- Quá trình reverse diffusion sẽ cố đảo ngược bức ảnh nhiễu, hướng tới hình ảnh mèo hoặc chó và tất nhiên không có gì ở giữa "chó" và "mèo". Đó là lý do tại sao kết quả có thể là một con mèo hoặc một con chó.
- Để đảo ngược sự khuếch tán (reverse diffusion), chúng ta cần biết lượng nhiễu được thêm vào hình ảnh là bao nhiêu. Câu trả lời là huấn luyện một mô hình mạng nơ ron để dự đoán bao nhiêu nhiễu đã được thêm vào. Nó được gọi là noise predictor trong stable diffusion.

**Hoạt động**

Một cách đơn giản, mô hình này có cơ chế hoạt động như hình bên dưới
<center><image src = "https://i.imgur.com/67n1BX1.png" height=50% weight=50%/></center>


#### **Google Translate**

- Google Dịch (tiếng Anh là Google Translate) là một công cụ dịch thuật trực tuyến đa ngôn ngữ miễn phí được phát triển bởi Google. 
- Google Dịch sử dụng công cụ dịch máy mô phỏng dây thần kinh - Google Neural Machine Translation (GNMT) - dịch "toàn bộ câu tại một thời điểm, chứ không phải từng mảnh một. Nó sử dụng ngữ cảnh rộng hơn này để giúp nó tìm ra bản dịch phù hợp nhất, sau đó nó sắp xếp lại và điều chỉnh để giống như một người nói với ngữ pháp thích hợp hơn".
- Google Neural Machine Translation (GNMT) hoạt động dựa trên một mạng nơ-ron nhân tạo lớn có khả năng học sâu. GNMT cải thiện chất lượng dịch bằng cách sử dụng hàng triệu ví dụ, sử dụng ngữ cảnh rộng hơn để suy ra bản dịch phù hợp nhất. Kết quả sau đó được sắp xếp lại và điều chỉnh để tiếp cận ngôn ngữ dựa trên ngữ pháp của con người.


#### **Google Speech Recognition**

- Google Nhận dạng Giọng nói là công nghệ do Google phát triển để chuyển đổi ngôn ngữ nói thành văn bản viết với các cơ chế bảo mật quyền riêng tư rất tốt.

**Công nghệ sử dụng để huấn luyện mô hình:**
-	*Conventional Learning:* Các mẫu âm thanh sẽ được thu thập và lưu trữ trên máy chủ của Google. Một phần của các mẫu âm thanh này được con người chú thích. Một thuật toán huấn luyện học từ các mẫu dữ liệu âm thanh có chú thích.
    - Trong quá trình đào tạo có giám sát, các mô hình được huấn luyện để bắt chước chú thích của con người cho cùng một âm thanh.
    - Trong đào tạo không giám sát, chú thích của máy được sử dụng thay vì chú thích của con người
-	*Federated Learning:* Đây là kỹ thuật bảo vệ quyền riêng tư được phát triển tại Google để huấn luyện các mô hình AI trực tiếp trên điện thoại hoặc thiết bị khác của người dùng. Với federated learning, các mẫu giọng nói sẽ được đào tạo mà không gửi dữ liệu âm thanh của người dùng đến máy chủ của Google. Một thuật toán huấn luyện học từ dữ liệu âm thanh này trên thiết bị. Từ đó, một mô hình giọng nói mới được hình thành bằng cách kết hợp thông tin học được tổng hợp từ tất cả các thiết bị tham gia.
-	*Ephemeral Learning:* Đây là một kỹ thuật bảo vệ quyền riêng tư khác được sử dụng khi mẫu giọng nói chạy trên máy chủ của Google. Khi hệ thống của Google chuyển đổi các mẫu âm thanh đầu vào thành văn bản, các mẫu đó sẽ được gửi tới bộ nhớ ngắn hạn (RAM). Sau khi học thời gian thực, các mẫu dữ liệu âm thanh này sẽ bị xóa khỏi bộ nhớ ngắn hạn trong vòng vài phút.


### **Cách thức hoạt động của trang web**

#### **Chọn chủ đề**

<center><image src="https://i.imgur.com/dlKuLHy.png" height=50% width=50%/></center>

- Mỗi tập hợp lựa chọn đến từ người dùng thông qua việc gọi API, sẽ được ChatGPT xây dựng thành một prompt hoàn chỉnh.
- Prompt này sau khi được tạo ra thành công sẽ được gửi đến mô hình OpenJourney thông qua API cung cấp bởi Huggingface
- Sau một thời gian xử lý, ảnh được sáng tạo sẽ hiển thị cho người dùng.

#### **Giọng nói**

<center><image src="https://i.imgur.com/SXIqJoJ.png" width = 50% height = 50%/></center>

- Từ âm thanh đầu vào nhớ vào SpeechRecognize sẽ chuyển thành văn bản tiếng Việt.
- Văn bản này sẽ được Google dịch phiên dịch thành tiếng Anh cho mô hình sáng tạo hình ảnh sử dụng.
- Tại bước này người dùng có 2 lựa chọn:
    - Sử dụng trực tiếp văn bản vừa phiên dịch để tạo ảnh.
    - Nhờ sự hỗ trợ của ChatGPT của OpenAI để đoạn văn bản tốt hơn.
- Cuối cùng dữ liệu văn bản (prompt) được truyền cho mô hình OpenJourney thông qua API cung cấp bởi Huggingface để tạo ra hình ảnh theo yêu cầu.

#### **Văn bản**

<center><image src="https://i.imgur.com/RoZHc3P.png" height=50% width=50%</center>

- Văn bản đầu vào được thông qua API của Google dịch, phiên dịch thành tiếng Anh.
- Tại bước này người dùng có 2 lựa chọn:  
    - Sử dụng trực tiếp văn bản vừa phiên dịch để tạo ảnh.
    - Nhờ sự hỗ trợ của ChatGPT của OpenAI để đoạn văn bản tốt hơn.
- Cuối cùng dữ liệu văn bản (prompt) được truyền cho mô hình OpenJourney thông qua API cung cấp bởi Huggingface để tạo ra hình ảnh theo yêu cầu.
