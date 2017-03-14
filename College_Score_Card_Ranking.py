# Final Project
# Tufang Xu, Yier Yin
# CSE 160 AB

import csv
import urllib
import heapq
import matplotlib.pyplot as plt

from enum import Enum
class Student(Enum):
  Unknow =0
  International = 1
  Local = 2
  Transfer = 3
  
class Profile:
  sat_score =0
  max_tuition =0
  category =Student.Unknow
  def __init__(self, sat_score, max_tuition, category):
      self.sat_score = sat_score
      self.max_tuition = max_tuition
      self.category =category

class CollageInfo: 
  rank =0
  city =''
  state =''
  tuition =0
  sat =0
  accept_rate =0
  debt =0
  male_ratio =0
  def __init__(self, rank, city, state, tuition, sat, accept_rate, debt, male_ratio):
      self.rank = rank
      self.city = city
      self.state =state
      self.tuition = tuition
      self.sat =sat
      self.accept_rate =accept_rate
      self.debt =debt
      self.male_ratio =male_ratio  
  
  def ToString(self) :
      return self.city + '\t' + self.state +'\t' + str(self.rank) +'\t' + str(self.tuition) +'\t' + str(self.sat) +'\t' + str(self.accept_rate) +'\t' + str(self.debt) +'\t' + str(self.male_ratio)

  def ToStringWithName(self) :
      return 'city:' + self.city + '\tstate:' + self.state +'\trank:' + str(self.rank) +'\ttuition:' + str(self.tuition) +'\tsat:' + str(self.sat) +'\tAC:' + str(self.accept_rate) +'\tdebt:' + str(self.debt) +'\tMal:' + str(self.male_ratio)

def extract_ranking_field(filename, column_names):
  reader = open(filename)
  input_file = csv.DictReader(reader)
  ret ={};
  for key in column_names:
    ret[key]=[]
  for row in input_file:   
    for key in column_names:
       if key in row.keys():
         ret[key].append(row[key])
  reader.close()
  return ret
  
def process_input() :
  while True:
    print "a) International \r\nb) Local \r\nc) Tranfer: \r\n? (Please Type a, b, c):"
    input1_tmp = raw_input("")
    if input1_tmp !="a" and input1_tmp !="b" and input1_tmp !="c" :
      continue;
    if input1_tmp =="a":
      input1 =Student.International
    if input1_tmp =="b":
      input1 =Student.Local
    if input1_tmp =="c":
      input1 =Student.Transfer
    break
  while True:    
    input2_tmp = raw_input("please input your sat score:")
    try:
      input2 =float(input2_tmp)
    except Exception as ex:
      continue
    break
  while True:    
    input3_tmp = raw_input("please input your maximum tuition you can accept:")
    try:
      input3 =float(input3_tmp)
    except Exception as ex:
      continue
    break
  return Profile(input2, input3, input1)

def CrawlUniversityRank() :
  url = "http://www.4icu.org/us/"
  handle = urllib.urlopen(url)
  html =  handle.read()
  ret ={}
  loc =0
  rank =1
  while True :
    try:
      loc1 =html.index('class=\"lead\">', loc)
      loc2 =html.index('</a>', loc1)
      ret[html[(loc1 + len('class=\"lead\">')): loc2]] =rank
      rank =rank +1
      loc =loc2 +1
    except Exception as ex:
      break
  return ret

def ProcessFinalData(collage_data, ranking_data):
   size =len(collage_data['INSTNM'])
   ret ={}
   for i in range(size):
      name =collage_data['INSTNM'][i]
      if ranking_data.has_key(name) ==False:
         continue
      rank =ranking_data[name]
      city =collage_data['CITY'][i]
      state =collage_data['STABBR'][i]
      try:
        tuition =float(collage_data['TUITIONFEE_OUT'][i])
        sat =float(collage_data['SAT_AVG_ALL'][i])
        accept_rate =float(collage_data['ADM_RATE_ALL'][i])
        tuition =float(collage_data['TUITIONFEE_OUT'][i])
        debt =float(collage_data['DEBT_MDN_SUPP'][i])
        male_ratio =float(collage_data['UGDS_MEN'][i])
        ret[name] =CollageInfo(rank, city, state, tuition, sat, accept_rate, debt, male_ratio)
      except Exception as ex:
        pass
   return ret

def saveDataToFile(final_data) :
   f = open('cleanData.tsv', 'w')
   for (k, v) in final_data.items():
     f.write(k + '\t' + v.ToString()+'\n')
   f.close()


def FilterCollage(user_profile, data):
   ret ={}
   for (k, v) in data.items():
      if user_profile.sat_score >= v.sat and user_profile.max_tuition >= v.tuition:
          ret[k] =v
   return ret

def NormalizeData(data) :
# normalize data which is not between 0,1
  mmax =max(data)
  mmin =min(data)
  
  ret =[]
  for i in data:
    if (mmax ==mmin):
      ret.append(1)
    else:
      ret.append((i - mmin)*1.0 /(mmax -mmin))
  return ret

def GetTopN(data, score, N):
  Top = sorted(score.iteritems(), key=lambda x:-x[1])[:5]
  for item in Top:
     print "college : " + item[0]
     print "score: " +str(item[1])
     print data[item[0]].ToStringWithName() +'\n\n'

