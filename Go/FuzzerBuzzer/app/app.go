package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/test", testHandler)
	fmt.Println("Server starting on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("Server error:", err)
	}
}

func testHandler(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()
	input := r.FormValue("input")

	// Simple response based on input
	if input == "" {
		http.Error(w, "No input provided", http.StatusBadRequest)
		return
	}

	response := fmt.Sprintf("Received input: %s", input)
	w.Write([]byte(response))
}
