import random
class Job:
    def __init__(self,salary, education_requirements, work_requirements,low_raise,high_raise,years_in) -> None:
        self.salary=salary
        self.education_requirements=education_requirements
        self.work_experience=work_requirements
        self.years_since_raise=0
        self.lower_raise_bound=low_raise
        self.upper_raise_bound=high_raise
        self.years_in=years_in

    def salary_upgrade(self):
        if self.years_since_raise>0:
            if random.random()>0.5:
                self.salary=self.salary+ self.years_since_raise*random.uniform(self.lower_raise_bound,
                                                                               self.upper_raise_bound)
                
class Education:
    def __init__(self,general_ed,years_in,cost) -> None:
        self.general_ed=general_ed
        self.years_in=years_in
        self.cost=cost
#cost=0 years_in depends on user input        
general_ed=Education(True,0,0)
comp_sci=Education(False,0,100)
economics=Education(False,0,123)
literature=Education(False,0,1203)
math=Education(False,0,241)
edu_board=[general_ed,comp_sci,economics,literature,math]
#Job board would be the same sort of thing just defining everything


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