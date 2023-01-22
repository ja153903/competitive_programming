#![allow(dead_code)]

struct Solution;

impl Solution {
    pub fn alternate_digit_sum(n: i32) -> i32 {
        let mut res = 0;
        let as_str = n.to_string();

        for (i, ch) in as_str.char_indices() {
            if i % 2 == 0 {
                res += ch.to_digit(10).unwrap() as i32;
            } else {
                res -= ch.to_digit(10).unwrap() as i32;
            }
        }

        res
    }
}
