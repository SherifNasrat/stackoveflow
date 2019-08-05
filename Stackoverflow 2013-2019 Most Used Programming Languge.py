#!/usr/bin/env python
# coding: utf-8

# __Each year since 2011, Stack Overflow has asked developers about their favorite technologies, coding habits, and work preferences, as well as how they learn, share, and level up.__
# 
# __Let's go through the survey results and see if we can pick up trends over the years.__

# In[1]:



import Helper as hlpr
import pandas as pd
from collections import defaultdict
get_ipython().run_line_magic('matplotlib', 'inline')


# # What is the most dominant and widely used programming language/technology over the years ?
# 
# For our first question, what is the most dominant and widely used programming language/technology over the years ?
# Notice that I didn't take into consideration the dataset of 2011 and 2012 as the question used for that purpose is "Which languages are you proficient in?" while in later datasets the question used is "Which of the following languages or technologies have you used significantly in the past year? 
# 
# While the two are similar, I chose to treat them differently as they hold a bit of a different meaning.

# In[2]:


#Reading the datasets
#Note: ISO-8859-1 encoding was used as it caused some issues while reading data in datasets older then < 2017
data_2013 = hlpr.read_data('./2013 Stack Overflow Survey Responses/2013 Stack Overflow Survey Responses.csv','ISO-8859-1')
data_2014 = hlpr.read_data('./2014 Stack Overflow Survey Responses/2014 Stack Overflow Survey Responses.csv','ISO-8859-1')
data_2015 = hlpr.read_data('./2015 Stack Overflow Developer Survey Responses/2015 Stack Overflow Developer Survey Responses.CSV','ISO-8859-1')
data_2016 = hlpr.read_data('./2016 Stack Overflow Survey Results/2016 Stack Overflow Survey Results/2016 Stack Overflow Survey Responses.CSV','ISO-8859-1')
data_2017 = hlpr.read_data('./developer_survey_2017/survey_results_public.CSV','ISO-8859-1')
data_2018 = hlpr.read_data('./developer_survey_2018/survey_results_public.CSV','ISO-8859-1')
data_2019 = hlpr.read_data('./developer_survey_2019/survey_results_public.CSV','ISO-8859-1')


# In[3]:


#A quick look at each dataset in terms of dimensions and columns
#2013 Survey results data set:
print(data_2013.columns)
data_2013.shape


# In[4]:


#2014 Survey results data set:
print(data_2014.columns)
data_2014.shape


# In[5]:


#2015 Survey results data set:
print(data_2015.columns)
data_2015.shape


# In[6]:


#2016 Survey results data set:
print(data_2016.columns)
data_2016.shape


# In[7]:


#2017 Survey results data set:
print(data_2017.columns)
data_2017.shape


# In[8]:


#2018 Survey results data set:
print(data_2018.columns)
data_2018.shape


# In[9]:


#2019 Survey results data set:
print(data_2019.columns)
data_2019.shape


# # Preparing the data
# ## 2013 dataset
# After checking the 2013 dataset, the structure is all wrong. It appears to have been some kind of a label then a few cells with checkboxes or something similar which results in incorrect headings and a messed up structure that needs repairing.
# Note that the first row is useless and each column represents a language or technology on it's own.

# In[10]:


#A closer look on the unprepared dataset of 2013 columns
cols_2013 = data_2013.columns.tolist()
print(cols_2013)

pl_2013 = data_2013[[
        'Which of the following languages or technologies have you used significantly in the past year?',
        'Unnamed: 57', 'Unnamed: 58', 'Unnamed: 59', 'Unnamed: 60', 
        'Unnamed: 61', 'Unnamed: 62', 'Unnamed: 63', 'Unnamed: 64', 
        'Unnamed: 65', 'Unnamed: 66', 'Unnamed: 67', 'Unnamed: 68', 
        'Unnamed: 69']]
pl_2013_want = data_2013[['Which technologies are you excited about?',
                          'Unnamed: 71',
                          'Unnamed: 72',
                          'Unnamed: 73',
                          'Unnamed: 74',
                          'Unnamed: 75',
                          'Unnamed: 76',
                          'Unnamed: 77',
                          'Unnamed: 78',
                          'Unnamed: 79',
                          'Unnamed: 80']]


# In[32]:


# Drop first row as it's useless
pl_2013 = pl_2013[1:]
pl_2013_want = pl_2013_want[1:]

