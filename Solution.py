from Match import Match
import pdb
class Solution:
    
    def __init__(self, m, n, hospital_list, student_list, hosp_open_slots):
        """
            The constructor exists only to initialize variables. You do not need to change it.
            :param m: The number of hospitals
            :param n: The number of students
            :param hospital_list: The preference list of hospitals, as a dictionary.
            :param student_list: The preference list of the students, as a dictionary.
            :param hosp_open_slots: Open slots of each hospital
            """
        self.m = m
        self.n = n
        self.hospital_list = hospital_list
        self.student_list = student_list
        self.hosp_open_slots = hosp_open_slots

    def list_checker(self):
        keep_checking = False
        for i in self.hosp_open_slots.values():
            if i > 0:
                keep_checking = True
        return keep_checking

    def get_matches(self):
        i = 1
        k = 0
        student_hosp_map = {}
        holder_array = []
        while self.list_checker() and i != len(self.hosp_open_slots) + 1:
            hosp_pref = self.hospital_list[i]
            student = hosp_pref[k]
            student_pref = self.student_list[student]
            if student not in student_hosp_map:
                #add the matching of student to hospital
                student_hosp_map[student] = i
                #holder_array.append(Match(i, student))
                #print(student_hosp_map)
                self.hosp_open_slots[i] -= 1
                k += 1
            else:
                #if the index of the new hospital is less that the index of the old
                if student_pref.index(i) < student_pref.index(student_hosp_map[student]):
                    self.hosp_open_slots[i] -= 1
                    self.hosp_open_slots[student_hosp_map[student]] += 1
                    #holder_array.remove(Match(student_hosp_map[student], student))
                    #holder_array.append(Match(i, student))
                    #print(student_hosp_map[student])
                    del student_hosp_map[student]
                    student_hosp_map[student] = i
                    #print(student_hosp_map[student])
                    #print(student_hosp_map)
                    i = 1
                    k = 0
                else:
                    k += 1
            #if k > len(self.student_list.keys()) - 1:
            if self.hosp_open_slots[i] == 0:
                i += 1
                k = 0
        #print(student_hosp_map)
        #print(holder_array)
        hold_me = []
        #print(self.hosp_open_slots)
        for student in student_hosp_map:
            hold_me.append(Match(student_hosp_map[student],student))
        #print(hold_me)
        return hold_me

