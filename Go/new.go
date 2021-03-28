package main

import (
	"fmt"
)

type Student struct {
	name string
	age  int
}

func main() {
	//new 一个内建类型
	num := new(int)
	fmt.Println(*num)
	//new 一个自定义类型
	s := new(Student)
	s.name = "wangbm"
}
