package main

import (
	"fmt"
)

var arr0 [5]int = [5]int{1, 2, 3}
var arr1 = [5]int{1, 2, 3, 4, 5}
var arr2 = [...]int{1, 2, 3, 4, 5, 6}
var str = [5]string{3: "hello world", 4: "tom"}

func main() {
	a := [3]int{1, 2}
	b := [...]int{1, 2, 3, 4}
	c := [5]int{2: 100, 4: 200}
	d := [...]struct {
		name string
		age  uint8
	}{
		{"user1", 10},
		{"user2", 20},
	}
	fmt.Println(arr0, arr1, arr2, str)
	fmt.Println(a, b, c, d)
}
