import subprocess
import operator
import csv

def toHours(duration):
  duration = duration.split(":");
  duration = duration[0] + "." + str(int(duration[1]) * 100 / 60);
  return float(duration);

apps = ["UnFollow","Psych!","VidMate","Steam","Feedback","Clash of Clans","WhatsApp","TubeMate","TTT","StorySaver","Follower Analyzer","LIKE","Messenger Lite","Udemy","Conversations Legacy","Voot","HaikuJAM","SonyLIV","WeChat","QuizUp","Followers - Unfollowers","Slack","WhatsApp Stickers","Unfollowers","Social","Gitter","Duo","ZEE5","StarMaker","hike","Skype Lite","2ndLine","Mail","Yellow pages","Docs","instabig repost big photo","Messaging","Google","Discord","Call management","Quora","Instagram","Prime Video","BookMyShow","Gmail","Helo","Bitmoji","Bitmoji","Hotstar","InCallUI","Phone","YourQuote","Snapchat","E-mail","Psiphon Pro","Messages","Amazon Shopping","Personal stickers for WhatsApp","qmiran","Phone service","YouTube","Unfollow Pro for Instagram","Fake Call","Messenger","Email","Facebook","Google+","WhatsApp Sticker","MediaSaver","Neutrino+","Contacts","Lite","TikTok","Pinterest","TED","ExpertOption","Diwali Stickers","Instant DP Downloader","Telegram","Twitter","Badoo","HashTags","LinkedIn","Netflix","DAWebmail","Medium","Tinder"]


data = [];

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
    totalTimeElapsed = 0;

    for row in reader:
      try:
        _accessCount = int(row[2].replace("\"", ""));
        _app = row[0].replace("\"", "");
        _timeElapsed = row[1].replace("\"", "");


        totalTimeElapsed += toHours(_timeElapsed);

        _userData = {
          "averageSocialMediaUsage": totalTimeElapsed / len(_datetime)
        }

      except IndexError:
        pass;
      except ValueError:
        pass;

    data.append(_userData);

index = 0;
userDataUsageHours = 0;
for userData in data:
  index += 1;
  userDataUsageHours += userData["averageSocialMediaUsage"];

print userDataUsageHours / index;
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