#Rename every row to the language it represents
new_headers_2013 = hlpr.column_rename_firstvalue(pl_2013)
pl_2013.columns = new_headers_2013

#Get the count
pl_2013_counter = {}
pl_2013_counter.fromkeys(new_headers_2013)

for col in pl_2013:
    pl_2013_counter[col]=pl_2013[col].value_counts()[0]

df_2013 = pd.DataFrame(list(pl_2013_counter.items()),columns=['Programming Language','Users Count']).sort_values(by=['Users Count'],ascending=False)
df_2013.reset_index(drop=True,inplace=True)
display(df_2013)


# In[39]:


#Plot the data
hlpr.plot_barchart_dictionary(df_2013['Programming Language'], df_2013['Users Count'],
                              90,'Usage','Most used programming languages in 2013',10,10)


# ## 2014 dataset
# This one is exactly the same as the 2013 dataset in terms of structure and cleaning.

# In[46]:


#A closer look on the unprepared dataset of 2014 columns
cols_2014 = data_2014.columns.tolist()

pl_2014 = data_2014[[
        'Which of the following languages or technologies have you used significantly in the past year?',
        'Unnamed: 43','Unnamed: 44','Unnamed: 45','Unnamed: 46','Unnamed: 47',
        'Unnamed: 48','Unnamed: 49','Unnamed: 50','Unnamed: 51','Unnamed: 52',
        'Unnamed: 53',]]

pl_2014 = pl_2014[1:]

#Rename every row to the language it represents
new_headers_2014 = hlpr.column_rename_firstvalue(pl_2014)
pl_2014.columns = new_headers_2014

#Get the count
pl_2014_counter = {}
pl_2014_counter.fromkeys(new_headers_2014)

for col in pl_2014:
    pl_2014_counter[col]=pl_2014[col].value_counts()[0]

df_2014 = pd.DataFrame(list(pl_2014_counter.items()),columns=['Programming Language','Users Count']).sort_values(by=['Users Count'],ascending=False)
df_2014.reset_index(drop=True,inplace=True)
display(df_2014)
 
#Plot the data
hlpr.plot_barchart_dictionary(df_2014['Programming Language'], df_2014['Users Count'],
                              90,'Usage','Most used programming languages in 2014',10,10)


# ## 2015 dataset
# This time, the fist row in 2015 is useless so, a different type of preparation is required.

# In[14]:


#The case is different with the 2015 dataset, the first row is completely useless.
data_2015.columns = data_2015.iloc[0]

#Rename the headers
pl_2015 = data_2015[['Current Lang & Tech: Android', 'Current Lang & Tech: Arduino',
                     'Current Lang & Tech: AngularJS','Current Lang & Tech: C',
                     'Current Lang & Tech: C++','Current Lang & Tech: C++11',
                     'Current Lang & Tech: C#','Current Lang & Tech: Cassandra',
                     'Current Lang & Tech: CoffeeScript','Current Lang & Tech: Cordova',
                     'Current Lang & Tech: Clojure','Current Lang & Tech: Cloud',
                     'Current Lang & Tech: Dart','Current Lang & Tech: F#','Current Lang & Tech: Go',
                     'Current Lang & Tech: Hadoop','Current Lang & Tech: Haskell','Current Lang & Tech: iOS','Current Lang & Tech: Java',
                     'Current Lang & Tech: JavaScript',
                     'Current Lang & Tech: LAMP',
                     'Current Lang & Tech: Matlab',
                     'Current Lang & Tech: MongoDB',
                     'Current Lang & Tech: Node.js',
                     'Current Lang & Tech: Objective-C',
                     'Current Lang & Tech: Perl',
                     'Current Lang & Tech: PHP',
                     'Current Lang & Tech: Python',
                     'Current Lang & Tech: R',
                     'Current Lang & Tech: Redis',
                     'Current Lang & Tech: Ruby',
                     'Current Lang & Tech: Rust',
                     'Current Lang & Tech: Salesforce',
                     'Current Lang & Tech: Scala',
                     'Current Lang & Tech: Sharepoint',
                     'Current Lang & Tech: Spark',
                     'Current Lang & Tech: SQL',
                     'Current Lang & Tech: SQL Server',
                     'Current Lang & Tech: Swift',
                     'Current Lang & Tech: Visual Basic',
                     'Current Lang & Tech: Windows Phone',
                     'Current Lang & Tech: Wordpress',
                     'Current Lang & Tech: Write-In',]]
