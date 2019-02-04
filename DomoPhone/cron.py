from django_cron import CronJobBase, Schedule
from modules.RFID.RFID import *



class Setup(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours
    ALLOW_PARALLEL_RUNS = True
    
    print ("setup")
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'DomoPhone.Setup'    # a unique code

    def do(self):
        pass    # do your thing here


class Loop(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours
    ALLOW_PARALLEL_RUNS = True

    print ("loop")
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'DomoPhone.Loop'    # a unique code

    while True:
        Read_uid()




    def do(self):
        pass    # do your thing here
