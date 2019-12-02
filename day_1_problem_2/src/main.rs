use std::fs::File;
use std::io::{BufRead, BufReader, Error};

fn read(path: &str) -> Result<Vec<i32>, Error> {
    let v = BufReader::new(File::open(path)?)
        .lines()
        .map(|line| line.unwrap()
             .trim()
             .parse::<i32>()
             .unwrap()
        )
        .collect();

    Ok(v)
}

fn get_extra_fuel(fuel: i32) -> i32 {
    if fuel <= 0 {
        0
    }
    else {
        let next_val = (fuel / 3) - 2;
        fuel + get_extra_fuel(next_val)
    }
}

fn get_fuel_required_recur(module_mass: &i32) -> i32 {
    let initial_fuel = (module_mass / 3) - 2;
    let extra_fuel = get_extra_fuel(initial_fuel);
    extra_fuel
}

fn main() {
    let total: i32 = read("project_input.txt")
        .unwrap()
        .iter()
        .map(get_fuel_required_recur)
        .sum();

    println!("{:?}", total);
}