pl_2015 = pl_2015[1:]
new_headers_2015 = hlpr.column_rename_firstvalue(pl_2015)
pl_2015.columns = new_headers_2015


# In[33]:


#Get the count
pl_2015_counter = {}
pl_2015_counter.fromkeys(new_headers_2015)

for col in pl_2015:
    pl_2015_counter[col]=pl_2015[col].value_counts()[0]
    
df_2015 = pd.DataFrame(list(pl_2015_counter.items()),columns=['Programming Language','Users Count']).sort_values(by=['Users Count'],ascending=False)
df_2015.reset_index(drop=True,inplace=True)
display(df_2015)


# In[47]:


#Plot the data
hlpr.plot_barchart_dictionary(df_2015['Programming Language'], df_2015['Users Count'],
                              90,'Usage','Most used programming languages in 2015',10,10)


# ## 2016 dataset
# 2016 dataset is a much simpler one with little cleaning to do.

# In[34]:


pl_2016 = data_2016['tech_do']
#drop nan values as they are not needed.
pl_2016.dropna(inplace=True)

#Getting the count
pl_2016_counter = defaultdict(int)
for st in pl_2016:
    row = st.split(';')
    for subst in row:
        pl_2016_counter[subst]+=1

df_2016 = pd.DataFrame(list(pl_2016_counter.items()),columns=['Programming Language','Users Count']).sort_values(by=['Users Count'],ascending=False)
df_2016.reset_index(drop=True,inplace=True)
display(df_2016)


# In[48]:


#Plot the data
hlpr.plot_barchart_dictionary(df_2016['Programming Language'], df_2016['Users Count'],
                              90,'Usage','Most used programming languages in 2016',10,10)


# ## 2017 dataset
# Again, a simple one.

# In[35]:


#2017 dataset
pl_2017 = data_2017['HaveWorkedLanguage']
pl_2017.dropna(inplace=True)
pl_2017_counter = defaultdict(int)
for st in pl_2017:
    row = st.split(';')
    for subst in row:
        pl_2017_counter[subst]+=1

df_2017 = pd.DataFrame(list(pl_2017_counter.items()),columns=['Programming Language','Users Count']).sort_values(by=['Users Count'],ascending=False)
df_2017.reset_index(drop=True,inplace=True)
display(df_2017)


# In[49]:


#Plot the data
hlpr.plot_barchart_dictionary(df_2017['Programming Language'], df_2017['Users Count'],
                              90,'Usage','Most used programming languages in 2017',10,10)


# ## 2018 dataset
# from 2017 to 2019, the steps are almost the same.

# In[37]:


#2018 dataset
pl_2018 = data_2018['LanguageWorkedWith']
pl_2018.dropna(inplace=True)
pl_2018_counter = defaultdict(int)
for st in pl_2018:
    row = st.split(';')
    for subst in row:
        pl_2018_counter[subst]+=1
        
df_2018 = pd.DataFrame(list(pl_2018_counter.items()),columns=['Programming Language','Users Count']).sort_values(by=['Users Count'],ascending=False)
df_2018.reset_index(drop=True,inplace=True)
display(df_2018)


# In[50]:


#Plot the data
hlpr.plot_barchart_dictionary(df_2018['Programming Language'], df_2018['Users Count'],
                              90,'Usage','Most used programming languages in 2018',10,10)


# ## 2019 dataset
# 

# In[38]:


#2019 dataset
pl_2019 = data_2019['LanguageWorkedWith']
pl_2019.dropna(inplace=True)
pl_2019_counter = defaultdict(int)
for st in pl_2019:
    row = st.split(';')
    for subst in row:
        pl_2019_counter[subst]+=1
df_2019 = pd.DataFrame(list(pl_2019_counter.items()),columns=['Programming Language','Users Count']).sort_values(by=['Users Count'],ascending=False)
df_2019.reset_index(drop=True,inplace=True)
display(df_2019)


# In[51]:


#Plot the data
hlpr.plot_barchart_dictionary(df_2019['Programming Language'], df_2019['Users Count'],
                              90,'Usage','Most used programming languages in 2019',10,10)


# # Conclusion
# Clearly __JavaScript__ is the __\#1__ most used programming language over the years followed by SQL (We can honestly drop the HTML/CSS part) but notice that __Python__ is on the rise, getting higher and higher each year...is it because of the sudden Data Science and Machine Learning trend ?

# ## What do you think is the reason JavaScript and SQL are widely used like that ? and what languages do you expect to become more popular in the next few years ?

# In[ ]:




