import random
class Job:
    def __init__(self,salary, education_requirements, work_requirements,low_raise,high_raise) -> None:
        self.salary=salary
        self.education_requirements=education_requirements
        self.work_experience=work_requirements
        self.years_since_raise=0
        self.lower_raise_bound=low_raise
        self.upper_raise_bound=high_raise
    def salary_upgrade(self):
        if self.years_since_raise>0:
            if random.random()>0.5:
                self.salary=self.salary+ self.years_since_raise*random.uniform(self.lower_raise_bound,
                                                                               self.upper_raise_bound)

def check_job_requirements(state, job):
    #check if state stuff passes requirements
    return True

def check_edu_requirements(state, edu):
    #check if state stuff passes requirements
    return True

def job_options(state, jobs):
    possible_jobs=[]
    for job in jobs:
        if check_job_requirements(state,job):
            possible_jobs.append(job)
    return possible_jobs

def education_options(state, education):
    possible_edu=[]
    for edu in education:
        if check_edu_requirements(state,education): 
            possible_edu.append(edu)
    return possible_edu

def actions(state, jobs, education):
    actions=job_options(state,jobs)+education_options(state,education)
    return actions