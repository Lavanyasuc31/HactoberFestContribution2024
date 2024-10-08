# FuzzerBuzzer

FuzzerBuzzer is a fuzzing tool designed to test web applications by sending random inputs to specified endpoints. This tool can help identify vulnerabilities and unexpected behavior in applications.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Code Structure](#code-structure)

## Features

- Generate random strings and JSON data as input.
- Send fuzzed inputs to specified HTTP endpoints.
- Simple configuration via YAML file.

## Installation

To set up FuzzerBuzzer, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Ayushi40804/Hacktoberfest2024.git
   cd Hacktoberfest2024/FuzzerBuzzer
2. Ensure you have Go installed on your machine. If not, download and install it from https://golang.org.

3. Install necessary dependencies:

    ```bash
    go mod tidy
    ```
## Usage
1. Start your target web application on http://localhost:8080/test. You can do to app directory and run app.go file.
    
    ```bash
    go run app.go
    ```

2. Configure the fuzzer by editing the config/config.yaml file:
    
    ```yaml
    target_url: "http://localhost:8080/test"
    seed: 12345
    ```
3. Run the fuzzer:

    ```bash
    go run cmd/fuzzer.go
    ```
## Configuration
The configuration file config/config.yaml should include the following fields:

 - target_url: The URL to which the fuzzing requests will be sent.
 - seed: An integer seed value for random number generation to ensure reproducibility.

Example configuration:
    
```yaml
target_url: "http://localhost:8080/test"
seed:12345
```

## Testing
To run tests for the FuzzerBuzzer:

1. Navigate to the tests directory:
    
        ```bash
        cd tests
        ```
2. Execute the tests:

```bash
go test -v
```
## Code Structure
The project follows a modular structure:

```bash
FuzzerBuzzer/
├── cmd/
│   └── fuzzer.go              # Main entry point for the fuzzer
├── config/
│   └── config.yaml            # Configuration file
├── internal/
│   ├── fuzz_logic/
│   │   └── fuzz.go            # Fuzzing logic and HTTP requests
│   └── generator/
│       └── input_gen.go       # Input generation logic
├── pkg/
│   └── helpers.go             # Utility functions (if any)
├── tests/
│   └── fuzzer_test.go         # Test cases for the fuzzer
├── go.mod                      # Go module definition
└── README.md                   # Project documentation