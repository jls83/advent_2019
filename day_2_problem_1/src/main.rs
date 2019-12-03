use std::fs;
use std::io::Error;

const INSTRUCTION_SIZE: usize = 4;

fn parse_file(filename: &str) -> Result<Vec<i32>, Error> {
    let contents = fs::read_to_string(filename)
        .unwrap()
        .split(",")
        .map(|i| i.trim()
             .parse::<i32>()
             .unwrap()
         )
        .collect();

    Ok(contents)
}

struct Instruction {
    op_code: i32,
    operator_left: usize,
    operator_right: usize,
    dest_addr: usize,
}

fn create_instruction(instruction_slice: &[i32]) -> Instruction {
    Instruction {
        op_code:        instruction_slice[0],
        operator_left:  instruction_slice[1] as usize,
        operator_right: instruction_slice[2] as usize,
        dest_addr:      instruction_slice[3] as usize,
    }
}

fn get_result(instruction: &Instruction, contents: &Vec<i32>) -> i32 {
    let value_left = contents[instruction.operator_left];
    let value_right = contents[instruction.operator_right];
    let op_code = instruction.op_code;

    match op_code {
        1 => value_left + value_right,
        2 => value_left * value_right,
        _ => 0,
    }
}

fn main() {
    let mut contents = parse_file("project_input.txt")
        .unwrap();

    // Do some pre-set up
    contents[1] = 12;
    contents[2] = 2;

    let mut offset = 0;

    loop {
        let instruction = create_instruction(&contents[offset..offset+4]);

        if instruction.op_code == 99 { break; }

        let new_value = get_result(&instruction, &contents);

        contents[instruction.dest_addr] = new_value;
        offset = offset + INSTRUCTION_SIZE;
    }
    println!("{:?}", contents[0]);
}

