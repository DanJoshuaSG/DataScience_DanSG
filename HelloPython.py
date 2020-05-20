# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Hello, Python!
#
# *This work is aim to make all the tasks of Python lesson from Kaggle*
#
# ## Cheking the types of text
# %%
spam_amount = 0
print (spam_amount) #It is evident that is a numeric response 

# %% [markdown]
# **Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)**
# %%
spam_amount = spam_amount + 4 #Numeric and operation
if spam_amount>0: #Conditional
    print("But I don't want ANY spam!") #String

viking_song= "Spam"*spam_amount

# %% [markdown]
# ## Type of numbers
# %% 
spam_amount = 0 #Don't need declare before, also not requires tell the type of value
type(1) #Integer
#
type(9.8) #Float
#
type(-1) #Integer
#
type(-9.8) #Float
# %% [markdown]
# ## Type of operations

# %%
print(1+3) #Addition
print(5-2.3) #Subtraction
print(3*2) #Multiplication
print(3**2) #Exponentiation
print(3/2) #True division --> Quotient of 3/2
print(3//2) #Floor division --> removing fractional parts
print(3%2) # Modulus, Integer remainder after division
print(-1) #Negatio
# Special numbers
import math as math
print(math.pi)
print(math.e)
# Math's library contains more interesting operations.

# %% [markdown]
# *Be careful in the order of the operations. Take account that is better invest time putting brackets than checking again the code*
#
# ## Using Builtin Functions


# %%
print(min(1,2,3)) #min
print(max(1,2,3)) #max
print(abs(-4)) #absolute values
print(int("809")+1) #converting a string into a integer

# %% [markdown]
# ## Your Turn: Resolved

# %% [markdown]
# ## Prev. Running a code
# %%
print("You've sucessfully run some Python code")
print("Congratulations!")
print("Hello world")
i=0 #Define initial value of i
while i<6: #If i is less than 6, i will sum 1. But if i=3 doesn't print the number.
    i+=1
    if i==3:
        continue
    print(i)
# %% [markdown]
# *Esc+a -> Inserts a code cell above of an existing one
# *Esc+b -> Inserts a code cell bellow of an existing one
# %% [markdown]
# ## 0. What's your favorite color?
# %%
# from learntools.core import binder; binder.bind(globals()) #It isn't in my repository then is impossible go away. but i insert images



