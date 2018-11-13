import csv

reserved = [
  "Access count"
];

data = {
  "WhatsApp": [
    {
      "accessCount": 32,
      "timeElapsed": "10",
    },
  ]
}

with open("data/AUM_V4_Usage_2018-11-13_19-27-59.csv", "rb") as csvfile:
  reader = csv.reader(csvfile, delimiter=",", quotechar="|")
  for row in reader:
    try:
      if str(row[2]) not in reserved:
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

      else:
        print("Hello");

    except IndexError:
      pass;
    except ValueError:
      pass;

for app in data:
  print app, data[app]
