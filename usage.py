import subprocess
import operator
import csv

data = {}

fileList = subprocess.Popen("ls data/UsageHistory", shell=True, stdout=subprocess.PIPE).stdout.read()
fileList = fileList.split("\n");
fileList = filter(lambda fl: fl != '' and fl.split(".")[-1] == "csv", fileList);

for fileName in fileList:
  with open("data/UsageHistory/" + fileName, "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    reader = list(reader)[::-1]

    blanks = 0;
    push = False;
    _datetime = [];

    for row in reader:
      if push:
        _datetime.append(row);

      if row == ['""']:
        push = True;
        blanks += 1;

      if blanks == 2:
        break;

    # Delete useless data
    del _datetime[-1];
    del _datetime[-1];

    # Prints ontime on respective date
    # for i in _datetime:
    #   print(i);

    for row in reader:
      try:
        _accessCount = int(row[2].replace("\"", ""));
        _app = row[0].replace("\"", "");
        _timeElapsed = row[1].replace("\"", "");

        # App data object;
        _appData = {
          "accessCount": _accessCount,
          "averageAccessCount": float(_accessCount) / len(_datetime),
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

appAverageData = [];

for app in data:
  totalAccessCount = 0;
  for appData in data[app]:
    totalAccessCount += appData["averageAccessCount"];

  _tempAppData = {
    "App": app,
    "totalAverageAccessCount": totalAccessCount / len(data[app])
  }

  appAverageData.append(_tempAppData);

sortedAppAverageData = sorted(appAverageData, key=lambda k: k['totalAverageAccessCount']) 

for data in sortedAppAverageData:
  print data["App"] + "," + str(data["totalAverageAccessCount"]);

"""
for app in data:
  totalTime = [0, 0, 0];
  totalAccessCount = 0;
  info = {};

  for i in data[app]:
    time = i["timeElapsed"];
    time = time.split(":");

    try:
      info[i["timeElapsed"]] += i["accessCount"];
    except:
      info[i["timeElapsed"]] = i["accessCount"];

    try:
      totalTime[0] += int(time[0]);
      totalTime[1] += int(time[1]);
      totalTime[2] += int(time[2]);

      totalAccessCount += i["accessCount"];
    except:
      pass;


  totalTime[1] += int(totalTime[2] / 60);
  totalTime[2] = int(totalTime[2] % 60);
  totalTime[0] += int(totalTime[1] / 60);
  totalTime[1] = int(totalTime[1] % 60);

  totalTime = [str(x) for x in totalTime];
  print totalAccessCount, app, ":".join(totalTime);
  for time in info:
    print time, info[time];
"""
