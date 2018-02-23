import csv
text_file = "/home/joelrj/unicode.txt"
csv_file = "/home/joelrj/unicode.csv"
in_txt = csv.reader(open(text_file, "rb"), delimiter = "-")
out_csv = csv.writer(open(csv_file, "wb"))
out_csv.writerows(in_txt)
print "done"
