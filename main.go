package main

import (
    "fmt"
    "strings"
    "time"
	"math/rand"
)

type machine struct {
	id int
	load int
}


func main() {
    // Example slice of machine structs
    machines1 := []*machine{}
    machines2 := []*machine{}
	i := 0
	for i < 20 {
		machines1 = append(machines1,&machine{id:i,load:0})
        machines2 = append(machines2,&machine{id:i,load:0})
		i+=1
	}
    // Print the initial state of machines
    printMachines(machines1, machines2)

    // Loop to dynamically change and display the machines' load
    for i := 0; i < 5000; i++ {
        // Update the load of each machine (for demonstration, increment each load)
		// minimum := electMachineTwoRandom(machines)
        minimum := electMachineRandom(machines1)
		currentLoad := minimum.load
		newLoad := rand.Intn(4)
		machines1[minimum.id] = &machine{id:minimum.id,load:currentLoad+newLoad}

        minimum = electMachineTwoRandom(machines2)
        currentLoad = minimum.load
        machines2[minimum.id] = &machine{id:minimum.id,load:currentLoad+newLoad}

		printMachines(machines1, machines2)
        time.Sleep(10 * time.Millisecond)
    }
}

func electMachineRandom(machines []*machine) machine {
    rand.Seed(time.Now().UnixNano())
    r := rand.Intn(20)
    return *machines[r]
}

func electMachineTwoRandom(machines []*machine) machine {
    rand.Seed(time.Now().UnixNano())
    r1,r2 := rand.Intn(20), rand.Intn(20)
	minimum := minLoad(*machines[r1],*machines[r2])
    return minimum
}

// Function to print the machines' load
// Function to generate the load values as a string
func generateLoadString(machines []machine) string {
    var loads []string
    for _, m := range machines {
        loads = append(loads, fmt.Sprintf("Machine %d: %d", m.id, m.load))
    }
    return strings.Join(loads, ", ")
}
// Function to print the machines' load
func printMachines(machines1 []*machine, machines2 []*machine) {
    // Get the maximum width of machine ID for formatting
    maxWidth := getMaxIDWidth(machines1)

    // Print each machine's load
    for index, m := range machines1 {
        fmt.Printf("Machine %-*d: 1st technique %d 2nd technique %d\n", maxWidth, m.id, m.load, machines2[index].load)
    }
    // Clear the previous output if the number of machines has increased
    clearPreviousOutput(len(machines1))
}

// Function to get the maximum width of machine ID
func getMaxIDWidth(machines []*machine) int {
    maxWidth := 0
    for _, m := range machines {
        idWidth := len(fmt.Sprint(m.id))
        if idWidth > maxWidth {
            maxWidth = idWidth
        }
    }
    return maxWidth
}

// Function to clear the previous output
func clearPreviousOutput(numLines int) {
    if numLines > 1 {
        fmt.Printf("\033[%dA", numLines-1)
    }
    fmt.Print("\033[K")
}


func minLoad(machineA machine, machineB machine) machine {
	if machineA.load < machineB.load {
		return machineA
	} else {
		return machineB
	}
}

