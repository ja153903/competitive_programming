#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn count_triplets(arr: Vec<i32>) -> i32 {
        let mut prefix_xor = vec![0; arr.len()];

        for i in 0..arr.len() {
            if i == 0 {
                prefix_xor[i] = arr[i];
            } else {
                prefix_xor[i] = prefix_xor[i - 1] ^ arr[i];
            }
        }

        prefix_xor.insert(0, 0);

        let n = arr.len() + 1;
        let mut res = 0;

        for i in 0..n {
            for j in (i + 1)..n {
                if prefix_xor[i] == prefix_xor[j] {
                    res += (j as i32) - (i as i32) - 1;
                }
            }
        }

        res
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn should_pass_sample_case() {
        let arr = vec![2, 3, 1, 6, 7];
        assert_eq!(Solution::count_triplets(arr), 4);
    }

    #[test]
    pub fn should_pass_another_sample_case() {
        let arr = vec![1, 1, 1, 1, 1];
        assert_eq!(Solution::count_triplets(arr), 10);
    }
}
