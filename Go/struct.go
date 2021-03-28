package main

import "fmt"

type Profile struct {
	name   string
	age    int
	gender string
	mother *Profile
	father *Profile
}

func (person Profile) FmtProfile() {
	fmt.Printf("名字: %s\n", person.name)
	fmt.Printf("年龄: %d\n", person.age)
	fmt.Printf("性别: %s\n", person.gender)
}
func main() {
	myself := Profile{name: "小明", age: 24, gender: "male"}
	myself.FmtProfile()

}
