class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        courses = {}
        degree = {}
        for course in range(numCourses):
            courses[course] = []
            degree[course] = 0
        
        for prereq in prerequisites:
            courses[prereq[1]].append(prereq[0])
            degree[prereq[0]] += 1
        
        res = []
        queue = []
        for course in degree:
            if degree[course] == 0:
                queue.append(course)
        
        while queue:
            curr = queue.pop(0)
            res.append(curr)
            for neighbor in courses[curr]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
                
        if len(res) != numCourses:
            return []
        return res
                
                
            
        
        
        