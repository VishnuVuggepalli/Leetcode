class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def calc_gain(pass_students, total_students):
            return (pass_students + 1) / (total_students + 1) - pass_students/total_students
        
        max_heap = [( -calc_gain(pass_s, total_s) , pass_s, total_s) for pass_s, total_s in classes]
        heapq.heapify(max_heap)

        for _ in range(extraStudents):
            _, pass_s, total_s = heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-calc_gain(pass_s + 1,total_s + 1), pass_s+ 1, total_s+1))
        
        return sum(pass_s / total_s for _, pass_s, total_s in max_heap)/ len(max_heap)

        
        # Brute Force 
        # max_avg_PR =0
        # len_classes = len(classes)
        # pass_ratio = [0]*len_classes
        # for section in range(len(classes)):
        #     passed_students , total_students = classes[section][0] , classes[section][1]
        #     pass_ratio[section] = passed_students/ total_students
        # print("pass ratio : ", pass_ratio)
        # for section in range(len(classes)):
        #     extra_added = (classes[section][0] + extraStudents) / (classes[section][1] + extraStudents)
        #     avg_section_pr = (sum(pass_ratio[:section]) + sum(pass_ratio[section+1 :]) + extra_added)/ len_classes
        #     print(avg_section_pr)
        #     max_avg_PR = max(max_avg_PR,avg_section_pr)
        
        # return max_avg_PR