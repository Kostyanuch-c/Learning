from sandbox.trening import TreeNode


class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        max_num, min_num = max(nums), min(nums)

        def can_choose(target: int) -> bool:
            count = 0
            i = 0
            l = len(nums)
            while i < l:
                if nums[i] <= target:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k

        while min_num < max_num:
            mid = (max_num + min_num) // 2
            if can_choose(target=mid):
                max_num = mid
            else:
                min_num = mid + 1

        return min_num


if __name__ == "__main__":
    arr = [7, 3, 9, 5]
    k = 2
    sol = Solution()
    print(sol.minCapability(nums=arr, k=k))
