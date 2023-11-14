class state:
    def __init__(self,current_state,work,charging_status):
        self.current_state=current_state
        self.work_state=work
        self.charging_status=charging_status
        
    def change_current_state(self,state):
        self.current_state=state
        
    def change_work_state(self,state):
        self.work_state=state
        
    def change_charging_status(self,state):
        self.charging_status=state


def at_charging_station():
    self.change_current_state("at_charging_station")
    while state.charging_status!="done"):
        if current_charge==100:
            state.change_charging_status("done")
    else:
        if work_status== done:
            go to next goal
        else:
            go to same goal
def main():
    state=state("at_charging_station","not_doing",lambda x:if x==100,"done" else,"charging")
    goals=[goal1,goal2,goal3]
    while state.charging_status!="done"):
        if current_charge==100:
            state.change_charging_status("done")
    else:
        go to goal1
        
    while True:
        if current_state==at_goal:
            if work_state=="done":
                drive_charge= (distance_to_goal+distance_charging_station_from_goal)/dist_per_charge
                if current_charge-(safe_charge+drive_charge)>40:
                    go to goal
                else:
                    go to charging station
                    at_charging_station
            else:
                while work_state!="done":
                    if color=="green":
                        state.change_work_state("done")
                    else:
                        if current_charge-(safe_charge+drive_charge)<=5:
                            go to charging station
                            at_charging_station()
                        else:
                            pass
                else:
                    if work_state=="done":
                    drive_charge= (distance_to_goal+distance_charging_station_from_goal)/dist_per_charge
                    if current_charge-(safe_charge+drive_charge)>40:
                        go to goal
                    else:
                        go to charging station
                        at_charging_station
                    elif work_status=="doing":
                        while work_status!="done":
                            if led=='green':
                                work_status="done"
                            else:
                                pass
                       else:
                           go to goal
                           
        
def __main__():
    main()