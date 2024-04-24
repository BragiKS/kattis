use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let reader = stdin.lock();

    for line in reader.lines() {
        let line = line.expect("Failed to read line");

        // Split the line into numbers and collect them into a Vec<u64>
        let numbers: Vec<u64> = line
            .split_whitespace()
            .map(|n| n.parse::<u64>().expect("Expected a number"))
            .collect();

        // Check if we have exactly two numbers
        if numbers.len() == 2 {
            let diff = numbers[0].abs_diff(numbers[1]);
            println!("{}", diff);
        } else {
            eprintln!("Warning: Expected exactly 2 numbers per line, found {}", numbers.len());
        }
    }

    Ok(())
}
