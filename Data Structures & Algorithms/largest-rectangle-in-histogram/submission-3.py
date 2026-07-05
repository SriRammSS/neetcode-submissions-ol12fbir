class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if len(heights)-1==0:
            return heights[-1]

        
        left_wall=[0] * len(heights)
        right_wall=[len(heights)-1] * len(heights)

        stack=[]

        max_area=0

     

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:
                right_wall[stack[-1]]=i-1
                stack.pop()

            stack.append(i)

        stack=[]

        for i in range(len(heights)-1,-1,-1):

            while stack and heights[i] <= heights[stack[-1]]:
                left_wall[stack[-1]]=i
                stack.pop()

            stack.append(i)



        for i in range(len(heights)):


            width=right_wall[i]-left_wall[i]
            height=heights[i]


            max_area=max(height*width,max_area)
        
        return max_area

        