def InternationalStudentChoice(data) :
  names =[]
  tuitions =[]
  sats =[]  
  accept_rates =[]
  ranks =[]
  for (k, v) in data.items():
     names.append(k)
     tuitions.append(v.tuition)
     sats.append(v.sat)
     accept_rates.append(v.accept_rate)
     ranks.append(v.rank)
  tuitions =NormalizeData(tuitions)
  ranks =NormalizeData(ranks)
  sats =NormalizeData(sats)
  
  c2score={}
  for i in range(len(names)):
    c2score[names[i]] =0.15 * (1 - tuitions[i]) + 0.4* (1 -sats[i]) + 0.35*accept_rates[i] + 0.2*(1-ranks[i])
  GetTopN(data, c2score, 5)


def LocalStudentChoice(data) :
  names =[]
  tuitions =[]
  sats =[]  
  accept_rates =[]
  debts =[]
  male_ratios =[]
  for (k, v) in data.items():
     names.append(k)
     tuitions.append(v.tuition)
     sats.append(v.sat)
     accept_rates.append(v.accept_rate)
     male_ratios.append(v.male_ratio)
     debts.append(v.debt)
  tuitions =NormalizeData(tuitions)
  debts =NormalizeData(debts)
  sats =NormalizeData(sats)
  
  c2score={}
  for i in range(len(names)):
    c2score[names[i]] =0.2* (1 -tuitions[i]) + 0.1* (1-debts[i]) + 0.1*(1-abs(male_ratios[i] -0.5)) + 0.25*(1-sats[i]) + 0.35 * accept_rates[i]
  GetTopN(data, c2score, 5)

def TransferStudentChoice(data) :
  names =[]
  tuitions =[]
  sats =[]  
  accept_rates =[]
  ranks =[]
  for (k, v) in data.items():
     names.append(k)
     tuitions.append(v.tuition)
     sats.append(v.sat)
     accept_rates.append(v.accept_rate)
     ranks.append(v.rank)
  tuitions =NormalizeData(tuitions)
  ranks =NormalizeData(ranks)
  sats =NormalizeData(sats)
  
  c2score={}
  for i in range(len(names)):
    c2score[names[i]] =0.3 * (1-tuitions[i]) + 0.1* (1-sats[i]) + 0.4*accept_rates[i] + 0.2*(1-ranks[i])
  GetTopN(data, c2score, 5)

def LoadAcceptRate():
   year2file ={2004:'MERGED2004_05_PP 2.csv', 2005:'MERGED2005_06_PP 2.csv', 2006:'MERGED2006_07_PP 2.csv', 
   2008:'MERGED2008_09_PP 2.csv',2009:'MERGED2009_10_PP 2.csv',2011:'MERGED2011_12_PP 2.csv',2012:'MERGED2012_13_PP 2.csv',
   2013:'MERGED2013_14_PP 2.csv'}
   ret ={}
   for (k, v) in year2file.items():
     print 'Loading Data\\' +v
     collage_data =extract_ranking_field(v, ['INSTNM', 'ADM_RATE_ALL'])
     size =len(collage_data['INSTNM'])
  
     for i in range(size):
        name =collage_data['INSTNM'][i]
        
        if ret.has_key(name) ==False:
           ret[name]={}
        try:
           ret[name][k] =float(collage_data['ADM_RATE_ALL'][i])
        except Exception as ex:
           ret[name][k] =0
   return ret
    
def plotGraph(data):
   x =[]
   y =[]
   labels =[]
   plt.clf()
   
   for (k, v) in data.items():
      x.append(k)
      labels.append(str(k))
      y.append(v)
   
   
   plt.ylabel('AC rate')
   plt.xlabel('year')  
   plt.xticks(x, labels, rotation=0)
   plt.grid()
   plt.plot(x, y, 'r--')
   
   plt.show()
  
   
def main():
   print "loading Recent University data"
   colleage_data =extract_ranking_field('MERGED2013_14_PP 2.csv', ['INSTNM', 'CITY', 'STABBR' ,'TUITIONFEE_OUT',  'SAT_AVG_ALL', 'ADM_RATE_ALL', 'DEBT_MDN_SUPP', 'UGDS_MEN'])
   ranking_data = CrawlUniversityRank()
   final_data = ProcessFinalData(colleage_data, ranking_data)
   saveDataToFile(final_data)
   
   print "loading History accept rate data"
   HistoryData =LoadAcceptRate()
 
   while True:
     
     while True:
        choice =raw_input('Recommend College OR Check Accept Rate? Enter R or A or Exit: ')
        if choice !='R' and choice !='A' and choice !='Exit':
           continue;
        break;
     if choice =='R':
        user_profile = process_input()
   
        filter_data =FilterCollage(user_profile, final_data)        
        if len(filter_data) ==0 :
          print "Sorry, There is no choice for you"
          continue
        if user_profile.category ==Student.International:
           InternationalStudentChoice(filter_data)
        elif user_profile.category ==Student.Transfer:
           TransferStudentChoice(filter_data)
        elif user_profile.category ==Student.Local:
           LocalStudentChoice(filter_data)   
     elif choice =='A':
        query =raw_input('Enter a University Name(Full Name):')
        if HistoryData.has_key(query):
           plotGraph(HistoryData[query])
        else:
           print "Sorry, No such univesity"
     elif choice =='Exit':
        break

if __name__ == "__main__": 
    main()