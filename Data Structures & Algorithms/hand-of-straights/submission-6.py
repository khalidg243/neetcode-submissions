class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num] > 0:
                for i in range(1, groupSize):
                    if num + i not in count or count[num] == 0:
                        return False
                    count[num + i] -= 1
            count[num] -= 1
        return True