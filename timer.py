import datetime as DT
import os

duration = input('Duration(H:MM): //hours should be less than 10\n')
start = input("Start now (Y/N)? ")
if start == 'Y':
	starttime = DT.datetime.now()
	endtime = starttime + DT.timedelta(hours = int(duration[0:1]), minutes=int(duration[2:4]))
	timelapse = DT.datetime.strptime(str(duration), "%H:%M")
	printedtime = DT.datetime.strftime(starttime, "%H:%M")
	print("Start now: " + DT.datetime.strftime(starttime, "%H:%M"))
	while (DT.datetime.strftime(DT.datetime.now(), "%H:%M") != DT.datetime.strftime(endtime, "%H:%M")):
		now = DT.datetime.strftime(DT.datetime.now(), "%H:%M")
		if(now != printedtime):
			if(now == DT.datetime.strftime(DT.datetime.strptime(printedtime, "%H:%M") + DT.timedelta(minutes=15), "%H:%M")):
				timelapse += DT.timedelta(minutes=-15)
				print("=======================================")
				print(("Now: {0}").format(now))
				print(("Timelapse: {0}").format(DT.datetime.strftime(timelapse, "%H:%M")))
				print("=======================================")
				printedtime = DT.datetime.strftime(DT.datetime.now(), "%H:%M")
	if(DT.datetime.strftime(DT.datetime.now(), "%H:%M") == DT.datetime.strftime(endtime, "%H:%M")):
		os.system("say 'Time is up and put down your pen'")
