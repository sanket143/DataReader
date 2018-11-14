import subprocess
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

    print("----"); # Separator

    # Prints ontime on respective date
    for i in _datetime:
      print(i);

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
  totalTime = [0, 0, 0];
  print(app);
  for i in data[app]:
    time = i["timeElapsed"];
    time = time.split(":");
    try:
      totalTime[0] += int(time[0]);
      totalTime[1] += int(time[1]);
      totalTime[2] += int(time[2]);
    except:
      pass;

    print(i);

  totalTime[1] += int(totalTime[2] / 60);
  totalTime[2] = int(totalTime[2] % 60);
  totalTime[0] += int(totalTime[1] / 60);
  totalTime[1] = int(totalTime[1] % 60);

  totalTime = [str(x) for x in totalTime];
  print(":".join(totalTime));
