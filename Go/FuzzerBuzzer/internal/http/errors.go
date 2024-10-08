package http

import (
	"fmt"
	"net/http"
)

// HTTPError represents an error that occurred during an HTTP request
type HTTPError struct {
	StatusCode int
	Message    string
}

// Error implements the error interface for HTTPError
func (e *HTTPError) Error() string {
	return fmt.Sprintf("HTTP %d: %s", e.StatusCode, e.Message)
}

// NewHTTPError creates a new instance of HTTPError
func NewHTTPError(statusCode int, message string) *HTTPError {
	return &HTTPError{
		StatusCode: statusCode,
		Message:    message,
	}
}

// CheckResponse checks the HTTP response and returns an error if the status code indicates failure
func CheckResponse(resp *http.Response) error {
	if resp.StatusCode < 200 || resp.StatusCode >= 300 {
		return NewHTTPError(resp.StatusCode, http.StatusText(resp.StatusCode))
	}
	return nil
}
