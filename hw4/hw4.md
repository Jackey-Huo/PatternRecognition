1.	已知三个高斯概率密度函数，其类中心分别为：A（1， 1， 1），B（3， 3， 3），C（7， 8， 9）；相应的方差分别为：A（1， 1， 1），B（2， 3， 4），C（6， 6， 9）。

2.	基于上述三个概率密度函数，每类随机产生100个样本，得样本集A1，B1，C1。

3.	基于上述三个概率密度函数，随机产生A2类1000个样本，B2类600个样本，C2类1600个样本。

4.	以D2={A2, B2, C2}为训练样本集，用KNN方法，对D1={A1, B1, C1}中的300个样本进行分类，并计算分类的正确率。其中K=3~9，可以根据自己电脑的计算能力设定。

5.	以D2={A2, B2, C2}为训练样本集，训练线性分类机，对D1={A1, B1, C1}中的300个样本进行分类，并计算分类的正确率。

6.	以D2={A2, B2, C2}为训练样本集，采用扩展的线性分类机（二次）的方法，对D1={A1, B1, C1}中的300个样本进行分类，并计算分类的正确率。

7.	对比分析5，6的结果。