# Stepper-Motor Driven Slit
This program implements controls for a slit in the MHz system oscillator that's driven by a stepper motor.

You can set the position of the slit in either steps of the stepper motor or in nanometers. The default is in steps.
```
$ slit move 220785
$ slit move -w 810
```

You can also report the current position either once or in a continuous loop with the `-l` flag (useful for calibration).
```
$ slit pos
242787
$ slit pos -l
242787
242787
242787
242787
...
```

## Installation
The binary wheel is built using `poetry` inside the project directory. 
```
$ poetry build
```

This builds a program called `slit`, rather than `zaber_slit`, for the sake of convenience. The binary will be installed in the new `dist` directory.

Install the wheel using `pip`:
```
$ python -m pip install dist/zaber_slit-<some stuff>.whl
```

Now you can call the program from any directory:
```
$ cd ~
$ slit move -w 825
```

## License

Licensed under either of

 * Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally
submitted for inclusion in the work by you, as defined in the Apache-2.0
license, shall be dual licensed as above, without any additional terms or
conditions.