class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = [(position[i], speed[i]) for i in range(len(position))]
        data = sorted(data, reverse=True)
        fleet = []

        for pos, speed in data:
            fleet.append((target - pos) / speed)
            if len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        return len(fleet)
        