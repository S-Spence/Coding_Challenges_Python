# Power Set: Write a method to return all subsets of a set
# The subsets of a set {a1, a2, a3, a4, an} are also called a power set

"""Two types of dynamic programming: 
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

"""Solution one: recursion"""

def get_subsets(s: set, index: int) -> dict:

   if len(s) == index:
       all_subsets = []
       all_subsets.append([])

   else:
      all_subsets = get_subsets(s, index+1)
      item = s[index]
      more_subsets = []
      for subset in all_subsets:
         new_subset = []
         new_subset.append(subset)
         new_subset.append(item)
         more_subsets.append(new_subset) 
      all_subsets.append(more_subsets)
   return all_subsets


test_1 = [1, 2, 3, 4, 5, 6]

print(get_subsets(test_1, 1))
        


