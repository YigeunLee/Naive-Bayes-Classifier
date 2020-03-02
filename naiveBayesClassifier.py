
from collections import defaultdict
import csv
import numpy as np
import math
from google.colab import drive

drive.mount('/content/gdrive',force_remount=True)

class Prob:
    def __init__(self):
      self.positive_cnt = 0
      self.negative_cnt = 0
      self.positive_prob = 0.0
      self.negative_prob = 0.0
      self.prob = 0.0
      self.cnt = 0
class NaiveBayesClassifier:
    def load_tables(self):
      f = open('/content/gdrive/My Drive/dataset.csv', 'r', encoding='utf-8')
      rdr = csv.reader(f)
    
      self.tables = {};
      self.headerindex =  {"outlook" : 0, "temperature":1 , "humidity":2 , "windy" : 3, "play_golf" : 4}
      self.positive_cnt = 0
      self.negative_cnt = 0
      row_idx = 0
      for row in rdr:
          col_idx = 0
          if row[4] == 'Yes':
            self.positive_cnt += 1
          else:
            self.negative_cnt += 1

          for col in row:
            if col_idx < 4:
              if col not in self.tables:
                self.tables[col] = Prob() # process header

              self.tables[col].cnt += 1
              if row[4] == 'Yes':
                self.tables[col].positive_cnt += 1
              else:
                self.tables[col].negative_cnt += 1


            col_idx += 1
          row_idx += 1
      f.close()  
    def get_prob(self,features):
      prob = [1.0,1.0]
      predictor_prior_prob = 1; # 0.001 is rejecting to divide 0
      for col in features:
        prob[0] = prob[0] * (self.tables[col].positive_cnt /  self.positive_cnt)
        prob[1] = prob[1] * (self.tables[col].negative_cnt / self.negative_cnt)
        predictor_prior_prob = predictor_prior_prob * (self.tables[col].cnt / 14)
      

      prob[0] = ((prob[0]  * 0.5) / predictor_prior_prob)
      prob[1] = ((prob[1]  * 0.5) / predictor_prior_prob)
      return prob


classifier = NaiveBayesClassifier()
classifier.load_tables()
prob = classifier.get_prob(['Rainy','Mild','High','FALSE'])
print(prob)