CC = gcc
GO = go
CFLAGS = -O3
GOFLAGS =

BUILD_DIR = .
C_SRC = compare_gal_files/compare_gal_files.c
GO_SRC = human_print_gal/human_print_gal.go

all: cmp_gal print

# Build GAL file comparison program
cmp_gal: $(C_SRC)
	$(CC) $(CFLAGS) $(C_SRC) -o $(BUILD_DIR)/cmp_gal

# Build human print program for GAL files
print: $(GO_SRC)
	$(GO) build -o $(BUILD_DIR)/print $(GO_SRC)

clean:
	rm -f $(BUILD_DIR)/cmp_gal $(BUILD_DIR)/print

.PHONY: all cmp_gal print clean
