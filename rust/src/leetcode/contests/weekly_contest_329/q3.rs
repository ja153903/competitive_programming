#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn make_strings_equal(s: String, target: String) -> bool {
        s == target || (s.contains('1') && target.contains('1'))
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_sample_case() {
        let s = String::from("1010");
        let target = String::from("0110");

        assert!(Solution::make_strings_equal(s, target));
    }
}
