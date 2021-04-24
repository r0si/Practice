package main

import (
	"fmt"
	"image"
	"log"
	"os"

	"github.com/RH12503/Triangula/algorithm"
	"github.com/RH12503/Triangula/algorithm/evaluator"
	"github.com/RH12503/Triangula/generator"
	imageData "github.com/RH12503/Triangula/image"
	"github.com/RH12503/Triangula/mutation"
	"github.com/RH12503/Triangula/normgeom"
)

func main() {
	file, err := os.Open("image.png")

	if err != nil {
		log.Fatal(err)
	}
	image, _, err := image.Decode()
	file.Close()
	if err != nil {
		log.Fatal(err)
	}
	img := imageData.ToData(image)

	pointFactory := func() normgeom.NormPointGroup {
		return (generator.RandomGenerator{}).Generate(200)
	}
	evaluatorFactory := func(n int) evaluator.Evaluator {
		return evaluator.NewParallel(img, 22, 5, n)
	}
	var mutator mutation.Method

	mutator = mutation.NewGaussianMethod(0.01, 0.3)
	algo := algorithm.NewSimple(pointFactory, 400, 5, evaluatorFactory, mutator)
	for {
		algo.Step()
		fmt.Println(algo.Stats().BestFitness)
	}
}
