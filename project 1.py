import csv
with open(r"C:\Users\jenij\Downloads\Bestseller - Sheet1.csv",'r',encoding='utf-8') as fh:
  csvreader=csv.reader(fh)
  next(csvreader) # Skip header row
  maxval=float('-inf')
  j=None
  for i in csvreader:
    if float(i[4])>maxval:  # Convert string to float for comparison
      maxval=float(i[4]) # Update maxval
      book=i[0]
  j=('The book with highest sales is :',book)
  print(j)

if j:
  with open('bestseller_info.csv','w',newline='',encoding='utf-8') as mh:
    psv=csv.writer(mh)
    psv.writerow(j)
  