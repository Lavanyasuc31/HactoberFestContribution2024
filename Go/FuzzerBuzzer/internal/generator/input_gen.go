package generator

import (
	"encoding/json"
	"math/rand"
)

// InputGenerator struct for generating various types of input
type InputGenerator struct {
	Seed int64
}

// NewInputGenerator creates a new InputGenerator with a specified seed
func NewInputGenerator(seed int64) *InputGenerator {
	rand.Seed(seed) // Seed the random number generator
	return &InputGenerator{Seed: seed}
}

// GenerateRandomString generates a random string of a specified length
func (ig *InputGenerator) GenerateRandomString(length int) string {
	letters := []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
	result := make([]rune, length)
	for i := range result {
		result[i] = letters[rand.Intn(len(letters))]
	}
	return string(result)
}

// GenerateRandomJSON generates random JSON input
func (ig *InputGenerator) GenerateRandomJSON() string {
	type RandomData struct {
		Name  string `json:"name"`
		Email string `json:"email"`
		Age   int    `json:"age"`
	}

	data := RandomData{
		Name:  ig.GenerateRandomString(10),
		Email: ig.GenerateRandomString(5) + "@example.com",
		Age:   rand.Intn(100),
	}

	// Convert to JSON
	jsonData, err := json.Marshal(data)
	if err != nil {
		return "{}" // Return empty JSON on error
	}
	return string(jsonData)
}
