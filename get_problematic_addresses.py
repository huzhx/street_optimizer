import sys, getopt
import csv
from opt_strategy_1 import OptimizationStrategy1
from address import Address

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print("get_problematic_addresses.py -i <inputfile> -o <outputfile>")
      sys.exit(2)
   for opt, arg in opts:
      if opt == "-h":
         print("get_problematic_addresses.py -i <inputfile> -o <outputfile>")
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print("Input file is ", inputfile)
   print("Output file is ", outputfile)
   
   os1 = OptimizationStrategy1()
   problematic_addresses = []
   fields = []
   with open(inputfile) as csvfile:
       csvreader = csv.reader(csvfile, delimiter=',')
       fileds = next(csvreader)
       for row in csvreader:
           address = Address(row[0], row[1], row[2], row[3], row[4])
           if (os1.missing_street_apt_term(address)):
               problematic_addresses.append(row)
    
   with open(outputfile, 'w') as csvfile:
       csvwriter = csv.writer(csvfile)
       csvwriter.writerow(fileds)
       csvwriter.writerows(problematic_addresses)

if __name__ == "__main__":
   main(sys.argv[1:])
