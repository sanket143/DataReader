import subprocess
import csv

def addDuration(duration1, duration2):
  duration = [0, 0, 0];
  duration1 = duration1.split(":");
  duration2 = duration2.split(":");

  duration[0] = int(duration1[0]) + int(duration2[0]);
  duration[1] = int(duration1[1]) + int(duration2[1]);
  duration[2] = int(duration1[2]) + int(duration2[2]);

  duration[1] += int(duration[2] / 60);
  duration[2] = duration[2] % 60;
  duration[0] += int(duration[1] / 60);
  duration[1] = duration[1] % 60;

  for i in range(len(duration)):
    duration[i] = str(duration[i]);

  return ":".join(duration);

_dir = "data/ActivityHistory";

apps = ["UnFollow","Psych!","VidMate","Steam","Feedback","Clash of Clans","WhatsApp","TubeMate","TTT","StorySaver","Follower Analyzer","LIKE","Messenger Lite","Udemy","Conversations Legacy","Voot","HaikuJAM","SonyLIV","WeChat","QuizUp","Followers - Unfollowers","Slack","WhatsApp Stickers","Unfollowers","Social","Gitter","Duo","ZEE5","StarMaker","hike","Skype Lite","2ndLine","Mail","Yellow pages","Docs","instabig repost big photo","Messaging","Google","Discord","Call management","Quora","Instagram","Prime Video","BookMyShow","Gmail","Helo","Bitmoji","Bitmoji","Hotstar","InCallUI","Phone","YourQuote","Snapchat","E-mail","Psiphon Pro","Messages","Amazon Shopping","Personal stickers for WhatsApp","qmiran","Phone service","YouTube","Unfollow Pro for Instagram","Fake Call","Messenger","Email","Facebook","Google+","WhatsApp Sticker","MediaSaver","Neutrino+","Contacts","Lite","TikTok","Pinterest","TED","ExpertOption","Diwali Stickers","Instant DP Downloader","Telegram","Twitter","Badoo","HashTags","LinkedIn","Netflix","DAWebmail","Medium","Tinder"]

month = [
  10,
  11
]
dataWithDate = {};

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

            appHour = str(time[0]);
            time = [str(time[0]), time[1], time[2].split(" ")[0]];
            appTime = ":".join(time);

          except IndexError:
            time = appTime.split(":");
            time[0] = int(time[0]);

            time[0] = str(time[0]);

            appHour = time[0];
            appTime = ":".join(time);
            pass


          try:
            temp = dataWithDate; 
            duration = temp[appHour][appName]["duration"];
            temp[appHour][appName]["duration"] = addDuration(duration, appDuration);

            dataWithDate = temp;

          except KeyError:
            temp = {
              "duration": appDuration
            };

            try:
              dataWithDate[appHour];

            except KeyError:
              dataWithDate[appHour] = {}

            dataWithDate[appHour][appName] = temp;

      except IndexError:
        pass;
      except ValueError:
        pass;

  for time in dataWithDate:
    for app in dataWithDate[time]:
      print time + "," + app + "," + dataWithDate[time][app]["duration"];
