class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
         pair = [(pos, spe) for pos, spe in zip(position, speed)]
         pair.sort(reverse=True)
         stack = []

         for car in pair:
            time = (target - car[0]) / car[1]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)

         return len(stack)
        
