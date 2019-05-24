# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 00:55:48 2019

@author: fovie
"""

11) We have two coins, A and B. For each toss of coin A, the probability of getting head is 1/2 and for each toss of coin B, the probability of getting Heads is 1/3. All tosses of the same coin are independent. We select a coin at random and toss it till we get a head. The probability of selecting coin A is ¼ and coin B is 3/4. What is the expected number of tosses to get the first heads?

A) 2.75
B) 3.35
C) 4.13
D) 5.33
Solution: (A)

If coin A is selected then the number of times the coin would be tossed for a guaranteed Heads is 2, similarly, for coin B it is 3. Thus the number of times would be

Tosses = 2 * (1/4)[probability of selecting coin A] + 3*(3/4)[probability of selecting coin B]

             = 2.75
             
A player is randomly dealt a sequence of 13 cards from a deck of 52-cards. All sequences of 13 cards are equally likely. In an equivalent model, the cards are chosen and dealt one at a time. When choosing a card, the dealer is equally likely to pick any of the cards that remain in the deck.

8) If you dealt 13 cards, what is the probability that the 13th card is a King?

A) 1/52
B) 1/13

C) 1/26

D) 1/12
Solution: (B)

Since we are not told anything about the first 12 cards that are dealt, the probability that the 13th card dealt is a King, is the same as the probability that the first card dealt, or in fact any particular card dealt is a King, and this equals: 4/52

7) Anita randomly picks 4 cards from a deck of 52-cards and places them back into the deck ( Any set of 4 cards is equally likely ). Then, Babita randomly chooses 8 cards out of the same deck ( Any set of 8 cards is equally likely). Assume that the choice of 4 cards by Anita and the choice of 8 cards by Babita are independent. What is the probability that all 4 cards chosen by Anita are in the set of 8 cards chosen by Babita?

A)48C4 x 52C4
B)48C4 x 52C8

C)48C8 x 52C8

D) None of the above
Solution: (A)

The total number of possible combination would be 52C4 (For selecting 4 cards by Anita) * 52C8 (For selecting 8 cards by Babita).

Since, the 4 cards that Anita chooses is among the 8 cards which Babita has chosen, thus the number of combinations possible is 52C4 (For selecting the 4 cards selected by Anita) * 48C4 (For selecting any other 4 cards by Babita, since the 4 cards selected by Anita are common)

4) 

A) True

B) False

Solution: (A)

P(AꓵCc) will be only P(A). P(only A)+P(C) will make it P(AꓴC). P(BꓵAcꓵCc) is P(only B) Therefore P(AꓴC) and P(only B) will make P(AꓴBꓴC)

12) Suppose a life insurance company sells a $240,000 one year term life insurance policy to a 25-year old female for $210. The probability that the female survives the year is .999592. Find the expected value of this policy for the insurance company.

A) $131
B) $140

C) $112

D) $125
Solution: (C)

P(company loses the money ) = 0.99592

P(company does not lose the money ) = 0.000408

The amount of money company loses if it loses = 240,000 – 210 = 239790

While the money it gains is $210

Expected money the company will have to give = 239790*0.000408 = 97.8

Expect money company gets = 210.

Therefore the value = 210 – 98 = $112

13) 

A) True

B) False

Solution: (A)

The above statement is true. You would need to know that

P(A/B) = P(AꓵB)/P(B)

P(CcꓵA|A) = P(CcꓵAꓵA)/P(A) = P(CcꓵA)/P(A)

P(B|A ꓵ Cc) = P(AꓵBꓵCc)/P(A ꓵ Cc)

Multiplying the three we would get – P(AꓵBꓵCc), hence the equations holds true

14) When an event A independent of itself?

A) Always
B) If and only if P(A)=0
C) If and only if P(A)=1
D) If and only if P(A)=0 or 1
Solution: (D)

The event can only be independent of itself when either there is no chance of it happening or when it is certain to happen. Event A and B is independent when P(AꓵB) = P(A)*P(B). Now if B=A, P(AꓵA) = P(A) when P(A) = 0 or 1.

 
17) A roulette wheel has 38 slots – 18 red, 18 black, and 2 green. You play five games and always bet on red slots. How many games can you expect to win?

A) 1.1165

B) 2.3684C) 2.6316

C) 2.6316

D) 4.7368
Solution: (B)

The probability that it would be Red in any spin is 18/38. Now, you are playing the game 5 times and all the games are independent of each other. Thus, the number of games that you can win would be 5*(18/38) = 2.3684

21) Which of the following events is most likely? 

A) At least one 6, when 6 dice are rolled

B) At least 2 sixes when 12 dice are rolled

C) At least 3 sixes when 18 dice are rolled

D) All the above have same probability
Solution: (A)

Probability of ‘6’ turning up in a roll of dice is P(6) = (1/6) & P(6’) = (5/6). Thus, probability of

∞ Case 1: (1/6) * (5/6)5 = 0.06698

∞ Case 2: (1/6)2 * (5/6)10 = 0.00448

∞ Case 3: (1/6)3 * (5/6)15 = 0.0003

Thus, the highest probability is Case 1

22) Suppose you were interviewed for a technical role. 50% of the people who sat for the first interview received the call for second interview. 95% of the people who got a call for second interview felt good about their first interview. 75% of people who did not receive a second call, also felt good about their first interview. If you felt good after your first interview, what is the probability that you will receive a second interview call?

A) 66%
B) 56%

C) 75%

D) 85%
Solution: (B)

Let’s assume there are 100 people that gave the first round of interview. The 50 people got the interview call for the second round. Out of this 95 % felt good about their interview, which is 47.5. 50 people did not get a call for the interview; out of which 75% felt good about, which is 37.5. Thus, the total number of people that felt good after giving their interview is (37.5 + 47.5) 85. Thus, out of 85 people who felt good, only 47.5 got the call for next round. Hence, the probability of success is (47.5/85) = 0.558.

Another more accepted way to solve this problem is the Baye’s theorem. I leave it to you to check for yourself. 

35) While it is said that the probabilities of having a boy or a girl are the same, let’s assume that the actual probability of having a boy is slightly higher at 0.51. Suppose a couple plans to have 3 children. What is the probability that exactly 2 of them will be boys?

A) 0.38
B) 0.48
C) 0.58
D) 0.68
E) 0.78
Solution: (A)

Think of this as a binomial distribution where getting a success is a boy and failure is a girl. Therefore we need to calculate the probability of getting 2 out of three successes.

P(X) = nCx pxqn-x = 3C2 (0.51)2(0.49)1 = 0.382


39) Jack is having two coins in his hand. Out of the two coins, one is a real coin and the second one is a faulty one with Tails on both sides. He blindfolds himself to choose a random coin and tosses it in the air. The coin falls down with Tails facing upwards. What is the probability that this tail is shown by the faulty coin?

A) 1/3
B) 2/3
C) 1/2
D) 1/4
Solution: (B)


We need to find the probability of the coin being faulty given that it showed tails.

P(Faulty) = 0.5

P(getting tails) = 3/4

P(faulty and tails) =0.5*1 = 0.5

Therefore the probability of coin being faulty given that it showed tails would be 2/3

STATISTICS

6) If a positively skewed distribution has a median of 50, which of the following statement is true?

A) Mean is greater than 50
B) Mean is less than 50
C) Mode is less than 50
D) Mode is greater than 50
E) Both A and C
F) Both B and D

Solution: (E)

Below are the distributions for Negatively, Positively and no skewed curves.

As we can see for a positively skewed curve, Mode<Median<Mean. So if median is 50, mean would be more than 50 and mode will be less than 50.

13) What would be the critical values of Z for 98% confidence interval for a two-tailed test ?

A) +/- 2.33
B) +/- 1.96
C) +/- 1.64
D) +/- 2.55

Solution: (A)

We need to look at the z table for answering this. For a 2 tailed test, and a 98% confidence interval, we should check the area before the z value as 0.99 since 1% will be on the left side of the mean and 1% on the right side. Hence we should check for the z value for area>0.99. The value will be +/- 2.33

Type 1 error means that we reject the null hypothesis when its actually true. Here the null hypothesis is that music does not improve memory. Type 1 error would be that we reject it and say that music does improve memory when it actually doesn’t.

18) A researcher concludes from his analysis that a placebo cures AIDS. What type of error is he making?

A) Type 1 error

B) Type 2 error

C) None of these. The researcher is not making an error.

D) Cannot be determined

Solution: (D)

By definition, type 1 error is rejecting the null hypothesis when its actually true and type 2 error is accepting the null hypothesis when its actually false. In this case to define the error, we need to first define the null and alternate hypothesis.

19) What happens to the confidence interval when we introduce some outliers to the data?

A) Confidence interval is robust to outliers

B) Confidence interval will increase with the introduction of outliers.

C) Confidence interval will decrease with the introduction of outliers.

D) We cannot determine the confidence interval in this case.

Solution: (B)

We know that confidence interval depends on the standard deviation of the data. If we introduce outliers into the data, the standard deviation increases, and hence the confidence interval also increases.

26) [True or False] F statistic cannot be negative.

A) TRUE

B) FALSE

Solution: (A)

F statistic is the value we receive when we run an ANOVA test on different groups to understand the differences between them. The F statistic is given by the ratio of between group variability to within group variability

Below is the formula for f Statistic.



Since both the numerator and denominator possess square terms, F statistic cannot be negative.

28) Correlation between two variables (Var1 and Var2) is 0.65. Now, after adding numeric 2 to all the values of Var1, the correlation co-efficient will_______ ?

A) Increase
B) Decrease
C) None of the above

Solution: (C)

If a constant value is added or subtracted to either variable, the correlation coefficient would be unchanged. It is easy to understand if we look at the formula for calculating the correlation.



If we add a constant value to all the values of x, the xi and  will change by the same number, and the differences will remain the same. Hence, there is no change in the correlation coefficient.


29) It is observed that there is a very high correlation between math test scores and amount of physical exercise done by a student on the test day. What can you infer from this?

High correlation implies that after exercise the test scores are high.
Correlation does not imply causation.
Correlation measures the strength of linear relationship between amount of exercise and test scores.
A) Only 1
B) 1 and 3
C) 2 and 3
D) All the statements are true

Solution: (C)

Though sometimes causation might be intuitive from a high correlation but actually correlation does not imply any causal inference. It just tells us the strength of the relationship between the two variables. If both the variables move together, there is a high correlation among them.

 
30) If the correlation coefficient (r) between scores in a math test and amount of physical exercise by a student is 0.86, what percentage of variability in math test is explained by the amount of exercise?

A) 86%
B) 74%
C) 14%
D) 26%

Solution: (B)

The % variability is given by r2, the square of the correlation coefficient. This value represents the fraction of the variation in one variable that may be explained by the other variable. Therefore % variability explained would be 0.862.

32) Consider a regression line y=ax+b, where a is the slope and b is the intercept. If we know the value of the slope then by using which option can we always find the value of the intercept?

A) Put the value (0,0) in the regression line True

B) Put any value from the points used to fit the regression line and compute the value of b False

C) Put the mean values of x & y in the equation along with the value a to get b False

D) None of the above can be used False

Solution: (C)

In case of ordinary least squares regression, the line would always pass through the mean values of x and y. If we know one point on the line and the value of slope, we can easily find the intercept.

33) What happens when we introduce more variables to a linear regression model?

A) The r squared value may increase or remain constant, the adjusted r squared may increase or decrease.

B) The r squared may increase or decrease while the adjusted r squared always increases.

C) Both r square and adjusted r square always increase on the introduction of new variables in the model.

D) Both might increase or decrease depending on the variables introduced.

Solution: (A)

The R square always increases or at least remains constant because in case of ordinary least squares the sum of square error never increases by adding more variables to the model. Hence the R squared does not decrease. The adjusted R-squared is a modified version of R-squared that has been adjusted for the number of predictors in the model. The adjusted R-squared increases only if the new term improves the model more than would be expected by chance. It decreases when a predictor improves the model by less than expected by chance.

LOGISTIC REGRESSION

12) Which of the following figure will represent the decision boundary as given by above classifier?

A)



B)



C)



D)



 

Solution: B

Option B would be the right answer. Since our line will be represented by y = g(-6+x2) which is shown in the option A and option B. But option B is the right answer because when you put the value x2 = 6 in the equation then y = g(0) you will get that means y= 0.5 will be on the line, if you increase the value of x2 greater then 6 you will get negative values so output will be the region y =0.

3) True-False: Is it possible to design a logistic regression algorithm using a Neural Network Algorithm?

A) TRUE
B) FALSE

Solution: A

True, Neural network is a is a universal approximator so it can implement linear regression algorithm.

 

4) True-False: Is it possible to apply a logistic regression algorithm on a 3-class Classification problem?

A) TRUE
B) FALSE

Solution: A

Yes, we can apply logistic regression on 3 classification problem, We can use One Vs all method for 3 class classification in logistic regression.

 

5) Which of the following methods do we use to best fit the data in Logistic Regression?

A) Least Square Error
B) Maximum Likelihood
C) Jaccard distance
D) Both A and B

Solution: B

Logistic regression uses maximum likely hood estimate for training a logistic regression.

 

6) Which of the following evaluation metrics can not be applied in case of logistic regression output to compare with target?

A) AUC-ROC
B) Accuracy
C) Logloss
D) Mean-Squared-Error

Solution: D

Since, Logistic Regression is a classification algorithm so it’s output can not be real time value so mean squared error can not use for evaluating it

 

7) One of the very good methods to analyze the performance of Logistic Regression is AIC, which is similar to R-Squared in Linear Regression. Which of the following is true about AIC?

A) We prefer a model with minimum AIC value
B) We prefer a model with maximum AIC value
C) Both but depend on the situation
D) None of these

Solution: A

We select the best model in logistic regression which can least AIC. For more information refer this source: http://www4.ncsu.edu/~shu3/Presentation/AIC.pdf

MACHINE LEARNING
2) Which of the following is an example of a deterministic algorithm?

A) PCA

B) K-Means

C) None of the above

Solution: (A)

A deterministic algorithm is that in which output does not change on different runs. PCA would give the same result if we run again, but not k-means.

8) Below are the 8 actual values of target variable in the train file.

[0,0,0,1,1,1,1,1]

What is the entropy of the target variable? 

A) -(5/8 log(5/8) + 3/8 log(3/8))

B) 5/8 log(5/8) + 3/8 log(3/8)

C) 3/8 log(5/8) + 5/8 log(3/8)

D) 5/8 log(3/8) – 3/8 log(5/8)

Solution: (A)

The formula for entropy is  

So the answer is A.

9) Let’s say, you are working with categorical feature(s) and you have not looked at the distribution of the categorical variable in the test data.

You want to apply one hot encoding (OHE) on the categorical feature(s). What challenges you may face if you have applied OHE on a categorical variable of train dataset? 

A) All categories of categorical variable are not present in the test dataset.

B) Frequency distribution of categories is different in train as compared to the test dataset.

C) Train and Test always have same distribution.

D) Both A and B

E) None of these

Solution: (D)

Both are true, The OHE will fail to encode the categories which is present in test but not in train so it could be one of the main challenges while applying OHE. The challenge given in option B is also true you need to more careful while applying OHE if frequency distribution doesn’t same in train and test.

15) Suppose you want to project high dimensional data into lower dimensions. The two most famous dimensionality reduction algorithms used here are PCA and t-SNE. Let’s say you have applied both algorithms respectively on data “X” and you got the datasets “X_projected_PCA” , “X_projected_tSNE”.

Which of the following statements is true for “X_projected_PCA” & “X_projected_tSNE” ?

A) X_projected_PCA will have interpretation in the nearest neighbour space.

B) X_projected_tSNE will have interpretation in the nearest neighbour space.

C) Both will have interpretation in the nearest neighbour space.

D) None of them will have interpretation in the nearest neighbour space.

Solution: (B)

t-SNE algorithm consider nearest neighbour points to reduce the dimensionality of the data. So, after using t-SNE we can think that reduced dimensions will also have interpretation in nearest neighbour space. But in case of PCA it is not the case.


CAUSATION VS CORRELATION

What are the keypoints in establishing causation?
Here are the key point ( X = > Y ) pairs used in establishing causation :

1. Alternate Reasoning :  If there is an alternate reason (Z) which indeed can influence both X and Y (Z => X &  Z => Y are true) , we can reject the hypothesis of X => Y.

2. Inverse Causality : If instead of X influencing Y, we have Y influencing X , we can reject X => Y hypothesis based on inverse causality.

3. Mutual independence : Sometimes X and Y might just be correlated and nothing else. In such cases we reject hypothesis based on mutual independence.

 
Two Phone screens. Machine Learning question and coding question. Interviewers were helpful and friendly. The turn around process was quick. The questions were easy and straight forward. GIven a time series dataset how will you predict the future value.


	
Accepted Offer
Positive Experience
Difficult Interview
Application

I applied online. The process took 4+ weeks. I interviewed at Microsoft (Dublin, Co. Dublin (Ireland)) in May 2017.

Interview

I applied online on the Microsoft Career website. I received an email a week after saying that they would like to plan a phone call. During this phone call we talked about my formation, my experience, what is this internship about, in which team, ... . Then after I received a mail saying that they were very impressed during the phone call and they would like to have on face… 
Show More

Interview Questions

Data science : I had a graph showing different step were a client is interested by microsoft product to the real buying act. If you have a dataset of previous clients who bought/didn't buy, how to make prediction for new clients ?  
1 Answer
Data science : What is a good/bad Data visualisation ?  
1 Answer
Data science : Explain Markov Chains to a 8 years old chilf  

Markov Chain Monte Carlo

Bayes theorem

	
No Offer
Neutral Experience
Easy Interview
Application

I applied online. I interviewed at Microsoft (Haifa (Israel)) in April 2017.

Interview

After short telephone conversation, 90 minutes meeting in Microsoft with one data scientist.
After this interview I was sure I was very good in all questions. But I don't accepted.

Interview Questions

How can you find percentile? Write code  
2 Answers
Find max sum subsequence.  
1 Answer
Standard question about Bayes formula. Ill people. Test. And you need to find different quantities of interest  
2 Answers
Ask me to say what I now about logit  
2 Answers
Say about different regularization metrics L1 and L2  
2 Answers
Say about neural networks  


Create a function that checks if a word is a palindrome  


https://www.geeksforgeeks.org/maximum-product-subarray/

https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/

https://www.geeksforgeeks.org/microsoft-interview-preparation/


The ROC space and plots of the four prediction examples.
The contingency table can derive several evaluation "metrics" (see infobox). To draw an ROC curve, only the true positive rate (TPR) and false positive rate (FPR) are needed (as functions of some classifier parameter). The TPR defines how many correct positive results occur among all positive samples available during the test. FPR, on the other hand, defines how many incorrect positive results occur among all negative samples available during the test.


Sensitivity and specificity
Sensitivity and specificity are statistical measures of the performance of a binary classification test, also known in statistics as a classification function:

Sensitivity (also called the true positive rate, the recall, or probability of detection[1] in some fields) measures the proportion of actual positives that are correctly identified as such (e.g., the percentage of sick people who are correctly identified as having the condition).
Specificity (also called the true negative rate) measures the proportion of actual negatives that are correctly identified as such (e.g., the percentage of healthy people who are correctly identified as not having the condition).

Simply put, a z-score is the number of standard deviations from the mean a data point is. But more technically it’s a measure of how many standard deviations below or above the population mean a raw score is. A z-score is also known as a standard score and it can be placed on a normal distribution curve. Z-scores range from -3 standard deviations (which would fall to the far left of the normal distribution curve) up to +3 standard deviations (which would fall to the far right of the normal distribution curve). In order to use a z-score, you need to know the mean μ and also the population standard deviation σ.


In statistics, the coefficient of determination, denoted R2 or r2 and pronounced "R squared", is the proportion of the variance in the dependent variable that is predictable from the independent variable(s).



