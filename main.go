package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseFile(filename string) ([][]int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var pairs [][]int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		pair, err := parseLine(line)
		if err != nil {
			return nil, err
		}
		pairs = append(pairs, pair)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return pairs, nil
}

func parseLine(line string) ([]int, error) {
	fields := strings.Fields(line)
	var pair []int

	for _, field := range fields {
		num, err := strconv.Atoi(field)
		if err != nil {
			return nil, err
		}
		pair = append(pair, num)
	}

	return pair, nil
}

func main() {
	filename := "pairs.txt" // Replace with the actual filename
	pairs, err := parseFile(filename)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Println("Parsed pairs:")
	for _, pair := range pairs {
		fmt.Printf("%d %d\n", pair[0], pair[1])
	}
}
