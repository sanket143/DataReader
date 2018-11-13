import csv

reserved = [
  "Access count"
];

data = {
  "WhatsApp": [
    {
      _accessCount: 32,
      _timeElapsed: "10",
    },
  ]
}
with open("data/AUM_V4_Usage_2018-11-13_19-27-59.csv", "rb") as csvfile:
  reader = csv.reader(csvfile, delimiter=",", quotechar="|")
  data = {};
  for row in reader:
    try:
      if str(row[2]) not in reserved:
        _accessCount = int(row[2].replace("\"", ""));
        _app = row[0].replace("\"", "");
        _timeElapsed = row[1].replace("\"", "");
        
        print _app, _accessCount, _timeElapsed;
      else:
        print("Hello");

    except IndexError:
      pass;
    except ValueError:
      pass;
