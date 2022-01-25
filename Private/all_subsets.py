# Power Set: Write a method to return all subsets of a set
# The subsets of a set {a1, a2, a3, a4, an} are also called a power set

"""
Notes:
   Two types of dynamic programming: 
   Botton-Up Approach: Start with knowing how to solve the problem for a simple case, like a like with only one element.
                       Then, figure out how to solve the problem for two elements, then three, and so on. Think about how you can
                       build the solution for one case off the previous case.
    Top-Down Approach: Think about how to divide the problem for case N into sub-problem. Case N being the final case. 
    Hald anf Half Approach: Binary search works with the half and half approach by dividing the dataset in half. Merge sort is an
                            example of a half and half approach by sorting each half of the array and merging the sorted halves together. """
"""p(2) = {}, {a1}, {a2}, {a1, a2}
   p(3) = {}, {a1}, {a2}, {a3}, {a1, a2}, {a1, a3}, {a2, a3}, {a1, a2, a3}
   The differernece between the two subsets is that p2 is amissing all the element contained in p3.
   How can we build off of p2 for the bottom up approahc? Clone the subsets in p(2) and add them to P(3).
   p(2) += p(2) + a3"""

def get_subsets(s: set) -> dict:
   """recursion"""

   if len(s) == 1:
      return [s]
   results = []
   subsets = get_subsets(s[0:-1])
   results = results+subsets
   results.append([s[-1]])
   for sub in subsets:
      results.append(sub+[s[-1]])
   return results


test_1 = [1, 2, 3]

print(get_subsets(test_1))
        
