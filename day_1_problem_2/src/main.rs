use std::fs::File;
use std::io::{BufRead, BufReader, Error, ErrorKind};

fn read(path: &str) -> Result<Vec<i32>, Error> {
    let file = File::open(path)?;
    let br = BufReader::new(file);

    let mut v = Vec::new();
    for line in br.lines() {
        let line = line?;
        let n = line
            .trim()
            .parse::<i32>()
            .map_err(|e| Error::new(ErrorKind::InvalidData, e))?;
        v.push(n);
    }
    Ok(v)
}

fn ugh(fuel: i32) -> i32 {
    let mut res = 0;
    if fuel > 0 {
        let next_val = (fuel / 3) - 2;
        res = fuel + ugh(next_val);
    }
    res
}


fn get_fuel_required_recur(module_mass: &i32) -> i32 {
    let initial_fuel = (module_mass / 3) - 2;
    let extra_fuel = ugh(initial_fuel);
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

