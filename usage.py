import subprocess
import csv

data = {}

fileList = subprocess.Popen("ls data/UsageHistory", shell=True, stdout=subprocess.PIPE).stdout.read()
fileList = fileList.split("\n");
fileList = filter(lambda fl: fl != '' and fl.split(".")[-1] == "csv", fileList);

for fileName in fileList:
  with open("data/UsageHistory/" + fileName, "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    for row in reader:
      try:
        _accessCount = int(row[2].replace("\"", ""));
        _app = row[0].replace("\"", "");
        _timeElapsed = row[1].replace("\"", "");
        
        # App data object;
        _appData = {
          "accessCount": _accessCount,
          "timeElapsed": _timeElapsed
        };

        try:
          data[_app].append(_appData);
        except KeyError:
          data[_app] = [_appData];

      except IndexError:
        pass;
      except ValueError:
        pass;

for app in data:
  print(app);
  for i in data[app]:
    print i
