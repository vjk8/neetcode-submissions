class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        count = 0
        visited = [False for _ in range(len(people))]

        left = 0
        right = len(people)-1

        while left < right:
            first = people[left]
            second = people[right]

            if first + second <= limit:
                count += 1
                visited[left] = True
                visited[right] = True
                left += 1
                right -= 1
            elif first + second > limit:
                right -= 1
        
        for v in visited:
            if v == False:
                count += 1
        
        return count

        