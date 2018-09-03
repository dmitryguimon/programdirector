from itertools import combinations
class ProgramDirector:
    def __init__(self, preferences):
        self.courses = preferences["courses"]
        self.terms = preferences["terms"]
        self.longest = []
    def info(self):
        print ("N courses: ",len(self.courses))
        print ("N terms: ",len(self.terms))
    def find_term(self, id):
        for i in range(len(self.terms)):
            term = self.terms[i]            
            if term["id"] == id:
                return i
        return -1
    def meet_prereqs(self, taken, test_course):
        if "prereqs" not in test_course:
            return 1
        taken_list = []
        for term,courses in taken:
            
            taken_list = taken_list + courses
            
        for prereq in test_course["prereqs"]:
            met = 0
            for course in taken_list:
                met = met or (course == prereq)
            if met == 0:
                return 0
        return 1
    def subtract_courses(self, a, b):
        c = []
        for x in a:
            if(x["id"] not in b):
                c.append(x)
        return c
       
    def test_schedule_rec(self, plan, need_to_take, offerings, n_terms_filled, terms_to_graduate, starting_term_i, max_n_courses_per_term):
        
        #for i in range(terms_to_graduate-n_terms_filled):
        #courses_taking = []
        #courses_taking_indecies = []
        if len(need_to_take) == 0:
            for t,c in plan:
                print(t,c)
            return 1
        term = self.terms[(starting_term_i + n_terms_filled) % len(self.terms)]
        print("\t"*n_terms_filled + term["id"])
        if term["id"] in offerings:
            courses_offered = offerings[term["id"]]
        else:
            courses_offered = []
        courses_fit = []
        for j in range(len(need_to_take)):
            need_course = need_to_take[j]                
            if (need_course["id"] in courses_offered) and (self.meet_prereqs(plan, need_course)):
                 courses_fit.append(need_course["id"])                    
        options = combinations(courses_fit, max_n_courses_per_term)
        
        feasible_new_plan = 0
        feasible_new_new_need_to_take = 0
        for c in options:
            list_c = list(c)
            plan_this_term = [(term, list_c)]               
            new_plan = plan + plan_this_term
            new_need_to_take = self.subtract_courses(need_to_take, list_c)
            #print("testing", int(len(new_plan)/len(self.terms)), new_plan[-1])
            if self.test_schedule_rec (new_plan, new_need_to_take , offerings, n_terms_filled +1, terms_to_graduate - 1, starting_term_i, max_n_courses_per_term):
                feasible_new_plan = new_plan
                feasible_new_need_to_take = new_need_to_take
                
                break
       
        if feasible_new_plan == 0:            
            return 0
        #if len(feasible_new_plan) > len(self.longest):
        #    self.longest = feasible_new_plan
        
        return 1

    def test_schedule(self, starting_term, offerings, max_n_courses_per_term, max_n_terms_to_graduate):
        plan = []
        print (starting_term)
        need_to_take = self.courses.copy()
        starting_term_i = self.find_term(starting_term)
        if starting_term_i == -1:
            raise ValueError('Starting term is invalid.') 

        return self.test_schedule_rec(plan, need_to_take, offerings, 0, max_n_terms_to_graduate, starting_term_i, max_n_courses_per_term)
    
    def test_schedule_open_enrollment(self, offerings, max_n_courses_per_term, max_n_terms_to_graduate):
        result = {}
        for term in self.terms:
            result[term["id"]] = self.test_schedule(term["id"], offerings, max_n_courses_per_term, max_n_terms_to_graduate)
        return result
                     
            
            
        
        
