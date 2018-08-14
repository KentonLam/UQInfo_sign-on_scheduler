import json

from UQCourses.Course import Course
from UQCourses.Program import Program
from UQCourses.Semester import Semester


class CourseJSONEncoder(json.encoder.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Course, Program, Semester)):
            d = obj.__dict__.copy()
            d['__class__'] = obj.__class__.__name__
            return d
        elif isinstance(obj, set):
            return list(obj)
        else:
            return super().default(obj)

