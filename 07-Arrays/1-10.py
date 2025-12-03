###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
correct_answers = 0
for i in test_results:
   if test_results[i+1]==True:
      correct_answers += 1

# calculates the number of incorrect answers
incorrect_answers = 0
for i in test_results:
   if test_results[i+1]==False:
      incorrect_answers += 1

# calculates the percentage of correct answers
prct = (correct_answers/question_number)*100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers', prct)