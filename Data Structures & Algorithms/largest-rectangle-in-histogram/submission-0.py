class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left=[-1] * len(heights)
        stack=[]
        right=[len(heights)] * len(heights)
        max_area=0
        

        for i in range(len(heights)):

            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            if not stack:
                left[i]=-1
            else:
                left[i]=stack[-1]
            
            stack.append(i)
        stack=[]
        for i in range(len(heights)-1,-1,-1):

            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            if not stack:
                right[i]=len(heights)
            else:
                right[i]=stack[-1]
            
            stack.append(i)
   

        for i in range (len(heights)):
            width=right[i]-left[i]-1
            area=width*heights[i]
            max_area=max(max_area,area)
        return max_area
