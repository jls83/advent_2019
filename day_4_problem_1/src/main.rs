fn get_number_length(n: i32) -> u32{
    let float_n = n as f32;
    let res = float_n.log10().floor() + 1.0;
    res as u32
}

fn get_digit_vec(n: i32) -> Vec<i32> {
    // Apparently `pow` requires a u32?
    let mut new_n = n;
    let mut n_length = get_number_length(new_n);

    let mut res = Vec::new();

    while n_length > 1 {
        let mult = i32::pow(10, n_length - 1);
        let first_digit = new_n / mult;
        res.push(first_digit);

        new_n = new_n - (first_digit * mult);
        n_length = n_length - 1;
    }
    res.push(new_n);
    res
}

fn combo_check(n: i32) -> bool {
    let digit_vec = get_digit_vec(n);
    let mut has_adjacent_digits = false;

    let mut cur_val = digit_vec[0];
    for val in digit_vec.iter().skip(1) {
        if *val < cur_val {
            return false;
        }
        else if *val == cur_val {
            has_adjacent_digits = true;
        }
        cur_val = *val;
    }
    has_adjacent_digits
}

fn checker(start: i32, end: i32) -> i32 {
    (start..end+1)
        .fold(0, |acc, cur| acc + (combo_check(cur)) as i32)
}

fn main() {
    let res = checker(284639, 748759);

    println!("{:?}", res);
}
