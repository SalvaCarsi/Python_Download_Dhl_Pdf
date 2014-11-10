import glob
import os
from os.path import isfile

f = open("./shipment_orders.csv")

total_lines = 0
not_present = 0

for line in f:
  total_lines = total_lines + 1
  fileString = "./download/Status-of-shipment-"+line
  if not isfile(fileString.rstrip()):
    print line
    not_present = not_present + 1

print "Missing " + str(not_present) + " out of " + str(total_lines) + " total files"

f.close()
