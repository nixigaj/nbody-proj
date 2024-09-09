package main

import (
	"encoding/binary"
	"fmt"
	"math"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run main.go <file_path>")
		return
	}

	filePath := os.Args[1]
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer file.Close()

	info, err := file.Stat()
	if err != nil {
		fmt.Printf("Error getting file stats: %v\n", err)
		return
	}

	fileSize := info.Size()
	if fileSize%48 != 0 {
		fmt.Printf("File size is not divisible by 48 bytes\n")
		return
	}

	var particles int = int(fileSize / 48)

	for i := 0; i < particles; i++ {
		offset := int64(i * 48)
		if _, err := file.Seek(offset, 0); err != nil {
			fmt.Printf("Error seeking file: %v\n", err)
			return
		}

		var data [6]float64
		for j := 0; j < 6; j++ {
			var buf [8]byte
			if _, err := file.Read(buf[:]); err != nil {
				fmt.Printf("Error reading file: %v\n", err)
				return
			}
			bits := binary.LittleEndian.Uint64(buf[:])
			data[j] = math.Float64frombits(bits)
		}

		fmt.Printf("particle %d position x: %f\n", i, data[0])
		fmt.Printf("particle %d position y: %f\n", i, data[1])
		fmt.Printf("particle %d mass: %f\n", i, data[2])
		fmt.Printf("particle %d velocity x: %f\n", i, data[3])
		fmt.Printf("particle %d velocity y: %f\n", i, data[4])
		fmt.Printf("particle %d brightness: %f\n", i, data[5])
	}
}
