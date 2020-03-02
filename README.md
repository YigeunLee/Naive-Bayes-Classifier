# Naive-Bayes-Classifier

Introduction
-------------
기본 베이즈정리를 이용하여 작성

기존의 데이터를 기반으로 새로운 데이터가 주어지면 결과를 추측할 수 있다

Reference
-------------
##### Ref #1: https://www.analyticsvidhya.com/blog/2017/09/naive-bayes-explained/
##### Ref #2: https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c

Example #1
-------------
##### Input : ['Rainy','Mild','High','FALSE']
##### Expectation : NO
##### Output : [0.25093735711019655, 0.8780800000000001] => Positive Prob 0.25, Negative Prob 0.87

Example #2
-------------
##### Input : ['Rainy','Cool','Normal','FALSE']
##### Expectation : YES
##### Output : [0.5646090534979423, 0.16464000000000004] => Positive Prob 0.56, Negative Prob 0.16
