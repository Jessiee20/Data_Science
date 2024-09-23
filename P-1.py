import numpy as np
student_scores = np.array([[85, 90, 78, 92], 
                           [88, 91, 80, 89],
                           [90, 92, 85, 93], 
                           [87, 88, 82, 90]])
subject_averages = np.mean(student_scores, axis=0)
subject_names = ['Math', 'Science', 'English', 'History']
highest_avg_subject_index = np.argmax(subject_averages)
highest_avg_subject = subject_names[highest_avg_subject_index]
print("Average scores for each subject:", subject_averages)
print("Subject with the highest average score:", highest_avg_subject)
