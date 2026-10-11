from datetime import datetime

sessions = []

def Start():
    todo=input("Enter an activity: ")
    name=input("Enter your name: ").strip().lower()
    time = datetime.now()
    activity = {
        "name" : name,
        "activity" : todo,
        "start_time": time,
        "end_time" : None
    }
    sessions.append(activity)
    if not name or not todo:
            print("Name or activity cannot be empty.")
    # print(sessions)
    for words in sessions:
        print(f"Name: {words['name']} | activity: {words['activity']} | start_time: {words['start_time']}")
# Start()


def Stop():
     name=input("Enter your name: ").strip().lower()
     for activities in sessions:
          if activities["name"] ==name and activities["end_time"] is None:
               activities["end_time"] = datetime.now()

               time_spent = activities["end_time"] - activities["start_time"] 
               activities["time_spent"] = time_spent
               print(time_spent)
               print(f"{name} you have spent {time_spent} at {activities["activity"]} ")
               return
# Stop()
     
def daily_activity():
     summary ={}
     for activities in sessions:
        print(activities)
        if activities["end_time"] is None:
               continue
          
        activity_did = activities["activity"]

        hours_spent = activities["time_spent"].total_seconds() /3600

        if activity_did not in summary:
            summary[activity_did]= 0

            summary[activity_did] += hours_spent
        print("----DAILY SUMMARY-----")
        print(f"You have spent a total of {hours_spent} on {activity_did}")
# daily_activity()


def main_menu():
     while True:
          print("This is a time tracking machine for all your activities")
          print("1: Enter your activities and start time: ")
          print("2: Enter your name to stop activity: ")
          print("3: View total on activity: ")
          print("4: To quit")

          chose_option =input("Select an option, from 1-4: ")
          if chose_option == "1":
               Start()
          elif chose_option == "2":
               Stop()
          elif chose_option == "3":
               daily_activity()
          elif chose_option == "4":
               break
          else:
            print("You have come to the end of your activity")
            break
main_menu()



