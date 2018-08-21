import datetime as datetime

from ScheduleSignOn.Schedule import ScheduleSignOn
from LoadCourses.Scraper import UQCourseScraper

# scraper = UQCourseScraper.deserialise("equine-2018")
# schedule = ScheduleSignOn(scraper.programs)
# schedule.schedule_signon(2018, 1, datetime.timedelta(minutes=10))
from UQCourses.Program import Program

# program = Program("https://my.uq.edu.au/programs-courses/program.html?acad_prog=2342")

import json
from LoadCourses.Encoder import CourseJSONEncoder
json_encoder = json.encoder.JSONEncoder(indent=4)
_json = json_encoder.encode
with open('full_ug_programs.html') as ug_html:
    with open('uq_programs.json', 'w') as programs_file:
        programs_file.write(_json(list(UQCourseScraper.get_programs(ug_html))))
    
    ug_html.seek(0)

    with open('uq_plans.json', 'w') as plans_file:
        plans_file.write(_json(list(UQCourseScraper.get_plans(ug_html))))
print(programs)
