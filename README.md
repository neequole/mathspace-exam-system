## Requirements
* python3

## Setup
* Create project folder
* Create virtual environment
* Unzip the repository

```shell
mkdir mathspace-exam-system
cd mathspace-exam-system
source env/bin/activate
unzip mathspace-exam-system.zip
```

## Sample Interface

```python
from models import *

finals = Exam('finals', '2017-12-12')  # Create an exam

question1 = Question(QuestionTopic.ALGEBRA.value, AlgebraSubTopic.QUADRATIC_EQ.value, 'Find x, x^2=4', 1)
finals.add_question(question1)  # Add a question to an exam
choice1 = Choice('2 and -2', is_valid=True)
question1.add_choice(choice1)  # Add choice to a question
Choice('2 and 4', question1)  # We can add choice to a question upon its initialization 

question2 = Question(QuestionTopic.GEOMETRY.value, GeometrySubTopic.CIRCLES.value, 'Parallel lines:', 2, finals)  # We can also add the question to an exam upon initialization
Choice('Can intersect', question2)
Choice('Never intersect', question2, is_valid=True)

finals.get_min_possible_mark()  # Calculate minimum possible examination mark

csv_exam = Exam('CSV exam', '2017-12-12')
csv_exam.import_from_csv('revision_exam_20171010.csv')  # Import exam from CSV
csv_exam.get_min_possible_mark()
csv_exam.export_to_csv('output.csv')  # Export exam to CSV

csv_exam.mark_result('revision_exam_answers.csv')  # Mark answers
csv_exam.print_statistics()  # Print exam marking statistics
```

* Questions and subtopic were created as Enums for consistency. You can use the ff. for the interface:
    * Question topics
      * `QuestionTopic.ALGEBRA.value` - Algebra
      * `QuestionTopic.GEOMETRY.value` - Geometry
      
    * Subtopics
      * Algebra
        * `AlgebraSubTopic.FRACTIONS.value` - Fractions
        * `AlgebraSubTopic.QUADRATIC_EQ.value` - Quadratic Equations
        * `AlgebraSubTopic.SIMULTANEOUS_EQ.value` - Simultaneous Equations
      * Geometry
        * `GeometrySubTopic.PARALLEL_LINES.value` - Parallel Lines
        * `GeometrySubTopic.CIRCLES.value` - Circles
    
* Assertion errors were raised for validation error but should be handled by serializer or database.
* No checking for question number uniqueness and date format.
* File parameters are searched under the assets folder.
* `Simultaenous Questions` were renamed to  `Simultaneous Equations` in the input file.

## Testing

Make sure to activate your virtual environment before running the ff. test commands:

```shell
python -m unittest tests/test_choice.py
python -m unittest tests/test_exam.py
python -m unittest tests/test_question.py
```
