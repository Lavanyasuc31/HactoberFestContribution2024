package tests

import (
	"testing"

	"github.com/Ayushi40804/Hacktoberfest2024/FuzzerBuzzer/internal/fuzz_logic"
	"github.com/Ayushi40804/Hacktoberfest2024/FuzzerBuzzer/internal/generator"
)

func TestFuzzer_Start(t *testing.T) {
	// Create an InputGenerator instance
	ig := generator.NewInputGenerator(12345) // Using a fixed seed for reproducibility

	// Create a Fuzzer instance
	f := fuzz_logic.NewFuzzer("http://localhost:8080/test", ig)

	// Call the Start method to test it
	f.Start()

	// Here you can add more assertions to verify the expected behavior
}
