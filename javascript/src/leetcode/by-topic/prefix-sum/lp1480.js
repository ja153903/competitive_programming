/**
 * @param {number[]} nums
 * @return {number[]}
 */
const runningSum = function (nums) {
  const result = []

  for (let i = 0; i < nums.length; i++) {
    if (i === 0) {
      result.push(nums[i])
    } else {
      result.push(result.at(-1) + nums[i])
    }
  }

  return result
}

module.exports = { runningSum }
