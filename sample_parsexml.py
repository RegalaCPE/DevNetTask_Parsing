import xml.etree.ElementTree as et
path = r"/home/devasc/Documents/sample.xml"
tree = et.parse("sample.xml")
root = tree.getroot()

Job_Title= []

Company_Name =[]
Categories = []
City = [] 


for title in root.iter('job_title'):
    Job_Title.append(title.text)

for company in root.iter('company_name'):
    Company_Name.append(company.text)

for categories in root.iter('category'):
    Categories.append(title.text)

for city in root.iter('city'):
    City.append(title.text)

print("job title: ",Job_Title)
print("Company names: " ,Company_Name)
print("Categories: " ,Categories)
print("cities:" ,City)