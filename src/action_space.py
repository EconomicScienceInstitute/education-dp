import random
class Job:
    def __init__(self,salary, edu_level_req, edu_type_req, work_experience_req,low_raise,high_raise,years_in) -> None:
        self.salary=salary
        self.edu_level_req=edu_level_req
        self.education_type_req=edu_type_req
        self.work_experience_req=work_experience_req
        self.years_since_raise=0
        self.lower_raise_bound=low_raise
        self.upper_raise_bound=high_raise
        self.years_in=years_in

    def salary_upgrade(self):
        if self.years_since_raise>0:
            if random.random()>0.5:
                self.salary=self.salary+ self.years_since_raise*random.uniform(self.lower_raise_bound,
                                                                               self.upper_raise_bound)
    def __str__(self):
        return f"Job(salary={self.salary}, edu_level_req={self.edu_level_req}, education_type_req={self.education_type_req}, work_experience_req={self.work_experience_req}, raise_range=({self.lower_raise_bound}-{self.upper_raise_bound})), years_in={self.years_in}"
                
class Education:
    def __init__(self, edu_degree, edu_field, years_in, years_for_degree, cost, edu_level_req, edu_type_req) -> None:        
        self.edu_degree=edu_degree
        self.edu_field=edu_field
        self.years_in=years_in
        self.years_for_degree=years_for_degree
        self.cost=cost
        self.edu_level_req=edu_level_req
        self.edu_type_req=edu_type_req
    def __str__(self):
        return f"Job(edu_field={self.edu_field}, edu_degree='{self.edu_degree}', years_in={self.years_in}, years_for_degree={self.years_for_degree}, cost={self.cost}"
    
#cost=0 for general eds years_in depends on user input        
general_ed=Education("High_School","General_Ed", 10,12,0,None,None)
bachelors_math=Education("Bacherlors","Math", 0,4,10000,"High_School","General_Ed")
masters_math=Education("Masters","Math", 0,2,10000,"Bachelors","Math")
education_board=[general_ed,bachelors_math,masters_math]
#Job board would be the same sort of thing just defining everything


def check_job_requirements(state, job):
    #check if state stuff passes requirements
    if state.years_of_experience<job.work_experience_required:
        return False
    field=job.edu_type_req
    degree=job.edu_level_req
    if field and degree is None:
        return True
    for education in state.education:
        if education.edu_degree==degree and education.edu_field==field:
            return True
    return False
    

def check_edu_requirements(state, edu):
    #check if state stuff passes requirements
    if edu.edu_requirement is None:
        return True
    degree=edu.edu_level_req
    field=edu.edu_type_req
    for education in state.education:
        if education.edu_degree==degree and education.edu_field==field:
            return True
    return False

def job_options(state, jobs):
    possible_jobs=[]
    for job in jobs:
        if check_job_requirements(state,job):
            possible_jobs.append(job)
    return possible_jobs

def education_options(state, educations):
    possible_edu=[]
    for edu in educations:
        if check_edu_requirements(state,edu): 
            possible_edu.append(edu)
    return possible_edu

def actions(state, jobs, education):
    action_set=[]
    action_set=job_options(state,jobs)+education_options(state,education)
    return action_set