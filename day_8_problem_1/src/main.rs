const LAYER_WIDTH: usize = 25;
const LAYER_HEIGHT: usize = 6;

fn split_into_layers() {

}

fn main() {
    let bar: Vec<Vec<i32>> = (0..50)
        .collect::<Vec<i32>>()
        .chunks(10)
        .map(|x| x.to_vec())
        .collect();

    println!("{:?}", bar);
}
