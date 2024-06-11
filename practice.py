import pandas as pd

data={'Name': ['Jai', 'Princi', 'Gaurav', 
                 'Anuj', 'Ravi', 'Natasha', 'Riya'],
        'Age': [17, 17, 18, 17, 18, 17, 17],
        'Gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F'],
        'Marks': [90, 76, 'NaN', 74, 65, 'NaN', 71]}
df=pd.DataFrame(data)
print(df)

c = avg = 0
for x in df['Marks']:
	if str(x).isnumeric():
		c += 1
		avg += x
avg /= c

# Replace missing values
df = df.replace(to_replace="NaN",
				value=avg)

print(df)




d={'M':0,'F':1}
df['Gender']=df['Gender'].map(d)
print(df)


df=df[df['Marks']>=75].copy()
df.drop('Age',axis=1,inplace=True)
print(df)





details = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105, 
           106, 101, 108, 104, 110],
    'NAME': ['Jagroop', 'Praveen', 'Harjot', 
             'Pooja', 'Rahul', 'Nikita',
             'Saurabh', 'Ayush', 'Dolly', "Mohit"],
    'BRANCH': ['CSE', 'CSE', 'CSE', 'CSE', 'CSE', 
               'CSE', 'CSE', 'CSE', 'CSE', 'CSE']})

fees_status = pd.DataFrame(
    {'ID': [101, 102, 103, 104, 105, 
            106, 101, 108, 104, 110],
     'PENDING': ['5000', '250', 'NIL', 
                 '9000', '15000', 'NIL',
                 '4500', '1800', '250', 'NIL']})

df=pd.merge(details,fees_status,on='ID')



nd=df[~df.duplicated('ID')]

print(nd)