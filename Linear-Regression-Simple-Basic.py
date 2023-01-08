//libray ที่เราจะใช้มี 4 อย่างก็คือ 
1.Pandas มาใช้อ่านข้อมูล 
2.Matplotlib จะใช้ในการสร้างกราฟ 
3.ผมโหลด sklearn เพื่อโหลดโมเดล มาใช้ ซึ่งมี2ตัว LinearRegression เพื่อใช้คาดคะเนโอกาสในอนาคต ส่วน metrics ใช้ตรวจสอบโอกาสคคาดเคลื่อนของการคาดคะเน//
import pandas as pd
import matplotlib as plt
from sklearn.linear_model import linearRegression
from sklearn import metrics

//อ่านไฟล์ CSV//
df = pd.read_csv('ไฟล์ของเรา.csv')

//ใช้หาค่าสหสัมพันธ์//
df.corr()

//สร้างกราฟ//
df.plot(x='คอลัมน์ของข้อมูล',y='คอลัมน์ของข้อมูล',style='o')
plt.ylabel('Sales')

//สร้างตัวแปรเต้นและตามพื่อใช้ในการ Predict//
X =df[['คอลัมน์ของข้อมูล']]
y = df['คอลัมน์ของข้อมูล']

//นำตัวแปรต้น-ตามใส่่ข้อมูลเข้าไปเพื่อเป็นแบบจำลอง//
lrm = LinearRegression()
lrm.fit(X,y)

//กรณีอยากเห็นจุดตัดกับค่าความชัน//
Irm.intercept_
Irm.coef_

//พยากรณ์ข้อมูล//
predictions = Orm.predict(ตัวแปรที่อยากPredict)
predictions

//สร้างกราฟที่อยากพยากรณ์//
plt.scatter(X,y,color='black')
plt.plot(X,predictions,color='blue',linewidth=3)

//ต่อไปพยากรณ์ตัวแปรต้นแล้วจะเกิดตัวแปรตามเท่าไหร่//
lrm.predict([[130]])

//หาความคลาดเคลื่อนของการคาดคะเน//
metrics.mean_absolute_error(y,predictions)
