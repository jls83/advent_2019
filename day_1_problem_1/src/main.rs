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

fn get_fuel_required(module_mass: &i32) -> i32 {
    (module_mass / 3) - 2
}

fn main() {
    let result_vec = read("project_input.txt").unwrap();
    let foo: Vec<i32> = result_vec.iter().map(get_fuel_required).collect();
    let total: i32 = foo.iter().sum();

    println!("{:?}", total);
}

