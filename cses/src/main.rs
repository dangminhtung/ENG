use std::io::{self, stdin};

fn main() {
    let mut a = String::new();
    io::stdin().read_line(&mut a).expect("Failed to read line");

    let mut number: i64 = a.trim().parse().expect("not a number");
    print!("{} ", number);
    while number != 1 {
        if number % 2 == 0 {
            print!("{} ", number / 2);
            number = number / 2;
        } else {
            print!("{} ", number * 3 + 1);
            number = number * 3 + 1;
        }
    }
}
