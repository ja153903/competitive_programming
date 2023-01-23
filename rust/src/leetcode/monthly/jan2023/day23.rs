#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        let mut indegree: Vec<i32> = vec![0; n as usize];
        let mut outdegree: Vec<i32> = vec![0; n as usize];

        for t in trust.iter() {
            let a = t[0] as usize;
            let b = t[1] as usize;

            indegree[b - 1] += 1;
            outdegree[a - 1] += 1;
        }

        for (i, &indeg) in indegree.iter().enumerate() {
            if indeg == n - 1 && outdegree[i] == 0 {
                return i as i32 + 1;
            }
        }

        -1
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn should_pass_sample_case() {
        let n = 2;
        let trust = vec![vec![1, 2]];

        assert_eq!(Solution::find_judge(n, trust), 2);
    }

    #[test]
    pub fn should_pass_sample_case2() {
        let n = 3;
        let trust = vec![vec![1, 3], vec![2, 3]];

        assert_eq!(Solution::find_judge(n, trust), 3);
    }
}
