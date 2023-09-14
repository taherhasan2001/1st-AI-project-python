# AI First Project

<div style="text-align:center;"><img src="dm/Aspose.Words.5a48beaf-f0c8-44a8-a99c-0972bb35b50e.001.png" alt="Project Image" /></div>

## Course: AI – ENCS3340
### First semester 2022/2023

#### Team Members:
- Diaeddin Tahboub – 1200136
- Saleh Khatib - 1200991
- Taher Hasan - 1191740

#### Instructor:
Dr. Aziz Qaroush

---

## Goal
This programming project can be viewed as an application of searching algorithms (local searching algorithms) in real-world problems.

## Specifications
Developing a department courses distribution is not an easy task. It has many variables: time slots, courses, sections, student priorities, teacher priorities, etc. The aim of this project is to distribute the department courses with maximum diversity.

The aim of this project is to use Genetic algorithm to optimize the distribution of the courses to achieve maximum diversity. The input for this project is the course browser of the current semester. Your program needs to have a reasonable interface that can easily show the distribution of the courses.

## Idea
The project’s aim is to read the information about labs and courses (read the instructors, time of start, and time of end for each course) and make chromosomes for them. Then we apply crossover and mutation on them and take the best chromosome (has the best fitness function). Note: we change the sections of an instructor if there is a reflection of time in his labs/courses.

## Methods and Functions
1. **readCour**: Read courses and their instructors from the courses file.
2. **readlab**: Read the labs and their instructors from the labs file.
3. **MakeFirChrom**: Make chromosomes represented by 10 time slots, each time slot will be filled by multiple sections for courses.
4. **MakePop**: Create the other chromosomes after making the first and to make the population so we can start the crossover.
5. **Fit and FitHelp**: Fit takes the first chromosome and grasps each time slot in the chromosome, then for every time slot, if we have more than one section for a course, then we will take half of them and take. Otherwise, if there are courses with the same year, we will take just one section from one course. After that, we will take the rest of the number of sections that fit left in the time slot and add it to the one and a half (if it exists).
6. **FitHelp**: Calculates the fitness for a single time slot, but the Fit function calculates the fitness for all time slots in the chromosome using this function.
7. **Crossover**: Uses three functions (Unaited, ToForm, Realcro). Firstly, we double the number of the population. Then Unaited takes two chromosomes and combines the sections that are inside the two chromosomes inside a new list, then the ToForm function swaps the indexes of the list. The RealCro function takes the two chromosomes and fills them from the mixed list, so we will have after that two chromosomes as a result of the crossover. Repeat all these steps for all the population, after that, we will calculate the fitness function for each chromosome in the population and then return the one with the higher fitness function. If this fitness achieved the goal return it, take the best ten from the doubled population and repeat the crossing-over for them. Note: for 100 iterations we will make mutation for all the population.
8. **DistrubTeach**: Gives every teacher his section.
9. **Fix**: If the teacher has more than one section in the same time slot then we move the repeated section to another time slot.
10. **FixL**: If the teacher has more than one lab in the same time slot then we move the repeated lab to another time slot.
11. **CopyLC**: Combines the chromosome of the courses and the chromosome of the labs into one chromosome.
12. **YaaaaRabee**: Works like Fix function but for the combined chromosome.
13. **TimeStr**: Splits the time slots for labs and courses.
14. **Save**: Prints the output in the table file.

Note: The chromosome for the courses has 10 time slots, the first 5 time slots represent Monday courses and the other slots represent the Tuesday courses, we made this because the courses of Monday are reflected to Wednesday and Saturday, and the courses of Tuesday are reflected to Thursday.

For labs, we have 15 time slots, and each 3 represents a day.

## Interface Part

In the first UI, we can choose between searching by course label or instructor name as shown below:

![UI1](dm/Aspose.Words.5a48beaf-f0c8-44a8-a99c-0972bb35b50e.002.png)

After we have chosen the way we need to search, we can add any courses from the list if "Search by Course" is selected or if "Search by Instructor Name" is selected.

![UI2](dm/Aspose.Words.5a48beaf-f0c8-44a8-a99c-0972bb35b50e.003.png)

The table appears at the end.

![UI3](dm/Aspose.Words.5a48beaf-f0c8-44a8-a99c-0972bb35b50e.004.png)

If we get a conflict between two or more sections, it will appear as a red button. If selected, the name of the conflicting sections and other details will appear.

![UI4](dm/Aspose.Words.5a48beaf-f0c8-44a8-a99c-0972bb35b50e.005.png)
