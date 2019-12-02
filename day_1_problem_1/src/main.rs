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

fn get_fuel_required(module_mass: &i32) -> i32 {
    (module_mass / 3) - 2
}

fn main() {
    let total: i32 = read("project_input.txt")
        .unwrap()
        .iter()
        .map(get_fuel_required)
        .sum();

    println!("{:?}", total);
}

