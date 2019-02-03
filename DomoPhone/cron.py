from django_cron import CronJobBase, Schedule
from modules.RFID.RFID import *

class Setup(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours
    print ("setup")
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'DomoPhone.Setup'    # a unique code

    def do(self):
        pass    # do your thing here


class Loop(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours
    print ("loop")
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'DomoPhone.Loop'    # a unique code

    while True:
        Read_uid()




    def do(self):
        pass    # do your thing here
