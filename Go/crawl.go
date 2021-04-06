package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"regexp"
)

var (
	reQQEmail = `(\d+)@qq.com`
)

func GetEmail() {
	resp, err := http.Get("https://tieba.baidu.com/p/6051076813?red_tag=1573533731")
	HandleError(err, "http.Get url")
	defer resp.Body.Close()
	pageBytes, err := ioutil.ReadAll(resp.Body)
	HandleError(err, "ioutil.ReadAll")
	pageStr := string(pageBytes)
	re := regexp.MustCompile(reQQEmail)
	results := re.FindAllStringSubmatch(pageStr, -1)

	for _, result := range results {
		fmt.Println("email:", result[0])
		fmt.Println("qq:", result[1])
	}
}
func HandleError(err error, why string) {
	if err != nil {
		fmt.Println(why, err)
	}
}
func main() {
	GetEmail()
}
