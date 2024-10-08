package main

import (
	"log"
	"os"

	"github.com/Ayushi40804/Hacktoberfest2024/FuzzerBuzzer/internal/fuzz_logic"
	"github.com/Ayushi40804/Hacktoberfest2024/FuzzerBuzzer/internal/generator"
	"gopkg.in/yaml.v2"
)

type Config struct {
	TargetURL string `yaml:"target_url"`
	Seed      int64  `yaml:"seed"`
}

func main() {
	// Load the configuration
	config, err := loadConfig("config/config.yaml")
	if err != nil {
		log.Fatalf("Error reading config file: %v", err)
	}

	// Create an InputGenerator
	inputGen := generator.NewInputGenerator(config.Seed)

	// Create a Fuzzer
	fuzzer := fuzz_logic.NewFuzzer(config.TargetURL, inputGen)

	// Start the fuzzing process
	fuzzer.Start()
}

// loadConfig loads the configuration from a YAML file
func loadConfig(path string) (Config, error) {
	var config Config
	data, err := os.ReadFile(path)
	if err != nil {
		return config, err
	}
	err = yaml.Unmarshal(data, &config)
	return config, err
}
