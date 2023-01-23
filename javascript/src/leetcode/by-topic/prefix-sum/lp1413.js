/**
 * @param {number[]} nums
 * @return {number}
 */
const minStartValue = function (nums) {
  let minValue = Number.MAX_VALUE
  let rs = 0

  for (let i = 0; i < nums.length; i++) {
    rs += nums[i]
    minValue = Math.min(minValue, rs)
  }

  return minValue < 0 ? Math.abs(minValue) + 1 : 1
}

module.exports = { minStartValue }
