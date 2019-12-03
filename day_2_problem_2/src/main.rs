use std::fs;
use std::io::{Error, stdin};

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

#[derive(Debug)]
struct Instruction {
    location: usize,
    op_code: i32,
    operator_left: usize,
    operator_right: usize,
    dest_addr: usize,
}

fn create_instruction(instruction_location: usize, instruction_slice: &[i32]) -> Instruction {
    Instruction {
        location:       instruction_location,
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
    contents[1] = 10;
    contents[2] = 3;

    let mut offset = 0;

    loop {
        let instruction = create_instruction(
            offset,
            &contents[offset..offset+4]
        );

        println!("{:?}", instruction);
        if instruction.op_code == 99 {
            break;
        }

        let new_value = get_result(&instruction, &contents);
        contents[instruction.dest_addr] = new_value;
        println!(
            "Contents of {}: {:?}",
            instruction.dest_addr,
            new_value
        );
        // let mut foo = String::new();
        // stdin().read_line(&mut foo);
        // println!("");

        offset = offset + INSTRUCTION_SIZE;
    }
}

