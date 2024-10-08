package http

import (
	"fmt"
	"io"
	"net/http"
)

// Client struct that wraps the http.Client and any custom configurations
type Client struct {
	HTTPClient *http.Client
	Headers    map[string]string
}

// NewClient creates a new HTTP client with custom headers

func NewClient(headers map[string]string) *http.Client {

	client := &http.Client{}

	// You can add custom headers handling logic here if needed

	return client

}

// Post sends a POST request to the specified URL with the provided data
func (c *Client) Post(url string, contentType string, body io.Reader) (*http.Response, error) {
	// Create a new request
	req, err := http.NewRequest("POST", url, body)
	if err != nil {
		return nil, fmt.Errorf("failed to create request: %w", err)
	}

	// Add custom headers to the request
	for key, value := range c.Headers {
		req.Header.Set(key, value)
	}

	// Send the request
	resp, err := c.HTTPClient.Do(req)
	if err != nil {
		return nil, fmt.Errorf("failed to send request: %w", err)
	}

	return resp, nil
}
