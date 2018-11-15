import subprocess
import csv

_dir = "data/ActivityHistory";

apps = [
  "WhatsApp",
  "Instagram"
]

month = [
  10,
  11
]

fileList = subprocess.Popen("ls " + _dir, shell=True, stdout=subprocess.PIPE).stdout.read()
fileList = fileList.split("\n");
fileList = filter(lambda fl: fl != '' and fl.split(".")[-1] == "csv", fileList);

for fileName in fileList:
  with open(_dir + "/" + fileName, "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    for row in reader:
      format = 0;
      try:
        # Update row
        updatedRow = [];
        for item in row:
          updatedRow.append(item.replace("\"", ""));

        appName = updatedRow[0];
        appDate = updatedRow[1];
        appTime = updatedRow[2];
        appDuration = updatedRow[3];


        if appName in apps:

          if int(appDate.split("/")[1]) in month:
            format = 1

          if format == 0:
            appDate = appDate.split("/");
            temp = appDate[0];
            appDate[0] = appDate[1];
            appDate[1] = temp;

            appDate = "/".join(appDate);

          try:
            meridian = appTime.split(" ")[1];
            time = appTime.split(":");

            if meridian.lower() == "pm":
              if time[0] != "12":
                time[0] = int(time[0]) + 12;

            else:
              if time[0] == "12":
                time[0] = 0
            time = [str(time[0]), time[1], time[2].split(" ")[0]];
            appTime = ":".join(time);

          except IndexError:
            time = appTime.split(":");
            time[0] = int(time[0]);

            time[0] = str(time[0]);
            appTime = ":".join(time);
            pass

          print appDate, appTime, appDuration;

      except IndexError:
        pass;
      except ValueError:
        pass;

  print("---------------------------------------------------------------------------------");
