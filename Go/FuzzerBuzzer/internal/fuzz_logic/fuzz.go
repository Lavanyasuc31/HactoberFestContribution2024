package fuzz_logic

import (
	"fmt"
	"net/http"

	"github.com/Ayushi40804/Hacktoberfest2024/FuzzerBuzzer/internal/generator"
)

// Fuzzer struct represents the fuzzer with necessary fields
type Fuzzer struct {
	TargetURL string
	Generator *generator.InputGenerator
}

// NewFuzzer creates a new Fuzzer instance
func NewFuzzer(targetURL string, generator *generator.InputGenerator) *Fuzzer {
	return &Fuzzer{
		TargetURL: targetURL,
		Generator: generator,
	}
}

// Start method to begin fuzzing process
func (f *Fuzzer) Start() {
	// Generate random input
	randomInput := f.Generator.GenerateRandomString(10)
	fmt.Println("Generated input:", randomInput)

	// Send a POST request
	resp, err := http.Post(f.TargetURL+"?input="+randomInput, "application/json", nil)
	if err != nil {
		fmt.Println("Error sending request:", err)
		return
	}
	defer resp.Body.Close()

	fmt.Println("Response Status:", resp.Status)
}
