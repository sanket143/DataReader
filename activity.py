import subprocess
import csv

data = {}
_dir = "data/ActivityHistory";

fileList = subprocess.Popen("ls " + _dir, shell=True, stdout=subprocess.PIPE).stdout.read()
fileList = fileList.split("\n");
fileList = filter(lambda fl: fl != '' and fl.split(".")[-1] == "csv", fileList);

for fileName in fileList:
  with open(_dir + "/" + fileName, "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    for row in reader:
      try:
        print(row);
      except IndexError:
        pass;
      except ValueError:
        pass;

  print("---------------------------------------------------------------------------------");

for app in data:
  print(app);
  for i in data[app]:
    print i
