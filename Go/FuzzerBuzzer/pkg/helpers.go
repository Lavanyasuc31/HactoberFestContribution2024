package pkg

import (
	"encoding/json"
	"fmt"
	"os"
)

// ReadFile reads a file and returns its content as a byte slice
func ReadFile(filePath string) ([]byte, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return nil, fmt.Errorf("failed to read file %s: %w", filePath, err)
	}
	return data, nil
}

// WriteFile writes data to a file
func WriteFile(filePath string, data []byte) error {
	err := os.WriteFile(filePath, data, 0644)
	if err != nil {
		return fmt.Errorf("failed to write file %s: %w", filePath, err)
	}
	return nil
}

// JSONPrettyPrint takes a JSON string and returns it in a pretty format
func JSONPrettyPrint(data []byte) (string, error) {
	var prettyJSON map[string]interface{}
	err := json.Unmarshal(data, &prettyJSON)
	if err != nil {
		return "", fmt.Errorf("failed to unmarshal JSON: %w", err)
	}

	pretty, err := json.MarshalIndent(prettyJSON, "", "    ")
	if err != nil {
		return "", fmt.Errorf("failed to marshal JSON: %w", err)
	}

	return string(pretty), nil
}

// FileExists checks if a file exists at the given path
func FileExists(filePath string) bool {
	_, err := os.Stat(filePath)
	return !os.IsNotExist(err)
}
