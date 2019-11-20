# Xtracta_interview_question
## Idea
The main idea is written in the Xtracta.txt file. 

### Question strategy:
1. Read the word from the invoice.txt file into a list A. (Deal with the Json)
2. Read the supplier name from the suppliername.txt into a list B.
3. Join the list A and list B into a list C. (list C contains the all existing supplier name)
4. Analyse the (page_id, line_id, pos_id) of the list C and train a model.
5. Predict the possible supplier name from the remaining invoice.txt.

## File description
### intersection_suppliername.py
#### This file has finished the strategy 1, 2, 3.
