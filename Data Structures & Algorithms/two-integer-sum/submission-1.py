class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we always have nums >=2 and <= 1000 len
        # do we always have target ? yes, we have
        # can we have target and nums negative? - yes

        # APPROACH 1:
        # I keep dictionary of my reminders and indexes that I have for this reminder
        # [3,4,5,6] and 7
        # 7 - 3 = 4: 0
        # 4 -
        reminder_dict = dict()
        for i in range(len(nums)):
            if nums[i] in reminder_dict:
                return [reminder_dict[nums[i]], i]
            else:
                reminder = target - nums[i]
                reminder_dict[reminder] = i
            # reminder = target - nums[i]
            # if reminder in reminder_dict:
            #     return [reminder_dict[reminder], i]
            # elif:
            #     reminder_dict[reminder] = i